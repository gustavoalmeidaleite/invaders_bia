class Pontuacao:
    """
    Classe para representar os dados de pontuação do jogo.
    Implementa apenas a estrutura de dados, sem lógicas de operação.
    Segue os princípios de POO: foca na representação dos dados de pontuação.
    """
    def __init__(self, pontos_iniciais=0, vidas_iniciais=3):
        """
        Construtor da classe Pontuacao.
        Inicializa apenas os atributos de dados da pontuação.
        """
        self.pontos = pontos_iniciais
        self.vidas_jogador = vidas_iniciais

    def definir_pontos(self, pontos):
        """
        Método para definir diretamente os pontos.
        Apenas atualiza o dado, sem lógica de cálculo.
        """
        self.pontos = pontos

    def definir_vidas(self, vidas):
        """
        Método para definir diretamente as vidas.
        Apenas atualiza o dado, sem lógica de operação.
        """
        self.vidas_jogador = vidas