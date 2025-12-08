# ============================================================================
# IMPORTAÇÕES
# ============================================================================
import random  # Para seleção aleatória de inimigo atirador
from ..Dados.inimigo import Inimigo  # Classe de dados Inimigo
from ..Dados.projetil import Projetil  # Classe de dados Projetil
from ..utils import LARGURA_TELA, VELOCIDADE_INIMIGO  # Constantes

# ============================================================================
# CLASSE INIMIGOBUSINESS - CAMADA DE LÓGICA DE NEGÓCIO (BUSINESS)
# ============================================================================
class InimigoBusiness:
    """
    ========================================================================
    CLASSE INIMIGOBUSINESS - LÓGICA DE NEGÓCIO
    ========================================================================

    PROPÓSITO:
    Esta classe contém as REGRAS DE NEGÓCIO relacionadas aos inimigos.
    Implementa a LÓGICA de comportamento dos inimigos, separada dos DADOS.

    PRINCÍPIOS DE POO APLICADOS:

    1. SEPARAÇÃO DE RESPONSABILIDADES (SRP - Single Responsibility Principle):
       - Dados: Classe Inimigo (armazena estado)
       - Lógica: Classe InimigoBusiness (processa comportamento)
       - Esta separação facilita manutenção e testes

    2. COESÃO:
       - Responsabilidade única: gerenciar comportamento dos inimigos
       - Todas as regras de negócio de inimigos estão aqui
       - NÃO contém renderização (isso é no Controller)

    3. COMPOSIÇÃO/AGREGAÇÃO:
       - Recebe lista de inimigos (agregação)
       - Não cria os inimigos, apenas gerencia comportamento
       - Relacionamento fraco: Business pode existir sem inimigos

    PADRÃO DE ARQUITETURA:
    Este é um exemplo de ARQUITETURA EM CAMADAS:
    - Camada de DADOS (Inimigo): O QUE é um inimigo
    - Camada de NEGÓCIO (InimigoBusiness): COMO inimigos se comportam
    - Camada de CONTROLE (Jogo): QUANDO executar comportamentos

    RELACIONAMENTOS:
    - USA: Inimigo (lê e modifica estado via properties)
    - CRIA: Projetil (quando inimigo atira)
    - USADO POR: Jogo/JogoHeadless (controladores)

    ATRIBUTOS:
    - inimigos: Lista de objetos Inimigo a gerenciar
    - velocidade_base: Velocidade de movimento dos inimigos
    ========================================================================
    """

    def __init__(self, inimigos, velocidade_base=VELOCIDADE_INIMIGO):
        """
        CONSTRUTOR DA CLASSE INIMIGOBUSINESS

        Inicializa o gerenciador de lógica de negócio dos inimigos.

        AGREGAÇÃO:
        - Recebe lista de inimigos existente (não cria)
        - Armazena referência para gerenciar comportamento

        Args:
            inimigos (list): Lista de objetos Inimigo a gerenciar
            velocidade_base (int): Velocidade de movimento (padrão: VELOCIDADE_INIMIGO)

        Exemplo de uso:
            inimigos = [Inimigo(100, 50), Inimigo(200, 50)]
            business = InimigoBusiness(inimigos, velocidade_base=2)
        """
        self.inimigos = inimigos              # Lista de inimigos a gerenciar
        self.velocidade_base = velocidade_base  # Velocidade de movimento

    # ========================================================================
    # MÉTODOS DE LÓGICA DE NEGÓCIO
    # ========================================================================

    def atirar_aleatorio(self):
        """
        REGRA DE NEGÓCIO: Inimigo aleatório dispara projétil

        LÓGICA IMPLEMENTADA:
        1. Seleciona um inimigo aleatório da lista
        2. Calcula posição central do inimigo para origem do tiro
        3. Cria novo projétil na posição calculada
        4. Retorna o projétil criado

        SEPARAÇÃO DE RESPONSABILIDADES:
        - InimigoBusiness: decide QUAL inimigo atira e ONDE criar projétil
        - Projetil: armazena dados do projétil
        - ProjetilBusiness: gerencia movimento do projétil

        ENCAPSULAMENTO EM AÇÃO:
        - Usa properties do Inimigo: atirador.x, atirador.largura, etc.
        - Não acessa atributos privados diretamente

        Returns:
            Projetil: Novo projétil criado, ou None se não há inimigos

        Exemplo de uso:
            novo_tiro = inimigo_business.atirar_aleatorio()
            if novo_tiro:
                projeteis_inimigo.append(novo_tiro)
        """
        # Verifica se há inimigos disponíveis
        if self.inimigos:
            # Seleciona inimigo aleatório usando random.choice()
            atirador = random.choice(self.inimigos)

            # Calcula posição X central do inimigo
            # atirador.largura // 2: centro do inimigo
            # - 3: ajuste para centralizar projétil (largura do projétil / 2)
            tiro_x = atirador.x + atirador.largura // 2 - 3

            # Posição Y: logo abaixo do inimigo
            tiro_y = atirador.y + atirador.altura

            # Cria novo projétil marcado como de inimigo
            # eh_inimigo=True: determina direção (para baixo) e cor
            novo_tiro = Projetil(tiro_x, tiro_y, eh_inimigo=True)

            return novo_tiro

        # Sem inimigos: retorna None
        return None

    def mover_inimigos(self, largura_tela):
        """
        REGRA DE NEGÓCIO: Movimento dos inimigos em formação

        LÓGICA IMPLEMENTADA (padrão clássico do Space Invaders):
        1. Todos os inimigos se movem lateralmente na mesma direção
        2. Quando qualquer inimigo atinge a borda da tela:
           a. TODOS invertem direção (esquerda <-> direita)
           b. TODOS descem uma linha (20 pixels)
        3. Movimento sincronizado: todos se movem juntos

        ALGORITMO:
        - Fase 1: Move todos lateralmente e detecta colisão com borda
        - Fase 2: Se houve colisão, inverte direção e desce todos

        SEPARAÇÃO DE RESPONSABILIDADES:
        - InimigoBusiness: implementa LÓGICA de movimento
        - Inimigo: armazena DADOS de posição e direção
        - Properties do Inimigo: validam limites automaticamente

        ENCAPSULAMENTO EM AÇÃO:
        - Usa properties: inimigo.x, inimigo.y, inimigo.direcao
        - Não acessa __x, __y, __direcao diretamente
        - Validação automática via setters das properties

        Args:
            largura_tela (int): Largura da tela para detectar bordas

        Exemplo de uso:
            inimigo_business.mover_inimigos(LARGURA_TELA)
        """
        # Flag para indicar se algum inimigo atingiu a borda
        mover_baixo = False

        # ====================================================================
        # FASE 1: Movimento lateral e detecção de borda
        # ====================================================================
        for inimigo in self.inimigos:
            # Move inimigo lateralmente
            # velocidade_base * direcao: positivo (direita) ou negativo (esquerda)
            # Usa property x: inimigo.x += valor chama o setter
            inimigo.x += self.velocidade_base * inimigo.direcao

            # Verifica se inimigo atingiu borda esquerda ou direita
            if inimigo.x <= 0 or inimigo.x >= largura_tela - inimigo.largura:
                mover_baixo = True  # Marca que precisa descer

        # ====================================================================
        # FASE 2: Inversão de direção e descida (se necessário)
        # ====================================================================
        if mover_baixo:
            for inimigo in self.inimigos:
                # Inverte direção: 1 vira -1, -1 vira 1
                # Usa property direcao com validação automática
                inimigo.direcao *= -1

                # Desce uma linha (20 pixels)
                # Usa property y com validação automática
                inimigo.y += 20
