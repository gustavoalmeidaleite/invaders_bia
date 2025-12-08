# ============================================================================
# ARQUIVO UTILS.PY - CONSTANTES E CLASSES UTILITÁRIAS
# ============================================================================
"""
PROPÓSITO:
Este arquivo centraliza CONSTANTES e CLASSES UTILITÁRIAS usadas em todo o jogo.

PRINCÍPIO DE POO:
- CENTRALIZAÇÃO: Todas as constantes em um único lugar
- MANUTENIBILIDADE: Fácil modificar valores do jogo
- REUTILIZAÇÃO: Importado por todas as outras classes
"""

import pygame  # Biblioteca para desenvolvimento de jogos
import os      # Para manipulação de caminhos de arquivos

# ============================================================================
# CONSTANTES DO JOGO - CONFIGURAÇÕES PRINCIPAIS
# ============================================================================
# Dimensões da tela
LARGURA_TELA = 800  # Largura da janela do jogo em pixels
ALTURA_TELA = 600   # Altura da janela do jogo em pixels

# Cores RGB (Red, Green, Blue) - valores de 0 a 255
COR_FUNDO = (0, 0, 0)              # Preto - cor de fundo do jogo
COR_JOGADOR = (0, 255, 0)          # Verde - cor da nave do jogador
COR_INIMIGO = (255, 0, 0)          # Vermelho - cor dos inimigos
COR_TIRO = (255, 255, 0)           # Amarelo - cor dos tiros do jogador
COR_TIRO_INIMIGO = (255, 100, 100) # Vermelho claro - tiros dos inimigos

# Velocidades de movimento (pixels por frame)
VELOCIDADE_JOGADOR = 5  # Velocidade de movimento da nave do jogador
VELOCIDADE_TIRO = 7     # Velocidade dos projéteis
VELOCIDADE_INIMIGO = 2  # Velocidade lateral dos inimigos

# ============================================================================
# CONSTANTES DE INTERFACE - CORES DE TEXTO E MENUS
# ============================================================================
COR_TEXTO = (255, 255, 255)           # Branco - texto normal
COR_TEXTO_SELECIONADO = (255, 255, 0) # Amarelo - opção selecionada no menu
COR_TITULO = (0, 255, 255)            # Ciano - títulos

# ============================================================================
# CONSTANTES DE ESTADO - MÁQUINA DE ESTADOS DO JOGO
# ============================================================================
# O jogo usa uma MÁQUINA DE ESTADOS para controlar fluxo
ESTADO_MENU = 0       # Estado: exibindo menu principal
ESTADO_JOGANDO = 1    # Estado: jogando (gameplay ativo)
ESTADO_GAME_OVER = 2  # Estado: game over (fim de jogo)

# ============================================================================
# CLASSE EFEITOEXPLOSAO - EFEITO VISUAL
# ============================================================================
class EfeitoExplosao:
    """
    ========================================================================
    CLASSE EFEITOEXPLOSAO - EFEITO VISUAL TEMPORÁRIO
    ========================================================================

    PROPÓSITO:
    Representa um efeito visual de explosão quando projéteis colidem.
    Efeito temporário que cresce e desaparece após um tempo.

    PRINCÍPIOS DE POO:
    1. ENCAPSULAMENTO: Atributos privados com properties
    2. COESÃO: Responsabilidade única - gerenciar efeito de explosão
    3. ABSTRAÇÃO: Esconde lógica de tempo e animação

    RELACIONAMENTOS:
    - USADO POR: ProjetilBusiness (cria explosões em colisões)
    - USADO POR: Jogo (renderiza explosões)

    ATRIBUTOS:
    - Posição (x, y)
    - Tamanho (inicial e atual)
    - Tempo de vida e criação
    - Estado ativo/inativo
    - Sprite opcional
    ========================================================================
    """

    def __init__(self, x: int, y: int, tamanho: int = 20):
        """
        CONSTRUTOR DA CLASSE EFEITOEXPLOSAO

        Args:
            x (int): Posição horizontal da explosão
            y (int): Posição vertical da explosão
            tamanho (int): Tamanho inicial da explosão em pixels
        """
        # ENCAPSULAMENTO: Atributos privados
        self.__x = x
        self.__y = y
        self.__tamanho_inicial = tamanho
        self.__tamanho_atual = tamanho
        self.__tempo_vida = 300  # Duração em milissegundos
        self.__tempo_criacao = pygame.time.get_ticks()  # Momento da criação
        self.__ativo = True      # Explosão está ativa
        self.__sprite = None     # Sprite opcional para renderização

        # Cores para efeito de fallback (gradiente de explosão)
        self.__cores_explosao = [
            (255, 255, 255),  # Branco (centro)
            (255, 255, 0),    # Amarelo
            (255, 165, 0),    # Laranja
            (255, 0, 0),      # Vermelho
            (128, 0, 0)       # Vermelho escuro
        ]

    # ========================================================================
    # PROPERTIES SOMENTE LEITURA - ENCAPSULAMENTO
    # ========================================================================
    @property
    def x(self) -> int:
        """Posição X da explosão (somente leitura)"""
        return self.__x

    @property
    def y(self) -> int:
        """Posição Y da explosão (somente leitura)"""
        return self.__y

    @property
    def tamanho_inicial(self) -> int:
        """Tamanho inicial da explosão (somente leitura)"""
        return self.__tamanho_inicial

    @property
    def tamanho_atual(self) -> float:
        """Tamanho atual - cresce com animação (somente leitura)"""
        return self.__tamanho_atual

    @property
    def tempo_vida(self) -> int:
        """Duração da explosão em ms (somente leitura)"""
        return self.__tempo_vida

    @property
    def tempo_criacao(self) -> int:
        """Momento de criação (somente leitura)"""
        return self.__tempo_criacao

    @property
    def ativo(self) -> bool:
        """Status ativo da explosão (somente leitura)"""
        return self.__ativo

    @property
    def cores_explosao(self) -> list:
        """Lista de cores do gradiente (retorna cópia - ENCAPSULAMENTO)"""
        return self.__cores_explosao.copy()

    @property
    def sprite(self):
        """Sprite da explosão - AGREGAÇÃO (pode ser None)"""
        return self.__sprite

    @sprite.setter
    def sprite(self, surface):
        """Define sprite - INJEÇÃO DE DEPENDÊNCIA"""
        self.__sprite = surface

    # ========================================================================
    # MÉTODOS PÚBLICOS - LÓGICA DE ANIMAÇÃO
    # ========================================================================
    def atualizar(self):
        """
        LÓGICA: Atualiza animação da explosão
        - Verifica se tempo expirou
        - Aumenta tamanho progressivamente
        """
        tempo_atual = pygame.time.get_ticks()
        tempo_decorrido = tempo_atual - self.__tempo_criacao

        if tempo_decorrido >= self.__tempo_vida:
            self.__ativo = False  # Desativa explosão
        else:
            # Efeito de expansão progressiva
            progresso = tempo_decorrido / self.__tempo_vida
            self.__tamanho_atual = self.__tamanho_inicial * (1 + progresso * 0.5)

# ============================================================================
# FUNÇÕES UTILITÁRIAS - CARREGAMENTO DE RECURSOS
# ============================================================================
def carregar_sprite(nome_arquivo, largura, altura):
    """
    Carrega e redimensiona sprite do diretório static

    TRATAMENTO DE ERROS: Retorna fallback magenta se falhar

    Args:
        nome_arquivo (str): Nome do arquivo de imagem
        largura (int): Largura desejada
        altura (int): Altura desejada

    Returns:
        pygame.Surface: Imagem carregada ou fallback
    """
    caminho = os.path.join("static", nome_arquivo)
    try:
        imagem = pygame.image.load(caminho)
        imagem = pygame.transform.scale(imagem, (largura, altura))
        return imagem
    except Exception as e:
        print(f"Erro ao carregar sprite {nome_arquivo}: {e}")
        # Fallback: quadrado magenta indica erro visualmente
        surface = pygame.Surface((largura, altura))
        surface.fill((255, 0, 255))  # Magenta
        return surface
