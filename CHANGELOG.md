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

A partir daqui (sessão Claude, 2026-11-17), o trabalho segue versionado
normalmente no Git a partir da tag `baseline-pre-mixer`.
