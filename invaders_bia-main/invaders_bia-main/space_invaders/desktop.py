"""
Módulo Desktop - Entry Point para Jogo Local (Pygame)

Este é o ponto de entrada para executar o jogo no modo desktop,
com interface gráfica completa usando Pygame.

Como executar:
    python -m space_invaders.desktop

Controles:
    - WASD ou Setas: Movimentar a nave
    - Z: Atirar
    - ESC: Abrir menu / Voltar
    - ENTER ou ESPAÇO: Confirmar opção no menu
"""

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
