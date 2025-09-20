import pygame
from jogador import Jogador
from projetil import Projetil
from utils import LARGURA_TELA, ALTURA_TELA

class JogadorBusiness:
    def __init__(self, jogador, velocidade=None):
        self.jogador = jogador
        self.velocidade = velocidade if velocidade is not None else jogador.velocidade

    def mover_esquerda(self):
        """
        Método para mover o jogador para a esquerda.
        Demonstra encapsulamento: o método controla como o estado do objeto é alterado.
        """
        if self.jogador.x > 0:
            self.jogador.x -= self.velocidade
            self.jogador.rect.x = self.jogador.x
    
    def mover_direita(self):
        """
        Método para mover o jogador para a direita.
        """
        if self.jogador.x < LARGURA_TELA - self.jogador.largura:
            self.jogador.x += self.velocidade
            self.jogador.rect.x = self.jogador.x

    def mover_cima(self):
        """
        Método para mover o jogador para cima.
        """
        if self.jogador.y > 0:
            self.jogador.y -= self.velocidade
            self.jogador.rect.y = self.jogador.y

    def mover_baixo(self):
        """
        Método para mover o jogador para baixo.
        """
        if self.jogador.y < ALTURA_TELA - self.jogador.altura:
            self.jogador.y += self.velocidade
            self.jogador.rect.y = self.jogador.y

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