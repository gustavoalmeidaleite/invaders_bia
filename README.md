# Space Invaders - Protótipo

Este é um protótipo inicial do clássico jogo Space Invaders, desenvolvido em Python usando a biblioteca pygame. O projeto foi criado seguindo os princípios da Programação Orientada a Objetos (POO) conforme descrito no arquivo `Contexto.md`.

## Características do Protótipo

### Funcionalidades Implementadas
- ✅ Tela preta de fundo (800x600 pixels)
- ✅ Quadrado verde representando a nave do jogador
- ✅ Movimento horizontal da nave (esquerda/direita)
- ✅ Controles responsivos usando as setas ou teclas A/D

### Conceitos de POO Aplicados

O código demonstra os principais conceitos da Programação Orientada a Objetos:

#### 1. **Classes e Objetos**
- `Jogador`: Representa a nave espacial do jogador
- `Jogo`: Classe principal que gerencia todo o jogo

#### 2. **Encapsulamento**
- Atributos privados controlados através de métodos
- Métodos específicos para cada ação (mover_esquerda, mover_direita)

#### 3. **Abstração**
- Métodos como `desenhar()` escondem os detalhes de implementação
- Interface simples para controlar o jogador

#### 4. **Composição**
- A classe `Jogo` contém uma instância da classe `Jogador`
- Demonstra o relacionamento "tem um" entre as classes

#### 5. **Delegação**
- O jogo delega o controle do movimento para os métodos do jogador
- Separação clara de responsabilidades

## Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- pygame

### Instalação
```bash
# Instalar pygame
pip install pygame

# Executar o jogo
python space_invaders_prototype.py
```

### Controles
- **Seta Esquerda** ou **A**: Move a nave para a esquerda
- **Seta Direita** ou **D**: Move a nave para a direita
- **ESC** ou **X**: Fechar o jogo

## Estrutura do Código

```
space_invaders_prototype.py
├── Classe Jogador
│   ├── __init__()          # Construtor
│   ├── mover_esquerda()    # Movimento para esquerda
│   ├── mover_direita()     # Movimento para direita
│   └── desenhar()          # Renderização na tela
│
└── Classe Jogo
    ├── __init__()          # Inicialização do jogo
    ├── processar_eventos() # Gerenciamento de input
    ├── atualizar()         # Lógica do jogo
    ├── desenhar()          # Renderização geral
    └── executar()          # Loop principal
```

## Próximos Passos

Este protótipo serve como base para implementar:
- [ ] Inimigos (invasores espaciais)
- [ ] Sistema de tiro
- [ ] Detecção de colisões
- [ ] Sistema de pontuação
- [ ] Múltiplas vidas
- [ ] Níveis de dificuldade
- [ ] Efeitos sonoros

## Conceitos de POO Demonstrados

O código segue fielmente os princípios descritos no `Contexto.md`:

- **Variáveis de Instância**: `self.x`, `self.y`, `self.velocidade`
- **Métodos**: Funções que alteram o estado dos objetos
- **Construtor**: `__init__()` para inicializar objetos
- **Mensagens**: Comunicação entre objetos através de chamadas de métodos

Este protótipo estabelece uma base sólida para o desenvolvimento completo do jogo Space Invaders, demonstrando como aplicar os conceitos fundamentais da POO em um projeto prático.
