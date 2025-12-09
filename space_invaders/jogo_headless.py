# ============================================================================
# JOGO_HEADLESS.PY - CONTROLADOR SEM INTERFACE GRÁFICA
# ============================================================================
"""
PROPÓSITO:
Versão HEADLESS (sem cabeça/interface) do jogo Space Invaders.
Usado para integração WEB - lógica pura sem renderização pygame.

DIFERENÇA ENTRE JOGO.PY E JOGO_HEADLESS.PY:
- jogo.py: TEM renderização (desenha na tela)
- jogo_headless.py: SEM renderização (apenas lógica)

USO:
- Aplicação web (Flask) usa esta versão
- Lógica roda no servidor
- Estado é enviado para cliente via JSON
- Cliente renderiza no navegador

VANTAGEM DA SEPARAÇÃO:
- MESMA LÓGICA para desktop e web
- Apenas interface muda
- Demonstra REUTILIZAÇÃO de código
"""

import pygame  # Apenas para Rect e time (não para display)
# Importa mesmas classes que jogo.py
from .Dados.jogador import Jogador
from .Business.jogador_business import JogadorBusiness
from .Dados.inimigo import Inimigo
from .Business.inimigo_business import InimigoBusiness
from .Business.projetil_business import ProjetilBusiness
from .Dados.pontuacao import Pontuacao
from .Business.pontuacao_business import PontuacaoBusiness
from .utils import *

# ============================================================================
# CLASSE JOGOHEADLESS - CONTROLADOR SEM RENDERIZAÇÃO
# ============================================================================
class JogoHeadless:
    """
    ========================================================================
    CLASSE JOGOHEADLESS - LÓGICA PURA SEM INTERFACE
    ========================================================================

    PROPÓSITO:
    Mesma lógica que Jogo, mas SEM renderização gráfica.
    Usado para aplicação web.

    DIFERENÇAS EM RELAÇÃO A JOGO:
    - NÃO cria janela pygame
    - NÃO desenha na tela
    - NÃO carrega sprites
    - APENAS processa lógica e estado

    PADRÃO DE DESIGN:
    - SEPARAÇÃO: Lógica separada de apresentação
    - REUTILIZAÇÃO: Mesmas classes Dados e Business
    - ADAPTAÇÃO: Interface diferente, lógica igual

    USO:
    - Flask (web) cria instância desta classe
    - Processa comandos do cliente
    - Retorna estado do jogo em JSON
    - Cliente renderiza no navegador
    ========================================================================
    """

    def __init__(self):
        """
        CONSTRUTOR - Inicializa jogo sem interface gráfica

        DIFERENÇA: Não cria tela, não carrega sprites
        """
        # Inicializa pygame apenas para funcionalidades básicas
        # (Rect para colisão, time para controle de tempo)
        # NÃO inicializa display (tela) ou mixer (som)
        if not pygame.get_init():
            pygame.init()

        # Estado do jogo
        self.rodando = True
        self.game_over = False
        self.pausado = False
        self.estado = ESTADO_MENU

        # Opções de menu (para web)
        self.menu_opcoes = ["JOGAR COM IA", "JOGAR SOLO", "SAIR"]
        self.menu_selecionada = 0
        self.game_over_opcoes = ["JOGAR NOVAMENTE", "MENU PRINCIPAL", "SAIR"]
        self.game_over_selecionada = 0
        self.deseja_sair = False

        # Comandos ativos (controlados pela web)
        self.comandos_ativos = {
            "esquerda": False,
            "direita": False,
            "cima": False,
            "baixo": False,
            "atirar": False
        }

        # COMPOSIÇÃO: Mesmas entidades que jogo.py
        self.pontuacao = Pontuacao()
        self.pontuacao_business = PontuacaoBusiness(self.pontuacao)
        self.efeitos_explosao = []
        self.velocidade_inimigo_base = VELOCIDADE_INIMIGO

        # Inicializa componentes
        self.inicializar_jogo(reset_velocidade=True)

        # Velocidades (mesmas constantes)
        self.velocidade_jogador = VELOCIDADE_JOGADOR
        self.velocidade_inimigo = VELOCIDADE_INIMIGO
        self.velocidade_tiro = VELOCIDADE_TIRO

    def inicializar_jogo(self, reset_velocidade=False):
        """
        Inicializa componentes do jogo

        MESMA LÓGICA que jogo.py, mas sem sprites
        """
        if reset_velocidade:
            self.velocidade_inimigo_base = VELOCIDADE_INIMIGO
        self.jogador = Jogador(LARGURA_TELA // 2 - 25, ALTURA_TELA - 50)
        self.jogador_business = JogadorBusiness(self.jogador)
        self.inimigos = self.criar_inimigos()
        self.inimigo_business = InimigoBusiness(self.inimigos, velocidade_base=self.velocidade_inimigo_base)
        self.projeteis_jogador = []
        self.projeteis_inimigo = []
        self.projetil_business = ProjetilBusiness(
            self.projeteis_jogador,
            self.projeteis_inimigo,
            jogador=self.jogador,
            sprite_explosao=None,
        )
        self.pontuacao_business.resetar_pontuacao()
        self.game_over = False
        self.pausado = False
        self.deseja_sair = False

        # Reseta comandos contínuos
        self.resetar_comandos_continuos()

        # Tempos para tiros
        self.tempo_ultimo_tiro = 0
        self.intervalo_tiro = 200  # milissegundos
        self.tempo_ultimo_tiro_inimigo = 0
        self.intervalo_tiro_inimigo = 800  # milissegundos
        self.max_tiros_inimigos = 5  # Limite de tiros inimigos na tela

    def iniciar_partida(self):
        """Prepara um novo jogo e entra no estado de jogo."""
        self.inicializar_jogo(reset_velocidade=True)
        self.estado = ESTADO_JOGANDO
        self.game_over_selecionada = 0
        self.menu_selecionada = 0

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

    def processar_comando(self, comando, estado=None):
        """
        Processa comandos recebidos (ex: do cliente via rede).
        Substitui o processamento de eventos de teclado local.
        
        Args:
            comando (str): O comando a ser executado ("esquerda", "direita", "cima", "baixo", "atirar", "reiniciar", "pausar", "menu", "menu_cima", "menu_baixo", "menu_selecionar")
            estado (str|None): "pressionar" ou "soltar" para comandos contínuos
        """
        if comando is None:
            return

        # Sempre permite reiniciar
        if comando == "reiniciar":
            self.iniciar_partida()
            return

        # Ir para menu (equivale ao ESC no jogo original)
        if comando == "menu":
            self.estado = ESTADO_MENU
            self.pausado = False
            self.game_over = False
            self.resetar_comandos_continuos()
            return

        # Navegação de menu principal
        if self.estado == ESTADO_MENU:
            self.processar_menu(comando)
            return

        # Navegação de menu de game over
        if self.estado == ESTADO_GAME_OVER:
            self.processar_game_over(comando)
            return

        if self.estado != ESTADO_JOGANDO:
            return

        if self.game_over:
            return

        if comando == "pausar":
            # Toggle simples; pausa congela o loop de atualização até novo toggle
            self.pausado = not self.pausado
            return

        if comando in self.comandos_ativos:
            # estado None ou diferente de "soltar" = pressionado
            self.comandos_ativos[comando] = (estado != "soltar")
            return

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
            self.entrar_game_over()
            return

        # Verifica se inimigos chegaram muito perto do jogador
        for inimigo in self.inimigos:
            if inimigo.y + inimigo.altura >= self.jogador.y:
                self.entrar_game_over()
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
        if self.pausado or self.game_over or self.estado != ESTADO_JOGANDO:
            return

        # Aplica comandos contínuos antes de atualizar o resto do jogo
        self.aplicar_controles_continuos()

        self.mover_inimigos()
        self.mover_projeteis()
        self.inimigos_atiram()
        self.verificar_colisoes()
        self.atualizar_efeitos_explosao()

        # Reinicia o nível se todos os inimigos forem destruídos
        if len(self.inimigos) == 0:
            self.velocidade_inimigo_base += 0.5
            self.inicializar_jogo()
            # Mantém a dificuldade aumentando a cada onda

    def entrar_game_over(self):
        """Configura estado de game over e limpa controles contínuos."""
        self.game_over = True
        self.estado = ESTADO_GAME_OVER
        self.pausado = False
        self.game_over_selecionada = 0
        self.resetar_comandos_continuos()

    def aplicar_controles_continuos(self):
        """
        Aplica comandos de entrada contínuos (movimento/tiro) a cada frame lógico.
        """
        # Movimento horizontal
        if self.comandos_ativos["esquerda"] and not self.comandos_ativos["direita"]:
            self.mover_jogador_esquerda()
        elif self.comandos_ativos["direita"] and not self.comandos_ativos["esquerda"]:
            self.mover_jogador_direita()

        # Movimento vertical
        if self.comandos_ativos["cima"] and not self.comandos_ativos["baixo"]:
            self.mover_jogador_cima()
        elif self.comandos_ativos["baixo"] and not self.comandos_ativos["cima"]:
            self.mover_jogador_baixo()

        # Tiro contínuo (segurando)
        if self.comandos_ativos["atirar"]:
            agora = pygame.time.get_ticks()
            if agora - self.tempo_ultimo_tiro > self.intervalo_tiro:
                projetil = self.jogador_business.atirar()
                if projetil:
                    self.projeteis_jogador.append(projetil)
                self.tempo_ultimo_tiro = agora

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
            "game_over": self.game_over,
            "pausado": self.pausado,
            "estado": self.obter_estado_nome(),
            "menu": {
                "opcoes": self.menu_opcoes,
                "selecionada": self.menu_selecionada
            },
            "menu_game_over": {
                "opcoes": self.game_over_opcoes,
                "selecionada": self.game_over_selecionada
            },
            "deseja_sair": self.deseja_sair
        }
        return estado

    def resetar_comandos_continuos(self):
        """Limpa o estado de entradas contínuas para evitar movimento preso."""
        for comando in self.comandos_ativos:
            self.comandos_ativos[comando] = False

    def processar_menu(self, comando):
        """Processa entradas no menu principal."""
        if comando in ("menu_cima", "cima"):
            self.menu_selecionada = (self.menu_selecionada - 1) % len(self.menu_opcoes)
        elif comando in ("menu_baixo", "baixo"):
            self.menu_selecionada = (self.menu_selecionada + 1) % len(self.menu_opcoes)
        elif comando == "menu_selecionar":
            opcao = self.menu_opcoes[self.menu_selecionada]
            if opcao == "JOGAR COM IA":
                self.iniciar_partida()
            elif opcao == "JOGAR SOLO":
                self.iniciar_partida()
            elif opcao == "SAIR":
                # No webservice não encerramos o servidor; sinalizamos intenção
                self.deseja_sair = True
                self.game_over = False
        elif comando == "pausar":
            # Pausa no menu não faz nada, mas não gera erro
            return

    def processar_game_over(self, comando):
        """Processa entradas na tela de game over."""
        if comando in ("menu_cima", "cima"):
            self.game_over_selecionada = (self.game_over_selecionada - 1) % len(self.game_over_opcoes)
        elif comando in ("menu_baixo", "baixo"):
            self.game_over_selecionada = (self.game_over_selecionada + 1) % len(self.game_over_opcoes)
        elif comando == "menu_selecionar":
            opcao = self.game_over_opcoes[self.game_over_selecionada]
            if opcao == "JOGAR NOVAMENTE":
                self.iniciar_partida()
            elif opcao == "MENU PRINCIPAL":
                self.estado = ESTADO_MENU
                self.pausado = False
                self.game_over = False
                self.resetar_comandos_continuos()
            elif opcao == "SAIR":
                self.deseja_sair = True
                self.estado = ESTADO_MENU
                self.game_over = False
        elif comando == "reiniciar":
            self.iniciar_partida()
        elif comando == "pausar":
            return

    def obter_estado_nome(self):
        """Retorna o nome legível do estado atual."""
        if self.estado == ESTADO_MENU:
            return "menu"
        if self.estado == ESTADO_JOGANDO:
            return "jogando"
        if self.estado == ESTADO_GAME_OVER:
            return "game_over"
        return "desconhecido"
