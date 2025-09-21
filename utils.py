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

# Diretório de sprites
SPRITES_DIR = "sprites"

# Dicionário para armazenar sprites carregados
sprites_cache = {}

def carregar_sprite(nome_arquivo, largura=None, altura=None):
    """
    Carrega um sprite do diretório sprites com tratamento de erro.
    Retorna None se o arquivo não existir ou houver erro no carregamento.

    Args:
        nome_arquivo (str): Nome do arquivo de sprite
        largura (int, optional): Largura para redimensionar
        altura (int, optional): Altura para redimensionar

    Returns:
        pygame.Surface ou None: Sprite carregado ou None se houver erro
    """
    # Verifica se já está no cache
    cache_key = f"{nome_arquivo}_{largura}_{altura}"
    if cache_key in sprites_cache:
        return sprites_cache[cache_key]

    caminho_sprite = os.path.join(SPRITES_DIR, nome_arquivo)

    try:
        if os.path.exists(caminho_sprite):
            sprite = pygame.image.load(caminho_sprite).convert_alpha()

            # Redimensiona se especificado
            if largura and altura:
                sprite = pygame.transform.scale(sprite, (largura, altura))

            # Armazena no cache
            sprites_cache[cache_key] = sprite
            return sprite
        else:
            print(f"Aviso: Sprite '{nome_arquivo}' não encontrado em '{SPRITES_DIR}'. Usando fallback.")
            return None
    except pygame.error as e:
        print(f"Erro ao carregar sprite '{nome_arquivo}': {e}. Usando fallback.")
        return None

def criar_sprite_fallback(largura, altura, cor):
    """
    Cria um sprite de fallback (retângulo colorido) quando o sprite não está disponível.

    Args:
        largura (int): Largura do sprite
        altura (int): Altura do sprite
        cor (tuple): Cor RGB do sprite

    Returns:
        pygame.Surface: Sprite de fallback
    """
    sprite = pygame.Surface((largura, altura))
    sprite.fill(cor)
    return sprite

class EfeitoExplosao:
    """Classe para representar efeitos de explosão quando projéteis colidem."""

    def __init__(self, x, y, tamanho=20):
        self.x = x
        self.y = y
        self.tamanho_inicial = tamanho
        self.tamanho_atual = tamanho
        self.tempo_vida = 300  # milissegundos
        self.tempo_criacao = pygame.time.get_ticks()
        self.ativo = True

        # Carrega sprite de explosão ou usa fallback
        self.sprite = carregar_sprite("explosion.png", tamanho, tamanho)

        # Cores para efeito de fallback (gradiente de explosão)
        self.cores_explosao = [
            (255, 255, 255),  # Branco (centro)
            (255, 255, 0),    # Amarelo
            (255, 165, 0),    # Laranja
            (255, 0, 0),      # Vermelho
            (128, 0, 0)       # Vermelho escuro
        ]

    def atualizar(self):
        """Atualiza o efeito de explosão."""
        tempo_atual = pygame.time.get_ticks()
        tempo_decorrido = tempo_atual - self.tempo_criacao

        if tempo_decorrido >= self.tempo_vida:
            self.ativo = False
        else:
            # Efeito de expansão e fade
            progresso = tempo_decorrido / self.tempo_vida
            self.tamanho_atual = self.tamanho_inicial * (1 + progresso * 0.5)

    def desenhar(self, tela):
        """Desenha o efeito de explosão."""
        if not self.ativo:
            return

        if self.sprite:
            # Redimensiona o sprite baseado no tamanho atual
            sprite_escalado = pygame.transform.scale(self.sprite,
                                                    (int(self.tamanho_atual), int(self.tamanho_atual)))
            pos_x = self.x - self.tamanho_atual // 2
            pos_y = self.y - self.tamanho_atual // 2
            tela.blit(sprite_escalado, (pos_x, pos_y))
        else:
            # Efeito de fallback: círculos concêntricos
            tempo_atual = pygame.time.get_ticks()
            tempo_decorrido = tempo_atual - self.tempo_criacao
            progresso = tempo_decorrido / self.tempo_vida

            for i, cor in enumerate(self.cores_explosao):
                raio = int(self.tamanho_atual * (1 - i * 0.2) * (1 - progresso))
                if raio > 0:
                    pygame.draw.circle(tela, cor, (int(self.x), int(self.y)), raio)