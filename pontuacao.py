class Pontuacao:
    def __init__(self):
        self.pontos = 0
        self.vidas_jogador = 3

    def adicionar_pontos(self, pontos):
        self.pontos += pontos

    def perder_vida(self):
        self.vidas_jogador -= 1

    def resetar(self):
        self.pontos = 0
        self.vidas_jogador = 3