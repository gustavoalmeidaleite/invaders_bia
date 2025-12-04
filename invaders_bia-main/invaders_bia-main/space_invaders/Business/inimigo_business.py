"""
Módulo InimigoBusiness - Camada de Negócio (Business Logic)

Este módulo contém as REGRAS DE NEGÓCIO relacionadas aos inimigos.
Responsabilidades:
- Movimento coordenado dos inimigos em formação
- Lógica de disparo aleatório
- Inversão de direção ao atingir bordas da tela

Padrão de Movimento Space Invaders Clássico:
1. Todos os inimigos movem-se horizontalmente juntos
2. Ao atingir uma borda, todos invertem direção e descem uma linha
3. A cada onda, a velocidade base aumenta (dificuldade progressiva)
"""

import random
from ..Dados.inimigo import Inimigo
from ..Dados.projetil import Projetil
from ..utils import LARGURA_TELA, VELOCIDADE_INIMIGO


class InimigoBusiness:
    """
    Classe de negócio para gerenciar o comportamento dos inimigos.
    
    Atributos:
        inimigos (list): Lista de instâncias de Inimigo
        velocidade_base (float): Velocidade atual da formação
    """

    def __init__(self, inimigos, velocidade_base=VELOCIDADE_INIMIGO):
        """
        Inicializa o gerenciador de comportamento dos inimigos.
        
        Args:
            inimigos (list): Lista de instâncias de Inimigo a gerenciar
            velocidade_base (float): Velocidade inicial de movimento
        """
        self.inimigos = inimigos
        self.velocidade_base = velocidade_base

    def atirar_aleatorio(self):
        """
        Regra de negócio: Inimigo aleatório atira.
        Seleciona um inimigo aleatório para disparar projétil.
        """
        if self.inimigos:
            atirador = random.choice(self.inimigos)
            tiro_x = atirador.x + atirador.largura // 2 - 3
            tiro_y = atirador.y + atirador.altura
            novo_tiro = Projetil(tiro_x, tiro_y, eh_inimigo=True)  # Direção para baixo
            return novo_tiro
        return None

    def mover_inimigos(self, largura_tela):
        """
        Regra de negócio: Movimento dos inimigos em formação.
        Move lateralmente e desce quando atinge as bordas.
        Agora usa properties que incluem validação.
        """
        mover_baixo = False

        # Primeiro, move todos os inimigos lateralmente
        for inimigo in self.inimigos:
            inimigo.x += self.velocidade_base * inimigo.direcao

            # Verifica se algum inimigo atingiu a borda
            if inimigo.x <= 0 or inimigo.x >= largura_tela - inimigo.largura:
                mover_baixo = True

        # Se algum inimigo atingiu a borda, todos mudam direção e descem
        if mover_baixo:
            for inimigo in self.inimigos:
                inimigo.direcao *= -1  # Inverte direção usando property
                inimigo.y += 20        # Desce uma linha usando property
