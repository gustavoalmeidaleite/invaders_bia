import pygame
from .jogo import Jogo

def main():
    """
    Função principal que inicia o jogo.
    Demonstra instanciação: cria um objeto da classe Jogo e executa.
    """
    pygame.init()
    jogo = Jogo()
    jogo.executar()

if __name__ == "__main__":
    main()
