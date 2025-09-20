import pygame
from utils import carregar_sprite

class Barreira:
    def __init__(self, x, y, largura=60, altura=40):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(x, y, largura, altura)
        self.sprite = None  # Carregado no business
        self.vida = 3

    def desenhar(self, tela):
        if self.sprite:
            tela.blit(self.sprite, (self.x, self.y))
        else:
            pygame.draw.rect(tela, (0, 0, 255), self.rect)