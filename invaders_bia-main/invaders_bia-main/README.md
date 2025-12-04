# Space Invaders — Projeto de Programação Orientada a Objetos

Jogo Space Invaders desenvolvido como exercício de POO no Bacharelado de IA/UFG. O código segue separação clara entre dados, regras de negócio e controladores (desktop e web).

## Estrutura do Projeto
```
space_invaders/          ← Pacote principal
├── Dados/               ← Modelos de dados (estado + properties)
├── Business/            ← Regras de negócio (movimento, pontuação, tiros)
├── utils.py             ← Constantes e efeitos
├── jogo.py              ← Orquestrador pygame (render/controller)
├── jogo_headless.py     ← Orquestrador headless (lógica para web)
├── desktop.py           ← Entry point local (pygame)
└── web/                 ← Camada web (Flask + Socket.IO)
    ├── app.py           ← Controllers/rotas
    └── main.py          ← Entry point web
static/                  ← Imagens/sprites
templates/               ← HTML (frontend web)
documentacao/            ← Guias e análises
Referencia/              ← Materiais das aulas
requirements.txt         ← Dependências
```

## POO na Prática (resumo)
- **Encapsulamento**: atributos privados com `@property` em Dados/.
- **Separação de responsabilidades**: Dados/ só estado; Business/ só regras; controladores em `jogo.py`/`jogo_headless.py`/`web/app.py`.
- **Composição/Delegação**: `Jogo` contém entidades e delega lógica para as classes *Business*.
- **Baixo acoplamento**: imports relativos no pacote e dependências unidirecionais.

## Requisitos
- Python 3.7+ (recomendado usar venv)
- Dependências: `pip install -r requirements.txt`

## Como Executar
```bash
# (opcional) criar/ativar venv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# jogo local (pygame)
python -m space_invaders.desktop

# webservice (Flask + Socket.IO)
python -m space_invaders.web.main
```

## Controles (jogo local e web)
- Movimento: setas ou WASD
- Atirar: Z ou Espaço
- Pausar: P
- Reiniciar: R
- Menu/Game Over: Enter/Espaço para selecionar, ESC volta ao menu

## Funcionalidades
- Menu principal e tela de game over
- Movimento em 4 direções
- Tiros de jogador e inimigos, colisão projétil vs projétil
- Pontuação e vidas com bônus por interceptação
- Efeitos de explosão e sprites para jogador/inimigos/projéteis
- Três tipos de inimigos com pontuações distintas
