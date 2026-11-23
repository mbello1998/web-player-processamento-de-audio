# DropHunter Studio - Guia de Projeto & Arquitetura

## 📌 Visão Geral
**DropHunter Studio** é um Web Player avançado de alta fidelidade para streaming e discotecagem com motor de áudio Web Audio API DSP, visualizador de frequências, mixagem inteligente de drops (Drop Hunter), detecção e sincronização de BPM, equalizador ISO de 10 bandas, simulador de Stems (Zero-Bleed) e suporte a catálogo multi-fonte (YouTube, SoundCloud e faixas locais).

---

## 🛠️ Comandos de Desenvolvimento & Build
- **Iniciar Servidor Local**:
  ```bash
  python server.py
  ```
  Servidor Flask rodando em `http://localhost:5050`. Rota principal do player: `http://localhost:5050/player.html`.
- **Compilar Assets e Gerar `player.html`**:
  ```bash
  python build_full_player.py
  ```
  Sempre execute este comando após editar `player_template.html`, `assets/css/player.css` ou `assets/js/player.js`.
- **Checagem de Sintaxe JavaScript**:
  ```bash
  node --check assets/js/player.js
  ```

---

## 🏗️ Estrutura do Projeto
```
├── player.html               # Aplicação web final compilada (gerada automaticamente)
├── player_template.html      # Template mestre do player
├── build_full_player.py      # Script de inlining e empacotamento
├── server.py                 # Servidor backend Python (APIs de streaming, cache e download)
├── assets/
│   ├── css/player.css        # Estilos, temas neon, animações FLIP e grids
│   ├── js/player.js          # Motor Web Audio DSP, lógica do player, eventos de UI
│   └── img/                  # Logos e recursos visuais
├── CHANGELOG.md              # Registro cronológico detalhado de alterações
├── README.md                 # Documentação pública e linha do tempo
└── CLAUDE.md                 # Guia técnico e convenções para agentes
```

---

## 🎛️ Motor de Áudio & Arquitetura Web Audio DSP
- **Cadeia de Sinal**:
  1. `<audio>` elemento capturado via `createMediaElementSource`.
  2. Filtro Stems (Zero-Bleed Crossover com fase linear e ganho compensado).
  3. EQ ISO 10 Bandas (31Hz a 16kHz via BiquadFilterNode).
  4. AnalyserNode (FFT 2048 para VU meter, espectro e detecção de drop/silêncio).
  5. Master Gain Node (Volume VLC até 200%).
  6. Compressor Master (Mastering transparente: threshold -1.5 dBFS, ratio 3.5:1, attack 10ms, release 250ms, knee 12dB).
  7. Safety WaveShaper (Soft-clip protetor ultra-limpo com threshold em 0.98).
  8. AudioDestinationNode (saída de som).

---

## 🛡️ Regras e Diretrizes do Projeto
1. **Regra de Documentação Obrigatória**: Sempre que qualquer alteração ou melhoria for implementada, atualize `CHANGELOG.md`, `README.md` e `CLAUDE.md`.
2. **Ícones**: Não utilize emojis Unicode soltos no HTML/JS para botões ou controles de interface. Utilize SVGs inline através do helper `window.uiIcon(...)` ou classes `.ui-icon`.
3. **Versão de Cache**: Ao modificar `assets/js/player.js` ou `assets/css/player.css`, atualize a query string de versão em `player_template.html` (`v=...`) e rode `python build_full_player.py`.
4. **Proteção Anti-Looping de Áudio**:
   - Falhas no YouTube (ex: restrição +18) possuem cache negativo de 10 min no backend (`server.py`).
   - O player usa `skipUnplayableTrack` para pular faixas inacessíveis sem travar a interface.
   - Para desbloquear faixas com restrição de idade no YouTube, adicione um `cookies.txt` (formato Netscape) na raiz do projeto.
