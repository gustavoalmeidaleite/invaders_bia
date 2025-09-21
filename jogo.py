import pygame
import sys
from Dados.jogador import Jogador
from Business.jogador_business import JogadorBusiness
from Dados.inimigo import Inimigo
from Business.inimigo_business import InimigoBusiness
from Business.projetil_business import ProjetilBusiness
from Dados.pontuacao import Pontuacao
from utils import *

class Menu:
    """Classe para gerenciar o menu principal do jogo."""

    def __init__(self, tela):
        self.tela = tela
        self.fonte_titulo = pygame.font.Font(None, 72)
        self.fonte_opcao = pygame.font.Font(None, 48)
        self.opcao_selecionada = 0
        self.opcoes = ["INICIAR", "SAIR"]

    def processar_eventos(self):
        """Processa eventos do menu."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)
                elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)
                elif evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE:
                    if self.opcao_selecionada == 0:  # INICIAR
                        return "iniciar"
                    elif self.opcao_selecionada == 1:  # SAIR
                        return "sair"
                elif evento.key == pygame.K_ESCAPE:
                    return "sair"
        return None

    def desenhar(self):
        """Desenha o menu na tela."""
        self.tela.fill(COR_FUNDO)

        # Título
        titulo = self.fonte_titulo.render("SPACE INVADERS", True, COR_TITULO)
        titulo_rect = titulo.get_rect(center=(LARGURA_TELA // 2, 200))
        self.tela.blit(titulo, titulo_rect)

        # Opções do menu
        for i, opcao in enumerate(self.opcoes):
            cor = COR_TEXTO_SELECIONADO if i == self.opcao_selecionada else COR_TEXTO
            texto = self.fonte_opcao.render(opcao, True, cor)
            texto_rect = texto.get_rect(center=(LARGURA_TELA // 2, 350 + i * 80))
            self.tela.blit(texto, texto_rect)

        # Instruções
        fonte_instrucao = pygame.font.Font(None, 24)
        instrucoes = [
            "Use as setas ou W/S para navegar",
            "Pressione ENTER ou ESPAÇO para selecionar",
            "ESC para sair"
        ]

        for i, instrucao in enumerate(instrucoes):
            texto = fonte_instrucao.render(instrucao, True, COR_TEXTO)
            texto_rect = texto.get_rect(center=(LARGURA_TELA // 2, 520 + i * 25))
            self.tela.blit(texto, texto_rect)

        pygame.display.flip()

class GameOver:
    """Classe para gerenciar a tela de game over."""

    def __init__(self, tela, pontuacao=0):
        self.tela = tela
        self.fonte_titulo = pygame.font.Font(None, 72)
        self.fonte_texto = pygame.font.Font(None, 48)
        self.fonte_instrucao = pygame.font.Font(None, 32)
        self.pontuacao = pontuacao
        self.opcao_selecionada = 0
        self.opcoes = ["JOGAR NOVAMENTE", "MENU PRINCIPAL", "SAIR"]

    def processar_eventos(self):
        """Processa eventos da tela de game over."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)
                elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)
                elif evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE:
                    if self.opcao_selecionada == 0:  # JOGAR NOVAMENTE
                        return "reiniciar"
                    elif self.opcao_selecionada == 1:  # MENU PRINCIPAL
                        return "menu"
                    elif self.opcao_selecionada == 2:  # SAIR
                        return "sair"
                elif evento.key == pygame.K_ESCAPE:
                    return "menu"
        return None

    def desenhar(self):
        """Desenha a tela de game over."""
        self.tela.fill(COR_FUNDO)

        # Título Game Over
        titulo = self.fonte_titulo.render("GAME OVER", True, COR_INIMIGO)
        titulo_rect = titulo.get_rect(center=(LARGURA_TELA // 2, 150))
        self.tela.blit(titulo, titulo_rect)

        # Pontuação
        pontos = self.fonte_texto.render(f"Pontuação: {self.pontuacao}", True, COR_TEXTO)
        pontos_rect = pontos.get_rect(center=(LARGURA_TELA // 2, 220))
        self.tela.blit(pontos, pontos_rect)

        # Opções
        for i, opcao in enumerate(self.opcoes):
            cor = COR_TEXTO_SELECIONADO if i == self.opcao_selecionada else COR_TEXTO
            texto = self.fonte_instrucao.render(opcao, True, cor)
            texto_rect = texto.get_rect(center=(LARGURA_TELA // 2, 320 + i * 60))
            self.tela.blit(texto, texto_rect)

        # Instruções
        fonte_pequena = pygame.font.Font(None, 24)
        instrucoes = [
            "Use as setas ou W/S para navegar",
            "Pressione ENTER ou ESPAÇO para selecionar",
            "ESC para voltar ao menu"
        ]

        for i, instrucao in enumerate(instrucoes):
            texto = fonte_pequena.render(instrucao, True, COR_TEXTO)
            texto_rect = texto.get_rect(center=(LARGURA_TELA // 2, 520 + i * 25))
            self.tela.blit(texto, texto_rect)

        pygame.display.flip()

class Jogo:
    """
    Classe principal que gerencia o jogo.
    Demonstra composição: o jogo é composto por um jogador.
    """

    def __init__(self):
        """
        Construtor da classe Jogo.
        Inicializa a tela e cria uma instância do jogador.
        """
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Space Invaders - Protótipo")
        self.clock = pygame.time.Clock()
        self.rodando = True

        # Estado do jogo
        self.estado = ESTADO_MENU

        # Carrega sprite de fundo
        self.background = carregar_sprite("background.png", LARGURA_TELA, ALTURA_TELA)

        # Inicializa componentes de interface
        self.menu = Menu(self.tela)
        self.game_over = None

        # Variáveis do jogo
        self.pontuacao = Pontuacao()
        self.efeitos_explosao = []

        # Inicializa componentes do jogo
        self.inicializar_jogo()

    def inicializar_jogo(self):
        """Inicializa ou reinicializa os componentes do jogo."""
        # Composição: o jogo contém um jogador
        self.jogador = Jogador(LARGURA_TELA // 2 - 25, ALTURA_TELA - 50)
        self.jogador_business = JogadorBusiness(self.jogador)
        self.inimigos = self.criar_inimigos()
        self.inimigo_business = InimigoBusiness(self.inimigos)
        self.projeteis_jogador = []
        self.projeteis_inimigo = []
        self.projetil_business = ProjetilBusiness(self.projeteis_jogador, self.projeteis_inimigo)
        self.pontuacao.resetar()

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

    def processar_eventos(self):
        """
        Método para processar eventos do pygame baseado no estado atual.
        """
        if self.estado == ESTADO_MENU:
            resultado = self.menu.processar_eventos()
            if resultado == "iniciar":
                self.estado = ESTADO_JOGANDO
                self.inicializar_jogo()
            elif resultado == "sair":
                self.rodando = False

        elif self.estado == ESTADO_GAME_OVER:
            resultado = self.game_over.processar_eventos()
            if resultado == "reiniciar":
                self.estado = ESTADO_JOGANDO
                self.inicializar_jogo()
            elif resultado == "menu":
                self.estado = ESTADO_MENU
            elif resultado == "sair":
                self.rodando = False

        elif self.estado == ESTADO_JOGANDO:
            self.processar_eventos_jogo()

    def processar_eventos_jogo(self):
        """
        Processa eventos durante o gameplay.
        """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.estado = ESTADO_MENU

        teclas = pygame.key.get_pressed()
        # Movimento horizontal
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.jogador_business.mover_esquerda()
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.jogador_business.mover_direita()
        # Movimento vertical
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.jogador_business.mover_cima()
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.jogador_business.mover_baixo()
        # Atira segurando Z
        if teclas[pygame.K_z]:
            agora = pygame.time.get_ticks()
            if agora - self.tempo_ultimo_tiro > self.intervalo_tiro:
                self.jogador_business.atirar()
                self.projeteis_jogador.append(self.jogador.tiros[-1])
                self.tempo_ultimo_tiro = agora

    def inimigos_atiram(self):
        """
        Método para fazer inimigos atirarem aleatoriamente.
        Limita a quantidade de tiros inimigos na tela.
        """
        agora = pygame.time.get_ticks()
        if (agora - self.tempo_ultimo_tiro_inimigo > self.intervalo_tiro_inimigo and
            len(self.projeteis_inimigo) < self.max_tiros_inimigos and
            len(self.inimigos) > 0):
            tiro = self.inimigo_business.atirar_aleatorio()
            if tiro:
                self.projeteis_inimigo.append(tiro)
                self.tempo_ultimo_tiro_inimigo = agora

    def verificar_colisoes(self):
        """
        Método para verificar colisões entre tiros e inimigos/jogador.
        """
        # Colisão entre projéteis
        self.projetil_business.verificar_colisao_projeteis(self.efeitos_explosao, self.pontuacao)

        # Colisões com objetos
        self.projetil_business.verificar_colisoes_com_objetos(self.jogador, self.inimigos, self.pontuacao)

        # Verifica se o jogador perdeu todas as vidas
        if self.pontuacao.vidas_jogador <= 0:
            self.game_over = GameOver(self.tela, self.pontuacao.pontos)
            self.estado = ESTADO_GAME_OVER
            return

        # Verifica se inimigos chegaram muito perto do jogador
        for inimigo in self.inimigos:
            if inimigo.y + inimigo.altura >= self.jogador.y:
                self.game_over = GameOver(self.tela, self.pontuacao.pontos)
                self.estado = ESTADO_GAME_OVER
                break

    def atualizar_efeitos_explosao(self):
        """
        Atualiza todos os efeitos de explosão e remove os que expiraram.
        """
        for efeito in self.efeitos_explosao[:]:
            efeito.atualizar()
            if not efeito.ativo:
                self.efeitos_explosao.remove(efeito)

    def atualizar(self):
        """
        Método para atualizar o estado do jogo.
        """
        if self.estado == ESTADO_JOGANDO:
            self.inimigo_business.mover_inimigos()
            self.jogador_business.atualizar_tiros()
            self.projetil_business.mover_projeteis()
            self.inimigos_atiram()
            self.verificar_colisoes()
            self.atualizar_efeitos_explosao()

            # Reinicia o nível se todos os inimigos forem destruídos
            if len(self.inimigos) == 0:
                self.inicializar_jogo()
                # Aumenta a dificuldade (opcional)
                global VELOCIDADE_INIMIGO
                VELOCIDADE_INIMIGO += 0.5

    def desenhar(self):
        """
        Método para desenhar todos os elementos na tela baseado no estado.
        """
        if self.estado == ESTADO_MENU:
            self.menu.desenhar()
        elif self.estado == ESTADO_GAME_OVER:
            self.game_over.desenhar()
        elif self.estado == ESTADO_JOGANDO:
            self.desenhar_jogo()

    def desenhar_jogo(self):
        """
        Desenha os elementos do jogo durante o gameplay.
        """
        # Desenha fundo
        if self.background:
            self.tela.blit(self.background, (0, 0))
        else:
            self.tela.fill(COR_FUNDO)

        self.jogador.desenhar(self.tela)
        for inimigo in self.inimigos:
            inimigo.desenhar(self.tela)
        # Desenha projéteis
        for projetil in self.projeteis_jogador + self.projeteis_inimigo:
            projetil.desenhar(self.tela)

        # Desenha efeitos de explosão
        for efeito in self.efeitos_explosao:
            efeito.desenhar(self.tela)

        # Desenha HUD
        self.desenhar_hud()
        pygame.display.flip()

    def desenhar_hud(self):
        """
        Desenha a interface do usuário (HUD) com pontuação e vidas.
        """
        fonte = pygame.font.Font(None, 36)

        # Pontuação
        texto_pontos = fonte.render(f"Pontos: {self.pontuacao.pontos}", True, COR_TEXTO)
        self.tela.blit(texto_pontos, (10, 10))

        # Vidas
        texto_vidas = fonte.render(f"Vidas: {self.pontuacao.vidas_jogador}", True, COR_TEXTO)
        self.tela.blit(texto_vidas, (10, 50))

        # Instruções
        fonte_pequena = pygame.font.Font(None, 24)
        instrucoes = fonte_pequena.render("ESC: Menu | WASD/Setas: Mover | Z: Atirar", True, COR_TEXTO)
        self.tela.blit(instrucoes, (10, ALTURA_TELA - 30))
    
    def executar(self):
        """
        Loop principal do jogo.
        Demonstra o padrão de game loop: processar eventos, atualizar, desenhar.
        """
        while self.rodando:
            self.processar_eventos()
            self.atualizar()
            self.desenhar()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()