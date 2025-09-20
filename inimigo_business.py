import random
from inimigo import Inimigo
from projetil import Projetil
from utils import LARGURA_TELA, VELOCIDADE_INIMIGO

class InimigoBusiness:
    def __init__(self, inimigos, velocidade_base=VELOCIDADE_INIMIGO):
        self.inimigos = inimigos
        self.velocidade_base = velocidade_base

    def mover_inimigos(self):
        mover_baixo = False
        for inimigo in self.inimigos:
            inimigo.x += self.velocidade_base * inimigo.direcao
            inimigo.rect.x = inimigo.x
            if inimigo.x <= 0 or inimigo.x >= LARGURA_TELA - inimigo.largura:
                mover_baixo = True
        if mover_baixo:
            for inimigo in self.inimigos:
                inimigo.direcao *= -1
                inimigo.y += 20
                inimigo.rect.y = inimigo.y

    def atirar_aleatorio(self):
        if self.inimigos:
            atirador = random.choice(self.inimigos)
            tiro_x = atirador.x + atirador.largura // 2 - 3
            tiro_y = atirador.y + atirador.altura
            novo_tiro = Projetil(tiro_x, tiro_y, eh_inimigo=True)  # Direção para baixo
            return novo_tiro
        return None