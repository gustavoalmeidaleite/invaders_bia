import pygame
from utils import LARGURA_TELA, ALTURA_TELA

class Inimigo:
    """
    Classe para representar um inimigo.
    Implementa encapsulamento completo dos atributos com properties.
    Segue os princípios das aulas do Dr. Edson Nascimento.
    """

    def __init__(self, x: int, y: int, largura: int = 40, altura: int = 25, tipo: int = 1):
        """
        Construtor da classe Inimigo.
        Inicializa os atributos privados da instância.

        Args:
            x (int): Posição horizontal inicial
            y (int): Posição vertical inicial
            largura (int): Largura do inimigo
            altura (int): Altura do inimigo
            tipo (int): Tipo do inimigo (1, 2, 3 para diferentes sprites)
        """
        # Atributos privados (encapsulamento)
        self.__x = x
        self.__y = y
        self.__largura = largura
        self.__altura = altura
        self.__rect = pygame.Rect(x, y, largura, altura)
        self.__direcao = 1  # 1 = direita, -1 = esquerda
        self.__tipo = tipo

    # Properties para X (com validação de limites)
    @property
    def x(self) -> int:
        """Getter para posição X do inimigo."""
        return self.__x

    @x.setter
    def x(self, novo_x: int):
        """
        Setter para posição X com validação de limites.
        Permite movimento dentro da tela.
        """
        if -self.__largura <= novo_x <= LARGURA_TELA:
            self.__x = novo_x
            self.__rect.x = novo_x

    # Properties para Y (com validação de limites)
    @property
    def y(self) -> int:
        """Getter para posição Y do inimigo."""
        return self.__y

    @y.setter
    def y(self, novo_y: int):
        """
        Setter para posição Y com validação de limites.
        Permite movimento dentro da tela.
        """
        if -self.__altura <= novo_y <= ALTURA_TELA:
            self.__y = novo_y
            self.__rect.y = novo_y

    # Properties para largura (somente leitura)
    @property
    def largura(self) -> int:
        """Getter para largura do inimigo (somente leitura)."""
        return self.__largura

    # Properties para altura (somente leitura)
    @property
    def altura(self) -> int:
        """Getter para altura do inimigo (somente leitura)."""
        return self.__altura

    # Properties para rect (somente leitura)
    @property
    def rect(self) -> pygame.Rect:
        """Getter para rect do inimigo (somente leitura)."""
        return self.__rect

    # Properties para direção (com validação)
    @property
    def direcao(self) -> int:
        """Getter para direção do inimigo."""
        return self.__direcao

    @direcao.setter
    def direcao(self, nova_direcao: int):
        """
        Setter para direção com validação.
        Aceita apenas -1 (esquerda) ou 1 (direita).
        """
        if nova_direcao in [-1, 1]:
            self.__direcao = nova_direcao
        else:
            raise ValueError("Direção deve ser -1 (esquerda) ou 1 (direita)")

    # Properties para tipo (somente leitura após criação)
    @property
    def tipo(self) -> int:
        """Getter para tipo do inimigo (somente leitura)."""
        return self.__tipo


