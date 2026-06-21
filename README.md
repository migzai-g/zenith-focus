# zenith://focus

![Release](https://img.shields.io/github/v/release/migzai-g/zenith-focus?label=release&color=39ff14)
![Stars](https://img.shields.io/github/stars/migzai-g/zenith-focus?color=39ff14)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux-39ff14)
![License](https://img.shields.io/badge/license-MIT-39ff14)

**Zenith Focus Hub** é uma central de produtividade leve, minimalista e bonita.  
Ajuda você a manter o foco com timer Pomodoro, registra suas sessões e transforma seu progresso em um **heatmap de hábito** estilo GitHub.

---

## Screenshots

<div align="center">
<img src="docs/Captura%20de%20tela%202026-06-21%20050654.png" width="49%" style="border-radius: 8px;" />
<img src="docs/Captura%20de%20tela%202026-06-21%20050905.png" width="49%" style="border-radius: 8px;" />
</div>

<div align="center">
<img src="docs/Captura%20de%20tela%202026-06-21%20050944.png" width="70%" style="border-radius: 8px;" />
</div>

---

## Funcionalidades

- **Timer Pomodoro** com durações configuráveis (10/25/30/45/60 min), pausa e skip
- Som de conclusão ao final de cada ciclo
- Log de sessões — anote o que você fez ao terminar o ciclo
- **Heatmap de hábito** (estilo GitHub) mostrando os últimos ~6 meses
- Aba de Pensamentos com frases aleatórias
- **6 temas** de cores: `green`, `amber`, `blood`, `cyan`, `violet` e `mono`
- Janela sem borda, arrastável, redimensionável e com opção de **sempre no topo** (pin)
- Totalmente offline e salva os dados localmente

---

## Download

**Versão mais recente: [v4.3.1](https://github.com/migzai-g/zenith-focus/releases/tag/v4.3.1)**

- **Windows**: `zenith_v4.3_setup.exe`
- **Linux**: binário `zenith` → `chmod +x zenith && ./zenith`

---

## Rodando a partir do fonte

```bash
git clone https://github.com/migzai-g/zenith-focus.git
cd zenith-focus
pip install customtkinter
python zenith.py

