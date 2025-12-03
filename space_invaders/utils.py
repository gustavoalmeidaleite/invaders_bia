import pygame
import os

# Constantes do jogo
LARGURA_TELA = 800
ALTURA_TELA = 600
COR_FUNDO = (0, 0, 0)      # Preto
COR_JOGADOR = (0, 255, 0)  # Verde
COR_INIMIGO = (255, 0, 0)  # Vermelho
COR_TIRO = (255, 255, 0)   # Amarelo
COR_TIRO_INIMIGO = (255, 100, 100)  # Vermelho claro para tiros inimigos
VELOCIDADE_JOGADOR = 5
VELOCIDADE_TIRO = 7
VELOCIDADE_INIMIGO = 2

# Cores para interface
COR_TEXTO = (255, 255, 255)  # Branco
COR_TEXTO_SELECIONADO = (255, 255, 0)  # Amarelo
COR_TITULO = (0, 255, 255)  # Ciano

# Estados do jogo
ESTADO_MENU = 0
ESTADO_JOGANDO = 1
ESTADO_GAME_OVER = 2

class EfeitoExplosao:
    """
    Classe para representar efeitos de explosão quando projéteis colidem.
    Implementa encapsulamento completo dos atributos com properties.
    Segue os princípios das aulas do Dr. Edson Nascimento.
    """

    def __init__(self, x: int, y: int, tamanho: int = 20):
        """
        Construtor da classe EfeitoExplosao.
        Inicializa os atributos privados do efeito.

        Args:
            x (int): Posição horizontal da explosão
            y (int): Posição vertical da explosão
            tamanho (int): Tamanho inicial da explosão
        """
        # Atributos privados (encapsulamento)
        self.__x = x
        self.__y = y
        self.__tamanho_inicial = tamanho
        self.__tamanho_atual = tamanho
        self.__tempo_vida = 300  # milissegundos
        self.__tempo_criacao = pygame.time.get_ticks()
        self.__ativo = True
        self.__sprite = None

        # Cores para efeito de fallback (gradiente de explosão)
        self.__cores_explosao = [
            (255, 255, 255),  # Branco (centro)
            (255, 255, 0),    # Amarelo
            (255, 165, 0),    # Laranja
            (255, 0, 0),      # Vermelho
            (128, 0, 0)       # Vermelho escuro
        ]

    # Properties para X (somente leitura)
    @property
    def x(self) -> int:
        """Getter para posição X da explosão (somente leitura)."""
        return self.__x

    # Properties para Y (somente leitura)
    @property
    def y(self) -> int:
        """Getter para posição Y da explosão (somente leitura)."""
        return self.__y

    # Properties para tamanho_inicial (somente leitura)
    @property
    def tamanho_inicial(self) -> int:
        """Getter para tamanho inicial da explosão (somente leitura)."""
        return self.__tamanho_inicial

    # Properties para tamanho_atual (somente leitura)
    @property
    def tamanho_atual(self) -> float:
        """Getter para tamanho atual da explosão (somente leitura)."""
        return self.__tamanho_atual

    # Properties para tempo_vida (somente leitura)
    @property
    def tempo_vida(self) -> int:
        """Getter para tempo de vida da explosão (somente leitura)."""
        return self.__tempo_vida

    # Properties para tempo_criacao (somente leitura)
    @property
    def tempo_criacao(self) -> int:
        """Getter para tempo de criação da explosão (somente leitura)."""
        return self.__tempo_criacao

    # Properties para ativo (somente leitura)
    @property
    def ativo(self) -> bool:
        """Getter para status ativo da explosão (somente leitura)."""
        return self.__ativo

    # Properties para cores_explosao (somente leitura)
    @property
    def cores_explosao(self) -> list:
        """Getter para cores da explosão (retorna cópia para proteção)."""
        return self.__cores_explosao.copy()

    # Property para sprite (permite injeção de superfície pelo controlador)
    @property
    def sprite(self):
        """Getter para sprite da explosão (pode ser None)."""
        return self.__sprite

    @sprite.setter
    def sprite(self, surface):
        """Setter para sprite da explosão (aceita Surface ou None)."""
        self.__sprite = surface

    def atualizar(self):
        """
        Atualiza o efeito de explosão.
        Modifica atributos internos de forma controlada.
        """
        tempo_atual = pygame.time.get_ticks()
        tempo_decorrido = tempo_atual - self.__tempo_criacao

        if tempo_decorrido >= self.__tempo_vida:
            self.__ativo = False
        else:
            # Efeito de expansão e fade
            progresso = tempo_decorrido / self.__tempo_vida
            self.__tamanho_atual = self.__tamanho_inicial * (1 + progresso * 0.5)

def carregar_sprite(nome_arquivo, largura, altura):
    """
    Carrega uma imagem do diretório static, redimensiona e retorna.
    Em caso de erro, retorna uma superfície colorida (magenta) como fallback.
    """
    caminho = os.path.join("static", nome_arquivo)
    try:
        imagem = pygame.image.load(caminho)
        imagem = pygame.transform.scale(imagem, (largura, altura))
        return imagem
    except Exception as e:
        print(f"Erro ao carregar sprite {nome_arquivo}: {e}")
        # Fallback: quadrado magenta para indicar erro visualmente sem crashar
        surface = pygame.Surface((largura, altura))
        surface.fill((255, 0, 255))
        return surface
