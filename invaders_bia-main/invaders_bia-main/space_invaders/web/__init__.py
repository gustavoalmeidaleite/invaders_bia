"""
Pacote Web - Interface Web (Flask + Socket.IO)

Este pacote contém a interface web do jogo, permitindo jogar
através do navegador. Implementa o padrão MVC:

- app.py: Controller com rotas HTTP e eventos Socket.IO
- main.py: Entry point para executar o servidor

Componentes:
- Flask: Framework web para rotas HTTP e templates
- Socket.IO: Comunicação em tempo real (game state updates)

Endpoints principais:
- GET /: Página inicial (redireciona para login ou jogo)
- GET /login: Formulário de autenticação
- GET /cadastro: Formulário de registro
- GET /jogo: Interface do jogo (requer login)
- GET /api/estado: Estado atual do jogo (JSON)
- POST /api/comando: Enviar comandos ao jogo

Como executar:
    python -m space_invaders.web.main
"""
