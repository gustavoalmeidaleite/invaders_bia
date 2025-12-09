# ============================================================================
# JOGO.PY - CONTROLADOR PRINCIPAL (CAMADA DE CONTROLE/APRESENTAÇÃO)
# ============================================================================
"""
PROPÓSITO:
Este arquivo contém a CAMADA DE CONTROLE do jogo Space Invaders.
Coordena todas as outras camadas (Dados e Business) e gerencia a interface gráfica.

ARQUITETURA EM CAMADAS:
- DADOS (Jogador, Inimigo, etc.): O QUE são as entidades
- NEGÓCIO (JogadorBusiness, etc.): COMO as entidades se comportam
- CONTROLE (Jogo, Menu, GameOver): QUANDO executar ações e COMO exibir

PADRÃO MVC (Model-View-Controller):
- Model: Camadas Dados + Business
- View: Métodos de renderização (desenhar_*)
- Controller: Classe Jogo (coordena tudo)

CLASSES NESTE ARQUIVO:
1. Menu: Gerencia menu principal
2. GameOver: Gerencia tela de game over
3. Jogo: Controlador principal do jogo
"""

import pygame  # Biblioteca de jogos
import sys     # Para sair do programa
# Importa camada de DADOS (entidades)
from .Dados.jogador import Jogador
from .Dados.inimigo import Inimigo
from .Dados.pontuacao import Pontuacao
# Importa camada de NEGÓCIO (lógica)
from .Business.jogador_business import JogadorBusiness
from .Business.inimigo_business import InimigoBusiness
from .Business.projetil_business import ProjetilBusiness
from .Business.pontuacao_business import PontuacaoBusiness
# Importa constantes e utilitários
from .utils import *

# ============================================================================
# CLASSE MENU - INTERFACE DE MENU PRINCIPAL
# ============================================================================
class Menu:
    """
    Gerencia o menu principal do jogo

    RESPONSABILIDADE: Interface de menu (seleção de opções)
    PADRÃO: Separação de interface (Menu) e lógica (Jogo)
    """

    def __init__(self, tela):
        """
        Inicializa o menu

        Args:
            tela: Superfície pygame para renderização
        """
        self.tela = tela
        self.fonte_titulo = pygame.font.Font(None, 72)   # Fonte grande para título
        self.fonte_opcao = pygame.font.Font(None, 48)    # Fonte média para opções
        self.opcao_selecionada = 0  # Índice da opção atual
        self.opcoes = ["INICIAR", "SAIR"]  # Lista de opções do menu

    def processar_eventos(self):
        """
        Processa entrada do usuário no menu

        LÓGICA:
        - Detecta teclas de navegação (setas, W/S)
        - Detecta seleção (Enter, Espaço)
        - Detecta saída (ESC, fechar janela)

        Returns:
            str: "iniciar", "sair" ou None
        """
        for evento in pygame.event.get():
            # Usuário fechou a janela
            if evento.type == pygame.QUIT:
                return "sair"

            # Usuário pressionou tecla
            if evento.type == pygame.KEYDOWN:
                # Navegar para cima
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)
                # Navegar para baixo
                elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)
                # Selecionar opção
                elif evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE:
                    if self.opcao_selecionada == 0:  # INICIAR
                        return "iniciar"
                    elif self.opcao_selecionada == 1:  # SAIR
                        return "sair"
                # ESC para sair
                elif evento.key == pygame.K_ESCAPE:
                    return "sair"
        return None

    def desenhar(self):
        """
        Renderiza o menu na tela

        RESPONSABILIDADE: Apenas APRESENTAÇÃO (View)
        Não contém lógica de negócio
        """
        # Limpa tela com cor de fundo
        self.tela.fill(COR_FUNDO)

        # Renderiza título
        titulo = self.fonte_titulo.render("SPACE INVADERS", True, COR_TITULO)
        titulo_rect = titulo.get_rect(center=(LARGURA_TELA // 2, 200))
        self.tela.blit(titulo, titulo_rect)

        # Renderiza opções do menu
        for i, opcao in enumerate(self.opcoes):
            # Destaca opção selecionada com cor diferente
            cor = COR_TEXTO_SELECIONADO if i == self.opcao_selecionada else COR_TEXTO
            texto = self.fonte_opcao.render(opcao, True, cor)
            texto_rect = texto.get_rect(center=(LARGURA_TELA // 2, 350 + i * 80))
            self.tela.blit(texto, texto_rect)

        # Renderiza instruções
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

        # Atualiza display
        pygame.display.flip()

# ============================================================================
# CLASSE GAMEOVER - INTERFACE DE FIM DE JOGO
# ============================================================================
class GameOver:
    """
    Gerencia a tela de game over

    RESPONSABILIDADE: Exibir resultado final e opções de reinício
    """

    def __init__(self, tela, pontuacao=0):
        """
        Inicializa tela de game over

        Args:
            tela: Superfície pygame
            pontuacao (int): Pontuação final do jogador
        """
        self.tela = tela
        self.fonte_titulo = pygame.font.Font(None, 72)
        self.fonte_texto = pygame.font.Font(None, 48)
        self.fonte_instrucao = pygame.font.Font(None, 32)
        self.pontuacao = pontuacao
        self.opcao_selecionada = 0
        self.opcoes = ["JOGAR NOVAMENTE", "MENU PRINCIPAL", "SAIR"]

    def processar_eventos(self):
        """Processa entrada do usuário na tela de game over"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "sair"
            if evento.type == pygame.KEYDOWN:
                # Navegação
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)
                elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)
                # Seleção
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
        """Renderiza tela de game over"""
        self.tela.fill(COR_FUNDO)

        # Título
        titulo = self.fonte_titulo.render("GAME OVER", True, COR_INIMIGO)
        titulo_rect = titulo.get_rect(center=(LARGURA_TELA // 2, 150))
        self.tela.blit(titulo, titulo_rect)

        # Pontuação final
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

# ============================================================================
# CLASSE JOGO - CONTROLADOR PRINCIPAL (MVC CONTROLLER)
# ============================================================================
class Jogo:
    """
    ========================================================================
    CLASSE JOGO - CONTROLADOR PRINCIPAL DO JOGO
    ========================================================================

    PROPÓSITO:
    Esta é a classe CONTROLADORA principal que coordena todo o jogo.
    Implementa o padrão MVC (Model-View-Controller).

    RESPONSABILIDADES:
    1. COORDENAÇÃO: Gerencia todas as outras classes
    2. GAME LOOP: Implementa loop principal do jogo
    3. RENDERIZAÇÃO: Desenha todos os elementos na tela
    4. ENTRADA: Processa input do usuário
    5. MÁQUINA DE ESTADOS: Gerencia estados (menu, jogando, game over)

    COMPOSIÇÃO (HAS-A):
    - Jogo TEM UM Jogador
    - Jogo TEM VÁRIOS Inimigos
    - Jogo TEM UMA Pontuacao
    - Jogo TEM Business classes (delegação de lógica)

    PADRÃO MVC:
    - MODEL: Dados + Business (lógica)
    - VIEW: Métodos desenhar_* (renderização)
    - CONTROLLER: Esta classe (coordena Model e View)

    MÁQUINA DE ESTADOS:
    - ESTADO_MENU: Exibindo menu
    - ESTADO_JOGANDO: Gameplay ativo
    - ESTADO_GAME_OVER: Fim de jogo
    ========================================================================
    """

    def __init__(self):
        """
        CONSTRUTOR - Inicializa o jogo completo

        COMPOSIÇÃO: Cria todos os objetos necessários
        - Jogador (entidade)
        - Inimigos (lista de entidades)
        - Business classes (lógica)
        - Interface (Menu, GameOver)
        """
        # Inicializa pygame se necessário
        if not pygame.get_init():
            pygame.init()

        # Cria janela do jogo
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Space Invaders - Protótipo")
        self.clock = pygame.time.Clock()  # Controla FPS
        self.rodando = True

        # MÁQUINA DE ESTADOS: Estado inicial é o menu
        self.estado = ESTADO_MENU

        # Carrega recursos visuais (sprites)
        self._carregar_recursos()

        # COMPOSIÇÃO: Cria componentes de interface
        self.menu = Menu(self.tela)
        self.game_over = None

        # COMPOSIÇÃO: Cria entidade de pontuação
        self.pontuacao = Pontuacao()
        # COMPOSIÇÃO: Cria Business de pontuação
        self.pontuacao_business = PontuacaoBusiness(self.pontuacao)
        self.efeitos_explosao = []  # Lista de efeitos visuais
        self.velocidade_inimigo_base = VELOCIDADE_INIMIGO

        # Inicializa componentes do jogo
        self.inicializar_jogo(reset_velocidade=True)

        # Velocidades de movimento (constantes)
        self.velocidade_jogador = VELOCIDADE_JOGADOR
        self.velocidade_inimigo = VELOCIDADE_INIMIGO
        self.velocidade_tiro = VELOCIDADE_TIRO

    # ========================================================================
    # MÉTODOS PRIVADOS - INICIALIZAÇÃO
    # ========================================================================

    def _carregar_recursos(self):
        """
        Carrega sprites (imagens) do jogo

        SEPARAÇÃO: Recursos visuais separados da lógica
        """
        self.background = carregar_sprite("background.png", LARGURA_TELA, ALTURA_TELA)
        self.sprite_jogador = carregar_sprite("player_ship.png", 50, 30)
        # Sprites diferentes para cada tipo de inimigo
        self.sprites_inimigos = {
            1: carregar_sprite("invader_type1.png", 40, 25),
            2: carregar_sprite("invader_type2.png", 40, 25),
            3: carregar_sprite("invader_type3.png", 40, 25),
        }
        # Sprites de projéteis
        self.sprite_projeteis = {
            "jogador": carregar_sprite("bullet_player.png", 6, 15),
            "inimigo": carregar_sprite("bullet_enemy.png", 6, 15),
        }
        self.sprite_explosao = carregar_sprite("explosion.png", 32, 32)

    def inicializar_jogo(self, reset_velocidade=False):
        """
        Inicializa ou reinicializa componentes do jogo

        COMPOSIÇÃO EM AÇÃO:
        - Cria todas as entidades (Jogador, Inimigos)
        - Cria todas as Business classes
        - Conecta tudo via composição

        Chamado ao:
        - Iniciar novo jogo
        - Reiniciar após game over
        """
        if reset_velocidade:
            self.velocidade_inimigo_base = VELOCIDADE_INIMIGO

        # COMPOSIÇÃO: Cria jogador e seu business
        self.jogador = Jogador(LARGURA_TELA // 2 - 25, ALTURA_TELA - 50)
        self.jogador.sprite = self.sprite_jogador  # AGREGAÇÃO: injeta sprite
        self.jogador_business = JogadorBusiness(self.jogador)

        # COMPOSIÇÃO: Cria inimigos e seu business
        self.inimigos = self.criar_inimigos()
        self.inimigo_business = InimigoBusiness(self.inimigos, velocidade_base=self.velocidade_inimigo_base)

        # Listas de projéteis
        self.projeteis_jogador = []
        self.projeteis_inimigo = []

        # COMPOSIÇÃO: Cria business de projéteis
        self.projetil_business = ProjetilBusiness(
            self.projeteis_jogador,
            self.projeteis_inimigo,
            jogador=self.jogador,
            sprite_explosao=self.sprite_explosao,
        )

        # Reseta pontuação
        self.pontuacao_business.resetar_pontuacao()

        # Controle de tempo para tiros (cooldown)
        self.tempo_ultimo_tiro = 0
        self.intervalo_tiro = 200  # ms entre tiros do jogador
        self.tempo_ultimo_tiro_inimigo = 0
        self.intervalo_tiro_inimigo = 800  # ms entre tiros dos inimigos
        self.max_tiros_inimigos = 5  # Limite de tiros simultâneos

    def criar_inimigos(self):
        """
        Cria formação de inimigos

        LÓGICA: Cria grid de inimigos em 3 linhas
        - Linha 1 (topo): Tipo 1 (30 pontos)
        - Linha 2 (meio): Tipo 2 (20 pontos)
        - Linha 3 (baixo): Tipo 3 (10 pontos)

        Returns:
            list: Lista de objetos Inimigo
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
                inimigo = Inimigo(x, y, tipo=tipo_inimigo)
                inimigo.sprite = self.sprites_inimigos.get(tipo_inimigo)
                inimigos.append(inimigo)
        return inimigos

    def processar_eventos(self):
        """
        Método para processar eventos do pygame baseado no estado atual.
        """
        if self.estado == ESTADO_MENU:
            resultado = self.menu.processar_eventos()
            if resultado == "iniciar":
                self.estado = ESTADO_JOGANDO
                self.inicializar_jogo(reset_velocidade=True)
            elif resultado == "sair":
                self.rodando = False

        elif self.estado == ESTADO_GAME_OVER:
            resultado = self.game_over.processar_eventos()
            if resultado == "reiniciar":
                self.estado = ESTADO_JOGANDO
                self.inicializar_jogo(reset_velocidade=True)
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
            self.mover_jogador_esquerda()
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.mover_jogador_direita()
        # Movimento vertical
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.mover_jogador_cima()
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.mover_jogador_baixo()
        # Atira segurando Z
        if teclas[pygame.K_z]:
            agora = pygame.time.get_ticks()
            if agora - self.tempo_ultimo_tiro > self.intervalo_tiro:
                novo_tiro = self.jogador_business.atirar()
                if novo_tiro:
                    novo_tiro.sprite = self.sprite_projeteis["jogador"]
                    self.projeteis_jogador.append(novo_tiro)
                self.tempo_ultimo_tiro = agora

    def mover_jogador_esquerda(self):
        """
        Controlador: Delega movimento para JogadorBusiness.
        """
        try:
            self.jogador_business.mover_esquerda(LARGURA_TELA)
        except Exception as e:
            print(f"Erro ao mover jogador para esquerda: {e}")

    def mover_jogador_direita(self):
        """
        Controlador: Delega movimento para JogadorBusiness.
        """
        try:
            self.jogador_business.mover_direita(LARGURA_TELA)
        except Exception as e:
            print(f"Erro ao mover jogador para direita: {e}")

    def mover_jogador_cima(self):
        """
        Controlador: Delega movimento para JogadorBusiness.
        """
        try:
            self.jogador_business.mover_cima()
        except Exception as e:
            print(f"Erro ao mover jogador para cima: {e}")

    def mover_jogador_baixo(self):
        """
        Controlador: Delega movimento para JogadorBusiness.
        """
        try:
            self.jogador_business.mover_baixo(ALTURA_TELA)
        except Exception as e:
            print(f"Erro ao mover jogador para baixo: {e}")

    def mover_inimigos(self):
        """
        Controlador: Delega movimento para InimigoBusiness.
        """
        try:
            self.inimigo_business.mover_inimigos(LARGURA_TELA)
        except Exception as e:
            print(f"Erro ao mover inimigos: {e}")

    def mover_projeteis(self):
        """
        Controlador: Delega movimento para ProjetilBusiness.
        """
        try:
            # Utiliza a regra de negócio para mover todos os projéteis
            self.projetil_business.mover_todos_projeteis()

            # Utiliza a regra de negócio para remover projéteis fora da tela
            self.projetil_business.remover_projeteis_fora_tela()
        except Exception as e:
            print(f"Erro ao mover projéteis: {e}")

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
                tiro.sprite = self.sprite_projeteis["inimigo"]
                self.projeteis_inimigo.append(tiro)
                self.tempo_ultimo_tiro_inimigo = agora

    def verificar_colisoes(self):
        """
        Método para verificar colisões entre tiros e inimigos/jogador.
        Agora utiliza PontuacaoBusiness para aplicar regras de negócio.
        """
        # Colisão entre projéteis
        self.projetil_business.verificar_colisao_projeteis(self.efeitos_explosao, self.pontuacao_business)

        # Colisões com objetos
        self.projetil_business.verificar_colisoes_com_objetos(self.jogador, self.inimigos, self.pontuacao_business)

        # Verifica se o jogador perdeu todas as vidas usando regra de negócio
        if self.pontuacao_business.verificar_game_over():
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
            self.mover_inimigos()
            self.mover_projeteis()
            self.inimigos_atiram()
            self.verificar_colisoes()
            self.atualizar_efeitos_explosao()

            # Reinicia o nível se todos os inimigos forem destruídos
            if len(self.inimigos) == 0:
                self.velocidade_inimigo_base += 0.5
                self.inicializar_jogo()

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
        Responsabilidade do controlador: gerenciar toda a renderização.
        """
        # Desenha fundo
        if self.background:
            self.tela.blit(self.background, (0, 0))
        else:
            self.tela.fill(COR_FUNDO)

        # Desenha jogador usando método local
        self.desenhar_jogador()

        # Desenha inimigos usando método local
        for inimigo in self.inimigos:
            self.desenhar_inimigo(inimigo)

        # Desenha projéteis usando método local
        for projetil in self.projeteis_jogador + self.projeteis_inimigo:
            self.desenhar_projetil(projetil)

        # Desenha efeitos de explosão
        for efeito in self.efeitos_explosao:
            self.desenhar_efeito_explosao(efeito)

        # Desenha HUD
        self.desenhar_hud()
        pygame.display.flip()

    def desenhar_jogador(self):
        """
        Método do controlador para renderizar o jogador.
        Separação correta: renderização no controlador, dados na entidade.
        """
        if self.jogador.sprite:
            sprite_rect = self.jogador.sprite.get_rect(center=self.jogador.rect.center)
            self.tela.blit(self.jogador.sprite, sprite_rect)
        else:
            pygame.draw.rect(self.tela, COR_JOGADOR, self.jogador.rect)

    def desenhar_inimigo(self, inimigo):
        """
        Método do controlador para renderizar um inimigo.
        Separação correta: renderização no controlador, dados na entidade.
        """
        if inimigo.sprite:
            sprite_rect = inimigo.sprite.get_rect(center=inimigo.rect.center)
            self.tela.blit(inimigo.sprite, sprite_rect)
        else:
            pygame.draw.rect(self.tela, COR_INIMIGO, inimigo.rect)

    def desenhar_projetil(self, projetil):
        """
        Método do controlador para renderizar um projétil.
        Separação correta: renderização no controlador, dados na entidade.
        """
        if projetil.sprite:
            sprite_rect = projetil.sprite.get_rect(center=projetil.rect.center)
            self.tela.blit(projetil.sprite, sprite_rect)
        else:
            pygame.draw.rect(self.tela, projetil.cor_fallback, projetil.rect)

    def desenhar_efeito_explosao(self, efeito):
        """
        Método do controlador para renderizar efeitos de explosão.
        Separação correta: renderização no controlador, dados na entidade.
        """
        if not efeito.ativo:
            return

        if efeito.sprite:
            # Redimensiona o sprite baseado no tamanho atual
            sprite_escalado = pygame.transform.scale(efeito.sprite,
                                                    (int(efeito.tamanho_atual), int(efeito.tamanho_atual)))
            pos_x = efeito.x - efeito.tamanho_atual // 2
            pos_y = efeito.y - efeito.tamanho_atual // 2
            self.tela.blit(sprite_escalado, (pos_x, pos_y))
        else:
            # Efeito de fallback: círculos concêntricos
            tempo_atual = pygame.time.get_ticks()
            tempo_decorrido = tempo_atual - efeito.tempo_criacao
            progresso = tempo_decorrido / efeito.tempo_vida

            for i, cor in enumerate(efeito.cores_explosao):
                raio = int(efeito.tamanho_atual * (1 - i * 0.2) * (1 - progresso))
                if raio > 0:
                    pygame.draw.circle(self.tela, cor, (int(efeito.x), int(efeito.y)), raio)

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
    
    # ========================================================================
    # MÉTODO PRINCIPAL - GAME LOOP
    # ========================================================================

    def executar(self):
        """
        GAME LOOP PRINCIPAL - Coração do jogo

        PADRÃO GAME LOOP (padrão clássico de jogos):
        1. PROCESSAR EVENTOS: Lê input do usuário
        2. ATUALIZAR: Executa lógica do jogo
        3. DESENHAR: Renderiza tudo na tela
        4. CONTROLAR FPS: Limita velocidade do loop

        Este padrão se repete 60 vezes por segundo (60 FPS)

        DELEGAÇÃO:
        - Cada fase delegada para método específico
        - Mantém executar() simples e legível
        - Facilita manutenção

        MÁQUINA DE ESTADOS:
        - Métodos processar/atualizar/desenhar mudam comportamento
          baseado no estado atual (menu, jogando, game over)
        """
        # Loop infinito até self.rodando = False
        while self.rodando:
            # FASE 1: Processa entrada do usuário
            self.processar_eventos()

            # FASE 2: Atualiza lógica do jogo
            self.atualizar()

            # FASE 3: Renderiza tudo na tela
            self.desenhar()

            # FASE 4: Controla FPS (60 frames por segundo)
            self.clock.tick(60)

        # Finaliza pygame e sai do programa
        pygame.quit()
        sys.exit()
