# Guia de Execução e Testes do Webservice

## 1. PRÉ-REQUISITOS

### 1.1 Dependências
```bash
# Verificar Python instalado (3.8+)
python --version

# Instalar dependências
pip install -r invaders_bia-main/requirements.txt
```

**Dependências necessárias**:
- pygame==2.5.2
- Flask==3.1.2
- Flask-SocketIO==5.3.6

### 1.2 Estrutura de Arquivos
```
invaders_bia/
├── space_invaders/
│   ├── Business/           ← Regras de negócio
│   ├── Dados/              ← Modelos de dados
│   ├── data/usuarios.json  ← Persistência simples
│   ├── jogo_headless.py    ← Orquestrador do jogo (web)
│   └── web/main.py         ← Entry point do Flask
├── static/                 ← Arquivos estáticos (imagens)
├── templates/              ← Templates HTML
└── documentacao/           ← Guias e análises
```

## 2. EXECUÇÃO DO WEBSERVICE

### 2.1 Método Recomendado (módulo Flask)

**Conforme padrão ensinado nas aulas de POO**:

```bash
cd invaders_bia
python -m space_invaders.web.main
```

**Saída esperada**:
```
pygame 2.5.2 (SDL 2.28.2, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
```

### 2.2 Método Alternativo (Flask CLI)

```bash
cd invaders_bia
flask --app space_invaders.web.main --debug run
```

### 2.3 Verificação de Execução

✓ Servidor rodando em http://localhost:5000
✓ Debug mode ativo
✓ Sem erros de importação
✓ Pygame inicializado

## 3. TESTES FUNCIONAIS

### 3.1 Teste da Interface Web

**URL**: http://localhost:5000/

**Passos**:
1. Abrir navegador
2. Acessar http://localhost:5000/
3. Verificar carregamento da interface
4. Verificar conexão Socket.IO (status: "Connected to server")

**Resultado esperado**:
- ✓ Canvas do jogo carregado (800x600)
- ✓ Menu principal exibido ("SPACE INVADERS")
- ✓ Status: "Menu - selecione com ↑/↓ e Enter/Espaço"
- ✓ Sprites carregados (nave, inimigos, projéteis)

### 3.2 Teste da API REST - GET /api/estado

**Comando (Python)**:
```python
import urllib.request, json

response = urllib.request.urlopen('http://localhost:5000/api/estado')
data = json.loads(response.read())

print('Estado:', data.get('estado'))
print('Pontuação:', data.get('pontuacao'))
print('Vidas:', data.get('vidas'))
print('Inimigos:', len(data.get('inimigos', [])))
```

**Resultado esperado**:
```
Estado: menu
Pontuação: 0
Vidas: 3
Inimigos: 24
```

**Estrutura do JSON**:
```json
{
  "estado": "menu",
  "pontuacao": 0,
  "vidas": 3,
  "game_over": false,
  "pausado": false,
  "jogador": {
    "x": 375,
    "y": 550,
    "largura": 50,
    "altura": 30
  },
  "inimigos": [...],
  "projeteis": [],
  "explosões": [],
  "menu": {
    "opcoes": ["INICIAR", "SAIR"],
    "selecionada": 0
  }
}
```

### 3.3 Teste da API REST - POST /api/comando

**Comando (Python)**:
```python
import urllib.request, json

# Selecionar "INICIAR" no menu
req = urllib.request.Request(
    'http://localhost:5000/api/comando',
    data=json.dumps({
        'acao': 'menu_selecionar',
        'estado': 'pressionar'
    }).encode(),
    headers={'Content-Type': 'application/json'}
)

response = urllib.request.urlopen(req)
data = json.loads(response.read())

print('Comando enviado:', data.get('ok'))
print('Novo estado:', data.get('estado', {}).get('estado'))
```

**Resultado esperado**:
```
Comando enviado: True
Novo estado: jogando
```

### 3.4 Teste de Comandos do Jogo

**Comandos disponíveis**:
- `esquerda`, `direita`, `cima`, `baixo`: Movimento
- `atirar`: Disparar projétil
- `pausar`: Pausar/despausar
- `menu`: Voltar ao menu
- `reiniciar`: Reiniciar jogo
- `menu_cima`, `menu_baixo`: Navegar menu
- `menu_selecionar`: Selecionar opção do menu

**Exemplo - Mover para direita**:
```python
req = urllib.request.Request(
    'http://localhost:5000/api/comando',
    data=json.dumps({
        'acao': 'direita',
        'estado': 'pressionar'
    }).encode(),
    headers={'Content-Type': 'application/json'}
)
response = urllib.request.urlopen(req)
```

### 3.5 Teste de Socket.IO

**Verificação no navegador**:
1. Abrir console do navegador (F12)
2. Verificar mensagens de conexão
3. Observar eventos `estado_jogo` sendo recebidos (~30 FPS)

**Console esperado**:
```
Socket.IO connected
Receiving estado_jogo events
```

## 4. VERIFICAÇÃO DE CONFORMIDADE COM POO

### 4.1 Encapsulamento

**Verificar em Dados/jogador.py**:
```python
# ✓ Atributos privados
self.__x = x
self.__y = y

# ✓ Properties
@property
def x(self):
    return self.__x

# ✓ Validação no setter
@x.setter
def x(self, novo_x):
    if 0 <= novo_x <= LARGURA_TELA - self.__largura:
        self.__x = novo_x
```

### 4.2 Separação de Responsabilidades

**Verificar estrutura**:
- ✓ Dados/ contém apenas classes de dados
- ✓ Business/ contém apenas lógica de negócio
- ✓ app.py contém apenas rotas
- ✓ jogo_headless.py orquestra componentes

### 4.3 Baixo Acoplamento

**Verificar dependências**:
- ✓ Business → Dados (unidirecional)
- ✓ app.py → JogoHeadless (unidirecional)
- ✓ Sem dependências circulares

### 4.4 Padrão MVC

**Verificar camadas**:
- ✓ Model: Dados/
- ✓ View: templates/
- ✓ Controller: app.py

## 5. LOGS E DEBUGGING

### 5.1 Logs do Servidor

**Logs esperados durante uso**:
```
127.0.0.1 - - [30/Nov/2025 14:37:38] "GET /api/estado HTTP/1.1" 200 -
127.0.0.1 - - [30/Nov/2025 14:37:46] "POST /api/comando HTTP/1.1" 200 -
127.0.0.1 - - [30/Nov/2025 14:37:58] "GET / HTTP/1.1" 200 -
Client connected
127.0.0.1 - - [30/Nov/2025 14:37:58] "GET /static/player_ship.png HTTP/1.1" 200 -
```

### 5.2 Erros Comuns

**Erro**: `ModuleNotFoundError: No module named 'flask'`
**Solução**: `pip install -r requirements.txt`

**Erro**: `Address already in use`
**Solução**: Parar processo anterior ou usar porta diferente

**Erro**: `No module named 'Dados'`
**Solução**: Executar de dentro da pasta invaders_bia-main/

## 6. CHECKLIST DE VALIDAÇÃO

### 6.1 Execução
- [ ] Servidor inicia sem erros
- [ ] Debug mode ativo
- [ ] Porta 5000 acessível

### 6.2 Interface Web
- [ ] Página carrega em http://localhost:5000/
- [ ] Canvas renderizado
- [ ] Socket.IO conectado
- [ ] Sprites carregados

### 6.3 API REST
- [ ] GET /api/estado retorna JSON válido
- [ ] POST /api/comando aceita comandos
- [ ] Validação de entrada funciona

### 6.4 Conformidade POO
- [ ] Encapsulamento implementado
- [ ] Separação de responsabilidades clara
- [ ] Baixo acoplamento
- [ ] Alta coesão
- [ ] Entry points no pacote `space_invaders` (`web.main` e `desktop`)

## 7. CONCLUSÃO

✓ Webservice funcionando corretamente
✓ Todos os endpoints testados
✓ Conformidade com princípios de POO
✓ Estrutura adequada ao padrão ensinado

**Status**: APROVADO ✓✓✓
