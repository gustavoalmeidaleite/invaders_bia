import pygame
from jogo import Jogo

# Inicialização do pygame
pygame.init()

def main():
    """
    Função principal que inicia o jogo.
    Demonstra instanciação: cria um objeto da classe Jogo e executa.
    """
    jogo = Jogo()
    jogo.executar()

if __name__ == "__main__":
    main()