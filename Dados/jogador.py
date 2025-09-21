import pygame
from utils import carregar_sprite, COR_JOGADOR, VELOCIDADE_JOGADOR

class Jogador:
    """
    Classe que representa o jogador (nave espacial).
    Implementa os conceitos de POO: encapsulamento dos atributos e métodos.
    """

    def __init__(self, x, y, largura=50, altura=30):
        """
        Construtor da classe Jogador.
        Inicializa os atributos da instância (variáveis de instância).
        """
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = VELOCIDADE_JOGADOR
        self.rect = pygame.Rect(x, y, largura, altura)
        self.tiros = []

        # Carrega sprite do jogador
        self.sprite = carregar_sprite("player_ship.png", largura, altura)

    def desenhar(self, tela):
        """
        Método para desenhar o jogador na tela.
        Demonstra abstração: esconde os detalhes de como o desenho é feito.
        """
        if self.sprite:
            sprite_rect = self.sprite.get_rect(center=self.rect.center)
            tela.blit(self.sprite, sprite_rect)
        else:
            pygame.draw.rect(tela, COR_JOGADOR, self.rect)