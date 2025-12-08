# ============================================================================
# IMPORTAÇÕES
# ============================================================================
from ..Dados.pontuacao import Pontuacao  # Classe de dados Pontuacao

# ============================================================================
# CLASSE PONTUACAOBUSINESS - CAMADA DE LÓGICA DE NEGÓCIO (BUSINESS)
# ============================================================================
class PontuacaoBusiness:
    """
    ========================================================================
    CLASSE PONTUACAOBUSINESS - LÓGICA DE NEGÓCIO
    ========================================================================

    PROPÓSITO:
    Esta classe contém as REGRAS DE NEGÓCIO relacionadas à pontuação.
    Implementa CÁLCULOS e OPERAÇÕES sobre os dados de pontuação.

    PRINCÍPIOS DE POO APLICADOS:

    1. SEPARAÇÃO DE RESPONSABILIDADES (SRP):
       - Dados: Classe Pontuacao (armazena pontos e vidas)
       - Lógica: Classe PontuacaoBusiness (calcula e modifica pontuação)

    2. COESÃO:
       - Responsabilidade única: gerenciar regras de pontuação
       - Cálculo de pontos por tipo de inimigo
       - Adição/subtração de pontos e vidas
       - Verificação de game over

    3. ENCAPSULAMENTO:
       - Usa properties e métodos da classe Pontuacao
       - Não acessa atributos privados diretamente

    RELACIONAMENTOS:
    - USA: Pontuacao (lê e modifica via interface pública)
    - USADO POR: Jogo/JogoHeadless, ProjetilBusiness

    ATRIBUTOS:
    - pontuacao: Objeto Pontuacao a gerenciar
    ========================================================================
    """

    def __init__(self, pontuacao):
        """
        CONSTRUTOR DA CLASSE PONTUACAOBUSINESS

        COMPOSIÇÃO: Recebe objeto Pontuacao para gerenciar

        Args:
            pontuacao (Pontuacao): Objeto Pontuacao a gerenciar
        """
        self.pontuacao = pontuacao

    # ========================================================================
    # MÉTODOS DE LÓGICA DE NEGÓCIO - OPERAÇÕES DE PONTUAÇÃO
    # ========================================================================

    def adicionar_pontos(self, pontos):
        """
        REGRA DE NEGÓCIO: Adicionar pontos à pontuação atual

        VALIDAÇÃO: Aceita apenas valores positivos
        ENCAPSULAMENTO: Usa property e método da classe Pontuacao

        Args:
            pontos (int): Quantidade de pontos a adicionar
        """
        if pontos > 0:
            novos_pontos = self.pontuacao.pontos + pontos
            self.pontuacao.definir_pontos(novos_pontos)
        else:
            print("Aviso: Tentativa de adicionar pontos negativos ou zero.")

    def perder_vida(self):
        """
        REGRA DE NEGÓCIO: Jogador perde uma vida

        VALIDAÇÃO: Verifica se ainda há vidas antes de decrementar
        ENCAPSULAMENTO: Usa property e método da classe Pontuacao
        """
        if self.pontuacao.vidas_jogador > 0:
            novas_vidas = self.pontuacao.vidas_jogador - 1
            self.pontuacao.definir_vidas(novas_vidas)
        else:
            print("Aviso: Jogador já não possui vidas.")

    def resetar_pontuacao(self, pontos_iniciais=0, vidas_iniciais=3):
        """
        REGRA DE NEGÓCIO: Resetar pontuação para novo jogo

        Usado ao iniciar nova partida

        Args:
            pontos_iniciais (int): Pontos iniciais (padrão: 0)
            vidas_iniciais (int): Vidas iniciais (padrão: 3)
        """
        self.pontuacao.definir_pontos(pontos_iniciais)
        self.pontuacao.definir_vidas(vidas_iniciais)

    def calcular_pontos_inimigo(self, tipo_inimigo):
        """
        REGRA DE NEGÓCIO: Calcular pontos baseado no tipo de inimigo

        TABELA DE PONTUAÇÃO (regra do jogo):
        - Tipo 1 (linha superior): 30 pontos
        - Tipo 2 (linha média): 20 pontos
        - Tipo 3 (linha inferior): 10 pontos

        Demonstra LÓGICA DE NEGÓCIO centralizada
        Se mudar pontuação, muda apenas aqui

        Args:
            tipo_inimigo (int): Tipo do inimigo (1, 2 ou 3)

        Returns:
            int: Pontos que o inimigo vale
        """
        tabela_pontos = {
            1: 30,  # Inimigo Tipo 1 (mais difícil)
            2: 20,  # Inimigo Tipo 2 (médio)
            3: 10   # Inimigo Tipo 3 (mais fácil)
        }
        return tabela_pontos.get(tipo_inimigo, 10)  # Padrão: 10 pontos

    def adicionar_pontos_inimigo(self, tipo_inimigo):
        """
        REGRA DE NEGÓCIO: Adicionar pontos por destruir inimigo

        COMPOSIÇÃO DE REGRAS:
        1. Calcula pontos baseado no tipo
        2. Adiciona à pontuação atual

        Demonstra REUTILIZAÇÃO de métodos

        Args:
            tipo_inimigo (int): Tipo do inimigo destruído
        """
        pontos = self.calcular_pontos_inimigo(tipo_inimigo)
        self.adicionar_pontos(pontos)

    def adicionar_bonus_interceptacao(self):
        """
        REGRA DE NEGÓCIO: Bônus por interceptar projétil inimigo

        Quando tiro do jogador acerta tiro do inimigo: +5 pontos
        Valor fixo conforme especificação do jogo
        """
        self.adicionar_pontos(5)

    def verificar_game_over(self):
        """
        REGRA DE NEGÓCIO: Verificar se o jogo acabou

        CONDIÇÃO DE GAME OVER: Vidas <= 0

        Returns:
            bool: True se game over, False caso contrário
        """
        return self.pontuacao.vidas_jogador <= 0

    def obter_status_jogo(self):
        """
        MÉTODO UTILITÁRIO: Retorna status completo do jogo

        Facilita consulta de múltiplos dados de uma vez
        Útil para APIs e interfaces

        Returns:
            dict: Dicionário com pontos, vidas e status de game over
        """
        return {
            'pontos': self.pontuacao.pontos,
            'vidas': self.pontuacao.vidas_jogador,
            'game_over': self.verificar_game_over()
        }
