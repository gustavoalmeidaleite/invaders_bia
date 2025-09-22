import pygame
from utils import carregar_sprite, VELOCIDADE_JOGADOR, LARGURA_TELA, ALTURA_TELA

class Jogador:
    """
    Classe que representa o jogador (nave espacial).
    Implementa os conceitos de POO: encapsulamento completo dos atributos com properties.
    Segue os princípios das aulas do Dr. Edson Nascimento.
    """

    def __init__(self, x: int, y: int, largura: int = 50, altura: int = 30):
        """
        Construtor da classe Jogador.
        Inicializa os atributos privados da instância (variáveis de instância).

        Args:
            x (int): Posição horizontal inicial
            y (int): Posição vertical inicial
            largura (int): Largura da nave espacial
            altura (int): Altura da nave espacial
        """
        # Atributos privados (encapsulamento)
        self.__x = x
        self.__y = y
        self.__largura = largura
        self.__altura = altura
        self.__velocidade = VELOCIDADE_JOGADOR
        self.__rect = pygame.Rect(x, y, largura, altura)
        self.__tiros = []

        # Carrega sprite do jogador
        self.__sprite = carregar_sprite("player_ship.png", largura, altura)

    # Properties para X (com validação de limites da tela)
    @property
    def x(self) -> int:
        """Getter para posição X do jogador."""
        return self.__x

    @x.setter
    def x(self, novo_x: int):
        """
        Setter para posição X com validação de limites.
        Garante que o jogador não saia da tela.
        """
        if 0 <= novo_x <= LARGURA_TELA - self.__largura:
            self.__x = novo_x
            self.__rect.x = novo_x
        else:
            # Mantém dentro dos limites válidos
            if novo_x < 0:
                self.__x = 0
                self.__rect.x = 0
            else:
                self.__x = LARGURA_TELA - self.__largura
                self.__rect.x = self.__x

    # Properties para Y (com validação de limites da tela)
    @property
    def y(self) -> int:
        """Getter para posição Y do jogador."""
        return self.__y

    @y.setter
    def y(self, novo_y: int):
        """
        Setter para posição Y com validação de limites.
        Garante que o jogador não saia da tela.
        """
        if 0 <= novo_y <= ALTURA_TELA - self.__altura:
            self.__y = novo_y
            self.__rect.y = novo_y
        else:
            # Mantém dentro dos limites válidos
            if novo_y < 0:
                self.__y = 0
                self.__rect.y = 0
            else:
                self.__y = ALTURA_TELA - self.__altura
                self.__rect.y = self.__y

    # Properties para largura (somente leitura)
    @property
    def largura(self) -> int:
        """Getter para largura do jogador (somente leitura)."""
        return self.__largura

    # Properties para altura (somente leitura)
    @property
    def altura(self) -> int:
        """Getter para altura do jogador (somente leitura)."""
        return self.__altura

    # Properties para velocidade (com validação)
    @property
    def velocidade(self) -> int:
        """Getter para velocidade do jogador."""
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, nova_velocidade: int):
        """
        Setter para velocidade com validação.
        Garante velocidade dentro de limites razoáveis.
        """
        if nova_velocidade < 0:
            self.__velocidade = 0
        elif nova_velocidade > 20:  # Limite máximo razoável
            self.__velocidade = 20
        else:
            self.__velocidade = nova_velocidade

    # Properties para rect (somente leitura)
    @property
    def rect(self) -> pygame.Rect:
        """Getter para rect do jogador (somente leitura)."""
        return self.__rect

    # Properties para tiros (acesso controlado)
    @property
    def tiros(self) -> list:
        """Getter para lista de tiros (retorna cópia para proteção)."""
        return self.__tiros.copy()

    def adicionar_tiro(self, tiro):
        """
        Método para adicionar tiro à lista de forma controlada.
        Substitui o acesso direto à lista.
        """
        self.__tiros.append(tiro)

    def remover_tiro(self, tiro):
        """
        Método para remover tiro da lista de forma controlada.
        Substitui o acesso direto à lista.
        """
        if tiro in self.__tiros:
            self.__tiros.remove(tiro)

    def limpar_tiros(self):
        """Método para limpar todos os tiros."""
        self.__tiros.clear()

    # Properties para sprite (somente leitura)
    @property
    def sprite(self):
        """Getter para sprite do jogador (somente leitura)."""
        return self.__sprite

