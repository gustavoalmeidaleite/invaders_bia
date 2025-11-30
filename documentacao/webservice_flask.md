# Execução do webservice Flask

1. Ative o ambiente virtual: `source .venv/bin/activate`.
2. Instale/atualize as dependências: `pip install -r requirements.txt`.
3. Suba o servidor já a partir da raiz do projeto: `flask --app invaders_bia-main/app.py --debug run`.
   - Alternativa: `cd invaders_bia-main && flask --app app --debug run`.
4. Conecte pelo navegador em `http://localhost:5000/` (o loop do jogo inicia na primeira conexão).

Se precisar derrubar o servidor no terminal, use `Ctrl+C`.
