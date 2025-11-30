from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
from jogo_headless import JogoHeadless

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# Using threading as requested for simplicity
socketio = SocketIO(app, async_mode='threading')

# Controla o loop do jogo para não criar múltiplas threads quando o app é carregado pelo Flask
game_thread = None
thread_lock = threading.Lock()

# Initialize game
jogo = JogoHeadless()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    start_game_thread()

@socketio.on('input_jogador')
def handle_input(data):
    if 'acao' in data:
        jogo.processar_comando(data['acao'])

def start_game_thread():
    """
    Inicia o loop do jogo em segundo plano (apenas uma vez).
    Usamos o mecanismo do SocketIO para manter compatibilidade com diferentes servidores.
    """
    global game_thread
    with thread_lock:
        if game_thread is None or not game_thread.is_alive():
            game_thread = socketio.start_background_task(game_loop)

def game_loop():
    """
    Game loop running in a separate thread.
    Updates game state and emits it to clients.
    """
    while True:
        jogo.atualizar()
        state = jogo.obter_estado()
        socketio.emit('estado_jogo', state)
        socketio.sleep(0.03)  # ~30 FPS

if __name__ == '__main__':
    # Start game loop before serving
    start_game_thread()
    
    socketio.run(app, debug=True)
