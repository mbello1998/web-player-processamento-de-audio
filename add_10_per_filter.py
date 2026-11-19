# -*- coding: utf-8 -*-
"""
add_10_per_filter.py
Adiciona 10 playlists novas para cada um dos 11 chips de genero reais da aba Playlists
Spotify (top, sertanejo, funk, rap, pagode, eletronica, latino, cumbia, fiestero,
fronteira, rock, treino), seguindo o mesmo padrao do catalogo existente: metadados +
faixas reais amostradas das categorias correspondentes de complete_library.json
(mesma tecnica do generate_100_spotify_playlists.py original), sem sobrescrever nada
que ja existe no catalogo.
"""

import json
import random
from pathlib import Path

LIBRARY_FILE = Path("complete_library.json")
SPOTIFY_FILE = Path("spotify_playlists_catalog.json")

with open(LIBRARY_FILE, "r", encoding="utf-8") as f:
    library = json.load(f)
with open(SPOTIFY_FILE, "r", encoding="utf-8") as f:
    existing_catalog = json.load(f)

by_cat = {}
for t in library:
    by_cat.setdefault(t.get("category", "Outros"), []).append(t)

SERT_UNI = "Sertanejo Universitário & Atual"
SERT_ANT = "Sertanejo Antigo & Modão"
FUNK = "Funk Paulista, BH & Mandelão"
MEGA = "Mega Funk & Ritmadas"
LATINO = "Reggaeton, Cachengue & Latino"
ELETRO = "Eletrônica, House & Desande"
TRAP = "Trap & Rap Nacional"
PAGODE = "Samba & Pagode"
ROCK = "Rock & Pop Nostalgia"

NEW_PLAYLISTS = [
    # ===== TOP (chart geral - precisa de "top"/viral/tiktok/radar/semana/360/globais/all-stars) =====
    {"id": "top_20_brasil_diario", "name": "Top 20 Brasil Diário", "badge": "📊 Top 20 Diário", "icon": "📊", "genre": "Ranking Diário Geral", "desc": "As vinte faixas mais ouvidas no Brasil hoje, atualizadas todo dia.", "bpm": 128, "cats": [SERT_UNI, FUNK, MEGA]},
    {"id": "top_feminino_brasil", "name": "Top Feminino Brasil", "badge": "💜 Top Feminino", "icon": "💜", "genre": "Vozes Femininas em Alta", "desc": "As maiores artistas mulheres do momento em todos os ritmos do país.", "bpm": 126, "cats": [SERT_UNI, PAGODE]},
    {"id": "top_gringo_brasil", "name": "Top Gringo no Brasil", "badge": "🌎 Top Gringo", "icon": "🌎", "genre": "Internacional em Alta no BR", "desc": "Os hits internacionais que mais tocam nas rádios e festas brasileiras.", "bpm": 118, "cats": [ELETRO, LATINO]},
    {"id": "viral_tiktok_brasil_2", "name": "Viral TikTok Brasil Vol. 2", "badge": "📱 Viral TikTok 2", "icon": "📱", "genre": "Trends & Dancinhas", "desc": "Mais um round de músicas que viraram febre nos vídeos e desafios do TikTok.", "bpm": 136, "cats": [MEGA, FUNK]},
    {"id": "radar_internacional", "name": "Radar Internacional", "badge": "📡 Radar Internacional", "icon": "📡", "genre": "Novidades do Mundo", "desc": "Artistas emergentes de fora do Brasil que estão prestes a estourar por aqui.", "bpm": 120, "cats": [ELETRO, LATINO]},
    {"id": "top_remix_brasil", "name": "Top Remix Brasil", "badge": "🔄 Top Remix", "icon": "🔄", "genre": "Remixes em Alta", "desc": "As versões remixadas que estão dominando pistas e playlists do país.", "bpm": 130, "cats": [MEGA, ELETRO]},
    {"id": "globais_da_semana", "name": "Globais da Semana", "badge": "🌐 Globais da Semana", "icon": "🌐", "genre": "Ranking Mundial Semanal", "desc": "O resumo semanal das faixas mais ouvidas no planeta inteiro.", "bpm": 122, "cats": [LATINO, ELETRO]},
    {"id": "top_estrelas_latino_br", "name": "Top Estrelas Latino-BR", "badge": "⭐ Top Estrelas", "icon": "⭐", "genre": "Cruzamento Latino & Brasileiro", "desc": "Os maiores nomes do Brasil e da América Latina juntos numa só seleção.", "bpm": 118, "cats": [LATINO, SERT_UNI]},
    {"id": "hits_360_atual", "name": "360° Hits Atual", "badge": "🔄 360° Hits", "icon": "🔄", "genre": "Panorama Completo BR", "desc": "Uma volta completa pelos ritmos que estão tocando em todo o Brasil agora.", "bpm": 124, "cats": [SERT_UNI, FUNK, PAGODE]},
    {"id": "top_lancamentos_mes", "name": "Top Lançamentos do Mês", "badge": "🆕 Top Lançamentos", "icon": "🆕", "genre": "Mensal de Novidades", "desc": "O melhor do que saiu de novo nas últimas quatro semanas, sem enrolação.", "bpm": 126, "cats": [SERT_UNI, TRAP, FUNK]},

    # ===== SERTANEJO =====
    {"id": "sertanejo_chuveiro", "name": "Sertanejo pra Cantar no Chuveiro", "badge": "🚿 No Chuveiro", "icon": "🚿", "genre": "Sertanejo Descontraído", "desc": "Aquelas modas que todo mundo berra cantando no banho sem vergonha nenhuma.", "bpm": 120, "cats": [SERT_UNI]},
    {"id": "duplas_sertanejas_classicas", "name": "Duplas Sertanejas Clássicas", "badge": "👬 Duplas Clássicas", "icon": "👬", "genre": "Sertanejo de Dupla", "desc": "As duplas que construíram a história do sertanejo com harmonias inesquecíveis.", "bpm": 114, "cats": [SERT_ANT, SERT_UNI]},
    {"id": "sertanejo_feminejo", "name": "Sertanejo Feminejo", "badge": "👩 Feminejo", "icon": "👩", "genre": "Vozes Sertanejas", "desc": "As cantoras que mudaram a cara do sertanejo e tomaram conta das paradas.", "bpm": 126, "cats": [SERT_UNI]},
    {"id": "sertanejo_nordestino", "name": "Sertanejo Nordestino", "badge": "🌵 Sertanejo NE", "icon": "🌵", "genre": "Sertanejo do Nordeste", "desc": "O sotaque e o balanço nordestino dentro do sertanejo que toca o Brasil todo.", "bpm": 128, "cats": [SERT_UNI]},
    {"id": "sertanejo_viola_caipira", "name": "Sertanejo Viola Caipira & Raiz", "badge": "🎻 Viola Caipira", "icon": "🎻", "genre": "Sertanejo de Raiz Instrumental", "desc": "O dedilhado da viola caipira em sua forma mais pura e tradicional.", "bpm": 100, "cats": [SERT_ANT]},
    {"id": "sertanejo_remix_eletronico", "name": "Sertanejo Remix Eletrônico", "badge": "🎛️ Sertanejo Remix", "icon": "🎛️", "genre": "Sertanejo Eletrônico", "desc": "Clássicos sertanejos ganhando batida eletrônica pra ferver a pista.", "bpm": 128, "cats": [SERT_UNI, ELETRO]},
    {"id": "sertanejo_trabalho", "name": "Sertanejo pra Trabalhar", "badge": "💼 Sertanejo no Trampo", "icon": "💼", "genre": "Sertanejo de Fundo", "desc": "Uma seleção tranquila pra acompanhar o expediente sem distrair demais.", "bpm": 110, "cats": [SERT_UNI, SERT_ANT]},
    {"id": "sertanejo_anos_2000", "name": "Sertanejo Anos 2000", "badge": "💿 Sertanejo 2000s", "icon": "💿", "genre": "Sertanejo Nostalgia 2000s", "desc": "O sertanejo romântico e de festa que marcou a virada do milênio.", "bpm": 116, "cats": [SERT_ANT, SERT_UNI]},
    {"id": "modao_de_boteco", "name": "Modão de Boteco", "badge": "🍺 Modão de Boteco", "icon": "🍺", "genre": "Modão & Resenha", "desc": "Aquele modão que só faz sentido com uma cerveja gelada do lado.", "bpm": 112, "cats": [SERT_ANT]},
    {"id": "sertanejo_de_rodeio", "name": "Sertanejo de Rodeio", "badge": "🐂 Rodeio & Sertanejo", "icon": "🐂", "genre": "Trilha de Rodeio", "desc": "A trilha sonora clássica das arenas de rodeio e festas country do interior.", "bpm": 124, "cats": [SERT_UNI, SERT_ANT]},

    # ===== FUNK =====
    {"id": "funk_melody_2000s", "name": "Funk Melody Anos 2000", "badge": "💿 Funk Melody", "icon": "💿", "genre": "Funk Melody Nostalgia", "desc": "O funk romântico e dançante que embalou as festas dos anos 2000.", "bpm": 118, "cats": [FUNK]},
    {"id": "funk_ostentacao", "name": "Funk Ostentação", "badge": "💰 Ostentação", "icon": "💰", "genre": "Funk Ostentação", "desc": "O estilo que celebra conquista, estilo de vida e muito dinheiro no bolso.", "bpm": 128, "cats": [FUNK, MEGA]},
    {"id": "funk_carioca_raiz", "name": "Funk Carioca Raiz", "badge": "🏖️ Carioca Raiz", "icon": "🏖️", "genre": "Funk Carioca Clássico", "desc": "O som que nasceu nos bailes cariocas e virou patrimônio musical do Brasil.", "bpm": 130, "cats": [FUNK]},
    {"id": "funk_bh_classico", "name": "Funk BH Clássico", "badge": "⛰️ BH Clássico", "icon": "⛰️", "genre": "Funk de Minas", "desc": "Os clássicos que consolidaram o estilo mineiro de fazer funk.", "bpm": 134, "cats": [FUNK]},
    {"id": "funk_feminino", "name": "Funk Feminino", "badge": "💄 Funk Feminino", "icon": "💄", "genre": "MCs Mulheres", "desc": "As MCs que mandam bem e dominam os maiores palcos do funk nacional.", "bpm": 136, "cats": [FUNK, MEGA]},
    {"id": "baile_funk_anos_90", "name": "Baile Funk Anos 90", "badge": "📻 Baile 90s", "icon": "📻", "genre": "Funk Vintage 90s", "desc": "Os primeiros bailes e a batida original que deu origem a tudo isso.", "bpm": 110, "cats": [FUNK]},
    {"id": "funk_160_bpm", "name": "Funk 160 BPM Insano", "badge": "🚨 160 BPM", "icon": "🚨", "genre": "Acelerado Extremo", "desc": "Pra quem acha que 150 BPM ainda é pouco: o funk no limite da velocidade.", "bpm": 160, "cats": [FUNK, MEGA]},
    {"id": "funk_romantico", "name": "Funk Romântico", "badge": "💘 Funk Romântico", "icon": "💘", "genre": "Funk de Amor", "desc": "Quando o funk desacelera pra falar de paixão e coração partido.", "bpm": 108, "cats": [FUNK]},
    {"id": "funk_fluxo_rj", "name": "Funk do Fluxo RJ", "badge": "🎪 Fluxo RJ", "icon": "🎪", "genre": "Fluxo Carioca", "desc": "A energia crua dos maiores fluxos espalhados pelo Rio de Janeiro.", "bpm": 142, "cats": [FUNK]},
    {"id": "mandelao_de_verao", "name": "Mandelão de Verão", "badge": "🏝️ Mandelão Verão", "icon": "🏝️", "genre": "Mandelão de Praia", "desc": "A trilha perfeita pra praia, piscina e calor com grave no talo.", "bpm": 138, "cats": [FUNK, MEGA]},

    # ===== RAP / TRAP =====
    {"id": "rap_nacional_consciente", "name": "Rap Nacional Consciente", "badge": "✊ Rap Consciente", "icon": "✊", "genre": "Mensagem & Crítica Social", "desc": "Rimas que denunciam, refletem e inspiram mudança de verdade.", "bpm": 92, "cats": [TRAP]},
    {"id": "trap_feminino_brasil", "name": "Trap Brasileiro Feminino", "badge": "👑 Trap Feminino", "icon": "👑", "genre": "Trap de Mulheres", "desc": "As vozes femininas que dominam a cena trap nacional sem pedir licença.", "bpm": 136, "cats": [TRAP]},
    {"id": "batalha_de_rimas", "name": "Freestyle & Batalha de Rimas", "badge": "🎙️ Batalha de Rimas", "icon": "🎙️", "genre": "Freestyle & Competição", "desc": "A arte da improvisação e do confronto de rimas que vem das batalhas de rua.", "bpm": 96, "cats": [TRAP]},
    {"id": "trap_soul_brasil", "name": "Trap Soul Brasil", "badge": "🎹 Trap Soul", "icon": "🎹", "genre": "Trap Soul & R&B", "desc": "A fusão entre o groove do soul e a produção moderna do trap nacional.", "bpm": 90, "cats": [TRAP]},
    {"id": "rap_old_school_br", "name": "Rap Old School BR", "badge": "📼 Old School BR", "icon": "📼", "genre": "Rap dos Anos 90", "desc": "As batidas e os flows que fundaram o rap brasileiro como conhecemos hoje.", "bpm": 93, "cats": [TRAP]},
    {"id": "drill_paulista", "name": "Drill Paulista", "badge": "🗡️ Drill Paulista", "icon": "🗡️", "genre": "Drill de São Paulo", "desc": "A cena drill que vem crescendo forte nas periferias de São Paulo.", "bpm": 142, "cats": [TRAP]},
    {"id": "rap_romantico", "name": "Rap Romântico", "badge": "💌 Rap Romântico", "icon": "💌", "genre": "Trap & Rap de Amor", "desc": "Quando o flow desacelera e as rimas falam só de amor e saudade.", "bpm": 88, "cats": [TRAP]},
    {"id": "trap_808_pesado", "name": "Trap 808 Pesado", "badge": "🔊 808 Pesado", "icon": "🔊", "genre": "Trap de Grave Pesado", "desc": "Sub-bass profundo e 808s que fazem o carro inteiro tremer.", "bpm": 140, "cats": [TRAP]},
    {"id": "flow_autoral_br", "name": "Flow Autoral BR", "badge": "✒️ Flow Autoral", "icon": "✒️", "genre": "Autoral & Independente", "desc": "Artistas independentes construindo um flow só deles, sem fórmula pronta.", "bpm": 100, "cats": [TRAP]},
    {"id": "hip_hop_underground_br", "name": "Hip Hop Underground BR", "badge": "🕳️ Underground BR", "icon": "🕳️", "genre": "Cena Alternativa Hip Hop", "desc": "O que rola fora do mainstream: produções cruas direto da cena local.", "bpm": 94, "cats": [TRAP]},

    # ===== PAGODE / SAMBA =====
    {"id": "pagode_baiano", "name": "Pagode Baiano", "badge": "🌴 Pagode Baiano", "icon": "🌴", "genre": "Pagode da Bahia", "desc": "O suingue único do pagode baiano, irmão direto do samba e do axé.", "bpm": 118, "cats": [PAGODE]},
    {"id": "partido_alto_classico", "name": "Partido Alto & Samba Clássico", "badge": "🎼 Partido Alto", "icon": "🎼", "genre": "Partido Alto", "desc": "A tradição do improviso e do refrão repetido nas rodas mais raiz.", "bpm": 108, "cats": [PAGODE]},
    {"id": "pagode_vintage_90s", "name": "Pagode Vintage 90s", "badge": "📼 Pagode 90s", "icon": "📼", "genre": "Pagode Romântico Vintage", "desc": "O pagode romântico que fez sucesso e embalou casamentos nos anos 90.", "bpm": 110, "cats": [PAGODE]},
    {"id": "roda_de_samba_vivo", "name": "Roda de Samba ao Vivo", "badge": "🥁 Roda ao Vivo", "icon": "🥁", "genre": "Samba ao Vivo", "desc": "A energia de uma roda de samba de verdade, com direito a palma e clima de quintal.", "bpm": 112, "cats": [PAGODE]},
    {"id": "pagode_romantico_atual", "name": "Pagode Romântico Atual", "badge": "💕 Pagode Romântico", "icon": "💕", "genre": "Pagode Romântico Moderno", "desc": "As novas composições de amor que seguem a tradição do pagode romântico.", "bpm": 114, "cats": [PAGODE]},
    {"id": "samba_de_breque", "name": "Samba de Breque", "badge": "🛑 Samba de Breque", "icon": "🛑", "genre": "Samba de Breque", "desc": "Aquele samba que para o tempo todo pra contar uma historinha engraçada.", "bpm": 106, "cats": [PAGODE]},
    {"id": "pagode_trabalho", "name": "Pagode pra Trabalhar", "badge": "💼 Pagode no Trampo", "icon": "💼", "genre": "Pagode de Fundo", "desc": "Um clima leve de pagode pra acompanhar o dia de trabalho sem pesar.", "bpm": 110, "cats": [PAGODE]},
    {"id": "sambinha_fim_tarde", "name": "Sambinha de Fim de Tarde", "badge": "🌇 Sambinha Fim de Tarde", "icon": "🌇", "genre": "Samba Leve", "desc": "Aquele sambinha gostoso pra receber o fim de tarde com a galera.", "bpm": 108, "cats": [PAGODE]},
    {"id": "pagode_paulista", "name": "Pagode Paulista", "badge": "🏙️ Pagode Paulista", "icon": "🏙️", "genre": "Pagode de São Paulo", "desc": "A cena pagodeira que cresceu forte na capital e no interior paulista.", "bpm": 116, "cats": [PAGODE]},
    {"id": "classicos_samba_enredo", "name": "Clássicos do Samba Enredo", "badge": "🎺 Samba Enredo", "icon": "🎺", "genre": "Samba Enredo de Carnaval", "desc": "Os sambas enredo que já desfilaram pela avenida e ficaram pra história.", "bpm": 128, "cats": [PAGODE]},

    # ===== ELETRÔNICA =====
    {"id": "progressive_house_brasil", "name": "Progressive House Brasil", "badge": "🌀 Progressive House", "icon": "🌀", "genre": "Progressive House", "desc": "Camadas que evoluem devagar até explodir num drop satisfatório.", "bpm": 124, "cats": [ELETRO]},
    {"id": "techno_club_underground", "name": "Techno Club Underground BR", "badge": "🕳️ Techno Underground", "icon": "🕳️", "genre": "Techno de Club", "desc": "Batida hipnótica e repetitiva direto das pistas de clube mais exigentes.", "bpm": 128, "cats": [ELETRO]},
    {"id": "festival_edm_mainstage", "name": "Festival EDM Mainstage 2026", "badge": "🎪 Mainstage 2026", "icon": "🎪", "genre": "EDM de Festival", "desc": "As produções feitas pra explodir no palco principal dos maiores festivais.", "bpm": 128, "cats": [ELETRO]},
    {"id": "future_bass_brasil", "name": "Future Bass Brasil", "badge": "🔮 Future Bass", "icon": "🔮", "genre": "Future Bass", "desc": "Synths coloridos e quebras rítmicas que definem o som do futuro.", "bpm": 150, "cats": [ELETRO]},
    {"id": "afro_house_tropical", "name": "Afro House Tropical", "badge": "🌍 Afro House", "icon": "🌍", "genre": "Afro House", "desc": "Percussão africana encontrando a batida eletrônica num groove tropical.", "bpm": 122, "cats": [ELETRO]},
    {"id": "melodic_house_sunset", "name": "Melodic House Sunset", "badge": "🌅 Melodic House", "icon": "🌅", "genre": "Melodic House & Techno", "desc": "Melodias emotivas pra acompanhar o sol se pondo no horizonte.", "bpm": 120, "cats": [ELETRO]},
    {"id": "big_room_edm_anthems", "name": "Big Room EDM Anthems", "badge": "💥 Big Room", "icon": "💥", "genre": "Big Room EDM", "desc": "Drops massivos feitos pra levantar o público inteiro de uma vez.", "bpm": 128, "cats": [ELETRO]},
    {"id": "drum_bass_brasil", "name": "Drum & Bass Brasil", "badge": "🥁 D&B Brasil", "icon": "🥁", "genre": "Drum & Bass", "desc": "Breaks acelerados e baixo profundo numa velocidade que não para.", "bpm": 174, "cats": [ELETRO]},
    {"id": "club_remix_nacional", "name": "Club Remix Nacional", "badge": "🎚️ Club Remix", "icon": "🎚️", "genre": "Remix de Club", "desc": "Hits nacionais ganhando nova vida em versões feitas pra pista.", "bpm": 126, "cats": [ELETRO, SERT_UNI]},
    {"id": "trance_edm_journey", "name": "Trance & EDM Journey BR", "badge": "🌌 Trance Journey", "icon": "🌌", "genre": "Trance & EDM Melódico", "desc": "Uma jornada sonora hipnótica que cresce devagar até o clímax.", "bpm": 136, "cats": [ELETRO]},

    # ===== LATINO (reggaeton/cachengue) =====
    {"id": "reggaeton_old_school", "name": "Reggaeton Old School", "badge": "📻 Reggaeton Old School", "icon": "📻", "genre": "Reggaeton Clássico", "desc": "As raízes do reggaeton que vieram de Porto Rico e Panamá pro mundo todo.", "bpm": 94, "cats": [LATINO]},
    {"id": "perreo_intenso", "name": "Perreo Intenso", "badge": "🔥 Perreo Intenso", "icon": "🔥", "genre": "Perreo", "desc": "Pra quem não tem medo de descer até o chão no ritmo do perreo.", "bpm": 98, "cats": [LATINO]},
    {"id": "rkt_fiestero_2", "name": "RKT Fiestero Vol. 2", "badge": "🇦🇷 RKT Fiestero 2", "icon": "🇦🇷", "genre": "RKT & Cachengue", "desc": "Mais uma dose do RKT argentino que não sai da cabeça desde que estourou.", "bpm": 104, "cats": [LATINO]},
    {"id": "dembow_dominicano", "name": "Dembow Dominicano", "badge": "🇩🇴 Dembow DO", "icon": "🇩🇴", "genre": "Dembow", "desc": "O ritmo cru e direto que dominou as ruas da República Dominicana.", "bpm": 108, "cats": [LATINO]},
    {"id": "reggaeton_romantico", "name": "Reggaeton Romántico", "badge": "💞 Reggaeton Romântico", "icon": "💞", "genre": "Reggaeton de Amor", "desc": "Quando o reggaeton desacelera pra falar só de amor e desejo.", "bpm": 90, "cats": [LATINO]},
    {"id": "trap_latino_hits", "name": "Trap Latino Hits", "badge": "💎 Trap Latino", "icon": "💎", "genre": "Trap Latino", "desc": "A fusão entre o trap americano e as raízes urbanas latinas.", "bpm": 130, "cats": [LATINO, TRAP]},
    {"id": "cachengue_remix", "name": "Cachengue Remix", "badge": "🎧 Cachengue Remix", "icon": "🎧", "genre": "Cachengue", "desc": "Versões remixadas do cachengue argentino feitas pra previa e boliche.", "bpm": 126, "cats": [LATINO]},
    {"id": "latino_pop_urbano", "name": "Latino Pop Urbano", "badge": "🌆 Latino Pop", "icon": "🌆", "genre": "Pop Urbano Latino", "desc": "Produções pop com DNA urbano que dominam as rádios latinas.", "bpm": 100, "cats": [LATINO]},
    {"id": "reggaeton_colombiano", "name": "Reggaeton Colombiano", "badge": "🇨🇴 Reggaeton CO", "icon": "🇨🇴", "genre": "Reggaeton da Colômbia", "desc": "Medellín e Bogotá exportando o reggaeton mais pop da América Latina.", "bpm": 96, "cats": [LATINO]},
    {"id": "bachata_latina_urbana", "name": "Bachata Latina Urbana", "badge": "💃 Bachata Urbana", "icon": "💃", "genre": "Bachata Urbana & Reggaeton", "desc": "A bachata tradicional se misturando com o som urbano latino atual.", "bpm": 126, "cats": [LATINO]},

    # ===== CUMBIA (artistas reais) =====
    {"id": "rafaga_cumbia_pop", "name": "Ráfaga – Cumbia Pop Argentina", "badge": "🎷 Ráfaga", "icon": "🎷", "genre": "Cumbia Pop Argentina", "desc": "Um dos grupos mais vendidos da cumbia argentina, com décadas de hits.", "bpm": 110, "cats": [LATINO]},
    {"id": "walter_olmos_principe", "name": "Walter Olmos – El Príncipe de la Cumbia", "badge": "👑 Walter Olmos", "icon": "👑", "genre": "Cumbia Romántica Argentina", "desc": "A voz que ficou conhecida como o príncipe da cumbia romântica argentina.", "bpm": 106, "cats": [LATINO]},
    {"id": "agua_marina_cumbia_peruana", "name": "Agua Marina – Cumbia Peruana", "badge": "🌊 Agua Marina", "icon": "🌊", "genre": "Cumbia Peruana", "desc": "Um dos grupos mais tradicionais e amados da cumbia do norte do Peru.", "bpm": 112, "cats": [LATINO]},
    {"id": "armonia_10_cumbia_sabroso", "name": "Armonía 10 – Cumbia Sonido Sabroso", "badge": "🎺 Armonía 10", "icon": "🎺", "genre": "Cumbia Peruana Moderna", "desc": "A orquesta que renovou a cumbia peruana com arranjos cheios de sabor.", "bpm": 114, "cats": [LATINO]},
    {"id": "la_delio_valdez_orquestal", "name": "La Delio Valdez – Cumbia Orquestal", "badge": "🎻 La Delio Valdez", "icon": "🎻", "genre": "Cumbia Orquestal", "desc": "Uma big band argentina que leva a cumbia pra um formato orquestral único.", "bpm": 108, "cats": [LATINO]},
    {"id": "agrupacion_marilyn_sonidera", "name": "Agrupación Marilyn – Cumbia Sonidera", "badge": "📻 Agrupación Marilyn", "icon": "📻", "genre": "Cumbia Sonidera Mexicana", "desc": "Um clássico da cumbia sonidera que toca nos alto-falantes dos bairros mexicanos.", "bpm": 100, "cats": [LATINO]},
    {"id": "antonio_rios_romantico", "name": "Antonio Ríos – Cumbia Romántica de Siempre", "badge": "🌹 Antonio Ríos", "icon": "🌹", "genre": "Cumbia Romántica Clásica", "desc": "Uma das vozes mais queridas da era de ouro da cumbia romântica argentina.", "bpm": 104, "cats": [LATINO]},
    {"id": "daniel_agostini_pibe_oro", "name": "Daniel Agostini – Cumbia El Pibe de Oro", "badge": "🏅 Daniel Agostini", "icon": "🏅", "genre": "Cumbia Romántica Argentina", "desc": "Conhecido como o Pibe de Oro, um ícone da cumbia romântica dos anos 90.", "bpm": 106, "cats": [LATINO]},
    {"id": "comanche_cumbia_clasica", "name": "Comanche – Cumbia Clásica", "badge": "🪶 Comanche", "icon": "🪶", "genre": "Cumbia Clásica Argentina", "desc": "Uma das bandas mais tradicionais da cumbia romântica argentina dos anos 90.", "bpm": 108, "cats": [LATINO]},
    {"id": "grupo_aka_nueva_cumbia", "name": "Grupo AKA – Cumbia Nueva Generación", "badge": "🆕 Grupo AKA", "icon": "🆕", "genre": "Cumbia Nova Geração", "desc": "A nova geração que reinventa a cumbia argentina com som mais moderno.", "bpm": 116, "cats": [LATINO]},

    # ===== FIESTERO (enganchado/previa/boliche) =====
    {"id": "enganchados_fiesteros_2", "name": "Enganchados Fiesteros Vol. 2", "badge": "🎉 Enganchados 2", "icon": "🎉", "genre": "Enganchado Fiestero", "desc": "Mais um enganchado não-stop pra manter a festa animada do início ao fim.", "bpm": 126, "cats": [LATINO]},
    {"id": "previa_remix_2026", "name": "Previa Remix 2026", "badge": "🥂 Previa Remix", "icon": "🥂", "genre": "Previa & Remix", "desc": "Os remixes perfeitos pra esquentar antes de sair pro boliche.", "bpm": 124, "cats": [LATINO]},
    {"id": "mix_boliche_cachengue", "name": "Mix Boliche Cachengue", "badge": "🪩 Boliche Cachengue", "icon": "🪩", "genre": "Boliche & Cachengue", "desc": "O mix que não pode faltar na pista de qualquer boliche argentino.", "bpm": 128, "cats": [LATINO]},
    {"id": "fiestero_clasico_enganchado", "name": "Fiestero Clásico Enganchado", "badge": "🕺 Fiestero Clásico", "icon": "🕺", "genre": "Fiestero Clássico", "desc": "Os enganchados que já viraram clássico em qualquer previa que se preze.", "bpm": 122, "cats": [LATINO]},
    {"id": "previa_argentina_hits", "name": "Previa Argentina Hits", "badge": "🇦🇷 Previa Argentina", "icon": "🇦🇷", "genre": "Previa Argentina", "desc": "Os hits que tocam em toda previa argentina antes de cair na noite.", "bpm": 126, "cats": [LATINO]},
    {"id": "enganchado_cumbia_pop", "name": "Enganchado Cumbia Pop", "badge": "🎶 Enganchado Pop", "icon": "🎶", "genre": "Cumbia Pop Enganchada", "desc": "Cumbia pop em formato não-stop, uma música emendando na outra sem parar.", "bpm": 118, "cats": [LATINO]},
    {"id": "boliche_latino_mix", "name": "Boliche Latino Mix", "badge": "🌃 Boliche Latino", "icon": "🌃", "genre": "Boliche Latino", "desc": "A seleção latina completa pra fechar a noite na pista de dança.", "bpm": 124, "cats": [LATINO]},
    {"id": "fiestero_verao_2026", "name": "Fiestero Verão 2026", "badge": "☀️ Fiestero Verão", "icon": "☀️", "genre": "Fiestero de Verão", "desc": "A trilha fiestera perfeita pro calor, a praia e as festas de verão.", "bpm": 128, "cats": [LATINO]},
    {"id": "previa_boliche_remix_2", "name": "Previa Boliche Remix 2", "badge": "🔁 Previa Remix 2", "icon": "🔁", "genre": "Previa & Boliche Remix", "desc": "Mais remixes de previa pra deixar o clima pronto antes da balada.", "bpm": 126, "cats": [LATINO]},
    {"id": "enganchados_fim_semana", "name": "Enganchados de Fin de Semana", "badge": "🗓️ Enganchados FDS", "icon": "🗓️", "genre": "Enganchado de Fim de Semana", "desc": "O enganchado perfeito pra abrir o fim de semana com o pé direito.", "bpm": 124, "cats": [LATINO]},

    # ===== FRONTEIRA (Quaraí/Artigas, artistas reais) =====
    {"id": "mano_lima_trova_gaucha", "name": "Mano Lima – Trova Gaúcha Clássica", "badge": "🪕 Mano Lima", "icon": "🪕", "genre": "Trova Gaúcha", "desc": "Um dos maiores nomes da trova e do nativismo musical do Rio Grande do Sul.", "bpm": 92, "cats": [SERT_ANT]},
    {"id": "luiz_marenco_nativismo", "name": "Luiz Marenco – Nativismo Gaúcho", "badge": "🤠 Luiz Marenco", "icon": "🤠", "genre": "Nativismo Gaúcho", "desc": "Uma referência viva da música nativista e tradicionalista gaúcha.", "bpm": 96, "cats": [SERT_ANT]},
    {"id": "baitaca_vanerao", "name": "Baitaca – Vaneirão Tradicional", "badge": "🎷 Baitaca", "icon": "🎷", "genre": "Vaneirão", "desc": "Um dos grupos mais tradicionais do vaneirão, ritmo típico da fronteira sul.", "bpm": 98, "cats": [SERT_ANT]},
    {"id": "joca_martins_fronteira_raiz", "name": "Joca Martins – Fronteira Raiz", "badge": "🧉 Joca Martins", "icon": "🧉", "genre": "Música de Fronteira", "desc": "O som autêntico da fronteira entre o Rio Grande do Sul e o Uruguai.", "bpm": 100, "cats": [SERT_ANT]},
    {"id": "lucas_sugo_cumbia_uruguaia", "name": "Lucas Sugo – Cumbia Uruguaia", "badge": "🇺🇾 Lucas Sugo", "icon": "🇺🇾", "genre": "Cumbia Uruguaia", "desc": "Um dos maiores nomes atuais da cumbia romântica no Uruguai.", "bpm": 108, "cats": [LATINO]},
    {"id": "grupo_vagalume_charanga", "name": "Grupo Vagalume – Charanga de Fronteira", "badge": "🎺 Grupo Vagalume", "icon": "🎺", "genre": "Charanga de Fronteira", "desc": "A charanga animada que toca nos bailes de toda a linha de fronteira.", "bpm": 110, "cats": [LATINO]},
    {"id": "os_serranos_campeira", "name": "Os Serranos – Música Campeira da Fronteira", "badge": "🐴 Os Serranos", "icon": "🐴", "genre": "Música Campeira da Fronteira", "desc": "O som campeiro tradicionalista que representa a cultura gaúcha de verdade.", "bpm": 94, "cats": [SERT_ANT]},
    {"id": "chimarrita_vanerao_mix", "name": "Chimarrita & Vanerão da Fronteira", "badge": "💃 Chimarrita & Vanerão", "icon": "💃", "genre": "Chimarrita & Vanerão da Fronteira", "desc": "Os ritmos de salão mais dançados nos bailes tradicionalistas do Sul.", "bpm": 102, "cats": [SERT_ANT]},
    {"id": "fandango_fronteira", "name": "Fandango da Fronteira", "badge": "🎻 Fandango", "icon": "🎻", "genre": "Fandango Gaúcho", "desc": "O fandango animado que faz parte da tradição musical da fronteira.", "bpm": 104, "cats": [SERT_ANT]},
    {"id": "rancheira_charanga_sul", "name": "Rancheira & Charanga do Sul", "badge": "🤠 Rancheira & Charanga", "icon": "🤠", "genre": "Rancheira Gaúcha", "desc": "A rancheira tradicional que embala os galpões e bailes do extremo sul.", "bpm": 98, "cats": [SERT_ANT]},

    # ===== ROCK / POP / MPB =====
    {"id": "rock_alternativo_br", "name": "Rock Alternativo BR", "badge": "🎸 Alternativo BR", "icon": "🎸", "genre": "Rock Alternativo Nacional", "desc": "As bandas que fogem da fórmula e constroem um rock nacional mais autoral.", "bpm": 118, "cats": [ROCK]},
    {"id": "mpb_instrumental", "name": "MPB Instrumental", "badge": "🎷 MPB Instrumental", "icon": "🎷", "genre": "MPB Instrumental", "desc": "A riqueza harmônica da MPB sem letra nenhuma, só a música falando.", "bpm": 98, "cats": [ROCK]},
    {"id": "pop_rock_2000s", "name": "Pop Rock Nacional 2000s", "badge": "📀 Pop Rock 2000s", "icon": "📀", "genre": "Pop Rock Anos 2000", "desc": "As bandas pop rock que tocaram em toda rádio brasileira nos anos 2000.", "bpm": 124, "cats": [ROCK]},
    {"id": "bossa_nova_classica", "name": "Bossa Nova Clássica", "badge": "🌴 Bossa Nova", "icon": "🌴", "genre": "Bossa Nova & MPB", "desc": "O balanço suave que nasceu no Rio e conquistou o mundo inteiro.", "bpm": 92, "cats": [ROCK]},
    {"id": "rock_gaucho", "name": "Rock Gaúcho", "badge": "🎸 Rock Gaúcho", "icon": "🎸", "genre": "Rock do Sul", "desc": "A cena rockeira que nasceu e cresceu forte no Rio Grande do Sul.", "bpm": 122, "cats": [ROCK]},
    {"id": "indie_brasil", "name": "Indie Brasil", "badge": "🎨 Indie BR", "icon": "🎨", "genre": "Indie Pop Nacional", "desc": "Produções independentes que fogem do mainstream com personalidade própria.", "bpm": 112, "cats": [ROCK]},
    {"id": "axe_anos_2000", "name": "Axé Anos 2000", "badge": "🥁 Axé 2000s", "icon": "🥁", "genre": "Axé Music 2000s", "desc": "O axé que dominou o carnaval e as rádios na virada dos anos 2000.", "bpm": 132, "cats": [ROCK, PAGODE]},
    {"id": "forro_pe_de_serra", "name": "Forró Pé de Serra", "badge": "🪗 Pé de Serra", "icon": "🪗", "genre": "Forró & MPB Tradicional", "desc": "Sanfona, zabumba e triângulo no forró mais raiz que existe.", "bpm": 110, "cats": [SERT_ANT, ROCK]},
    {"id": "rock_progressivo_br", "name": "Rock Progressivo BR", "badge": "🌀 Progressivo BR", "icon": "🌀", "genre": "Rock Progressivo", "desc": "Composições complexas e mudanças de clima dentro de uma só música.", "bpm": 116, "cats": [ROCK]},
    {"id": "flashback_internacional_80s", "name": "Flashback Internacional 80s", "badge": "🕺 Flashback Intl 80s", "icon": "🕺", "genre": "Flashback Internacional", "desc": "Os clássicos internacionais dos anos 80 que tocaram no mundo inteiro.", "bpm": 120, "cats": [ROCK]},

    # ===== TREINO / VIBES =====
    {"id": "treino_hiit_extremo", "name": "Treino HIIT Extremo", "badge": "🔥 HIIT Extremo", "icon": "🔥", "genre": "Treino Intervalado", "desc": "Picos de energia pra acompanhar cada intervalo intenso do HIIT.", "bpm": 150, "cats": [FUNK, MEGA, ELETRO]},
    {"id": "corrida_na_academia", "name": "Corrida na Academia", "badge": "🏃 Corrida Academia", "icon": "🏃", "genre": "Cardio de Academia", "desc": "O ritmo certo pra manter o passo firme na esteira até o fim do treino.", "bpm": 145, "cats": [FUNK, ELETRO]},
    {"id": "sunset_na_praia", "name": "Sunset na Praia", "badge": "🌅 Sunset Praia", "icon": "🌅", "genre": "Pôr do Sol Tropical", "desc": "A trilha perfeita pra ver o sol se pôr com os pés na areia.", "bpm": 118, "cats": [ELETRO, LATINO]},
    {"id": "pool_session_remix", "name": "Pool Session Remix", "badge": "🏊 Pool Session", "icon": "🏊", "genre": "Festa de Piscina Remix", "desc": "Remixes animados pra manter a festa na piscina o dia inteiro.", "bpm": 124, "cats": [ELETRO, LATINO]},
    {"id": "estrada_afora", "name": "Estrada Afora", "badge": "🚗 Estrada Afora", "icon": "🚗", "genre": "Viagem de Estrada", "desc": "Pra rodar quilômetros de estrada com a janela aberta e boa companhia.", "bpm": 120, "cats": [SERT_UNI, ROCK]},
    {"id": "sitio_descanso", "name": "Sítio & Descanso", "badge": "🏡 Sítio & Descanso", "icon": "🏡", "genre": "Clima de Sítio", "desc": "Aquela paz de fim de semana no sítio longe da correria da cidade.", "bpm": 108, "cats": [SERT_ANT, SERT_UNI]},
    {"id": "almoco_familia_2", "name": "Almoço em Família Vol. 2", "badge": "🍝 Almoço Família 2", "icon": "🍝", "genre": "Reunião em Família", "desc": "Mais uma seleção gostosa pra tocar no almoço de domingo em família.", "bpm": 112, "cats": [SERT_ANT, PAGODE]},
    {"id": "relax_total_instrumental", "name": "Relax Total Instrumental", "badge": "🧘 Relax Instrumental", "icon": "🧘", "genre": "Instrumental Relaxante", "desc": "Só instrumentais suaves pra desligar a mente de verdade.", "bpm": 80, "cats": [ROCK]},
    {"id": "lofi_para_estudar", "name": "Lofi pra Estudar", "badge": "📚 Lofi Estudo", "icon": "📚", "genre": "Lofi de Estudo", "desc": "Batidas lo-fi constantes pra manter o foco durante horas de estudo.", "bpm": 82, "cats": [ROCK, TRAP]},
    {"id": "carro_estrada_vibes", "name": "Carro & Estrada Vibes", "badge": "🚙 Carro & Estrada", "icon": "🚙", "genre": "Vibe de Carro", "desc": "O som ideal pra tocar no carro em qualquer trajeto, curto ou longo.", "bpm": 122, "cats": [SERT_UNI, FUNK]},
]


def main():
    added = 0
    skipped = 0
    for pl in NEW_PLAYLISTS:
        pl_id = pl["id"]
        if pl_id in existing_catalog:
            print(f"  JA EXISTE, pulando: {pl_id}")
            skipped += 1
            continue

        candidate_tracks = []
        for cat in pl["cats"]:
            candidate_tracks.extend(by_cat.get(cat, []))
        if not candidate_tracks:
            candidate_tracks = library[:]

        rng = random.Random(pl_id)
        selected = rng.sample(candidate_tracks, min(len(candidate_tracks), rng.randint(12, 20)))

        tracks = []
        for i, t in enumerate(selected, 1):
            tracks.append({
                "rank": i,
                "title": t.get("title", ""),
                "artist": t.get("artist", ""),
                "category": pl["name"],
                "playlist_id": pl_id,
                "playlist_badge": pl["badge"],
                "video_id": t.get("video_id", ""),
                "duration": 180,
                "bpm": t.get("bpm", pl["bpm"]),
                "source": f"Spotify - {pl['name']}"
            })

        meta = {
            "id": pl_id,
            "name": pl["name"],
            "badge": pl["badge"],
            "icon": pl["icon"],
            "genre": pl["genre"],
            "desc": pl["desc"],
            "bpm": pl["bpm"]
        }
        existing_catalog[pl_id] = {"meta": meta, "tracks": tracks}
        added += 1

    with open(SPOTIFY_FILE, "w", encoding="utf-8") as f:
        json.dump(existing_catalog, f, ensure_ascii=False, indent=2)

    print(f"\nAdicionadas: {added} | Ja existiam (puladas): {skipped}")
    print(f"Total de definicoes no script: {len(NEW_PLAYLISTS)}")
    print(f"Total no catalogo agora: {len(existing_catalog)}")


if __name__ == "__main__":
    main()
