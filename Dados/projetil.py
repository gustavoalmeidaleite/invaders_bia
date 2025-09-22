import pygame
from utils import carregar_sprite, COR_TIRO, COR_TIRO_INIMIGO

class Projetil:
    """
    Classe para representar o tiro disparado pelo jogador ou inimigos.
    Implementa apenas a estrutura de dados, sem lógicas de comportamento.
    Segue os princípios de POO: foca na representação da entidade.
    """
    def __init__(self, x, y, largura=6, altura=15, eh_inimigo=False):
        """
        Construtor da classe Projetil.
        Inicializa apenas os atributos de dados da entidade.
        """
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(x, y, largura, altura)
        self.eh_inimigo = eh_inimigo

        # Carrega sprite apropriado baseado no tipo
        if eh_inimigo:
            self.sprite = carregar_sprite("bullet_enemy.png", largura, altura)
            self.cor_fallback = COR_TIRO_INIMIGO
        else:
            self.sprite = carregar_sprite("bullet_player.png", largura, altura)
            self.cor_fallback = COR_TIRO

    def atualizar_posicao(self, nova_x, nova_y):
        """
        Método para atualizar a posição do projétil.
        Apenas atualiza os dados de posição, sem lógica de movimento.
        """
        self.x = nova_x
        self.y = nova_y
        self.rect.x = nova_x
        self.rect.y = nova_y

