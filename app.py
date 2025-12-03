"""
Webservice Flask - Space Invaders
Controller/Routing do webservice conforme princípios de POO.

Estrutura baseada nos ensinamentos das aulas de POO (Prof. Vinícius Sebba Patto):
- Este arquivo atua como CONTROLLER (camada de controle)
- Define rotas (endpoints) e integra com a lógica de negócio
- Não contém lógica de negócio (delegada para Business/)
- Não manipula dados diretamente (delegado para Dados/)

Arquitetura do projeto:
- Dados/ (Model): Classes de dados com encapsulamento
- Business/: Regras de negócio
- app.py (Controller): Rotas e integração
- jogo_headless.py: Orquestrador principal (Facade)
- mainFlask.py: Executável principal
"""

from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from flask_socketio import SocketIO
from functools import wraps
import threading
import json
import os
import hashlib
import time
from jogo_headless import JogoHeadless

# Inicialização do Flask
app = Flask(__name__)
# Chave secreta única - muda a cada reinício para invalidar sessões antigas
app.config['SECRET_KEY'] = f'space_invaders_bia_{time.time()}'
app.config['SESSION_PERMANENT'] = False  # Sessão expira ao fechar navegador
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True

# Arquivo para armazenar usuários
USUARIOS_FILE = os.path.join(os.path.dirname(__file__), 'usuarios.json')

def carregar_usuarios():
    """Carrega usuários do arquivo JSON."""
    if os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_usuarios(usuarios):
    """Salva usuários no arquivo JSON."""
    with open(USUARIOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=2)

def hash_senha(senha):
    """Gera hash da senha."""
    return hashlib.sha256(senha.encode()).hexdigest()

def login_required(f):
    """Decorator para exigir login."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_email' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Socket.IO para comunicação em tempo real
# Usa threading para simplicidade (conforme requisitos)
socketio = SocketIO(app, async_mode='threading')

# Controle de thread do game loop
# Garante que apenas uma thread do jogo seja criada
game_thread = None
thread_lock = threading.Lock()

# Instância do jogo (Facade/Orchestrator)
# JogoHeadless coordena Dados/ e Business/ sem lógica de apresentação
jogo = JogoHeadless()

# ============================================================================
# ROTAS (ENDPOINTS) - Camada de Controle
# ============================================================================

@app.route('/')
def index():
    """
    Rota principal - redireciona para login ou jogo.
    """
    if 'usuario_email' in session:
        return redirect(url_for('jogo_route'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Rota de login.
    GET: Exibe formulário de login.
    POST: Processa autenticação.
    """
    if 'usuario_email' in session:
        return redirect(url_for('jogo_route'))

    error = None
    success = request.args.get('success')

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '')

        usuarios = carregar_usuarios()

        if email in usuarios and usuarios[email]['senha'] == hash_senha(senha):
            session.permanent = False  # Sessão expira ao fechar navegador
            session['usuario_email'] = email
            session['usuario_nome'] = usuarios[email]['nome']
            return redirect(url_for('jogo_route'))
        else:
            error = 'Email ou senha inválidos'

    return render_template('login.html', error=error, success=success)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """
    Rota de cadastro.
    GET: Exibe formulário de cadastro.
    POST: Processa novo cadastro.
    """
    if 'usuario_email' in session:
        return redirect(url_for('jogo_route'))

    error = None

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '')

        if not nome or not email or not senha:
            error = 'Todos os campos são obrigatórios'
        elif len(senha) < 4:
            error = 'Senha deve ter pelo menos 4 caracteres'
        else:
            usuarios = carregar_usuarios()

            if email in usuarios:
                error = 'Email já cadastrado'
            else:
                usuarios[email] = {
                    'nome': nome,
                    'senha': hash_senha(senha)
                }
                salvar_usuarios(usuarios)
                return redirect(url_for('login', success='Cadastro realizado com sucesso!'))

    return render_template('cadastro.html', error=error)

@app.route('/logout')
def logout():
    """Rota para logout."""
    session.pop('usuario_email', None)
    session.pop('usuario_nome', None)
    return redirect(url_for('login'))

@app.route('/jogo')
@login_required
def jogo_route():
    """
    Rota do jogo (protegida por login).
    Retorna a interface HTML do jogo.
    """
    return render_template('index.html')

# ============================================================================
# SOCKET.IO EVENTS - Comunicação em Tempo Real
# ============================================================================

@socketio.on('connect')
def handle_connect():
    """
    Handler de conexão Socket.IO.
    Inicia o game loop quando um cliente se conecta.
    """
    print('Client connected')
    start_game_thread()

@socketio.on('input_jogador')
def handle_input(data):
    """
    Handler de entrada do jogador via Socket.IO.
    Recebe comandos do cliente e delega para o jogo.

    Args:
        data (dict): {"acao": str, "estado": str}
    """
    acao = data.get('acao')
    estado = data.get('estado')
    if acao:
        jogo.processar_comando(acao, estado)

# ============================================================================
# API REST - Endpoints HTTP
# ============================================================================

@app.route('/api/estado', methods=['GET'])
def api_estado():
    """
    Endpoint REST para obter o estado atual do jogo em JSON.
    Método GET conforme padrão REST (leitura de dados).

    Conforme ensinado: métodos HTTP adequados (GET para leitura).

    Returns:
        JSON com estado completo do jogo
    """
    start_game_thread()
    return jsonify(jogo.obter_estado())

@app.route('/api/comando', methods=['POST'])
def api_comando():
    """
    Endpoint REST para enviar comandos ao jogo.
    Método POST conforme padrão REST (envio de dados).

    Conforme ensinado: @app.route com methods=['POST'] para receber dados.

    Request Body (JSON):
        {
            "acao": str,      # Comando a executar
            "estado": str     # "pressionar" ou "soltar"
        }

    Returns:
        JSON: {"ok": bool, "estado": dict} ou {"erro": str}
    """
    payload = request.get_json(silent=True) or {}
    acao = payload.get('acao')
    estado = payload.get('estado')

    # Validação de entrada
    if not acao:
        return jsonify({"erro": "campo 'acao' é obrigatório"}), 400

    start_game_thread()
    jogo.processar_comando(acao, estado)
    return jsonify({"ok": True, "estado": jogo.obter_estado()})

# ============================================================================
# LÓGICA DE THREAD E GAME LOOP
# ============================================================================

def start_game_thread():
    """
    Inicia o loop do jogo em segundo plano (apenas uma vez).

    Implementa padrão Singleton para a thread do jogo.
    Usa mecanismo do SocketIO para compatibilidade com diferentes servidores.
    """
    global game_thread
    with thread_lock:
        if game_thread is None or not game_thread.is_alive():
            game_thread = socketio.start_background_task(game_loop)

def game_loop():
    """
    Loop principal do jogo executado em thread separada.

    Responsabilidades:
    - Atualizar estado do jogo (~30 FPS)
    - Emitir estado para clientes conectados via Socket.IO

    Nota: A lógica do jogo está em jogo_headless.py (Facade),
    que coordena Dados/ e Business/ (separação de responsabilidades).
    """
    while True:
        jogo.atualizar()
        state = jogo.obter_estado()
        socketio.emit('estado_jogo', state)
        socketio.sleep(0.03)  # ~30 FPS

# Execução movida para mainFlask.py conforme padrão ensinado
# Para executar: python mainFlask.py
