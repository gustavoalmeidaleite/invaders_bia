from utils import LARGURA_TELA, ALTURA_TELA
from .entidade_jogo import EntidadeJogo

class Inimigo(EntidadeJogo):
    """
    Classe para representar um inimigo - SUBCLASSE de EntidadeJogo.
    Implementa HERANÇA: herda atributos e métodos comuns da superclasse EntidadeJogo.
    Demonstra especialização: adiciona atributos específicos (tipo, direção).
    Segue os princípios das aulas do Dr. Edson Nascimento.

    HERANÇA IMPLEMENTADA:
    - Herda: x, y, largura, altura, rect, sprite da superclasse
    - Adiciona: tipo, direção (especialização)
    - Sobrescreve: setters de x e y para validação específica do inimigo
    """

    def __init__(self, x: int, y: int, largura: int = 40, altura: int = 25, tipo: int = 1):
        """
        Construtor da classe Inimigo (subclasse).
        Chama o construtor da superclasse usando super() e adiciona atributos específicos.

        Args:
            x (int): Posição horizontal inicial
            y (int): Posição vertical inicial
            largura (int): Largura do inimigo
            altura (int): Altura do inimigo
            tipo (int): Tipo do inimigo (1, 2, 3 para diferentes sprites)
        """
        # Determina o sprite baseado no tipo antes de chamar super()
        sprite_names = {
            1: "invader_type1.png",
            2: "invader_type2.png",
            3: "invader_type3.png"
        }
        sprite_name = sprite_names.get(tipo, "invader_type1.png")

        # Chama o construtor da superclasse (HERANÇA)
        super().__init__(x, y, largura, altura, sprite_name)

        # Atributos específicos da subclasse (ESPECIALIZAÇÃO)
        self.__direcao = 1  # 1 = direita, -1 = esquerda
        self.__tipo = tipo

    # SOBRESCRITA DE MÉTODOS (Herança + Especialização)
    # Sobrescreve os setters da superclasse para adicionar validação específica do inimigo

    @property
    def x(self) -> int:
        """Getter herdado da superclasse (usa implementação da EntidadeJogo)."""
        return super().x

    @x.setter
    def x(self, novo_x: int):
        """
        SOBRESCRITA: Setter para posição X com validação específica do inimigo.
        Especializa o comportamento da superclasse permitindo movimento além das bordas.
        """
        if -self.largura <= novo_x <= LARGURA_TELA:
            super(Inimigo, self.__class__).x.fset(self, novo_x)

    @property
    def y(self) -> int:
        """Getter herdado da superclasse (usa implementação da EntidadeJogo)."""
        return super().y

    @y.setter
    def y(self, novo_y: int):
        """
        SOBRESCRITA: Setter para posição Y com validação específica do inimigo.
        Especializa o comportamento da superclasse permitindo movimento além das bordas.
        """
        if -self.altura <= novo_y <= ALTURA_TELA:
            super(Inimigo, self.__class__).y.fset(self, novo_y)

    # Properties herdadas da superclasse (largura, altura, rect, sprite)
    # Não precisam ser redefinidas - HERANÇA em ação!

    # Properties específicas da subclasse Inimigo (ESPECIALIZAÇÃO)
    @property
    def direcao(self) -> int:
        """Getter para direção do inimigo (atributo específico da subclasse)."""
        return self.__direcao

    @direcao.setter
    def direcao(self, nova_direcao: int):
        """
        Setter para direção com validação específica do inimigo.
        Aceita apenas -1 (esquerda) ou 1 (direita).
        """
        if nova_direcao in [-1, 1]:
            self.__direcao = nova_direcao
        else:
            raise ValueError("Direção deve ser -1 (esquerda) ou 1 (direita)")

    @property
    def tipo(self) -> int:
        """Getter para tipo do inimigo (atributo específico da subclasse, somente leitura)."""
        return self.__tipo

    # Sobrescrita do método __str__ da superclasse (HERANÇA + ESPECIALIZAÇÃO)
    def __str__(self) -> str:
        """
        Representação em string específica do inimigo.
        Sobrescreve o método da superclasse para incluir informações específicas.
        """
        return f"Inimigo(x={self.x}, y={self.y}, tipo={self.__tipo}, direcao={self.__direcao})"

