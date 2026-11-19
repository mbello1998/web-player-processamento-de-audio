import json
import re
import time
import base64
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

CATALOG_FILE = Path("spotify_playlists_catalog.json")
RESULTS_FILE = Path("spotify_cover_matches_round3.json")

with open("spotify_credentials.json", encoding="utf-8") as f:
    CREDS = json.load(f)

# Consultas extras pensadas a dedo pra cada uma das 39 que sobraram - nome do artista puro
# (pra quem a playlist homenageia um artista específico, a forma mais confiável de achar
# algo real é buscar só o nome dele, sem o resto do título estilizado) ou um termo mais
# simples/curto que uma playlist de verdade teria (sem "Top 10"/"Semanal", que nenhuma
# playlist real usa no título).
MANUAL_QUERIES = {
    "radar_spotify_brasil": ["Novas Revelações Brasil", "Descobertas Brasil"],
    "spotify_top_100": ["Top 100 Brasil", "As Mais Tocadas"],
    "sertanejo_no_ponto": ["Sertanejo Top", "Sertanejo Hits"],
    "noite_fria_sofrencia": ["Sofrência", "Modão Sofrência"],
    "top_10_funk_semanal": ["Funk Brasil Hits", "Funk 2026"],
    "trapperz_brasil": ["Trap Brasil", "Trap Nacional"],
    "trap_melodico_brasil": ["Trap Melódico", "Melodic Trap Brasil"],
    "flow_espacial": ["Space Trap", "Lofi Trap"],
    "hip_hop_brasil_classicos": ["Rap Nacional Clássicos", "Boom Bap Brasil"],
    "top_10_rap_trap_semanal": ["Rap Trap Brasil", "Trap Nacional Hits"],
    "pagode_romantico_90s": ["Pagode Romântico", "Pagode Anos 90"],
    "pagode_churrasco_parcas": ["Pagode Churrasco", "Samba Pagode Churrasco"],
    "top_10_pagode_semanal": ["Pagode Brasil Hits", "Pagode 2026"],
    "eletronica_brasil": ["Eletrônica Nacional", "Dance Brasil"],
    "fuego_latino": ["Latin Hits", "Fuego Latino Reggaeton"],
    "urban_latino_hits": ["Urbano Latino", "Latin Urban Hits"],
    "e_o_tchan_axe_90s": ["É o Tchan", "Axé Anos 90"],
    "pop_hits_brasil": ["Pop Nacional", "Pop Brasil Hits"],
    "resenha_com_amigos": ["Resenha", "Pagode Resenha"],
    "relaxing_acoustic_vibes": ["Acoustic Chill", "Acoustic Relax"],
    "pre_balada_hits": ["Pré Balada", "Esquenta Balada"],
    "bailao_automotivo": ["Som Automotivo", "Paredão Automotivo"],
    "paredao_200_bass": ["Paredão Bass", "Grave Pesado"],
    "top_brasil_sunset": ["Sunset Brasil", "Pôr do Sol Hits"],
    "top_10_mega_funk_semanal": ["Mega Funk Brasil", "Mega Funk 2026"],
    "damas_gratis_atr": ["Pablo Lescano", "Damas Gratis"],
    "mala_fama_guampa": ["Mala Fama", "Hernán Coronel"],
    "leo_mattioli_el_leon": ["Leo Mattioli"],
    "cumbia_santafesina_oro": ["Cumbia Santafesina", "Cumbia Santa Fe"],
    "cumbia_romantica_90s": ["Cumbia Romántica 90s", "Cumbia de los 90"],
    "la_champions_liga_romantica": ["La Champions Liga"],
    "el_polaco_de_gira": ["El Polaco"],
    "kumbia_kings_fiesta": ["Kumbia Kings"],
    "cumbia_para_el_asado": ["Cumbia Asado", "Cumbia Churrasco"],
    "quarai_artigas_fronteira_paz": ["Vanerão Fronteira", "Música de Fronteira Gaúcha"],
    "artigas_charanga_cumbia": ["Charanga Uruguaia", "Cumbia Uruguaya"],
    "quarai_gaucho_fronteira": ["Vanera Chamamé", "Nativismo Gaúcho"],
    "mix_fiesteros_previa_boliche_2026": ["Previa Boliche", "Cumbia Fiestera 2026"],
    "cumbia_fiestera_sonido_profesional": ["Sonido Profesional Cumbia", "Cumbia Fiestera Charanga"],
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


def pick_best_match(target_name, target_genre, candidates):
    target_tokens = normalize(target_name) + normalize(target_genre)
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
        queries = MANUAL_QUERIES.get(key, [])

        overall_best, overall_score, used_query = None, 0.0, None
        for q in queries:
            candidates = search_playlists(token, q)
            best, score = pick_best_match(name, genre, candidates)
            if score > overall_score:
                overall_best, overall_score, used_query = best, score, q
            time.sleep(0.1)

        # Limite um pouco mais flexivel que nas rodadas anteriores (0.4 em vez de 0.45) so
        # pra essas consultas pensadas a dedo, que ja miram o termo certo de proposito.
        if overall_best and overall_score >= 0.4:
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
