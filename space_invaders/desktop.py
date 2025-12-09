# ============================================================================
# DESKTOP.PY - PONTO DE ENTRADA PARA VERSÃO DESKTOP
# ============================================================================
"""
PROPÓSITO:
Este é o PONTO DE ENTRADA (entry point) para a versão desktop do jogo.
Arquivo executável que inicia o jogo com interface gráfica pygame.

PADRÃO DE DESIGN:
- SINGLE RESPONSIBILITY: Apenas inicializa e executa o jogo
- DELEGAÇÃO: Delega toda lógica para a classe Jogo
- SEPARAÇÃO: Interface (desktop) separada da lógica (Jogo)
"""

import pygame  # Biblioteca de jogos
from .jogo import Jogo  # Classe controladora principal

def main():
    """
    FUNÇÃO PRINCIPAL - Inicializa e executa o jogo

    FLUXO DE EXECUÇÃO:
    1. Inicializa pygame (biblioteca gráfica)
    2. INSTANCIA objeto Jogo (POO - criação de objeto)
    3. Executa o jogo (chama método executar)

    DEMONSTRAÇÃO DE POO:
    - INSTANCIAÇÃO: jogo = Jogo() cria novo objeto
    - ENCAPSULAMENTO: Toda lógica está dentro da classe Jogo
    - ABSTRAÇÃO: main() não precisa saber como Jogo funciona
    """
    # Inicializa todos os módulos do pygame
    pygame.init()

    # INSTANCIAÇÃO: Cria objeto da classe Jogo
    # Demonstra conceito fundamental de POO
    jogo = Jogo()

    # Executa o jogo (chama método público)
    # Demonstra ENCAPSULAMENTO: interface simples, complexidade oculta
    jogo.executar()

# ============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================================
if __name__ == "__main__":
    """
    Verifica se arquivo está sendo executado diretamente
    (não importado como módulo)

    Padrão Python para scripts executáveis
    """
    main()
