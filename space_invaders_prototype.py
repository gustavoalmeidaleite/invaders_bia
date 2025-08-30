import pygame
import sys
import random

# Inicialização do pygame
pygame.init()

# Constantes do jogo
LARGURA_TELA = 800
ALTURA_TELA = 600
COR_FUNDO = (0, 0, 0)      # Preto
COR_JOGADOR = (0, 255, 0)  # Verde
COR_INIMIGO = (255, 0, 0)  # Vermelho
COR_TIRO = (255, 255, 0)   # Amarelo
VELOCIDADE_JOGADOR = 5
VELOCIDADE_TIRO = 7
VELOCIDADE_INIMIGO = 2

class Tiro:
    """Classe para representar o tiro disparado pelo jogador."""
    def __init__(self, x, y, largura=6, altura=15):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(x, y, largura, altura)

    def mover(self):
        self.y -= VELOCIDADE_TIRO
        self.rect.y = self.y

    def desenhar(self, tela):
        pygame.draw.rect(tela, COR_TIRO, self.rect)

class Inimigo:
    """Classe para representar um inimigo."""
    def __init__(self, x, y, largura=40, altura=25):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(x, y, largura, altura)
        self.direcao = 1  # 1 = direita, -1 = esquerda

    def mover(self):
        self.x += VELOCIDADE_INIMIGO * self.direcao
        if self.x <= 0 or self.x >= LARGURA_TELA - self.largura:
            self.direcao *= -1
            self.y += 20
        self.rect.x = self.x
        self.rect.y = self.y

    def desenhar(self, tela):
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
        
        # Composição: o jogo contém um jogador
        self.jogador = Jogador(LARGURA_TELA // 2 - 25, ALTURA_TELA - 50)
        self.inimigos = self.criar_inimigos()
        self.tempo_ultimo_tiro = 0
        self.intervalo_tiro = 200  # milissegundos

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
            for coluna in range(colunas):
                x = 60 + coluna * espacamento_x
                y = 50 + linha * espacamento_y
                inimigos.append(Inimigo(x, y))
        return inimigos

    def processar_eventos(self):
        """
        Método para processar eventos do pygame.
        Demonstra delegação: delega o controle do jogador baseado nos eventos.
        """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE or evento.key == pygame.K_x:
                    self.rodando = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.jogador.mover_esquerda()
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.jogador.mover_direita()
        # Atira segurando Z
        if teclas[pygame.K_z]:
            agora = pygame.time.get_ticks()
            if agora - self.tempo_ultimo_tiro > self.intervalo_tiro:
                self.jogador.atirar()
                self.tempo_ultimo_tiro = agora

    def atualizar(self):
        """
        Método para atualizar o estado do jogo.
        Por enquanto, apenas mantém a lógica básica.
        """
        for inimigo in self.inimigos:
            inimigo.mover()
        self.jogador.atualizar_tiros()
        self.verificar_colisoes()

    def verificar_colisoes(self):
        """
        Método para verificar colisões entre tiros e inimigos.
        """
        for tiro in self.jogador.tiros[:]:
            for inimigo in self.inimigos[:]:
                if tiro.rect.colliderect(inimigo.rect):
                    self.jogador.tiros.remove(tiro)
                    self.inimigos.remove(inimigo)
                    break

    def desenhar(self):
        """
        Método para desenhar todos os elementos na tela.
        Demonstra abstração: esconde os detalhes de renderização.
        """
        # Preenche a tela com cor preta
        self.tela.fill(COR_FUNDO)
        
        # Desenha o jogador
        self.jogador.desenhar(self.tela)
        for inimigo in self.inimigos:
            inimigo.desenhar(self.tela)
        
        # Atualiza a tela
        pygame.display.flip()
    
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
