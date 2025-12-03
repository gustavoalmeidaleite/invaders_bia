from ..Dados.jogador import Jogador
from ..Dados.projetil import Projetil
from ..utils import LARGURA_TELA, ALTURA_TELA, VELOCIDADE_TIRO

class JogadorBusiness:
    """
    Classe para gerenciar as regras de negócio relacionadas ao jogador.
    Implementa as lógicas de ação e comportamento do jogador.
    Segue os princípios de POO: separação entre dados e regras de negócio.
    """
    def __init__(self, jogador, velocidade=None):
        self.jogador = jogador
        self.velocidade = velocidade if velocidade is not None else jogador.velocidade

    def atirar(self):
        """
        Regra de negócio: Disparar um projétil.
        Calcula posição correta e cria novo projétil.
        Agora usa properties e métodos controlados.
        """
        tiro_x = self.jogador.x + self.jogador.largura // 2 - 3
        tiro_y = self.jogador.y
        novo_tiro = Projetil(tiro_x, tiro_y)
        self.jogador.adicionar_tiro(novo_tiro)
        return novo_tiro

    def atualizar_tiros(self):
        """
        Regra de negócio: Atualizar posição dos tiros e remover os que saíram da tela.
        Agora utiliza properties e métodos controlados.
        """
        # Obtém cópia da lista de tiros para iteração segura
        tiros_atuais = self.jogador.tiros
        for tiro in tiros_atuais[:]:
            # Aplica movimento usando a lógica correta
            nova_y = tiro.y - VELOCIDADE_TIRO  # Tiros do jogador sobem
            tiro.atualizar_posicao(tiro.x, nova_y)

            # Remove tiros que saíram da tela usando método controlado
            if tiro.y < -tiro.altura:
                self.jogador.remover_tiro(tiro)

    def mover_esquerda(self, largura_tela):
        """
        Regra de negócio: Mover jogador para a esquerda.
        Agora usa properties que já incluem validação de limites.
        """
        self.jogador.x -= self.velocidade

    def mover_direita(self, largura_tela):
        """
        Regra de negócio: Mover jogador para a direita.
        Agora usa properties que já incluem validação de limites.
        """
        self.jogador.x += self.velocidade

    def mover_cima(self):
        """
        Regra de negócio: Mover jogador para cima.
        Agora usa properties que já incluem validação de limites.
        """
        self.jogador.y -= self.velocidade

    def mover_baixo(self, altura_tela):
        """
        Regra de negócio: Mover jogador para baixo.
        Agora usa properties que já incluem validação de limites.
        """
        self.jogador.y += self.velocidade
