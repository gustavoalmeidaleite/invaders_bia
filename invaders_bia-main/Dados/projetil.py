import pygame
from utils import COR_TIRO, COR_TIRO_INIMIGO, LARGURA_TELA, ALTURA_TELA

class Projetil:
    """
    Classe para representar o tiro disparado pelo jogador ou inimigos.
    Implementa encapsulamento completo dos atributos com properties.
    Segue os princípios das aulas do Dr. Edson Nascimento.
    """

    def __init__(self, x: int, y: int, largura: int = 6, altura: int = 15, eh_inimigo: bool = False):
        """
        Construtor da classe Projetil.
        Inicializa os atributos privados da entidade.

        Args:
            x (int): Posição horizontal inicial
            y (int): Posição vertical inicial
            largura (int): Largura do projétil
            altura (int): Altura do projétil
            eh_inimigo (bool): True se é projétil de inimigo, False se é do jogador
        """
        # Atributos privados (encapsulamento)
        self.__x = x
        self.__y = y
        self.__largura = largura
        self.__altura = altura
        self.__rect = pygame.Rect(x, y, largura, altura)
        self.__eh_inimigo = eh_inimigo

        # Carrega sprite apropriado baseado no tipo
        if eh_inimigo:
            self.__cor_fallback = COR_TIRO_INIMIGO
        else:
            self.__cor_fallback = COR_TIRO

    # Properties para X (com validação)
    @property
    def x(self) -> int:
        """Getter para posição X do projétil."""
        return self.__x

    @x.setter
    def x(self, novo_x: int):
        """
        Setter para posição X.
        Permite movimento além das bordas da tela para projéteis.
        """
        self.__x = novo_x
        self.__rect.x = novo_x

    # Properties para Y (com validação)
    @property
    def y(self) -> int:
        """Getter para posição Y do projétil."""
        return self.__y

    @y.setter
    def y(self, novo_y: int):
        """
        Setter para posição Y.
        Permite movimento além das bordas da tela para projéteis.
        """
        self.__y = novo_y
        self.__rect.y = novo_y

    # Properties para largura (somente leitura)
    @property
    def largura(self) -> int:
        """Getter para largura do projétil (somente leitura)."""
        return self.__largura

    # Properties para altura (somente leitura)
    @property
    def altura(self) -> int:
        """Getter para altura do projétil (somente leitura)."""
        return self.__altura

    # Properties para rect (somente leitura)
    @property
    def rect(self) -> pygame.Rect:
        """Getter para rect do projétil (somente leitura)."""
        return self.__rect

    # Properties para eh_inimigo (somente leitura após criação)
    @property
    def eh_inimigo(self) -> bool:
        """Getter para tipo do projétil (somente leitura)."""
        return self.__eh_inimigo

    # Properties para cor_fallback (somente leitura)
    @property
    def cor_fallback(self) -> tuple:
        """Getter para cor de fallback do projétil (somente leitura)."""
        return self.__cor_fallback

    def atualizar_posicao(self, nova_x: int, nova_y: int):
        """
        Método para atualizar a posição do projétil.
        Usa as properties para garantir validação.
        """
        self.x = nova_x
        self.y = nova_y

