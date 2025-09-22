# Space Invaders - Protótipo

Este é um protótipo inicial do clássico jogo Space Invaders, desenvolvido em Python usando a biblioteca pygame. O projeto foi criado seguindo os princípios da Programação Orientada a Objetos (POO) conforme descrito no arquivo `Contexto.md`.

## Características do Protótipo

### Funcionalidades Implementadas
- ✅ **Menu Principal** com opções de iniciar e sair
- ✅ **Tela de Game Over** com opções de reiniciar, menu ou sair
- ✅ **Sistema de Estados** (Menu, Jogando, Game Over)
- ✅ **Sistema de Pontuação** com diferentes valores por tipo de inimigo
- ✅ **Sistema de Vidas** (3 vidas iniciais)
- ✅ **Colisão entre Projéteis** com efeitos visuais de explosão
- ✅ **HUD** com pontuação, vidas e controles
- ✅ **Suporte a Sprites** com fallback para retângulos coloridos
- ✅ **3 Tipos de Inimigos** com sprites diferentes
- ✅ **Tiros do Jogador e Inimigos** com sprites específicos
- ✅ **Background Customizável** com suporte a imagem de fundo
- ✅ Tela de fundo (800x600 pixels)
- ✅ Nave do jogador com sprite ou fallback verde
- ✅ **Movimento completo da nave** (esquerda/direita/cima/baixo)
- ✅ Sistema de tiro contínuo
- ✅ Inimigos que se movem e atiram
- ✅ Detecção de colisões
- ✅ Controles responsivos

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

#### Menu e Game Over:
- **Seta Cima/Baixo** ou **W/S**: Navegar nas opções
- **ENTER** ou **ESPAÇO**: Selecionar opção
- **ESC**: Sair do jogo (menu) ou voltar ao menu (game over)

#### Durante o Jogo:
- **Seta Esquerda** ou **A**: Move a nave para a esquerda
- **Seta Direita** ou **D**: Move a nave para a direita
- **Seta Cima** ou **W**: Move a nave para cima
- **Seta Baixo** ou **S**: Move a nave para baixo
- **Z**: Atirar (pode segurar para tiro contínuo)
- **ESC**: Voltar ao menu principal

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

## Arquivos do Projeto

- `space_invaders_prototype.py` - Código principal do jogo
- `sprites/` - Diretório para imagens dos sprites
- `SPRITE_REQUIREMENTS.md` - Lista detalhada de sprites necessários
- `MENU_E_GAME_OVER.md` - Documentação das funcionalidades de menu e game over
- `MOVIMENTO_COMPLETO.md` - Documentação do sistema de movimento em 4 direções
- `COLISAO_PROJETEIS.md` - Documentação do sistema de colisão entre projéteis
- `requirements.txt` - Dependências do projeto

## Sistema de Pontuação

- **Inimigo Tipo 1** (linha superior): 30 pontos
- **Inimigo Tipo 2** (linha média): 20 pontos
- **Inimigo Tipo 3** (linha inferior): 10 pontos
- **Interceptação de Projétil**: 5 pontos bônus

## Próximos Passos

Funcionalidades que podem ser adicionadas:
- [ ] Efeitos sonoros e música
- [ ] Animações de explosão
- [ ] Power-ups especiais
- [ ] Sistema de high scores
- [ ] Múltiplos níveis
- [ ] Configurações de dificuldade
- [ ] Tela de créditos

## Conceitos de POO Demonstrados

O código segue fielmente os princípios descritos no `Contexto.md`:

- **Variáveis de Instância**: `self.x`, `self.y`, `self.velocidade`
- **Métodos**: Funções que alteram o estado dos objetos
- **Construtor**: `__init__()` para inicializar objetos
- **Mensagens**: Comunicação entre objetos através de chamadas de métodos

Este protótipo estabelece uma base sólida para o desenvolvimento completo do jogo Space Invaders, demonstrando como aplicar os conceitos fundamentais da POO em um projeto prático.
