"""
Entry point do webservice Flask (camada de controle).
Executa o servidor e inicia o loop do jogo headless.

Uso recomendado:
    python -m space_invaders.web.main
    flask --app space_invaders.web.main run --debug
"""

from .app import app, socketio, start_game_thread


def main():
    """Inicia o servidor web com Socket.IO."""
    start_game_thread()
    socketio.run(app, debug=True)


if __name__ == "__main__":
    main()
