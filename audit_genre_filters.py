# -*- coding: utf-8 -*-
"""
audit_genre_filters.py
Replica em Python a mesma logica de SPOTIFY_GENRE_FILTER_MAP do player.js pra auditar,
sem precisar de navegador: quais playlists nao caem em NENHUM chip de genero (orfas,
so aparecem em "Todas"), e quais caem em MAIS DE UM chip (ambiguas/conflito).
"""

import json
import re

with open("spotify_playlists_catalog.json", encoding="utf-8") as f:
    catalog = json.load(f)

PATTERNS = {
    "top": re.compile(r"\btop\b|viral|tiktok|radar|semana|360|globais|all-stars", re.I),
    "sertanejo": re.compile(r"sertanejo|modao|sofrencia|churrasco|potencia|fazenda|bruto|vaquejada|piseiro|pisadinha|arrocha|balada", re.I),
    "funk": re.compile(r"funk|mandelao|ritmada|favela|fluxo|cria|150", re.I),
    "rap": re.compile(r"rap|trap|drill|hip|poesia|rimas|flow", re.I),
    "pagode": re.compile(r"pagode|samba|resenha|churrasquinho|tardezinha|parcas|sambinha|cerveja", re.I),
    "eletronica": re.compile(r"eletronica|bass|desande|house|edm|club|vintage|alok", re.I),
    "latino": re.compile(r"reggaeton|latino|cachengue|rkt|perreo|dembow|fuego", re.I),
    "cumbia": re.compile(r"cumbia|villera|santafesina|chicha|sonidera|cuarteto|palmeras|damas|pibes|mattioli|gilda|marama|rombai|konga|luck", re.I),
    "fiestero": re.compile(r"fiestero|enganchado|previa|boliche", re.I),
    "fronteira": re.compile(r"quarai|artigas|fronteira|miriam britos|sonido profesional|chacho ramos|mano lima|baitaca|joca martins|marenco|lucas sugo|valdez|charanga|gaucho", re.I),
    "rock": re.compile(r"rock|pop|mpb|flashback|violao|axe|tchan|micareta", re.I),
    "treino": re.compile(r"treino|academia|sunset|pool|estrada|sitio|almoco|relax|lofi|chill|sextou|pre_balada|automotivo|carro|paredao", re.I),
}


def normalize_text(key, meta, include_desc):
    parts = [key, meta.get("name", ""), meta.get("genre", "")]
    if include_desc:
        parts.append(meta.get("desc", ""))
    return " ".join(parts)


orphans = []
multi = []
counts = {k: 0 for k in PATTERNS}

for key, entry in catalog.items():
    meta = entry.get("meta", {})
    matches = []
    for filt, pat in PATTERNS.items():
        include_desc = filt in ("cumbia", "fronteira", "fiestero")
        text = normalize_text(key, meta, include_desc)
        if pat.search(text):
            matches.append(filt)
            counts[filt] += 1
    if len(matches) == 0:
        orphans.append((key, meta.get("name", "")))
    elif len(matches) > 1:
        multi.append((key, meta.get("name", ""), matches))

print("=== Contagem por filtro ===")
for k, v in counts.items():
    print(f"  {k}: {v}")

print(f"\n=== Orfas (nao caem em NENHUM chip de genero, {len(orphans)}) ===")
for key, name in orphans:
    print(f"  {key} | {name}")

print(f"\n=== Em MAIS DE UM chip ({len(multi)}) ===")
for key, name, matches in multi:
    print(f"  {key} | {name} -> {matches}")
