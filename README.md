# 🎧 Web Player com Processamento de Áudio & DJ Mixer Pro

Um Web Player de alta fidelidade e sistema de discotecagem profissional executado diretamente no navegador via **Web Audio API** e **Web Animations API**, integrando catálogo híbrido (**YouTube**, **SoundCloud** e **Spotify**), processamento de sinal em tempo real (DSP), isolamento de stems zero-bleed, sincronização harmônica de BPM, curadoria de repertório assistida por IA e animações tridimensionais FLIP.

---

## 🚀 Principais Tecnologias & Funcionalidades

### 1. 🎚️ Motor de DSP & DJ Stems Pro (Zero-Bleed)
- **Isolamento de Stems em Tempo Real (3 Bandas)**: Separação cirúrgica de **Vocal**, **Bateria/Beat** e **Baixo** sem necessidade de pré-renderização pesada ou servidores externos.
- **Filtros Linkwitz-Riley de 8ª Ordem (48 dB/oitava)**: Divisão limpa de frequências sem defasagem de fase audível.
- **Center Channel Extraction & Side Rejection**: Elimina vazamentos estéreo laterais (guitarras, synths e reverbs) do canal de voz.
- **Transient De-Drummer**: Atenuação ultra-rápida (1ms de ataque) para impedir que transientes de caixas e pratos vazem no stem vocal.
- **Dual Snare Scoop Notches & Formant Boost**: Filtros de entalhe em 210Hz e 420Hz combinados com realce de formantes vocais (750Hz e 1950Hz).

### 2. 🎛️ Equalizador Profissional ISO (10 Bandas) & Super Volume VLC (200%)
- **10 Bandas ISO Padrão**: 32Hz, 64Hz, 125Hz, 250Hz, 500Hz, 1kHz, 2kHz, 4kHz, 8kHz e 16kHz.
- **Curva Paramétrica SVG Dinâmica**: Renderização da resposta em frequência em tempo real.
- **14 Presets Acústicos**: Bass Boost, Club DJ, Eletrônica, Vocal Cristalino, Mega Funk, Rock, Flat, Acústico, Hip-Hop, Sertanejo, etc.
- **Pré-Amplificador com Ganho Limpo**: Amplificação de volume de até 200% com soft limiter para evitar distorção digital (*hard clipping*).

### 3. ⚡ Auto BPM Sync & Beatmatch Harmônico
- **Análise & Ajuste de BPM**: Detecção em tempo real e pitch shifting com preservação de tom (*Keylock*).
- **Crossfade Dinâmico Inteligente**: Transições de áudio graduais e harmônicas entre faixas sucessivas, evitando quebras de ritmo em festas e pistas de dança.
- **Drop Hunter & Proteção de Refrão**: Detecção antecipada do drop da música seguinte para alinhamento rítmico perfeito.

### 4. 🎯 Curadoria de Músicas Assistida por IA
- **Telemetria de Audição Local**: Monitoramento em tempo real de reproduções reais (*plays*) e rejeições (*skips*).
- **Categorização Automática**:
  - 🔥 **Favoritas de Verdade**: Faixas ouvidas repetidamente e quase nunca puladas.
  - 📈 **Em Observação**: Músicas em crescimento no gosto do usuário.
  - ⚠️ **Candidatas a Sair da Rotação**: Faixas puladas com frequência.
- **3 Novidades Ideais por Faixa**: Mineração inteligente e contextual de faixas inéditas similares em ritmo, estilo e BPM fora da biblioteca do usuário.

### 5. ✨ Efeitos Visuais & Transições Morph FLIP (AutoPost)
- **Morph FLIP Universal**: Todos os botões do player (Stems DJ, Equalizador, Estúdio Pro, BPM Sync, Fila, Histórico, Curadoria) decolam e expandem a partir do botão clicado e, ao fechar, desmontam suavemente e contraem de volta para o botão original com um pulso neon ciano.
- **Fone de Ouvido Neon Animado**: Âncora central e logotipo com pulso de luz e anéis de refração no cabeçalho.
- **Transição de Modos de Atuação**: Animações de desmontagem e remontagem sequenciada com profundidade 3D, partículas ascendentes e fitas de aurora boreal na tela de carregamento.

### 6. 🌐 Catálogo Híbrido & Descoberta Multi-Fonte
- Suporte a reprodução de streaming do **YouTube** (modo Áudio HD e modo Clipe com persistência de posição de seek).
- Suporte nativo ao **SoundCloud** para sets, remixes e produções exclusivas.
- Mais de **150 playlists curadas do Spotify** categorizadas em uma grade de capas em alta resolução com filtros de gênero responsivos.

---

## 📅 Linha do Tempo Completa de Desenvolvimento

Abaixo está o registro cronológico de cada evolução, implementação e correção do projeto:

### 2026-11-15: Arquitetura Inicial do Mixer & Estilização
- **06:03** — Início da base do Spotify DJ Mixer: transições com fade suave, correção dos decks duplos A/B, tratamento de estouro de texto em títulos longos e ajuste de assets.
- **07:05** — Primeira rodada de validação funcional do pipeline de áudio no navegador.
- **13:03** — Implementação dos *Auto DJ Platters* (discos de vinil animados que giram conforme o estado da reprodução e BPM).
- **13:38** — Criação do visualizador espectral de áudio e transições suaves de entrada e saída.
- **14:03** — Estruturação do Gerenciador de Fila lateral inspirado no visual moderno do Spotify.
- **14:09** — Harmonização dos botões da barra de controle inferior e barra de status do player.
- **15:08** — Refinamento dos botões de fechamento, alinhamento geométrico e overlays dos modais.
- **15:28** — Resolução de erros 403 de streaming e padronização visual dos cards de música.
- **15:44** — Centralização dos controles de reprodução (play/pause/skip) e badges de status nos cards.
- **16:06** — Aperfeiçoamento do fluxo de autoplay contínuo e layout responsivo.
- **16:41** — Ingestão inicial de 111 playlists do Spotify e testes do sincronizador preliminar de BPM.
- **17:32** — Desenvolvimento do algoritmo de fade gradual em tempo real durante trocas de faixa.
- **19:17** — Implementação dos primeiros modos de atuação DJ e histórico de reprodução persistente.
- **19:42** — Ajuste de espaçamentos e refinamentos de tipografia para monitores de alta densidade.
- **19:55** — Restauração e estabilização de integridade do template HTML do player.
- **20:06** — Otimização de uso de tela e hierarquia visual de títulos e metadados.
- **22:07** — Consolidação dos seletores de modos de atuação DJ.
- **22:39** — Integração de 33 playlists temáticas de Cumbia e criação do motor DJ anti-repetição.
- **23:08** — Lançamento do motor inicial de **Stems DJ (3 Bandas)** com crossover de frequência e detecção de silêncio; inclusão de playlists regionais Quaraí/Artigas.
- **23:42** — Lançamento do **Modo Balada & Club DJ**, efeitos especiais (FX) e HUD de crossover de 3 barras.

### 2026-11-16: Arsenal de Efeitos, DSP Pro & Isolamento Acústico
- **00:14** — Expansão para um arsenal de **29 efeitos especiais DJ** e motor de rotação inteligente adaptada ao gênero musical.
- **01:03** — Implementação do **Equalizador Pro de 10 Bandas** e conjunto de presets acústicos.
- **11:11** — Refinamento do Modo Balada & Club com dropdown dedicado e disparadores sonoros de impacto.
- **11:49** — Criação da **Console de Estúdio Pro** e adição de cauda suave de reverb/delay nos efeitos DJ.
- **12:12** — Padronização de obediência estrita de volume geral e mudo em todos os nós de áudio.
- **17:27** — Criação do algoritmo de **Proteção Integral do Refrão** e sistema de *Mix Jumper* suave.
- **17:54** — Módulo de refrão preditivo, ajuste manual de ponto de mixagem e disparos automáticos de FX.
- **18:48** — Correção e alinhamento do cursor da barra de seek e dos 4 marcadores visuais da faixa.
- **19:30** — Sistema de exclusão e movimentação de faixas em tempo real entre fila e biblioteca.
- **20:38** — Expansão da Console de Estúdio Pro com módulos de **Mastering DSP** (compressor multibanda, exciter harmônico e de-esser).
- **21:02** — Aperfeiçoamento do HUD do *Drop Hunter* e correção do fechamento do Studio Pro.
- **21:26** — Atualização para o **Motor DJ Stems Pro 100%**, eliminando chiados residuais.
- **21:46** — Eliminação de vazamento harmônico: motor DJ Stems multi-gênero **zero-bleed**.
- **22:25** — Desbloqueio definitivo das transições com isolamento vocal cirúrgico sem interrupção de áudio.

### 2026-11-17: Estabilização de Áudio & Auditoria de Clipping
- **00:44** — Resolução definitiva dos 3 gargalos de DSP (stems, HUD e transições).
- **13:44** — Consolidação do histórico e criação do ponto de partida versionado no Git (`baseline-pre-mixer`).
- **14:15** — Investigação profunda e eliminação das 4 causas-raiz de clipping digital, desvio de ganho no DSP e vazamentos remanescentes entre stems.
- **14:48** — Eliminação de eco residual e balanceamento da imagem estéreo na Console de Estúdio Pro.

### 2026-11-18: Suporte SoundCloud, Grade do Spotify & Temas Dinâmicos
- **14:56** — Eliminação do clique audível (*pop/click*) ao realizar saltos na barra de progresso (seek).
- **15:38** — Correção do algoritmo de "músicas parecidas" para respeitar o gênero da faixa-semente; correção de congelamento ao alternar entre Áudio HD e Clipe durante um crossfade.
- **15:49** — Manutenção exata do tempo de reprodução ao alternar entre Áudio HD e Vídeo Clipe.
- **16:22** — Integração oficial do **SoundCloud** como segunda fonte primária de streaming e descoberta.
- **16:28** — Redesenho das playlists do Spotify: substituição de mais de 150 abas horizontais por uma **grade moderna de capas em alta resolução**.
- **16:35** — Correção da rolagem na grade, quebra de linha fluida nos chips de gênero e exibição de capas oficiais do Spotify.
- **17:19** — Correção do comportamento do botão de play inicial em páginas recém-abertas.
- **17:22** — Proteção de privacidade: credenciais e chaves adicionadas ao `.gitignore`.
- **18:16** — Atribuição de paleta de cores temática exclusiva para cada modo de atuação DJ.
- **20:58** — Aplicação do tema de cores em todo o layout do site com transição cromática suave.
- **21:05** — Suavização da transição de modos (substituindo cortes secos por fades visuais).
- **21:10** — Mecanismo real de **desmontagem e remontagem** dos painéis do player na troca de modo.
- **21:17** — Efeito de desmontagem e remontagem individual aplicado card a card.
- **21:35** — Ajuste da velocidade de cascata escalonada dos cards (~8,5 segundos de fluidez).
- **21:44** — Coleta de capas em alta definição para as playlists de Cumbia.
- **21:52 / 22:04** — Tratamento de resiliência: prevenção de silêncio travado caso uma faixa seguinte falhe no carregamento do SoundCloud ou YouTube.

### 2026-11-19: Animações 3D, IA de Curadoria & Morph FLIP Universal
- **04:29** — Redesenho da transição de modo com **profundidade 3D real** em 3 fases (Desmontar → Carregar → Remontar).
- **04:38** — Correção do z-index e posicionamento flutuante do overlay de carregamento.
- **04:42 a 04:45** — Adição de efeitos gráficos na tela de carregamento: barras de equalizador pulsantes, anel de energia com partículas ascendentes e fitas de aurora boreal no fundo.
- **04:50 a 11:06** — Cinco rodadas massivas de mineração de capas oficiais do Spotify (mais de 200 playlists cobertas) e expansão de 120 novas playlists categorizadas nos 12 filtros de gênero.
- **12:51** — Reordenação de músicas da fila por **Arrastar e Soltar (Drag & Drop)**; modais de confirmação não-bloqueantes; exclusão individual de itens do histórico.
- **12:56** — Correção do botão "Mover" para playlists no histórico.
- **13:01** — Simplificação e refinamento dos filtros da Pesquisa Livre.
- **13:06** — Abas de gênero com quebra de linha flexível sem barra de rolagem horizontal.
- **13:14** — Notificações flutuantes (*Toasts*) ajustadas para ficarem acima de qualquer modal aberto.
- **13:29** — Auditoria geral de interface, eliminando botões sem ação e travamentos de rede.
- **13:35** — Feedback visual claro nos botões de mudo dos stems (vermelho vivo quando ativos).
- **13:42** — Lançamento do **Sistema de Curadoria de Músicas Assistida por IA** (análise de plays e skips em tempo real, promoção automática de favoritas).
- **13:52** — Correção da métrica da curadoria que duplicava plays e diluía a taxa de skip.
- **14:00** — Motor de recomendação de novidades externas baseado nas favoritas reais do usuário.
- **14:09** — Correção de falso silêncio no Drop Hunter e inclusão da curadoria por faixa favorita individual.
- **17:12** — Inclusão do **Logotipo Neon de Fone de Ouvido** com anéis de refração luminosa e primeiro protótipo de abertura de modais com expansão FLIP.
- **17:28 a 17:37** — Criação de logotipo vetorial SVG desenhado por código para a transição de modos, voando do cabeçalho até o centro e retornando.
- **18:38** — Voo bidirecional milimétrico da logo: pintura dinâmica do traço SVG na cor do modo, sincronização do cabeçalho com a desmontagem do site e atraso da troca de cor do tema até a conclusão da transição.
- **18:55** — **Morph FLIP Universal Definitivo**:
  - Aplicação do efeito FLIP em **todos os botões do player** (Stems DJ, EQ, Estúdio Pro, BPM Sync, Fila, Histórico, Curadoria, Mover, Remover).
  - Remoção de regras CSS conflitantes (`animation: scaleIn`), eliminando o flash/pop visual e garantindo 60 FPS limpos.
  - Correção definitiva do travamento e piscamento na Curadoria: o card base (`#trackCurationBaseCard`) permanece estável e visível, enquanto as 3 novidades entram suavemente em cascata.
  - Ao fechar, desmontagem reversa com contração de volta ao botão que originou o clique e disparo de pulso neon.

---

## 🛠️ Como Executar Localmente

### Pré-requisitos
- **Python 3.10+**
- **FFmpeg** instalado e adicionado ao `PATH` do sistema.
- **yt-dlp** (instalado automaticamente via requirements).

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/mbello1998/web-player-processamento-de-audio.git
cd web-player-processamento-de-audio
```

2. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

3. Inicie o servidor local:
```bash
python server.py
```

4. Abra no seu navegador:
```
http://localhost:5050/player.html
```

---

## 🏗️ Estrutura de Arquivos

```
├── player.html               # Aplicação Web completa compilada
├── player_template.html      # Template mestre do player
├── build_full_player.py      # Script de inlining e empacotamento de assets
├── server.py                 # Servidor local Python com rotas de API
├── assets/
│   ├── css/
│   │   └── player.css        # Folha de estilo completa, temas neon e animações
│   ├── js/
│   │   └── player.js         # Lógica do player, Web Audio DSP, Web Animations API
│   └── img/
│       ├── headphone_logo.gif # Logo animado de fone de ouvido neon
│       └── headphone_logo.jpg # Versão estática de alta fidelidade
├── CHANGELOG.md              # Registro cronológico detalhado
└── README.md                 # Documentação e linha do tempo do projeto
```

---

## 📄 Licença

Distribuído sob licença aberta para uso e estudo pessoal. Desenvolvido para entusiastas de música, discotecagem e processamento avançado de sinal de áudio na Web.
