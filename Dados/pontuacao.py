class Pontuacao:
    """
    Classe para representar os dados de pontuação do jogo.
    Implementa encapsulamento completo dos atributos com properties.
    Segue os princípios das aulas do Dr. Edson Nascimento.
    """

    def __init__(self, pontos_iniciais: int = 0, vidas_iniciais: int = 3):
        """
        Construtor da classe Pontuacao.
        Inicializa os atributos privados de dados da pontuação.

        Args:
            pontos_iniciais (int): Pontuação inicial do jogador
            vidas_iniciais (int): Número inicial de vidas do jogador
        """
        # Atributos privados (encapsulamento)
        self.__pontos = pontos_iniciais
        self.__vidas_jogador = vidas_iniciais

    # Properties para pontos (com validação)
    @property
    def pontos(self) -> int:
        """Getter para pontos do jogador."""
        return self.__pontos

    @pontos.setter
    def pontos(self, novos_pontos: int):
        """
        Setter para pontos com validação.
        Garante que pontos não sejam negativos.
        """
        if novos_pontos < 0:
            self.__pontos = 0
        else:
            self.__pontos = novos_pontos

    # Properties para vidas_jogador (com validação)
    @property
    def vidas_jogador(self) -> int:
        """Getter para vidas do jogador."""
        return self.__vidas_jogador

    @vidas_jogador.setter
    def vidas_jogador(self, novas_vidas: int):
        """
        Setter para vidas com validação.
        Garante que vidas não sejam negativas e não excedam limite razoável.
        """
        if novas_vidas < 0:
            self.__vidas_jogador = 0
        elif novas_vidas > 99:  # Limite máximo razoável
            self.__vidas_jogador = 99
        else:
            self.__vidas_jogador = novas_vidas

    def definir_pontos(self, pontos: int):
        """
        Método para definir diretamente os pontos.
        Usa a property para garantir validação.
        """
        self.pontos = pontos

    def definir_vidas(self, vidas: int):
        """
        Método para definir diretamente as vidas.
        Usa a property para garantir validação.
        """
        self.vidas_jogador = vidas

    def __str__(self) -> str:
        """
        Método especial para representação em string.
        Facilita debug e exibição de informações.
        """
        return f"Pontuacao(pontos={self.__pontos}, vidas={self.__vidas_jogador})"

    def __eq__(self, other) -> bool:
        """
        Método especial para comparação de igualdade.
        Compara pontos e vidas entre duas instâncias.
        """
        if not isinstance(other, Pontuacao):
            return False
        return (self.__pontos == other.__pontos and
                self.__vidas_jogador == other.__vidas_jogador)