import pygame
import sys

# Inicialização do pygame
pygame.init()

# Constantes do jogo
LARGURA_TELA = 800
ALTURA_TELA = 600
COR_FUNDO = (0, 0, 0)  # Preto
COR_JOGADOR = (0, 255, 0)  # Verde
VELOCIDADE_JOGADOR = 5

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
    
    def desenhar(self, tela):
        """
        Método para desenhar o jogador na tela.
        Demonstra abstração: esconde os detalhes de como o desenho é feito.
        """
        pygame.draw.rect(tela, COR_JOGADOR, self.rect)

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
    
    def processar_eventos(self):
        """
        Método para processar eventos do pygame.
        Demonstra delegação: delega o controle do jogador baseado nos eventos.
        """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
        
        # Verifica teclas pressionadas continuamente
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.jogador.mover_esquerda()
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.jogador.mover_direita()
    
    def atualizar(self):
        """
        Método para atualizar o estado do jogo.
        Por enquanto, apenas mantém a lógica básica.
        """
        pass
    
    def desenhar(self):
        """
        Método para desenhar todos os elementos na tela.
        Demonstra abstração: esconde os detalhes de renderização.
        """
        # Preenche a tela com cor preta
        self.tela.fill(COR_FUNDO)
        
        # Desenha o jogador
        self.jogador.desenhar(self.tela)
        
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
