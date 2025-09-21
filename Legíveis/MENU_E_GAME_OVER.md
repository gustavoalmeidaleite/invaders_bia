# Menu e Game Over - Space Invaders

Este documento descreve as novas funcionalidades de menu e game over implementadas no jogo Space Invaders.

## ✅ Funcionalidades Implementadas

### 🎮 Sistema de Estados
O jogo agora possui três estados principais:
- **ESTADO_MENU**: Tela inicial com opções
- **ESTADO_JOGANDO**: Gameplay principal
- **ESTADO_GAME_OVER**: Tela de fim de jogo

### 📋 Menu Principal

#### Características:
- **Título**: "SPACE INVADERS" em destaque
- **Opções**: 
  - INICIAR - Inicia uma nova partida
  - SAIR - Fecha o jogo
- **Navegação**: Setas ou W/S para navegar
- **Seleção**: ENTER ou ESPAÇO para confirmar
- **Saída**: ESC para sair do jogo

#### Controles do Menu:
- ⬆️ **Seta para Cima** ou **W**: Navegar para cima
- ⬇️ **Seta para Baixo** ou **S**: Navegar para baixo
- ⏎ **ENTER** ou **ESPAÇO**: Selecionar opção
- **ESC**: Sair do jogo

### 💀 Tela de Game Over

#### Características:
- **Título**: "GAME OVER" em vermelho
- **Pontuação**: Exibe a pontuação final do jogador
- **Opções**:
  - JOGAR NOVAMENTE - Reinicia o jogo
  - MENU PRINCIPAL - Volta ao menu
  - SAIR - Fecha o jogo

#### Controles do Game Over:
- ⬆️ **Seta para Cima** ou **W**: Navegar para cima
- ⬇️ **Seta para Baixo** ou **S**: Navegar para baixo
- ⏎ **ENTER** ou **ESPAÇO**: Selecionar opção
- **ESC**: Voltar ao menu principal

### 🎯 Sistema de Pontuação
- **Inimigo Tipo 1** (linha superior): 30 pontos
- **Inimigo Tipo 2** (linha média): 20 pontos
- **Inimigo Tipo 3** (linha inferior): 10 pontos
- Pontuação é exibida no HUD durante o jogo
- Pontuação final é mostrada na tela de game over

### ❤️ Sistema de Vidas
- **Vidas Iniciais**: 3 vidas
- **Perda de Vida**: Quando o jogador é atingido por tiro inimigo
- **Game Over**: Quando todas as vidas são perdidas
- **Invasão**: Game over se inimigos chegarem muito perto do jogador

### 🖥️ HUD (Interface do Usuário)
Durante o gameplay, o HUD exibe:
- **Pontuação atual** (canto superior esquerdo)
- **Vidas restantes** (abaixo da pontuação)
- **Controles** (parte inferior da tela)

## 🎮 Controles do Jogo

### Durante o Gameplay:
- ⬅️ **Seta Esquerda** ou **A**: Mover nave para esquerda
- ➡️ **Seta Direita** ou **D**: Mover nave para direita
- ⬆️ **Seta Cima** ou **W**: Mover nave para cima
- ⬇️ **Seta Baixo** ou **S**: Mover nave para baixo
- **Z**: Atirar (pode segurar para tiro contínuo)
- **ESC**: Voltar ao menu principal

### Navegação Geral:
- **W/S** ou **Setas**: Navegar em menus
- **ENTER/ESPAÇO**: Confirmar seleção
- **ESC**: Voltar/Sair

## 🔄 Fluxo do Jogo

1. **Início**: Jogo abre no menu principal
2. **Seleção**: Jogador escolhe "INICIAR" ou "SAIR"
3. **Gameplay**: Jogo inicia com 3 vidas e pontuação zerada
4. **Progressão**: Jogador destrói inimigos e ganha pontos
5. **Dificuldade**: Velocidade dos inimigos aumenta a cada nível
6. **Game Over**: Quando vidas acabam ou inimigos invadem
7. **Opções**: Jogar novamente, voltar ao menu ou sair

## 🎨 Design Visual

### Cores Utilizadas:
- **Fundo**: Preto (0, 0, 0)
- **Título**: Ciano (0, 255, 255)
- **Texto Normal**: Branco (255, 255, 255)
- **Texto Selecionado**: Amarelo (255, 255, 0)
- **Game Over**: Vermelho (255, 0, 0)

### Fontes:
- **Títulos**: Fonte grande (72px)
- **Opções**: Fonte média (48px)
- **HUD**: Fonte média (36px)
- **Instruções**: Fonte pequena (24px)

## 🔧 Melhorias Técnicas

### Arquitetura:
- **Sistema de Estados**: Gerenciamento limpo de diferentes telas
- **Separação de Responsabilidades**: Classes específicas para Menu e GameOver
- **Reutilização**: Componentes podem ser facilmente modificados
- **Escalabilidade**: Fácil adicionar novos estados (ex: configurações, créditos)

### Classes Adicionadas:
- **Menu**: Gerencia a tela inicial
- **GameOver**: Gerencia a tela de fim de jogo
- **Estados**: Constantes para controle de fluxo

## 🚀 Próximas Funcionalidades Sugeridas

### Possíveis Melhorias:
- [ ] Tela de configurações
- [ ] Sistema de high scores
- [ ] Efeitos sonoros
- [ ] Animações de transição
- [ ] Múltiplos níveis de dificuldade
- [ ] Power-ups especiais
- [ ] Tela de créditos
- [ ] Salvamento de progresso

## 🎯 Como Testar

1. **Execute o jogo**: `python space_invaders_prototype.py`
2. **Teste o menu**: Navegue com W/S, selecione com ENTER
3. **Inicie o jogo**: Escolha "INICIAR"
4. **Jogue**: Use A/D para mover, Z para atirar
5. **Perca vidas**: Deixe-se atingir para testar game over
6. **Teste opções**: Experimente todas as opções do game over

O sistema está totalmente funcional e pronto para uso!
