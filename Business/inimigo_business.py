import random
from Dados.inimigo import Inimigo
from Dados.projetil import Projetil
from utils import LARGURA_TELA, VELOCIDADE_INIMIGO

class InimigoBusiness:
    def __init__(self, inimigos, velocidade_base=VELOCIDADE_INIMIGO):
        self.inimigos = inimigos
        self.velocidade_base = velocidade_base

    def atirar_aleatorio(self):
        if self.inimigos:
            atirador = random.choice(self.inimigos)
            tiro_x = atirador.x + atirador.largura // 2 - 3
            tiro_y = atirador.y + atirador.altura
            novo_tiro = Projetil(tiro_x, tiro_y, eh_inimigo=True)  # Direção para baixo
            return novo_tiro
        return None