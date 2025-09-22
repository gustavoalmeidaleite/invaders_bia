from utils import VELOCIDADE_JOGADOR, LARGURA_TELA, ALTURA_TELA
from .entidade_jogo import EntidadeJogo

class Jogador(EntidadeJogo):
    """
    Classe que representa o jogador (nave espacial) - SUBCLASSE de EntidadeJogo.
    Implementa HERANÇA: herda atributos e métodos comuns da superclasse EntidadeJogo.
    Demonstra especialização: adiciona atributos específicos (velocidade, tiros).
    Segue os princípios das aulas do Dr. Edson Nascimento.

    HERANÇA IMPLEMENTADA:
    - Herda: x, y, largura, altura, rect, sprite da superclasse
    - Adiciona: velocidade, tiros (especialização)
    - Sobrescreve: setters de x e y para validação específica do jogador
    """

    def __init__(self, x: int, y: int, largura: int = 50, altura: int = 30):
        """
        Construtor da classe Jogador (subclasse).
        Chama o construtor da superclasse usando super() e adiciona atributos específicos.

        Args:
            x (int): Posição horizontal inicial
            y (int): Posição vertical inicial
            largura (int): Largura da nave espacial
            altura (int): Altura da nave espacial
        """
        # Chama o construtor da superclasse (HERANÇA)
        super().__init__(x, y, largura, altura, "player_ship.png")

        # Atributos específicos da subclasse (ESPECIALIZAÇÃO)
        self.__velocidade = VELOCIDADE_JOGADOR
        self.__tiros = []

    # SOBRESCRITA DE MÉTODOS (Herança + Especialização)
    # Sobrescreve os setters da superclasse para adicionar validação específica do jogador

    @property
    def x(self) -> int:
        """Getter herdado da superclasse (usa implementação da EntidadeJogo)."""
        return super().x

    @x.setter
    def x(self, novo_x: int):
        """
        SOBRESCRITA: Setter para posição X com validação específica do jogador.
        Especializa o comportamento da superclasse adicionando limites da tela.
        """
        if 0 <= novo_x <= LARGURA_TELA - self.largura:
            super(Jogador, self.__class__).x.fset(self, novo_x)
        else:
            # Mantém dentro dos limites válidos
            if novo_x < 0:
                super(Jogador, self.__class__).x.fset(self, 0)
            else:
                super(Jogador, self.__class__).x.fset(self, LARGURA_TELA - self.largura)

    @property
    def y(self) -> int:
        """Getter herdado da superclasse (usa implementação da EntidadeJogo)."""
        return super().y

    @y.setter
    def y(self, novo_y: int):
        """
        SOBRESCRITA: Setter para posição Y com validação específica do jogador.
        Especializa o comportamento da superclasse adicionando limites da tela.
        """
        if 0 <= novo_y <= ALTURA_TELA - self.altura:
            super(Jogador, self.__class__).y.fset(self, novo_y)
        else:
            # Mantém dentro dos limites válidos
            if novo_y < 0:
                super(Jogador, self.__class__).y.fset(self, 0)
            else:
                super(Jogador, self.__class__).y.fset(self, ALTURA_TELA - self.altura)

    # Properties herdadas da superclasse (largura, altura, rect, sprite)
    # Não precisam ser redefinidas - HERANÇA em ação!

    # Properties específicas da subclasse Jogador (ESPECIALIZAÇÃO)
    @property
    def velocidade(self) -> int:
        """Getter para velocidade do jogador (atributo específico da subclasse)."""
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, nova_velocidade: int):
        """
        Setter para velocidade com validação específica do jogador.
        Garante velocidade dentro de limites razoáveis.
        """
        if nova_velocidade < 0:
            self.__velocidade = 0
        elif nova_velocidade > 20:  # Limite máximo razoável
            self.__velocidade = 20
        else:
            self.__velocidade = nova_velocidade

    # Properties herdadas (rect, sprite) não precisam ser redefinidas

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

    # Sobrescrita do método __str__ da superclasse (HERANÇA + ESPECIALIZAÇÃO)
    def __str__(self) -> str:
        """
        Representação em string específica do jogador.
        Sobrescreve o método da superclasse para incluir informações específicas.
        """
        return f"Jogador(x={self.x}, y={self.y}, velocidade={self.__velocidade}, tiros={len(self.__tiros)})"

