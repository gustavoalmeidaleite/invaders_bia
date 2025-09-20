import pygame
from utils import carregar_sprite, COR_TIRO, COR_TIRO_INIMIGO, VELOCIDADE_TIRO

class Projetil:
    """Classe para representar o tiro disparado pelo jogador ou inimigos."""
    def __init__(self, x, y, largura=6, altura=15, eh_inimigo=False):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(x, y, largura, altura)
        self.eh_inimigo = eh_inimigo

        # Carrega sprite apropriado
        if eh_inimigo:
            self.sprite = carregar_sprite("bullet_enemy.png", largura, altura)
            self.cor_fallback = COR_TIRO_INIMIGO
        else:
            self.sprite = carregar_sprite("bullet_player.png", largura, altura)
            self.cor_fallback = COR_TIRO

    def mover(self):
        if self.eh_inimigo:
            self.y += VELOCIDADE_TIRO  # Tiros inimigos descem
        else:
            self.y -= VELOCIDADE_TIRO  # Tiros do jogador sobem
        self.rect.y = self.y

    def desenhar(self, tela):
        if self.sprite:
            tela.blit(self.sprite, (self.x, self.y))
        else:
            pygame.draw.rect(tela, self.cor_fallback, self.rect)