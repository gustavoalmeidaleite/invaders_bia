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