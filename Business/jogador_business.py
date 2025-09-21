import pygame
from Dados.jogador import Jogador
from Dados.projetil import Projetil
from utils import LARGURA_TELA, ALTURA_TELA

class JogadorBusiness:
    def __init__(self, jogador, velocidade=None):
        self.jogador = jogador
        self.velocidade = velocidade if velocidade is not None else jogador.velocidade

    def atirar(self):
        """
        Método para disparar um tiro.
        """
        tiro_x = self.jogador.x + self.jogador.largura // 2 - 3
        tiro_y = self.jogador.y
        novo_tiro = Projetil(tiro_x, tiro_y)
        self.jogador.tiros.append(novo_tiro)

    def atualizar_tiros(self):
        """
        Método para atualizar a posição dos tiros e remover os que saíram da tela.
        """
        for tiro in self.jogador.tiros[:]:
            tiro.mover()
            if tiro.y < -tiro.altura:
                self.jogador.tiros.remove(tiro)