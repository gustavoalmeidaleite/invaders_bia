import pygame
from utils import carregar_sprite, VELOCIDADE_JOGADOR

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

