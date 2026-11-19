import json
import re
import time
import base64
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

CATALOG_FILE = Path("spotify_playlists_catalog.json")
RESULTS_FILE = Path("spotify_cover_matches_full.json")

with open("spotify_credentials.json", encoding="utf-8") as f:
    CREDS = json.load(f)


def get_token():
    auth = base64.b64encode(f"{CREDS['client_id']}:{CREDS['client_secret']}".encode()).decode()
    req = urllib.request.Request(
        "https://accounts.spotify.com/api/token",
        data=urllib.parse.urlencode({"grant_type": "client_credentials"}).encode(),
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())["access_token"]


EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF"
    "]+",
    flags=re.UNICODE,
)
STOPWORDS = {"the", "a", "de", "da", "do", "e", "and", "mix", "playlist", "radio", "oficial", "official"}


def normalize(text):
    text = EMOJI_RE.sub(" ", text or "")
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    tokens = [t.lower() for t in text.split() if len(t) > 1 and t.lower() not in STOPWORDS]
    return tokens


def name_overlap_score(target_tokens, candidate_tokens):
    if not target_tokens or not candidate_tokens:
        return 0.0
    tset, cset = set(target_tokens), set(candidate_tokens)
    inter = len(tset & cset)
    return inter / max(len(tset), 1)


def search_playlists(token, query, limit=10):
    q = urllib.parse.quote(query)
    url = f"https://api.spotify.com/v1/search?q={q}&type=playlist&limit={limit}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return [it for it in (data.get("playlists", {}).get("items") or []) if it]
    except urllib.error.HTTPError as e:
        print(f"  [erro busca] {e.code}: {e.read().decode()[:150]}")
        return []
    except Exception as e:
        print(f"  [erro busca] {e}")
        return []


def pick_best_match(target_name, target_genre, candidates):
    target_tokens = normalize(target_name) + normalize(target_genre)
    best = None
    best_score = 0.0
    for c in candidates:
        cand_tokens = normalize(c.get("name", ""))
        overlap = name_overlap_score(target_tokens, cand_tokens)
        owner = (c.get("owner") or {}).get("display_name", "") or ""
        is_official = owner.strip().lower() == "spotify"
        score = overlap + (0.6 if is_official else 0.0)
        if score > best_score:
            best_score = score
            best = c
    return best, best_score


def main():
    with open(CATALOG_FILE, encoding="utf-8") as f:
        catalog = json.load(f)

    results = {}
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE, encoding="utf-8") as f:
            results = json.load(f)

    targets = [
        (key, entry["meta"])
        for key, entry in catalog.items()
        if not entry.get("meta", {}).get("cover_url")
    ]
    print(f"Total de playlists sem capa: {len(targets)}")

    token = get_token()
    token_time = time.time()

    accepted = 0
    skipped = 0

    for i, (key, meta) in enumerate(targets, 1):
        if key in results:
            continue

        if time.time() - token_time > 1500:
            token = get_token()
            token_time = time.time()

        name = meta.get("name", "")
        genre = meta.get("genre", "")
        query = re.sub(r"\s+", " ", EMOJI_RE.sub(" ", name)).strip()

        candidates = search_playlists(token, query)
        best, score = pick_best_match(name, genre, candidates)

        if best and score >= 0.45:
            cover_sources = best.get("images") or []
            cover_url = cover_sources[0].get("url") if cover_sources else None
            owner = (best.get("owner") or {}).get("display_name", "")
            results[key] = {
                "status": "matched",
                "spotify_id": best.get("id"),
                "match_name": best.get("name"),
                "owner": owner,
                "is_official": owner.strip().lower() == "spotify",
                "score": round(score, 3),
                "cover_url": cover_url,
            }
            accepted += 1
            print(f"[{i}/{len(targets)}] OK ({'oficial' if results[key]['is_official'] else 'score '+str(round(score,2))}): {name} -> {best.get('name')}")
        else:
            results[key] = {"status": "no_match", "best_score": round(score, 3) if best else 0}
            skipped += 1
            print(f"[{i}/{len(targets)}] SEM MATCH BOM: {name} (melhor score: {round(score,2) if best else 0})")

        if i % 10 == 0:
            with open(RESULTS_FILE, "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=2)

        time.sleep(0.12)

    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nFinalizado. Aceitos: {accepted} | Sem match bom: {skipped}")
    print(f"Resultados salvos em {RESULTS_FILE}")


if __name__ == "__main__":
    main()
