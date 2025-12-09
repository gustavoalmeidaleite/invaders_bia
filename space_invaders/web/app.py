"""
# Webservice Flask - Space Invaders
# Controller/Routing do webservice conforme princípios de POO.

# Estrutura baseada nos ensinamentos das aulas de POO (Prof. Vinícius Sebba Patto):
# - Este arquivo atua como CONTROLLER (camada de controle)
# - Define rotas (endpoints) e integra com a lógica de negócio
# - Não contém lógica de negócio (delegada para Business/)
# - Não manipula dados diretamente (delegado para Dados/)

# Arquitetura do projeto:
# - space_invaders/Dados/ (Model): Classes de dados com encapsulamento
# - space_invaders/Business/: Regras de negócio
# - space_invaders/web/app.py (Controller): Rotas e integração
# - space_invaders/jogo_headless.py: Orquestrador principal (Facade)
# - space_invaders/web/main.py: Executável principal
"""

from pathlib import Path  # Importa a classe Path para manipulação de caminhos de arquivos de forma independente do SO
from flask import Flask, render_template, jsonify, request, redirect, url_for, session  # Importa componentes essenciais do Flask
from flask_socketio import SocketIO  # Importa SocketIO para comunicação de dados em tempo real (websockets) 
from functools import wraps  # Importa wraps para criar decorators que preservam metadados da função original
import threading  # Importa threading para lidar com execução concorrente (game loop)
import json  # Importa biblioteca para manipulação de arquivos JSON
import hashlib  # Importa hashlib para criptografia (hashing) de senhas
import time  # Importa time para funções relacionadas a tempo (timestamp)
from ..jogo_headless import JogoHeadless  # Importa a classe JogoHeadless do pacote pai (..)

# Diretórios relevantes
BASE_DIR = Path(__file__).resolve().parent.parent  # Define BASE_DIR como o diretório pai do pai deste arquivo (space_invaders/)
PROJECT_ROOT = BASE_DIR.parent                    # Define PROJECT_ROOT como o diretório pai de BASE_DIR (raiz do projeto)
DATA_DIR = BASE_DIR / "data"                      # Define DATA_DIR como o subdiretório "data" dentro de BASE_DIR

# Inicialização do Flask (controllers/views)
app = Flask(  # Cria a instância da aplicação Flask
    __name__,  # Passa o nome do módulo atual
    static_folder=str(PROJECT_ROOT / "static"),  # Define a pasta de arquivos estáticos (CSS, JS, Imagens)
    template_folder=str(PROJECT_ROOT / "templates"),  # Define a pasta de templates HTML
)
# Chave secreta única - muda a cada reinício para invalidar sessões antigas
app.config['SECRET_KEY'] = f'space_invaders_bia_{time.time()}'  # Configura uma chave secreta dinâmica para assinar cookies de sessão
app.config['SESSION_PERMANENT'] = False  # Configura a sessão para não ser permanente (expira ao fechar navegador)
app.config['SESSION_COOKIE_SECURE'] = False  # Permite cookies de sessão em HTTP (não exige HTTPS, útil para dev)
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Protege o cookie de sessão contra acesso via JavaScript (segurança)

# Arquivo para armazenar usuários (camada de dados persistentes)
USUARIOS_FILE = DATA_DIR / "usuarios.json"  # Define o caminho completo para o arquivo JSON de usuários

def carregar_usuarios():
    """Carrega usuários do arquivo JSON."""
    if USUARIOS_FILE.exists():  # Verifica se o arquivo de usuários existe
        with open(USUARIOS_FILE, 'r', encoding='utf-8') as f:  # Abre o arquivo em modo leitura ('r') com encoding UTF-8
            return json.load(f)  # Carrega e retorna o conteúdo do JSON como um dicionário Python
    return {}  # Retorna um dicionário vazio se o arquivo não existir

def salvar_usuarios(usuarios):
    """Salva usuários no arquivo JSON."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)  # Cria o diretório de dados se não existir (incluindo pais)
    with open(USUARIOS_FILE, 'w', encoding='utf-8') as f:  # Abre o arquivo em modo escrita ('w') com encoding UTF-8
        json.dump(usuarios, f, ensure_ascii=False, indent=2)  # Escreve o dicionário no arquivo JSON com formatação legível

def hash_senha(senha):
    """Gera hash da senha."""
    return hashlib.sha256(senha.encode()).hexdigest()  # Converte senha para bytes, gera hash SHA-256 e retorna em hex

def login_required(f):
    """Decorator para exigir login."""
    @wraps(f)  # Preserva os metadados da função original 'f'
    def decorated_function(*args, **kwargs):  # Define a função wrapper que aceita quaisquer argumentos
        if 'usuario_email' not in session:  # Verifica se o email do usuário não está na sessão (não logado)
            return redirect(url_for('login'))  # Redireciona para a rota de login
        return f(*args, **kwargs)  # Executa a função original se estiver logado
    return decorated_function  # Retorna a função decorada

# Socket.IO para comunicação em tempo real
# Usa threading para simplicidade (conforme requisitos)
socketio = SocketIO(app, async_mode='threading')  # Inicializa SocketIO integrando com o app Flask, modo threading

# Controle de thread do game loop
# Garante que apenas uma thread do jogo seja criada
game_thread = None  # Variável global para armazenar a thread do jogo
thread_lock = threading.Lock()  # Lock para garantir acesso exclusivo ao criar a thread (thread-safety)

# Instância do jogo (Facade/Orchestrator)
# JogoHeadless coordena Dados/ e Business/ sem lógica de apresentação
jogo = JogoHeadless()  # Instancia a classe JogoHeadless que gerencia a lógica do jogo

# ============================================================================
# ROTAS (ENDPOINTS) - Camada de Controle
# ============================================================================

@app.route('/')  # Define a rota raiz ('/')
def index():
    """
    Rota principal - redireciona para login ou jogo.
    """
    if 'usuario_email' in session:  # Verifica se o usuário já está logado
        return redirect(url_for('jogo_route'))  # Se logado, redireciona para a rota do jogo
    return redirect(url_for('login'))  # Se não logado, redireciona para a rota de login

@app.route('/login', methods=['GET', 'POST'])  # Define a rota '/login' aceitando métodos GET e POST
def login():
    """
    Rota de login.
    GET: Exibe formulário de login.
    POST: Processa autenticação.
    """
    if 'usuario_email' in session:  # Verifica se usuário já está logado
        return redirect(url_for('jogo_route'))  # Redireciona para o jogo se já logado

    error = None  # Inicializa variável de erro
    success = request.args.get('success')  # Obtém mensagem de sucesso da URL (query param), se houver

    if request.method == 'POST':  # Verifica se a requisição é do tipo POST (envio de formulário)
        email = request.form.get('email', '').strip()  # Obtém email do formulário e remove espaços
        senha = request.form.get('senha', '')  # Obtém senha do formulário

        usuarios = carregar_usuarios()  # Carrega a lista de usuários cadastrados

        # Verifica se email existe e se a senha (hash) confere
        if email in usuarios and usuarios[email]['senha'] == hash_senha(senha):
            session.permanent = False  # Sessão expira ao fechar navegador
            session['usuario_email'] = email  # Salva email na sessão
            session['usuario_nome'] = usuarios[email]['nome']  # Salva nome na sessão
            return redirect(url_for('jogo_route'))  # Redireciona para o jogo
        else:
            error = 'Email ou senha inválidos'  # Define mensagem de erro se falhar

    return render_template('login.html', error=error, success=success)  # Renderiza template de login com msgs

@app.route('/cadastro', methods=['GET', 'POST'])  # Define a rota '/cadastro' aceitando GET e POST
def cadastro():
    """
    Rota de cadastro.
    GET: Exibe formulário de cadastro.
    POST: Processa novo cadastro.
    """
    if 'usuario_email' in session:  # Verifica se já está logado
        return redirect(url_for('jogo_route'))  # Redireciona para o jogo

    error = None  # Inicializa erro

    if request.method == 'POST':  # Se for envio de formulário
        nome = request.form.get('nome', '').strip()  # Obtém nome
        email = request.form.get('email', '').strip()  # Obtém email
        senha = request.form.get('senha', '')  # Obtém senha

        if not nome or not email or not senha:  # Validação básica: campos vazios
            error = 'Todos os campos são obrigatórios'
        elif len(senha) < 4:  # Validação: tamanho da senha
            error = 'Senha deve ter pelo menos 4 caracteres'
        else:
            usuarios = carregar_usuarios()  # Carrega usuários existentes

            if email in usuarios:  # Verifica se email já existe
                error = 'Email já cadastrado'
            else:
                usuarios[email] = {  # Cria novo registro de usuário
                    'nome': nome,
                    'senha': hash_senha(senha)  # Salva senha com hash
                }
                salvar_usuarios(usuarios)  # Persiste no arquivo JSON
                return redirect(url_for('login', success='Cadastro realizado com sucesso!'))  # Redireciona login

    return render_template('cadastro.html', error=error)  # Renderiza template de cadastro

@app.route('/logout')  # Define rota de logout
def logout():
    """Rota para logout."""
    session.pop('usuario_email', None)  # Remove email da sessão
    session.pop('usuario_nome', None)  # Remove nome da sessão
    return redirect(url_for('login'))  # Redireciona para login

@app.route('/jogo')  # Define rota do jogo
@login_required  # Aplica decorator que exige login
def jogo_route():
    """
    Rota do jogo (protegida por login).
    Retorna a interface HTML do jogo.
    """
    return render_template('index.html')  # Renderiza o template principal do jogo

# ============================================================================
# SOCKET.IO EVENTS - Comunicação em Tempo Real
# ============================================================================

@socketio.on('connect')  # Define handler para evento de conexão Socket.IO
def handle_connect():
    """
    Handler de conexão Socket.IO.
    Inicia o game loop quando um cliente se conecta.
    """
    print('Client connected')  # Loga conexão no console
    start_game_thread()  # Inicia a thread do jogo se ainda não estiver rodando

@socketio.on('input_jogador')  # Define handler para evento 'input_jogador'
def handle_input(data):
    """
    Handler de entrada do jogador via Socket.IO.
    Recebe comandos do cliente e delega para o jogo.

    Args:
        data (dict): {"acao": str, "estado": str}
    """
    acao = data.get('acao')  # Extrai a ação do payload
    estado = data.get('estado')  # Extrai o estado (pressionado/solto)
    if acao:  # Se houver ação válida
        jogo.processar_comando(acao, estado)  # Envia para a lógica do jogo processar

# ============================================================================
# API REST - Endpoints HTTP
# ============================================================================

@app.route('/api/estado', methods=['GET'])  # Define endpoint REST GET /api/estado
def api_estado():
    """
    Endpoint REST para obter o estado atual do jogo em JSON.
    Método GET conforme padrão REST (leitura de dados).

    Conforme ensinado: métodos HTTP adequados (GET para leitura).

    Returns:
        JSON com estado completo do jogo
    """
    start_game_thread()  # Garante que o jogo está rodando
    return jsonify(jogo.obter_estado())  # Retorna estado do jogo como JSON

@app.route('/api/comando', methods=['POST'])  # Define endpoint REST POST /api/comando
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
    payload = request.get_json(silent=True) or {}  # Obtém JSON do corpo da requisição (seguro contra vazio)
    acao = payload.get('acao')  # Extrai ação
    estado = payload.get('estado')  # Extrai estado

    # Validação de entrada
    if not acao:  # Se não tiver ação
        return jsonify({"erro": "campo 'acao' é obrigatório"}), 400  # Retorna erro 400 Bad Request

    start_game_thread()  # Garante jogo rodando
    jogo.processar_comando(acao, estado)  # Processa comando
    return jsonify({"ok": True, "estado": jogo.obter_estado()})  # Retorna sucesso e novo estado

# ============================================================================
# LÓGICA DE THREAD E GAME LOOP
# ============================================================================

def start_game_thread():
    """
    Inicia o loop do jogo em segundo plano (apenas uma vez).

    Implementa padrão Singleton para a thread do jogo.
    Usa mecanismo do SocketIO para compatibilidade com diferentes servidores.
    """
    global game_thread  # Referencia variável global
    with thread_lock:  # Adquire lock para thread-safety
        if game_thread is None or not game_thread.is_alive():  # Se thread não existe ou morreu
            game_thread = socketio.start_background_task(game_loop)  # Inicia nova background task com game_loop

def game_loop():
    """
    Loop principal do jogo executado em thread separada.

    Responsabilidades:
    - Atualizar estado do jogo (~30 FPS)
    - Emitir estado para clientes conectados via Socket.IO

    Nota: A lógica do jogo está em jogo_headless.py (Facade),
    que coordena Dados/ e Business/ (separação de responsabilidades).
    """
    while True:  # Loop infinito
        jogo.atualizar()  # Atualiza lógica do jogo (física, movimentos)
        state = jogo.obter_estado()  # Obtém estado atualizado
        socketio.emit('estado_jogo', state)  # Envia estado para todos clientes conectados via WebSocket
        socketio.sleep(0.03)  # Pausa por ~30ms para manter aprox. 30 FPS e não travar CPU

# Execução movida para mainFlask.py conforme padrão ensinado
# Para executar: python mainFlask.py