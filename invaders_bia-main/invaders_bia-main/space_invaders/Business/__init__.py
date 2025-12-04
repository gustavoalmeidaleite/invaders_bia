"""
Pacote Business - Camada de Negócio (Business Logic)

Este pacote contém as classes com REGRAS DE NEGÓCIO do jogo.
Seguindo os princípios de POO, estas classes:

1. RECEBEM instâncias da camada Dados para operar
2. IMPLEMENTAM a lógica de comportamento e ações
3. VALIDAM operações antes de executá-las

Classes disponíveis:
- JogadorBusiness: Movimentação e disparo do jogador
- InimigoBusiness: Movimento em formação e tiro dos inimigos
- ProjetilBusiness: Movimento de projéteis e detecção de colisões
- PontuacaoBusiness: Cálculo de pontos, bônus e verificação de game over

Separação de Responsabilidades:
- Dados/: O QUE cada entidade É (atributos)
- Business/: O QUE cada entidade FAZ (comportamento)
"""