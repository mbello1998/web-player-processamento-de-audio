import json
import re
import time
import base64
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

CATALOG_FILE = Path("spotify_playlists_catalog.json")
RESULTS_FILE = Path("spotify_cover_matches_round4.json")

with open("spotify_credentials.json", encoding="utf-8") as f:
    CREDS = json.load(f)

MANUAL_QUERIES = {
    "radar_spotify_brasil": ["Artistas Emergentes Brasil", "Novidades Brasil 2026"],
    "spotify_top_100": ["Top Hits Brasil 2026", "As Mais Tocadas Brasil"],
    "sertanejo_no_ponto": ["Sertanejo Seleção", "Sertanejo Raiz"],
    "noite_fria_sofrencia": ["Sertanejo Acústico Sofrência", "Sofrência Acústico"],
    "top_10_funk_semanal": ["Funk Hits 2026", "Melhores Funk Brasil"],
    "trapperz_brasil": ["Trap Nacional Hits", "Trapper Brasil"],
    "trap_melodico_brasil": ["Trap Sad Brasil", "Trap Melodic Brasil"],
    "top_10_rap_trap_semanal": ["Rap Nacional Hits", "Trap BR Hits"],
    "resenha_com_amigos": ["Pagode Resenha Amigos", "Churrasco Amigos Pagode"],
    "pre_balada_hits": ["Esquenta Balada", "Pre Night Brasil"],
    "bailao_automotivo": ["Som Automotivo Grave", "Funk Automotivo Grave"],
    "top_10_mega_funk_semanal": ["Mega Funk Hits", "Mega Funk Ritmada"],
    "mala_fama_guampa": ["Mala Fama cumbia", "Hernan Coronel Mala Fama"],
    "leo_mattioli_el_leon": ["Leo Mattioli cumbia", "Leo Mattioli romantica"],
    "cumbia_romantica_90s": ["Antonio Rios Daniel Agostini", "Cumbia Romantica Argentina 90"],
    "el_polaco_de_gira": ["El Polaco cumbia", "Ezequiel Cwirkaluk"],
    "cumbia_para_el_asado": ["Cumbia Asado Churrasco", "Cumbia Fin de Semana Argentina"],
    "quarai_artigas_fronteira_paz": ["Vanerao Fronteira", "Musica Fronteira Gaucha Uruguaia"],
    "artigas_charanga_cumbia": ["Miriam Britos", "Chacho Ramos"],
    "quarai_gaucho_fronteira": ["Mano Lima", "Luiz Marenco"],
    "cumbia_fiestera_sonido_profesional": ["Sonido Profesional cumbia", "Sonido Profesional uruguay"],
}


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


EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]+", flags=re.UNICODE)
STOPWORDS = {"the", "a", "de", "da", "do", "e", "and", "mix", "playlist", "radio", "oficial", "official"}


def normalize(text):
    text = EMOJI_RE.sub(" ", text or "")
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    return [t.lower() for t in text.split() if len(t) > 1 and t.lower() not in STOPWORDS]


def name_overlap_score(target_tokens, candidate_tokens):
    if not target_tokens or not candidate_tokens:
        return 0.0
    tset, cset = set(target_tokens), set(candidate_tokens)
    return len(tset & cset) / max(len(tset), 1)


def search_playlists(token, query, limit=10):
    q = urllib.parse.quote(query)
    url = f"https://api.spotify.com/v1/search?q={q}&type=playlist&limit={limit}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return [it for it in (data.get("playlists", {}).get("items") or []) if it]
    except urllib.error.HTTPError as e:
        print(f"    [erro busca {query!r}] {e.code}: {e.read().decode()[:150]}")
        return []
    except Exception as e:
        print(f"    [erro busca {query!r}] {e}")
        return []


def pick_best_match(target_name, target_genre, target_desc, candidates):
    target_tokens = normalize(target_name) + normalize(target_genre) + normalize(target_desc)
    best, best_score = None, 0.0
    for c in candidates:
        cand_tokens = normalize(c.get("name", ""))
        overlap = name_overlap_score(target_tokens, cand_tokens)
        owner = (c.get("owner") or {}).get("display_name", "") or ""
        is_official = owner.strip().lower() == "spotify"
        score = overlap + (0.6 if is_official else 0.0)
        if score > best_score:
            best_score, best = score, c
    return best, best_score


def main():
    with open(CATALOG_FILE, encoding="utf-8") as f:
        catalog = json.load(f)

    targets = [
        (key, entry["meta"])
        for key, entry in catalog.items()
        if not entry.get("meta", {}).get("cover_url")
    ]
    print(f"Total ainda sem capa: {len(targets)}")

    results = {}
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE, encoding="utf-8") as f:
            results = json.load(f)

    token = get_token()
    token_time = time.time()
    accepted = skipped = 0

    for i, (key, meta) in enumerate(targets, 1):
        if key in results:
            continue
        if time.time() - token_time > 1500:
            token = get_token()
            token_time = time.time()

        name = meta.get("name", "")
        genre = meta.get("genre", "")
        desc = meta.get("desc", "")
        queries = MANUAL_QUERIES.get(key, [])

        overall_best, overall_score, used_query = None, 0.0, None
        for q in queries:
            candidates = search_playlists(token, q)
            best, score = pick_best_match(name, genre, desc, candidates)
            if score > overall_score:
                overall_best, overall_score, used_query = best, score, q
            time.sleep(0.1)

        if overall_best and overall_score >= 0.35:
            cover_sources = overall_best.get("images") or []
            cover_url = cover_sources[0].get("url") if cover_sources else None
            owner = (overall_best.get("owner") or {}).get("display_name", "")
            results[key] = {
                "status": "matched",
                "spotify_id": overall_best.get("id"),
                "match_name": overall_best.get("name"),
                "owner": owner,
                "score": round(overall_score, 3),
                "query_used": used_query,
                "cover_url": cover_url,
            }
            accepted += 1
            print(f"[{i}/{len(targets)}] OK (query {used_query!r}, score {round(overall_score,2)}): {name} -> {overall_best.get('name')}")
        else:
            results[key] = {"status": "no_match", "best_score": round(overall_score, 3), "queries_tried": queries}
            skipped += 1
            print(f"[{i}/{len(targets)}] SEM MATCH: {name} (melhor score: {round(overall_score,2)})")

        if i % 10 == 0:
            with open(RESULTS_FILE, "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=2)

    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nFinalizado. Aceitos: {accepted} | Sem match: {skipped}")


if __name__ == "__main__":
    main()
