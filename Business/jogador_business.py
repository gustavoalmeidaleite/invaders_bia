import pygame
from Dados.jogador import Jogador
from Dados.projetil import Projetil
from utils import LARGURA_TELA, ALTURA_TELA, VELOCIDADE_TIRO

class JogadorBusiness:
    """
    Classe para gerenciar as regras de negócio relacionadas ao jogador.
    Implementa as lógicas de ação e comportamento do jogador.
    Segue os princípios de POO: separação entre dados e regras de negócio.
    """
    def __init__(self, jogador, velocidade=None):
        self.jogador = jogador
        self.velocidade = velocidade if velocidade is not None else jogador.velocidade

    def atirar(self):
        """
        Regra de negócio: Disparar um projétil.
        Calcula posição correta e cria novo projétil.
        """
        tiro_x = self.jogador.x + self.jogador.largura // 2 - 3
        tiro_y = self.jogador.y
        novo_tiro = Projetil(tiro_x, tiro_y)
        self.jogador.tiros.append(novo_tiro)

    def atualizar_tiros(self):
        """
        Regra de negócio: Atualizar posição dos tiros e remover os que saíram da tela.
        Agora utiliza o método correto de movimento dos projéteis.
        """
        for tiro in self.jogador.tiros[:]:
            # Aplica movimento usando a lógica correta
            nova_y = tiro.y - VELOCIDADE_TIRO  # Tiros do jogador sobem
            tiro.atualizar_posicao(tiro.x, nova_y)

            # Remove tiros que saíram da tela
            if tiro.y < -tiro.altura:
                self.jogador.tiros.remove(tiro)

    def mover_esquerda(self, largura_tela):
        """
        Regra de negócio: Mover jogador para a esquerda.
        Inclui validação de limites da tela.
        """
        if self.jogador.x > 0:
            self.jogador.x -= self.velocidade
            self.jogador.rect.x = self.jogador.x

    def mover_direita(self, largura_tela):
        """
        Regra de negócio: Mover jogador para a direita.
        Inclui validação de limites da tela.
        """
        if self.jogador.x < largura_tela - self.jogador.largura:
            self.jogador.x += self.velocidade
            self.jogador.rect.x = self.jogador.x

    def mover_cima(self):
        """
        Regra de negócio: Mover jogador para cima.
        Inclui validação de limites da tela.
        """
        if self.jogador.y > 0:
            self.jogador.y -= self.velocidade
            self.jogador.rect.y = self.jogador.y

    def mover_baixo(self, altura_tela):
        """
        Regra de negócio: Mover jogador para baixo.
        Inclui validação de limites da tela.
        """
        if self.jogador.y < altura_tela - self.jogador.altura:
            self.jogador.y += self.velocidade
            self.jogador.rect.y = self.jogador.y