import pygame
import sys
import random
import os

# Inicialização do pygame
pygame.init()

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

        # Pontuação (se implementada)
        if self.pontuacao > 0:
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

class Tiro:
    """Classe para representar o tiro disparado pelo jogador."""
    def __init__(self, x, y, largura=6, altura=15, eh_inimigo=False):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(x, y, largura, altura)
        self.eh_inimigo = eh_inimigo

        # Carrega sprite apropriado
        if eh_inimigo:
            self.sprite = carregar_sprite("bullet_enemy.png", largura, altura)
            self.cor_fallback = COR_TIRO_INIMIGO
        else:
            self.sprite = carregar_sprite("bullet_player.png", largura, altura)
            self.cor_fallback = COR_TIRO

    def mover(self):
        if self.eh_inimigo:
            self.y += VELOCIDADE_TIRO  # Tiros inimigos descem
        else:
            self.y -= VELOCIDADE_TIRO  # Tiros do jogador sobem
        self.rect.y = self.y

    def desenhar(self, tela):
        if self.sprite:
            tela.blit(self.sprite, (self.x, self.y))
        else:
            pygame.draw.rect(tela, self.cor_fallback, self.rect)

class Inimigo:
    """Classe para representar um inimigo."""
    def __init__(self, x, y, largura=40, altura=25, tipo=1):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(x, y, largura, altura)
        self.direcao = 1  # 1 = direita, -1 = esquerda
        self.tipo = tipo  # Tipo do inimigo (1, 2, 3 para diferentes sprites)

        # Carrega sprite baseado no tipo
        sprite_names = {
            1: "invader_type1.png",
            2: "invader_type2.png",
            3: "invader_type3.png"
        }
        sprite_name = sprite_names.get(tipo, "invader_type1.png")
        self.sprite = carregar_sprite(sprite_name, largura, altura)

    def mover(self):
        self.x += VELOCIDADE_INIMIGO * self.direcao
        if self.x <= 0 or self.x >= LARGURA_TELA - self.largura:
            self.direcao *= -1
            self.y += 20
        self.rect.x = self.x
        self.rect.y = self.y

    def desenhar(self, tela):
        if self.sprite:
            tela.blit(self.sprite, (self.x, self.y))
        else:
            pygame.draw.rect(tela, COR_INIMIGO, self.rect)

class Jogador:
    """
    Classe que representa o jogador (nave espacial).
    Implementa os conceitos de POO: encapsulamento dos atributos e métodos.
    """

    def __init__(self, x, y, largura=50, altura=30):
        """
        Construtor da classe Jogador.
        Inicializa os atributos da instância (variáveis de instância).
        """
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = VELOCIDADE_JOGADOR
        self.rect = pygame.Rect(x, y, largura, altura)
        self.tiros = []

        # Carrega sprite do jogador
        self.sprite = carregar_sprite("player_ship.png", largura, altura)

    def mover_esquerda(self):
        """
        Método para mover o jogador para a esquerda.
        Demonstra encapsulamento: o método controla como o estado do objeto é alterado.
        """
        if self.x > 0:
            self.x -= self.velocidade
            self.rect.x = self.x
    
    def mover_direita(self):
        """
        Método para mover o jogador para a direita.
        """
        if self.x < LARGURA_TELA - self.largura:
            self.x += self.velocidade
            self.rect.x = self.x

    def mover_cima(self):
        """
        Método para mover o jogador para cima.
        """
        if self.y > 0:
            self.y -= self.velocidade
            self.rect.y = self.y

    def mover_baixo(self):
        """
        Método para mover o jogador para baixo.
        """
        if self.y < ALTURA_TELA - self.altura:
            self.y += self.velocidade
            self.rect.y = self.y

    def atirar(self):
        """
        Método para disparar um tiro.
        """
        tiro_x = self.x + self.largura // 2 - 3
        tiro_y = self.y
        novo_tiro = Tiro(tiro_x, tiro_y)
        self.tiros.append(novo_tiro)

    def atualizar_tiros(self):
        """
        Método para atualizar a posição dos tiros e remover os que saíram da tela.
        """
        for tiro in self.tiros[:]:
            tiro.mover()
            if tiro.y < -tiro.altura:
                self.tiros.remove(tiro)

    def desenhar(self, tela):
        """
        Método para desenhar o jogador e seus tiros na tela.
        Demonstra abstração: esconde os detalhes de como o desenho é feito.
        """
        if self.sprite:
            tela.blit(self.sprite, (self.x, self.y))
        else:
            pygame.draw.rect(tela, COR_JOGADOR, self.rect)
        for tiro in self.tiros:
            tiro.desenhar(tela)

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
        self.pontuacao = 0
        self.vidas = 3

        # Lista de efeitos de explosão
        self.efeitos_explosao = []

        # Inicializa componentes do jogo
        self.inicializar_jogo()

    def inicializar_jogo(self):
        """Inicializa ou reinicializa os componentes do jogo."""
        # Composição: o jogo contém um jogador
        self.jogador = Jogador(LARGURA_TELA // 2 - 25, ALTURA_TELA - 50)
        self.inimigos = self.criar_inimigos()
        self.tempo_ultimo_tiro = 0
        self.intervalo_tiro = 200  # milissegundos

        # Lista de tiros dos inimigos
        self.tiros_inimigos = []
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
                self.pontuacao = 0
                self.vidas = 3
            elif resultado == "sair":
                self.rodando = False

        elif self.estado == ESTADO_GAME_OVER:
            resultado = self.game_over.processar_eventos()
            if resultado == "reiniciar":
                self.estado = ESTADO_JOGANDO
                self.inicializar_jogo()
                self.pontuacao = 0
                self.vidas = 3
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
            self.jogador.mover_esquerda()
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.jogador.mover_direita()
        # Movimento vertical
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.jogador.mover_cima()
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.jogador.mover_baixo()
        # Atira segurando Z
        if teclas[pygame.K_z]:
            agora = pygame.time.get_ticks()
            if agora - self.tempo_ultimo_tiro > self.intervalo_tiro:
                self.jogador.atirar()
                self.tempo_ultimo_tiro = agora

    def inimigos_atiram(self):
        """
        Método para fazer inimigos atirarem aleatoriamente.
        Limita a quantidade de tiros inimigos na tela.
        """
        agora = pygame.time.get_ticks()
        if (agora - self.tempo_ultimo_tiro_inimigo > self.intervalo_tiro_inimigo and
            len(self.tiros_inimigos) < self.max_tiros_inimigos and
            len(self.inimigos) > 0):
            inimigo = random.choice(self.inimigos)
            tiro_x = inimigo.x + inimigo.largura // 2 - 3
            tiro_y = inimigo.y + inimigo.altura
            novo_tiro = Tiro(tiro_x, tiro_y, eh_inimigo=True)
            self.tiros_inimigos.append(novo_tiro)
            self.tempo_ultimo_tiro_inimigo = agora

    def atualizar_tiros_inimigos(self):
        """
        Atualiza posição dos tiros dos inimigos e remove os que saíram da tela.
        """
        for tiro in self.tiros_inimigos[:]:
            tiro.mover()
            if tiro.y > ALTURA_TELA:
                self.tiros_inimigos.remove(tiro)

    def verificar_colisoes(self):
        """
        Método para verificar colisões entre tiros e inimigos/jogador.
        """
        # NOVA FUNCIONALIDADE: Colisão entre projéteis
        self.verificar_colisao_projeteis()

        # Tiros do jogador acertando inimigos
        for tiro in self.jogador.tiros[:]:
            for inimigo in self.inimigos[:]:
                if tiro.rect.colliderect(inimigo.rect):
                    self.jogador.tiros.remove(tiro)
                    self.inimigos.remove(inimigo)
                    # Adiciona pontos baseado no tipo do inimigo
                    pontos = {1: 30, 2: 20, 3: 10}
                    self.pontuacao += pontos.get(inimigo.tipo, 10)
                    break

        # Tiros dos inimigos acertando o jogador
        for tiro in self.tiros_inimigos[:]:
            if tiro.rect.colliderect(self.jogador.rect):
                self.tiros_inimigos.remove(tiro)
                self.vidas -= 1
                if self.vidas <= 0:
                    self.game_over = GameOver(self.tela, self.pontuacao)
                    self.estado = ESTADO_GAME_OVER
                break

        # Verifica se inimigos chegaram muito perto do jogador
        for inimigo in self.inimigos:
            if inimigo.y + inimigo.altura >= self.jogador.y:
                self.game_over = GameOver(self.tela, self.pontuacao)
                self.estado = ESTADO_GAME_OVER
                break

    def verificar_colisao_projeteis(self):
        """
        Verifica colisões entre projéteis do jogador e dos inimigos.
        Cria efeitos de explosão quando há colisão.
        """
        for tiro_jogador in self.jogador.tiros[:]:
            for tiro_inimigo in self.tiros_inimigos[:]:
                if tiro_jogador.rect.colliderect(tiro_inimigo.rect):
                    # Calcula posição central da colisão
                    pos_x = (tiro_jogador.x + tiro_inimigo.x) // 2
                    pos_y = (tiro_jogador.y + tiro_inimigo.y) // 2

                    # Cria efeito de explosão
                    explosao = EfeitoExplosao(pos_x, pos_y, tamanho=15)
                    self.efeitos_explosao.append(explosao)

                    # Remove ambos os projéteis
                    self.jogador.tiros.remove(tiro_jogador)
                    self.tiros_inimigos.remove(tiro_inimigo)

                    # Adiciona pontos bônus por interceptar projétil inimigo
                    self.pontuacao += 5

                    break  # Sai do loop interno para evitar erro de lista modificada

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
            for inimigo in self.inimigos:
                inimigo.mover()
            self.jogador.atualizar_tiros()
            self.inimigos_atiram()
            self.atualizar_tiros_inimigos()
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
        # Desenha tiros dos inimigos
        for tiro in self.tiros_inimigos:
            tiro.desenhar(self.tela)

        # Desenha efeitos de explosão
        for efeito in self.efeitos_explosao:
            efeito.desenhar(self.tela)

        # Desenha HUD (pontuação e vidas)
        self.desenhar_hud()
        pygame.display.flip()

    def desenhar_hud(self):
        """
        Desenha a interface do usuário (HUD) com pontuação e vidas.
        """
        fonte = pygame.font.Font(None, 36)

        # Pontuação
        texto_pontos = fonte.render(f"Pontos: {self.pontuacao}", True, COR_TEXTO)
        self.tela.blit(texto_pontos, (10, 10))

        # Vidas
        texto_vidas = fonte.render(f"Vidas: {self.vidas}", True, COR_TEXTO)
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

def main():
    """
    Função principal que inicia o jogo.
    Demonstra instanciação: cria um objeto da classe Jogo e executa.
    """
    jogo = Jogo()
    jogo.executar()

if __name__ == "__main__":
    main()
