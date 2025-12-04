"""
Módulo PontuacaoBusiness - Camada de Negócio (Business Logic)

Este módulo contém as REGRAS DE NEGÓCIO relacionadas à pontuação.
Responsabilidades:
- Adicionar pontos por destruir inimigos (baseado no tipo)
- Adicionar bônus por interceptar projéteis inimigos
- Gerenciar vidas do jogador (perder vida, verificar game over)
- Resetar pontuação para novo jogo

Tabela de Pontuação:
- Inimigo Tipo 1 (linha superior): 30 pontos
- Inimigo Tipo 2 (linha média): 20 pontos
- Inimigo Tipo 3 (linha inferior): 10 pontos
- Bônus de interceptação: 5 pontos

Separação de Responsabilidades:
- Pontuacao (Dados): Armazena valores
- PontuacaoBusiness (este arquivo): Aplica regras e validações
"""

from ..Dados.pontuacao import Pontuacao

class PontuacaoBusiness:
    """
    Classe para gerenciar as regras de negócio relacionadas à pontuação.
    Implementa as lógicas de operação sobre os dados de pontuação.
    Segue os princípios de POO: separação entre dados e regras de negócio.
    """
    
    def __init__(self, pontuacao):
        """
        Construtor da classe PontuacaoBusiness.
        Recebe uma instância de Pontuacao para aplicar as regras de negócio.
        """
        self.pontuacao = pontuacao

    def adicionar_pontos(self, pontos):
        """
        Regra de negócio: Adicionar pontos à pontuação atual.
        Valida se os pontos são positivos antes de adicionar.
        """
        if pontos > 0:
            novos_pontos = self.pontuacao.pontos + pontos
            self.pontuacao.definir_pontos(novos_pontos)
        else:
            print("Aviso: Tentativa de adicionar pontos negativos ou zero.")

    def perder_vida(self):
        """
        Regra de negócio: Jogador perde uma vida.
        Valida se ainda há vidas antes de decrementar.
        """
        if self.pontuacao.vidas_jogador > 0:
            novas_vidas = self.pontuacao.vidas_jogador - 1
            self.pontuacao.definir_vidas(novas_vidas)
        else:
            print("Aviso: Jogador já não possui vidas.")

    def resetar_pontuacao(self, pontos_iniciais=0, vidas_iniciais=3):
        """
        Regra de negócio: Resetar pontuação para início de novo jogo.
        Define valores padrão para início de partida.
        """
        self.pontuacao.definir_pontos(pontos_iniciais)
        self.pontuacao.definir_vidas(vidas_iniciais)

    def calcular_pontos_inimigo(self, tipo_inimigo):
        """
        Regra de negócio: Calcular pontos baseado no tipo de inimigo.
        Implementa a tabela de pontuação do jogo.
        """
        tabela_pontos = {
            1: 30,  # Inimigo Tipo 1 (linha superior)
            2: 20,  # Inimigo Tipo 2 (linha média)
            3: 10   # Inimigo Tipo 3 (linha inferior)
        }
        return tabela_pontos.get(tipo_inimigo, 10)  # Valor padrão: 10 pontos

    def adicionar_pontos_inimigo(self, tipo_inimigo):
        """
        Regra de negócio: Adicionar pontos por destruir inimigo.
        Combina cálculo de pontos com adição à pontuação.
        """
        pontos = self.calcular_pontos_inimigo(tipo_inimigo)
        self.adicionar_pontos(pontos)

    def adicionar_bonus_interceptacao(self):
        """
        Regra de negócio: Bônus por interceptar projétil inimigo.
        Valor fixo de 5 pontos conforme especificação do jogo.
        """
        self.adicionar_pontos(5)

    def verificar_game_over(self):
        """
        Regra de negócio: Verificar se o jogo acabou.
        Retorna True se o jogador não tem mais vidas.
        """
        return self.pontuacao.vidas_jogador <= 0

    def obter_status_jogo(self):
        """
        Método utilitário: Retorna informações do status atual.
        Facilita a consulta dos dados de pontuação.
        """
        return {
            'pontos': self.pontuacao.pontos,
            'vidas': self.pontuacao.vidas_jogador,
            'game_over': self.verificar_game_over()
        }
