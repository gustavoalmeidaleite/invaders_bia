import pygame
from utils import carregar_sprite

class Inimigo:
    """Classe para representar um inimigo."""
    def __init__(self, x, y, largura=40, altura=25, tipo=1):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(x, y, largura, altura)
        self.direcao = 1  # 1 = direita, -1 = esquerda
        self.tipo = tipo  # Tipo do inimigo (1, 2, 3 para diferentes sprites)

        # Carrega sprite baseado no tipo
        sprite_names = {
            1: "invader_type1.png",
            2: "invader_type2.png",
            3: "invader_type3.png"
        }
        sprite_name = sprite_names.get(tipo, "invader_type1.png")
        self.sprite = carregar_sprite(sprite_name, largura, altura)

