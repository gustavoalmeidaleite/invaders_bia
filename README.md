# Space Invaders — Projeto de Programação Orientada a Objetos

Jogo Space Invaders desenvolvido como exercício de POO no Bacharelado de IA/UFG. O código separa dados, regras de negócio e controladores, com duas frentes: desktop (pygame) e web (Flask + Socket.IO) alimentada por um orquestrador headless compartilhado.

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
    ├── app.py           ← Controllers/rotas + eventos Socket.IO
    └── main.py          ← Entry point web
space_invaders/data/     ← Persistência simples de usuários (JSON)
static/                  ← Imagens/sprites
templates/               ← HTML (frontend web)
requirements.txt         ← Dependências
```

## Mecânicas do Jogo
- Estados de fluxo: menu (opções JOGAR COM IA, JOGAR SOLO, SAIR), gameplay e game over (JOGAR NOVAMENTE, MENU PRINCIPAL, SAIR). Pausa alterna com `P` e reinício rápido com `R`.
- Formação de inimigos fixa: 3 linhas × 8 colunas, espaçamento 80x50 px; inimigos descem 20 px e invertem direção ao tocar bordas.
- Pontuação: tipos 1/2/3 valem 30/20/10 pontos; bônus de 5 pontos por interceptar tiro inimigo com tiro do jogador. Pontuação reinicia a cada nova partida.
- Vidas: jogador começa com 3 vidas; perde ao ser atingido ou se um inimigo alcançar sua linha. Game over quando vidas chegam a 0.
- Tiros: intervalo mínimo de 200 ms para o jogador e 800 ms para inimigos; máximo de 5 tiros inimigos simultâneos. Projéteis colidem entre si e com naves, criando efeitos de explosão temporários.
- Progressão: ao eliminar todos os inimigos, nova onda é criada e a velocidade base deles aumenta em 0.5.

## POO na Prática (resumo)
- **Encapsulamento**: atributos privados com `@property` em Dados/.
- **Separação de responsabilidades**: Dados/ só estado; Business/ só regras; controladores em `jogo.py`/`jogo_headless.py`/`web/app.py`.
- **Composição/Delegação**: `Jogo` contém entidades e delega lógica para as classes *Business*.
- **Baixo acoplamento**: imports relativos no pacote e dependências unidirecionais.

## Controles (desktop e web)
- Movimento: setas ou WASD
- Atirar: Z ou Espaço (segurando dispara continuamente)
- Pausar: P | Reiniciar: R
- Menu/Game Over: ↑/↓ ou W/S para navegar, Enter/Espaço para selecionar, ESC volta ao menu
- Opcional web: ao escolher “JOGAR COM IA”, abre overlay local para configurar camadas/neurônios (apenas visual; lógica do jogo segue igual à opção solo).

## Modos de Execução
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

## Integração Web, API e Sessão
- Autenticação: cadastro/login com senha armazenada via SHA-256 em `space_invaders/data/usuarios.json`; sessões expiram ao fechar o navegador.
- Socket.IO: cliente envia `input_jogador` com `{acao, estado}`; servidor emite `estado_jogo` ~30 FPS com snapshot completo (jogador, inimigos, projeteis, explosões, pontuação, vidas, estado, menus).
- REST:
  - `GET /api/estado` → estado atual do jogo em JSON.
  - `POST /api/comando` com `{"acao": "...", "estado": "pressionar|soltar"}` para acionar controles (movimento, tiro, pausa, menu, reiniciar).
- O loop do jogo headless roda em thread única e é iniciado na primeira conexão.

## Requisitos
- Python 3.7+ (recomendado usar venv)
- Dependências: `pip install -r requirements.txt`

## Recursos Visuais
- Sprites em `static/` para jogador, inimigos por tipo, projéteis, explosão e background.
- Efeito de explosão programático é usado como fallback se o sprite não carregar.