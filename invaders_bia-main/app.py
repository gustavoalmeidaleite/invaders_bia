from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import time
from jogo_headless import JogoHeadless

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# Using threading as requested for simplicity
socketio = SocketIO(app, async_mode='threading')

# Initialize game
jogo = JogoHeadless()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('input_jogador')
def handle_input(data):
    if 'acao' in data:
        jogo.processar_comando(data['acao'])

def game_loop():
    """
    Game loop running in a separate thread.
    Updates game state and emits it to clients.
    """
    while True:
        jogo.atualizar()
        state = jogo.obter_estado()
        socketio.emit('estado_jogo', state)
        time.sleep(0.03)  # ~30 FPS

if __name__ == '__main__':
    # Start game loop in a separate thread
    game_thread = threading.Thread(target=game_loop)
    game_thread.daemon = True
    game_thread.start()
    
    socketio.run(app, debug=True)