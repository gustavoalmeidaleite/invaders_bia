import pygame
from utils import carregar_sprite, LARGURA_TELA, ALTURA_TELA

class EntidadeJogo:
    """
    Classe base para todas as entidades do jogo (Superclasse).
    Implementa os atributos e métodos comuns a todas as entidades.
    Demonstra o conceito de HERANÇA
    
    Esta é a SUPERCLASSE que contém:
    - Atributos comuns: posição (x, y), dimensões (largura, altura), rect, sprite
    - Properties comuns: getters e setters para posição e dimensões
    - Métodos comuns: carregamento de sprite e atualização de rect
    """

    def __init__(self, x: int, y: int, largura: int, altura: int, sprite_nome: str = None):
        """
        Construtor da classe base EntidadeJogo.
        Inicializa os atributos privados comuns a todas as entidades.
        
        Args:
            x (int): Posição horizontal inicial
            y (int): Posição vertical inicial
            largura (int): Largura da entidade
            altura (int): Altura da entidade
            sprite_nome (str): Nome do arquivo de sprite (opcional)
        """
        # Atributos privados comuns (encapsulamento)
        self._x = x  # Protegido para permitir acesso das subclasses
        self._y = y
        self._largura = largura
        self._altura = altura
        self._rect = pygame.Rect(x, y, largura, altura)
        
        # Carrega sprite se fornecido
        if sprite_nome:
            self._sprite = carregar_sprite(sprite_nome, largura, altura)
        else:
            self._sprite = None

    # Properties para X (implementação base)
    @property
    def x(self) -> int:
        """Getter para posição X da entidade."""
        return self._x

    @x.setter
    def x(self, novo_x: int):
        """
        Setter para posição X (implementação base).
        Subclasses podem sobrescrever para adicionar validações específicas.
        """
        self._x = novo_x
        self._rect.x = novo_x

    # Properties para Y (implementação base)
    @property
    def y(self) -> int:
        """Getter para posição Y da entidade."""
        return self._y

    @y.setter
    def y(self, novo_y: int):
        """
        Setter para posição Y (implementação base).
        Subclasses podem sobrescrever para adicionar validações específicas.
        """
        self._y = novo_y
        self._rect.y = novo_y

    # Properties para largura (somente leitura)
    @property
    def largura(self) -> int:
        """Getter para largura da entidade (somente leitura)."""
        return self._largura

    # Properties para altura (somente leitura)
    @property
    def altura(self) -> int:
        """Getter para altura da entidade (somente leitura)."""
        return self._altura

    # Properties para rect (somente leitura)
    @property
    def rect(self) -> pygame.Rect:
        """Getter para rect da entidade (somente leitura)."""
        return self._rect

    # Properties para sprite (somente leitura)
    @property
    def sprite(self):
        """Getter para sprite da entidade (somente leitura)."""
        return self._sprite

    def atualizar_posicao(self, novo_x: int, novo_y: int):
        """
        Método comum para atualizar posição da entidade.
        Pode ser usado por todas as subclasses.
        """
        self.x = novo_x
        self.y = novo_y

    def obter_centro(self) -> tuple:
        """
        Método comum para obter o centro da entidade.
        Útil para cálculos de colisão e posicionamento.
        """
        centro_x = self._x + self._largura // 2
        centro_y = self._y + self._altura // 2
        return (centro_x, centro_y)

    def esta_dentro_da_tela(self) -> bool:
        """
        Método comum para verificar se a entidade está dentro da tela.
        Implementação base que pode ser sobrescrita pelas subclasses.
        """
        return (0 <= self._x <= LARGURA_TELA - self._largura and 
                0 <= self._y <= ALTURA_TELA - self._altura)

    def __str__(self) -> str:
        """
        Representação em string da entidade.
        Método especial que pode ser sobrescrito pelas subclasses.
        """
        return f"EntidadeJogo(x={self._x}, y={self._y}, largura={self._largura}, altura={self._altura})"
