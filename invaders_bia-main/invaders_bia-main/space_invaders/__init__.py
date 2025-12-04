"""
Pacote Space Invaders - Jogo Estilo Arcade Clássico

Este pacote contém toda a implementação do jogo Space Invaders,
seguindo os princípios de Programação Orientada a Objetos (POO).

Estrutura do Pacote:
├── Dados/          - Camada de Dados (Model)
│   ├── jogador.py      - Entidade do jogador
│   ├── inimigo.py      - Entidade dos inimigos
│   ├── projetil.py     - Entidade dos projéteis
│   └── pontuacao.py    - Dados de pontuação e vidas
│
├── Business/       - Camada de Negócio (Business Logic)
│   ├── jogador_business.py    - Regras do jogador
│   ├── inimigo_business.py    - Regras dos inimigos
│   ├── projetil_business.py   - Regras de colisão
│   └── pontuacao_business.py  - Regras de pontuação
│
├── web/            - Interface Web (Flask + Socket.IO)
│   ├── app.py      - Controller e rotas
│   └── main.py     - Entry point web
│
├── jogo.py         - Orquestrador com interface pygame
├── jogo_headless.py - Orquestrador para webservice
├── desktop.py      - Entry point desktop
└── utils.py        - Constantes e utilitários

Modos de Execução:
- Desktop: python -m space_invaders.desktop
- Web: python -m space_invaders.web.main
"""
