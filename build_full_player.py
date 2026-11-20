import json
import re
from pathlib import Path

LIBRARY_FILE = Path("complete_library.json")
SPOTIFY_FILE = Path("spotify_playlists_catalog.json")

CATEGORY_ORDER = [
    "Mega Funk & Ritmadas",
    "Funk Paulista, BH & Mandelão",
    "Eletrônica, House & Desande",
    "Sertanejo Universitário & Atual",
    "Sertanejo Antigo & Modão",
    "Reggaeton, Cachengue & Latino",
    "Samba & Pagode",
    "Trap & Rap Nacional",
    "Rock & Pop Nostalgia",
    "Outros",
]

CATEGORY_ICONS = {
    "Mega Funk & Ritmadas": '<svg class="ui-icon ui-icon-neon-pink" viewBox="0 0 24 24"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 17c1.38 0 2.5-1.12 2.5-2.5 0-1.63-1.5-3-1.5-3s-.5 1-1 1-1-1.5-1-1.5c0 0-1.5 2-1.5 3.5z"></path><path d="M12 2c1 3 4 5 4 9a6 6 0 1 1-12 0c0-4 3-6 4-9 1 2 3 3 4 0z"></path></svg>',
    "Funk Paulista, BH & Mandelão": '<svg class="ui-icon ui-icon-neon-cyan" viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>',
    "Eletrônica, House & Desande": '<svg class="ui-icon ui-icon-neon-cyan" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "Sertanejo Universitário & Atual": '<svg class="ui-icon ui-icon-neon-orange" viewBox="0 0 24 24"><path d="M2 17c1.5 1 4 2 10 2s8.5-1 10-2"></path><path d="M6 16c0-4 1.5-8 6-8s6 4 6 8"></path><path d="M8 8c1-3 2.5-4 4-4s3 1 4 4"></path></svg>',
    "Sertanejo Antigo & Modão": '<svg class="ui-icon ui-icon-neon-orange" viewBox="0 0 24 24"><path d="M6 9H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h2"></path><path d="M18 9h2a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2h-2"></path><path d="M4 5h16v6a7 7 0 0 1-14 0V5z"></path><line x1="12" y1="18" x2="12" y2="22"></line><line x1="8" y1="22" x2="16" y2="22"></line></svg>',
    "Reggaeton, Cachengue & Latino": '<svg class="ui-icon ui-icon-neon-green" viewBox="0 0 24 24"><path d="M12 22v-9"></path><path d="M12 13c-3-2-5-6-5-9 3 0 6 2 8 5"></path><path d="M12 13c3-2 5-6 5-9-3 0-6 2-8 5"></path><path d="M12 13c-4 0-8-1-10-4 2-1 6-1 8 2"></path><path d="M12 13c4 0 8-1 10-4-2-1-6-1-8 2"></path></svg>',
    "Samba & Pagode": '<svg class="ui-icon ui-icon-neon-orange" viewBox="0 0 24 24"><ellipse cx="12" cy="8" rx="8" ry="4"></ellipse><path d="M4 8v8c0 2.2 3.6 4 8 4s8-1.8 8-4V8"></path><line x1="6" y1="4" x2="9" y2="7"></line><line x1="18" y1="4" x2="15" y2="7"></line></svg>',
    "Trap & Rap Nacional": '<svg class="ui-icon ui-icon-neon-pink" viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>',
    "Rock & Pop Nostalgia": '<svg class="ui-icon ui-icon-neon-cyan" viewBox="0 0 24 24"><circle cx="12" cy="16" r="5"></circle><line x1="12" y1="11" x2="12" y2="3"></line><line x1="10" y1="3" x2="14" y2="3"></line><circle cx="12" cy="16" r="1.5"></circle></svg>',
    "Outros": '<svg class="ui-icon" viewBox="0 0 24 24"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path></svg>',
}

def resolve_cat(title, artist=""):
    text = (str(title) + " " + str(artist)).lower()
    if re.search(r'cumbia|villera|santafesina|charanga|chicha|cuarteto|reggaeton|latino|dembow|perreo|bachata|sonido profesional|fiestero|cachengue|el reja', text):
        return "Reggaeton, Cachengue & Latino"
    if re.search(r'megafunk|mega funk|ritmada|eletrofunk|eletro funk', text):
        return "Mega Funk & Ritmadas"
    if re.search(r'funk|mandel|bh|fluxo|favela|kondzilla|gr6|mc |montagem', text):
        return "Funk Paulista, BH & Mandelão"
    if re.search(r'eletr|house|desande|edm|techno|trance|psy|rave|alok|vintage', text):
        return "Eletrônica, House & Desande"
    if re.search(r'sertanejo|universit|agronejo|modao|modão|gusttavo|jorge|marilia|zeneto', text):
        return "Sertanejo Universitário & Atual"
    if re.search(r'samba|pagode|ferrugem|dilsinho|sorriso maroto|turma do pagode', text):
        return "Samba & Pagode"
    if re.search(r'trap|rap|drill|hip hop|hip-hop|matue|kayblack|veigh|filipe ret', text):
        return "Trap & Rap Nacional"
    if re.search(r'rock|pop|nostalgia|anos 80|anos 90|anos 2000', text):
        return "Rock & Pop Nostalgia"
    return "Outros"

def rebuild_player_html():
    if not LIBRARY_FILE.exists():
        return False
    with open(LIBRARY_FILE, "r", encoding="utf-8") as f:
        library = json.load(f)

    spotify_catalog = {}
    if SPOTIFY_FILE.exists():
        try:
            with open(SPOTIFY_FILE, "r", encoding="utf-8") as f:
                spotify_catalog = json.load(f)
        except Exception:
            spotify_catalog = {}

    grouped = {}
    for cat in CATEGORY_ORDER:
        grouped[cat] = [t for t in library if t.get("category") == cat and t.get("video_id")]

    for t in library:
        if t.get("video_id") and t.get("category") not in CATEGORY_ORDER:
            resolved = resolve_cat(t.get("title", ""), t.get("artist", ""))
            t["category"] = resolved
            if resolved in grouped:
                grouped[resolved].append(t)
            else:
                grouped["Outros"].append(t)

    with open("player_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    html_content = template \
        .replace("__LIBRARY_COUNT__", str(len(library))) \
        .replace("__SPOTIFY_COUNT__", f"{len(spotify_catalog)} Playlists") \
        .replace("__SPOTIFY_COUNT_NUM__", str(len(spotify_catalog))) \
        .replace("__DATA_JSON__", json.dumps(grouped, ensure_ascii=False)) \
        .replace("__ICONS_JSON__", json.dumps(CATEGORY_ICONS, ensure_ascii=False)) \
        .replace("__CATEGORIES_JSON__", json.dumps(CATEGORY_ORDER, ensure_ascii=False)) \
        .replace("__SPOTIFY_PLAYLISTS_JSON__", json.dumps(spotify_catalog, ensure_ascii=False))

    with open("player.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    return True

if __name__ == "__main__":
    rebuild_player_html()
    print("Build concluído com sucesso: player.html gerado!")
