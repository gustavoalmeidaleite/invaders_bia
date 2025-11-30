# Execução do webservice Flask

1. Ative o ambiente virtual: `source .venv/bin/activate`.
2. Instale/atualize as dependências: `pip install -r requirements.txt`.
3. Suba o servidor já a partir da raiz do projeto: `flask --app invaders_bia-main/app.py --debug run`.
   - Alternativa: `cd invaders_bia-main && flask --app app --debug run`.
4. Conecte pelo navegador em `http://localhost:5000/` (o loop do jogo inicia na primeira conexão).

Se precisar derrubar o servidor no terminal, use `Ctrl+C`.

## Controles no webservice
- Movimento contínuo: setas ou WASD (segure para andar).
- Tiro: Espaço ou Z (segure para disparo contínuo).
- Pausar/retomar: tecla P.
- Reiniciar (começa direto a partida): tecla R.
- Menu/Game Over: navegue com ↑/↓ ou W/S e selecione com Enter ou Espaço. ESC volta ao menu.
