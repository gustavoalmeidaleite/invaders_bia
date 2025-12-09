# ============================================================================
# MAIN.PY - PONTO DE ENTRADA PARA VERSÃO WEB
# ============================================================================
"""
PROPÓSITO:
Este é o PONTO DE ENTRADA (entry point) para a versão WEB do jogo.
Inicia servidor Flask com Socket.IO para comunicação em tempo real.

ARQUITETURA WEB:
- SERVIDOR (Python/Flask): Roda lógica do jogo (JogoHeadless)
- CLIENTE (JavaScript/HTML): Renderiza jogo no navegador
- COMUNICAÇÃO: Socket.IO (WebSockets) para tempo real

DIFERENÇA DESKTOP vs WEB:
- Desktop: desktop.py -> Jogo (com pygame)
- Web: main.py -> Flask -> JogoHeadless (sem pygame)

USO:
    python -m space_invaders.web.main
    flask --app space_invaders.web.main run --debug

PADRÃO DE DESIGN:
- SEPARAÇÃO: Lógica (servidor) separada de apresentação (cliente)
- REUTILIZAÇÃO: Mesmas classes Dados e Business
- ADAPTAÇÃO: Interface web em vez de desktop
"""

from .app import app, socketio, start_game_thread


def main():
    """
    FUNÇÃO PRINCIPAL - Inicia servidor web

    FLUXO:
    1. Inicia thread do game loop (JogoHeadless)
    2. Inicia servidor Flask com Socket.IO
    3. Servidor fica aguardando conexões de clientes

    SOCKET.IO:
    - Permite comunicação bidirecional em tempo real
    - Servidor envia estado do jogo para clientes
    - Clientes enviam comandos para servidor
    """
    # Inicia thread que roda game loop do JogoHeadless
    start_game_thread()

    # Inicia servidor Flask com Socket.IO
    # debug=True: recarrega automaticamente ao modificar código
    socketio.run(app, debug=True)


# ============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================================
if __name__ == "__main__":
    """
    Verifica se arquivo está sendo executado diretamente
    Padrão Python para scripts executáveis
    """
    main()
