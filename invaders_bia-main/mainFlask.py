"""
Arquivo executável principal do webservice Flask.
Segue o padrão ensinado nas aulas de POO (Prof. Vinícius Sebba Patto).

Estrutura conforme slides Aula 37-40:
- Este arquivo deve ficar na raiz do projeto
- Importa o app do módulo/pacote
- Executa o servidor Flask

Uso:
    python mainFlask.py
    ou
    flask --app mainFlask run --debug
"""

from app import app, socketio, start_game_thread

if __name__ == '__main__':
    # Inicia o game loop antes de servir
    # Conforme implementado no app.py original
    start_game_thread()
    
    # Executa o servidor Flask com Socket.IO
    # debug=True permite reload automático durante desenvolvimento
    socketio.run(app, debug=True)

