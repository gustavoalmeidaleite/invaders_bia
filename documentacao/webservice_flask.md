# Execução do webservice Flask

## Método 1: Usando módulo `space_invaders.web.main` (Recomendado)

1. Ative o ambiente virtual: `source .venv/bin/activate`.
2. Instale/atualize as dependências: `pip install -r requirements.txt`.
3. Execute o módulo principal:
   ```bash
   cd invaders_bia
   python -m space_invaders.web.main
   ```
4. Conecte pelo navegador em `http://localhost:5000/`

## Método 2: Usando Flask CLI

1. Ative o ambiente virtual: `source .venv/bin/activate`.
2. Instale/atualize as dependências: `pip install -r requirements.txt`.
3. Suba o servidor:
   ```bash
   flask --app space_invaders.web.main --debug run
   ```
   - Alternativa: `cd invaders_bia && flask --app space_invaders.web.main --debug run`
4. Conecte pelo navegador em `http://localhost:5000/`

**Nota**: O loop do jogo inicia automaticamente na primeira conexão.

Se precisar derrubar o servidor no terminal, use `Ctrl+C`.

## Controles no webservice
- Movimento contínuo: setas ou WASD (segure para andar).
- Tiro: Espaço ou Z (segure para disparo contínuo).
- Pausar/retomar: tecla P.
- Reiniciar (começa direto a partida): tecla R.
- Menu/Game Over: navegue com ↑/↓ ou W/S e selecione com Enter ou Espaço. ESC volta ao menu.

## Endpoints REST (alternativa ao Socket.IO)
- `GET /api/estado` — retorna o estado atual do jogo em JSON. Inicia o loop do jogo se ainda não estiver rodando.
- `POST /api/comando` — envia um comando ao jogo. Corpo JSON: `{"acao": "<comando>", "estado": "pressionar|soltar"}`. Usa os mesmos comandos do front-end (`esquerda`, `direita`, `cima`, `baixo`, `atirar`, `pausar`, `reiniciar`, `menu`, `menu_cima`, `menu_baixo`, `menu_selecionar`).
