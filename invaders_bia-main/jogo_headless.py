import pygame
from Dados.jogador import Jogador
from Business.jogador_business import JogadorBusiness
from Dados.inimigo import Inimigo
from Business.inimigo_business import InimigoBusiness
from Business.projetil_business import ProjetilBusiness
from Dados.pontuacao import Pontuacao
from Business.pontuacao_business import PontuacaoBusiness
from utils import *

class JogoHeadless:
    """
    Classe principal que gerencia o jogo em modo headless (sem interface gráfica).
    Focada apenas na lógica e estado do jogo.
    """

    def __init__(self):
        """
        Construtor da classe JogoHeadless.
        Inicializa os componentes lógicos do jogo.
        """
        # Inicializa pygame apenas para funcionalidades básicas (como Rect e time)
        # Não inicializa display ou mixer
        if not pygame.get_init():
            pygame.init()
            
        self.rodando = True
        self.game_over = False

        # Variáveis do jogo
        self.pontuacao = Pontuacao()
        self.pontuacao_business = PontuacaoBusiness(self.pontuacao)
        self.efeitos_explosao = []

        # Inicializa componentes do jogo
        self.inicializar_jogo()

        # Velocidades para movimento (mantendo as constantes do utils)
        self.velocidade_jogador = VELOCIDADE_JOGADOR
        self.velocidade_inimigo = VELOCIDADE_INIMIGO
        self.velocidade_tiro = VELOCIDADE_TIRO

    def inicializar_jogo(self):
        """Inicializa ou reinicializa os componentes do jogo."""
        self.jogador = Jogador(LARGURA_TELA // 2 - 25, ALTURA_TELA - 50)
        self.jogador_business = JogadorBusiness(self.jogador)
        self.inimigos = self.criar_inimigos()
        self.inimigo_business = InimigoBusiness(self.inimigos)
        self.projeteis_jogador = []
        self.projeteis_inimigo = []
        self.projetil_business = ProjetilBusiness(self.projeteis_jogador, self.projeteis_inimigo)
        self.pontuacao_business.resetar_pontuacao()
        self.game_over = False

        # Tempos para tiros
        self.tempo_ultimo_tiro = 0
        self.intervalo_tiro = 200  # milissegundos
        self.tempo_ultimo_tiro_inimigo = 0
        self.intervalo_tiro_inimigo = 800  # milissegundos
        self.max_tiros_inimigos = 5  # Limite de tiros inimigos na tela

    def criar_inimigos(self):
        """
        Método para criar uma formação de inimigos.
        """
        inimigos = []
        linhas = 3
        colunas = 8
        espacamento_x = 80
        espacamento_y = 50
        for linha in range(linhas):
            # Diferentes tipos de inimigos por linha
            tipo_inimigo = linha + 1  # Linha 0 = tipo 1, linha 1 = tipo 2, etc.
            for coluna in range(colunas):
                x = 60 + coluna * espacamento_x
                y = 50 + linha * espacamento_y
                inimigos.append(Inimigo(x, y, tipo=tipo_inimigo))
        return inimigos

    def processar_comando(self, comando):
        """
        Processa comandos recebidos (ex: do cliente via rede).
        Substitui o processamento de eventos de teclado local.
        
        Args:
            comando (str): O comando a ser executado ("esquerda", "direita", "cima", "baixo", "atirar", "reiniciar")
        """
        if self.game_over:
            if comando == "reiniciar":
                self.inicializar_jogo()
            return

        if comando == "esquerda":
            self.mover_jogador_esquerda()
        elif comando == "direita":
            self.mover_jogador_direita()
        elif comando == "cima":
            self.mover_jogador_cima()
        elif comando == "baixo":
            self.mover_jogador_baixo()
        elif comando == "atirar":
            agora = pygame.time.get_ticks()
            if agora - self.tempo_ultimo_tiro > self.intervalo_tiro:
                self.jogador_business.atirar()
                # Adiciona o último tiro criado à lista de projéteis do jogo
                if self.jogador.tiros:
                    self.projeteis_jogador.append(self.jogador.tiros[-1])
                self.tempo_ultimo_tiro = agora

    def mover_jogador_esquerda(self):
        try:
            self.jogador_business.mover_esquerda(LARGURA_TELA)
        except Exception as e:
            print(f"Erro ao mover jogador para esquerda: {e}")

    def mover_jogador_direita(self):
        try:
            self.jogador_business.mover_direita(LARGURA_TELA)
        except Exception as e:
            print(f"Erro ao mover jogador para direita: {e}")

    def mover_jogador_cima(self):
        try:
            self.jogador_business.mover_cima()
        except Exception as e:
            print(f"Erro ao mover jogador para cima: {e}")

    def mover_jogador_baixo(self):
        try:
            self.jogador_business.mover_baixo(ALTURA_TELA)
        except Exception as e:
            print(f"Erro ao mover jogador para baixo: {e}")

    def mover_inimigos(self):
        try:
            self.inimigo_business.mover_inimigos(LARGURA_TELA)
        except Exception as e:
            print(f"Erro ao mover inimigos: {e}")

    def mover_projeteis(self):
        try:
            self.projetil_business.mover_todos_projeteis()
            self.projetil_business.remover_projeteis_fora_tela()
        except Exception as e:
            print(f"Erro ao mover projéteis: {e}")

    def inimigos_atiram(self):
        agora = pygame.time.get_ticks()
        if (agora - self.tempo_ultimo_tiro_inimigo > self.intervalo_tiro_inimigo and
            len(self.projeteis_inimigo) < self.max_tiros_inimigos and
            len(self.inimigos) > 0):
            tiro = self.inimigo_business.atirar_aleatorio()
            if tiro:
                self.projeteis_inimigo.append(tiro)
                self.tempo_ultimo_tiro_inimigo = agora

    def verificar_colisoes(self):
        # Colisão entre projéteis
        self.projetil_business.verificar_colisao_projeteis(self.efeitos_explosao, self.pontuacao_business)

        # Colisões com objetos
        self.projetil_business.verificar_colisoes_com_objetos(self.jogador, self.inimigos, self.pontuacao_business)

        # Verifica se o jogador perdeu todas as vidas
        if self.pontuacao_business.verificar_game_over():
            self.game_over = True
            return

        # Verifica se inimigos chegaram muito perto do jogador
        for inimigo in self.inimigos:
            if inimigo.y + inimigo.altura >= self.jogador.y:
                self.game_over = True
                break

    def atualizar_efeitos_explosao(self):
        # Apenas atualiza o estado lógico, sem renderização
        for efeito in self.efeitos_explosao[:]:
            efeito.atualizar()
            if not efeito.ativo:
                self.efeitos_explosao.remove(efeito)

    def atualizar(self):
        """
        Método para atualizar o estado do jogo.
        """
        if not self.game_over:
            self.mover_inimigos()
            self.mover_projeteis()
            self.inimigos_atiram()
            self.verificar_colisoes()
            self.atualizar_efeitos_explosao()

            # Reinicia o nível se todos os inimigos forem destruídos
            if len(self.inimigos) == 0:
                self.inicializar_jogo()
                # Aumenta a dificuldade (opcional)
                # Nota: VELOCIDADE_INIMIGO é uma constante importada, 
                # alterar aqui não afeta o módulo utils, mas podemos ajustar a velocidade base no business se necessário
                # Por enquanto mantemos simples como no original

    def obter_estado(self):
        """
        Retorna um dicionário representando o estado atual do jogo.
        Usado para enviar dados ao cliente.
        """
        estado = {
            "jogador": {
                "x": self.jogador.x,
                "y": self.jogador.y,
                "largura": self.jogador.largura,
                "altura": self.jogador.altura
            },
            "inimigos": [
                {
                    "x": inimigo.x,
                    "y": inimigo.y,
                    "tipo": inimigo.tipo,
                    "largura": inimigo.largura,
                    "altura": inimigo.altura
                } for inimigo in self.inimigos
            ],
            "projeteis": [
                {
                    "x": p.x,
                    "y": p.y,
                    "tipo": "inimigo" if p.eh_inimigo else "jogador",
                    "largura": p.largura,
                    "altura": p.altura
                } for p in self.projeteis_jogador + self.projeteis_inimigo
            ],
            "explosões": [
                {
                    "x": e.x,
                    "y": e.y,
                    "tamanho": e.tamanho_atual
                } for e in self.efeitos_explosao
            ],
            "pontuacao": self.pontuacao.pontos,
            "vidas": self.pontuacao.vidas_jogador,
            "game_over": self.game_over
        }
        return estado