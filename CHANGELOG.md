# Changelog

Histórico funcional do player (`assets/js/player.js`, `assets/css/player.css`,
`player.html`/`player_template.html`), reconstruído a partir dos relatórios
de sessão deixados pelo Antigravity (outro assistente de código, da Google)
que trabalhou neste projeto antes desta sessão.

**Como ler isto:** cada entrada é o auto-relato daquela sessão do Antigravity
sobre o que ela implementou/corrigiu — não foi reverificado linha a linha por
esta sessão, exceto onde indicado. Não existem commits ou snapshots de código
correspondentes a cada entrada; o histórico do Git começa na tag
`baseline-pre-mixer`, que já contém o resultado acumulado de tudo listado
aqui. Esta lista serve para entender a ordem e o motivo das mudanças, não
para reverter para um ponto intermediário específico.

Fonte: `~/.gemini/antigravity/brain/4e736382-dc90-49a2-8585-11cbf9578576/*.md`
(35 relatórios, 2026-11-15 06:03 → 2026-11-17 00:44).

## 2026-11-15

- **06:03** — Spotify DJ Mixer & transição com fade: correção do esmagamento
  visual dos cards de deck (A/B), estouro de texto na troca de músicas, e
  erro 404 do favicon.
- **07:05** — Atualizações e validação geral do player.
- **13:03** — Auto DJ Platters (discos de vinil animados) e efeitos visuais —
  verificação completa.
- **13:38** — Implementação e validação: visualizador e transições do player.
- **14:03** — Implementação e validação: fila estilo Spotify e efeitos.
- **14:09** — Ajustes visuais e estilização dos botões (linha de status).
- **15:08** — Refinamento dos botões de fechar e alinhamento visual dos modais.
- **15:28** — Correção de erro 403 no streaming e padronização dos cards
  estilo Spotify.
- **15:44** — Correção dos badges dos cards, centralização do play/pause e
  da fila.
- **16:06** — Correções visuais, autoplay e layout do player.
- **16:41** — 111 playlists do Spotify, efeito entrando/saindo e sincronização
  de BPM.
- **17:32** — BPM Sync, fade gradual em tempo real e refinamentos visuais.
- **19:17** — Correções de interface, modos DJ e histórico.
- **19:42** — Correções visuais, espaçamento e modos do player.
- **19:55** — Restauração completa da interface e do player.
- **20:06** — Gerenciamento de espaço e correção de tipografia no player.
- **22:07** — Correção dos modos de atuação DJ e layout do player.
- **22:39** — 33 playlists de Cumbia; motor DJ anti-loop com expansão
  inteligente (evita repetir fora da lista).
- **23:08** — Stems DJ 3-bandas, crossover de frequências, silêncio
  inteligente; playlists Quaraí/Artigas.
- **23:42** — Modo Balada & Club DJ, efeitos especiais (FX) e HUD de
  crossover de 3 barras.

## 2026-11-16

- **00:14** — Expansão do arsenal de efeitos especiais (29 efeitos) e rotação
  inteligente por gênero.
- **01:03** — Correção do layout dos presets acústicos e Equalizador Pro.
- **11:11** — Modo Balada & Club DJ exclusivo, dropdown e efeitos sonoros.
- **11:49** — Console de Estúdio Pro e "cauda suave" nos efeitos DJ.
- **12:12** — Obediência estrita de volume e mudo em todos os efeitos.
- **17:27** — Proteção integral do refrão e "mix jumper" suave.
- **17:54** — Refrão preditivo, ajuste manual e efeitos DJ por gênero.
- **18:48** — Correção e validação dos 4 pontos visuais e do seek.
- **19:30** — Validação: exclusão e movimentação em tempo real (fila/biblioteca).
- **20:38** — Console de Estúdio Pro Extended & Mastering DSP.
- **21:02** — Correções visuais: HUD Drop Hunter e botão fechar do Studio Pro.
- **21:26** — Motor DJ Stems Pro 100% e correções visuais.
- **21:46** — Eliminação de vazamentos: motor DJ Stems multi-gênero zero-bleed.
- **22:25** — Transição de músicas desbloqueada e isolamento vocal absoluto
  (zero bleed).

## 2026-11-17

- **00:44** — Resolução definitiva de 3 problemas visuais e de DSP
  (stems, HUD e transição).

---

A partir daqui (sessão Claude, 2026-11-17) o trabalho segue versionado
normalmente no Git a partir da tag `baseline-pre-mixer` — cada entrada abaixo
corresponde a um commit de verdade (`git log baseline-pre-mixer..HEAD`), não
mais a um auto-relato reconstruído. Ao adicionar trabalho novo, continue essa
lista com uma entrada por mudança significativa.

## 2026-11-17

- **13:44** — Reconstrução deste changelog a partir dos relatórios de sessão
  do Antigravity (ponto de partida: tag `baseline-pre-mixer`).
- **14:15** — Eliminadas as 4 causas-raiz de clipping, desvio de DSP e
  vazamento entre stems.
- **14:48** — Correção do eco e da imagem estéreo desbalanceada do Studio Pro.

## 2026-11-18

- **14:56** — Eliminado o clique audível ao pular na barra de progresso
  (seek).
- **15:38** — Sugestões de "músicas parecidas" da IA ignoravam o gênero da
  faixa-semente; corrigido. Player travava ao trocar Áudio HD ↔ Clipe no meio
  de uma transição; corrigido.
- **15:49** — Trocar entre Áudio HD e Clipe no meio da faixa mantém a posição
  de reprodução.
- **16:22/16:23** — SoundCloud como segunda fonte de descoberta e playlists;
  tocar faixas do SoundCloud, mostrar a etiqueta da fonte, corrigir bugs de
  handoff/gênero.
- **16:28** — Playlists do Spotify viram uma grade de capas em vez de 150
  abas.
- **16:35** — Correção da rolagem da grade de playlists, quebra de linha dos
  filtros de gênero, capas reais do Spotify.
- **17:19** — Botão de play não fazia nada numa página recém-carregada;
  corrigido.
- **17:22** — Arquivo de credenciais da API do Spotify adicionado ao
  `.gitignore`.
- **18:16** — Cada modo de atuação DJ ganha sua própria cor de destaque.
- **20:58** — Tema de cor no site inteiro + transição animada + preset de
  gênero por modo DJ.
- **21:05** — Transição de modo lia como um "flash", não como um fade de fundo
  colorido; corrigido.
- **21:10** — Os painéis reais do player se desmontam e remontam de verdade
  ao trocar de modo.
- **21:17** — Cada card de música visível se desmonta individualmente, depois
  remonta.
- **21:35** — Cascata dos cards era instantânea em vez de escalonada;
  desacelerada para ~8,5s+.
- **21:44** — Capas reais do Spotify para as 2 playlists de Cumbia achadas por
  busca.
- **21:52/22:04** — Player ficava mudo pra sempre quando a faixa seguinte do
  crossfade falhava ao carregar (SoundCloud e depois YouTube quebrado);
  corrigido nos dois casos.

## 2026-11-19

- **04:29** — Transição de modo redesenhada: profundidade 3D de verdade +
  sequência (desmontar → carregar → remontar).
- **04:32** — Versão do asset em cache incrementada pra o navegador pegar o
  CSS/JS novo da transição.
- **04:38** — Tela de carregamento estava presa dentro do painel que ela
  precisa flutuar por cima; corrigido.
- **04:42/04:43/04:45** — Tela de hold do carregamento ganha vida: equalizador
  + brilho pulsante contínuo, partículas subindo + anel girando, faixas de
  aurora boreal fluindo no fundo.
- **04:50 a 05:18** — Várias rodadas de busca de capas reais do Spotify (89,
  depois +14, +18, +1 playlists cobertas); nova playlist de cachengue
  adicionada; filtros de gênero quebrados corrigidos; 120 playlists novas
  adicionadas aos 12 chips de filtro de gênero (10 por chip).
- **11:06** — 5ª rodada de busca acha capas reais do Spotify para mais 81
  playlists.
- **12:51** — Busca livre não ordena mais por BPM; reordenar a fila arrastando;
  confirmação de ações sem travar a tela; remover item único do histórico.
- **12:56** — Botão "Mover" do Histórico não abria o modal (o `video_id`
  sozinho não era capturado); corrigido.
- **13:01** — Filtros da Pesquisa Livre simplificados (sem mexer no Spotify).
- **13:06** — Abas de gênero da Biblioteca e Sugestões agora quebram linha em
  vez de exigir rolagem horizontal.
- **13:09** — Remover 1 música do histórico não removia de primeira nem
  notificava corretamente; corrigido.
- **13:14** — Notificação (`showToast`) ficava escondida atrás de qualquer
  modal aberto; corrigido.
- **13:29** — Auditoria geral: botões quebrados, HUD travado, UI sem estilo,
  timeouts de rede.
- **13:35** — Botão de mudo dos stems não ficava vermelho quando ativo; último
  código morto removido.
- **13:42** — Sistema de curadoria de músicas assistida por IA (favoritas por
  plays/skip rate, promoção automática).
- **13:52** — Curadoria contava cada play em dobro e diluía a taxa de skip
  pela metade; corrigido.
- **14:00** — Descoberta de músicas novas baseada nas favoritas da curadoria.
- **14:09** — Detecção de silêncio do Drop Hunter dava falso positivo quando o
  motor estava em modo "vídeo"; corrigido. Curadoria por favorita individual
  adicionada.
- **17:12** — Logo animado de fone de ouvido, animação de modal saindo do
  botão clicado, e curadoria por faixa individual (trabalho do Antigravity,
  commitado como estava, sem revisão).
- **17:28** — Logo própria (SVG por código, não mais a imagem/GIF) na
  transição de modo, voando do cabeçalho até o carregamento e de volta.
- **17:37** — Logo da transição movida pra uma camada própria (independente
  da opacidade do fundo escuro) e sequência de fases refeita na ordem certa:
  logo sai do cabeçalho → site desmonta → hold → logo volta → site remonta.
- **18:38** — Correção do voo de ida/volta da logo (posição exata do
  cabeçalho, não mais deslocada); cabeçalho entra no sistema de desmontagem
  junto com o resto do site; handoff da logo real só depois do cabeçalho
  remontar; logo troca de cor "pintando" o próprio traço ao chegar no
  carregamento; cor de destaque do site inteiro só muda depois que a
  transição termina, não mais no clique.
