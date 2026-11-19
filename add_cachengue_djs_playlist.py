# -*- coding: utf-8 -*-
"""
add_cachengue_djs_playlist.py
Cria a playlist "Fer Palacio, Yayo, Alan Gomez & Jona Mix" (cachengue/previa argentina)
e sincroniza as faixas com spotify_playlists_catalog.json e complete_library.json.
Faixas confirmadas via busca real no YouTube (yt-dlp ytsearch), não inventadas.
"""

import json
from pathlib import Path

SPOTIFY_CATALOG_FILE = Path("spotify_playlists_catalog.json")
LIBRARY_FILE = Path("complete_library.json")

PLAYLIST = {
    "id": "cachengue_djs_argentina",
    "name": "Fer Palacio, Yayo, Alan Gomez & Jona Mix",
    "badge": "🎧 Cachengue DJs",
    "icon": "🎧",
    "genre": "Previa & Cachengue Set en Vivo",
    "desc": "Os sets ao vivo mais pedidos da cena de previa e cachengue argentina: Fer Palacio, DJ Yayo, Alan Gomez e Jona Mix.",
    "bpm": 127,
    "tracks": [
        {
            "title": "MIX LO NUEVO 2026 | Enganchado | Cachengue | Fer Palacio Set en vivo @ oso.okkk",
            "artist": "Fer Palacio",
            "video_id": "HQ6UCBKXqEM",
            "duration": 1858,
            "bpm": 128
        },
        {
            "title": "Mix lo nuevo 2025 | Cachengue | Enganchado | Fer Palacio Set en vivo @ oso.okkk",
            "artist": "Fer Palacio",
            "video_id": "Gi55jQM7bp8",
            "duration": 1968,
            "bpm": 128
        },
        {
            "title": "SET LIVE #1 | ENGANCHADO REMIX - DJ Yayo & Kevo DJ / invitado “El Bandido”",
            "artist": "DJ Yayo",
            "video_id": "NxemeGNEHO4",
            "duration": 1524,
            "bpm": 126
        },
        {
            "title": "SET LIVE #2 - DJ Yayo / ENGANCHADO REMIX",
            "artist": "DJ Yayo",
            "video_id": "LXXeMFHw_rQ",
            "duration": 755,
            "bpm": 126
        },
        {
            "title": "LIVE SET (RETRO EDITION #1) - Alan Gomez, Maty Deejay (Lo mejor de Previa & Cachengue 2021)",
            "artist": "Alan Gomez",
            "video_id": "g91MHh2hzZQ",
            "duration": 747,
            "bpm": 125
        },
        {
            "title": "SESSION ALAN GOMEZ VOL. 1 / REGGAETON - CACHENGUE / DICIEMBRE 2020 | ARGENTINA REMIX",
            "artist": "Alan Gomez",
            "video_id": "LXkUH_54DPQ",
            "duration": 873,
            "bpm": 125
        },
        {
            "title": "MIX ENGANCHADO CACHENGUE #02 (LO MAS NUEVO 2023) - JONA MIX",
            "artist": "Jona Mix",
            "video_id": "Cs3rRurEeLY",
            "duration": 1640,
            "bpm": 129
        },
        {
            "title": "Mix Enganchado Navideño (Cachengue 2022) - Jona Mix",
            "artist": "Jona Mix",
            "video_id": "RonKP_xpXv0",
            "duration": 1474,
            "bpm": 129
        }
    ]
}


def update_catalog():
    with open(SPOTIFY_CATALOG_FILE, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    meta = {
        "id": PLAYLIST["id"],
        "name": PLAYLIST["name"],
        "badge": PLAYLIST["badge"],
        "icon": PLAYLIST["icon"],
        "genre": PLAYLIST["genre"],
        "desc": PLAYLIST["desc"],
        "bpm": PLAYLIST["bpm"]
    }
    tracks = []
    for i, t in enumerate(PLAYLIST["tracks"]):
        tracks.append({
            "rank": i + 1,
            "title": t["title"],
            "artist": t["artist"],
            "category": "Reggaeton, Cachengue & Latino",
            "playlist_id": PLAYLIST["id"],
            "playlist_badge": PLAYLIST["badge"],
            "video_id": t["video_id"],
            "duration": t["duration"],
            "bpm": t["bpm"],
            "source": f"Spotify - {PLAYLIST['name']}"
        })
    catalog[PLAYLIST["id"]] = {"meta": meta, "tracks": tracks}

    with open(SPOTIFY_CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print(f"Playlist adicionada: {PLAYLIST['name']} ({len(tracks)} faixas). Total catalogo: {len(catalog)}")


def update_library():
    with open(LIBRARY_FILE, "r", encoding="utf-8") as f:
        library = json.load(f)

    existing_ids = {t.get("video_id") for t in library if t.get("video_id")}
    added = 0
    for t in PLAYLIST["tracks"]:
        vid = t["video_id"]
        if vid and vid not in existing_ids:
            library.append({
                "title": t["title"],
                "artist": t["artist"],
                "video_id": vid,
                "duration": t["duration"],
                "bpm": t["bpm"],
                "category": "Reggaeton, Cachengue & Latino",
                "source": f"Mix Fiestero ({PLAYLIST['badge']})"
            })
            existing_ids.add(vid)
            added += 1

    with open(LIBRARY_FILE, "w", encoding="utf-8") as f:
        json.dump(library, f, indent=2, ensure_ascii=False)
    print(f"Biblioteca atualizada: {added} novas faixas. Total: {len(library)}")


if __name__ == "__main__":
    update_catalog()
    update_library()
