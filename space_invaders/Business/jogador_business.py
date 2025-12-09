# ============================================================================
# IMPORTAÇÕES
# ============================================================================
from ..Dados.jogador import Jogador  # Classe de dados Jogador
from ..Dados.projetil import Projetil  # Classe de dados Projetil
from ..utils import LARGURA_TELA, ALTURA_TELA, VELOCIDADE_TIRO  # Constantes

# ============================================================================
# CLASSE JOGADORBUSINESS - CAMADA DE LÓGICA DE NEGÓCIO (BUSINESS)
# ============================================================================
class JogadorBusiness:
    """
    ========================================================================
    CLASSE JOGADORBUSINESS - LÓGICA DE NEGÓCIO
    ========================================================================

    PROPÓSITO:
    Esta classe contém as REGRAS DE NEGÓCIO relacionadas ao jogador.
    Implementa a LÓGICA de comportamento do jogador, separada dos DADOS.

    PRINCÍPIOS DE POO APLICADOS:

    1. SEPARAÇÃO DE RESPONSABILIDADES (SRP):
       - Dados: Classe Jogador (armazena estado)
       - Lógica: Classe JogadorBusiness (processa comportamento)
       - Renderização: Classe Jogo (desenha na tela)

    2. COESÃO:
       - Responsabilidade única: gerenciar comportamento do jogador
       - Todas as ações do jogador (mover, atirar) estão aqui
       - NÃO contém dados (isso é no Jogador)
       - NÃO contém renderização (isso é no Controller)

    3. ENCAPSULAMENTO:
       - Usa properties do Jogador para acessar/modificar estado
       - Não acessa atributos privados diretamente
       - Respeita interface pública da classe Jogador

    4. COMPOSIÇÃO:
       - JogadorBusiness "tem um" Jogador (relacionamento forte)
       - Business não faz sentido sem um Jogador associado

    PADRÃO DE ARQUITETURA:
    Arquitetura em camadas (Layered Architecture):
    - DADOS (Jogador): O QUE é o jogador
    - NEGÓCIO (JogadorBusiness): COMO o jogador se comporta
    - CONTROLE (Jogo): QUANDO executar comportamentos

    RELACIONAMENTOS:
    - USA: Jogador (lê e modifica estado via properties)
    - CRIA: Projetil (quando jogador atira)
    - USA: Projetil (atualiza posição dos tiros)
    - USADO POR: Jogo/JogoHeadless (controladores)

    ATRIBUTOS:
    - jogador: Objeto Jogador a gerenciar
    - velocidade: Velocidade de movimento do jogador
    ========================================================================
    """

    def __init__(self, jogador, velocidade=None):
        """
        CONSTRUTOR DA CLASSE JOGADORBUSINESS

        Inicializa o gerenciador de lógica de negócio do jogador.

        COMPOSIÇÃO:
        - Recebe objeto Jogador existente
        - Armazena referência para gerenciar comportamento
        - Business está fortemente acoplado ao Jogador

        Args:
            jogador (Jogador): Objeto Jogador a gerenciar
            velocidade (int, optional): Velocidade customizada, ou usa velocidade do jogador

        Exemplo de uso:
            jogador = Jogador(400, 550)
            business = JogadorBusiness(jogador)
        """
        self.jogador = jogador  # Referência ao objeto Jogador
        # Usa velocidade customizada ou pega do jogador via property
        self.velocidade = velocidade if velocidade is not None else jogador.velocidade

    # ========================================================================
    # MÉTODOS DE LÓGICA DE NEGÓCIO - AÇÕES DO JOGADOR
    # ========================================================================

    def atirar(self):
        """
        REGRA DE NEGÓCIO: Jogador dispara um projétil

        LÓGICA IMPLEMENTADA:
        1. Calcula posição central do jogador para origem do tiro
        2. Cria novo projétil na posição calculada
        3. Adiciona tiro à lista do jogador (via método controlado)
        4. Retorna o projétil criado

        ENCAPSULAMENTO EM AÇÃO:
        - Usa properties: jogador.x, jogador.largura, jogador.y
        - Usa método controlado: jogador.adicionar_tiro()
        - Não acessa atributos privados diretamente

        SEPARAÇÃO DE RESPONSABILIDADES:
        - JogadorBusiness: decide ONDE criar projétil
        - Jogador: armazena lista de tiros
        - Projetil: armazena dados do projétil
        - ProjetilBusiness: gerencia movimento do projétil

        Returns:
            Projetil: Novo projétil criado

        Exemplo de uso:
            novo_tiro = jogador_business.atirar()
            projeteis_jogador.append(novo_tiro)
        """
        # Calcula posição X central do jogador
        # jogador.largura // 2: centro do jogador
        # - 3: ajuste para centralizar projétil (largura do projétil / 2)
        tiro_x = self.jogador.x + self.jogador.largura // 2 - 3

        # Posição Y: topo do jogador (tiro sai da frente da nave)
        tiro_y = self.jogador.y

        # Cria novo projétil (eh_inimigo=False por padrão)
        novo_tiro = Projetil(tiro_x, tiro_y)

        # Adiciona à lista de tiros do jogador via método controlado
        # Demonstra ENCAPSULAMENTO: não acessa lista diretamente
        self.jogador.adicionar_tiro(novo_tiro)

        return novo_tiro

    def atualizar_tiros(self):
        """
        REGRA DE NEGÓCIO: Atualizar posição dos tiros e remover os que saíram

        LÓGICA IMPLEMENTADA:
        1. Obtém lista de tiros do jogador (via property - retorna cópia)
        2. Para cada tiro:
           a. Move para cima (diminui Y)
           b. Se saiu da tela, remove da lista

        ENCAPSULAMENTO EM AÇÃO:
        - Usa property: jogador.tiros (retorna cópia para segurança)
        - Usa método: tiro.atualizar_posicao() (interface controlada)
        - Usa método: jogador.remover_tiro() (remoção controlada)

        ITERAÇÃO SEGURA:
        - tiros_atuais[:] cria cópia da lista para iteração
        - Permite remover itens durante iteração sem erro

        Exemplo de uso:
            jogador_business.atualizar_tiros()  # Chamado a cada frame
        """
        # Obtém cópia da lista de tiros via property
        # Property retorna cópia para proteger lista interna
        tiros_atuais = self.jogador.tiros

        # Itera sobre cópia da lista (permite remoção segura)
        for tiro in tiros_atuais[:]:
            # Calcula nova posição Y (tiros do jogador sobem)
            # VELOCIDADE_TIRO é subtraída (movimento para cima)
            nova_y = tiro.y - VELOCIDADE_TIRO

            # Atualiza posição via método (mantém sincronização com Rect)
            tiro.atualizar_posicao(tiro.x, nova_y)

            # Remove tiros que saíram da tela (parte superior)
            # tiro.y < -tiro.altura: completamente fora da tela
            if tiro.y < -tiro.altura:
                # Remove via método controlado (ENCAPSULAMENTO)
                self.jogador.remover_tiro(tiro)

    # ========================================================================
    # MÉTODOS DE MOVIMENTO - DELEGAM PARA PROPERTIES DO JOGADOR
    # ========================================================================
    # Estes métodos implementam a LÓGICA de movimento
    # Delegam para properties do Jogador que fazem VALIDAÇÃO automática

    def mover_esquerda(self, largura_tela):
        """
        REGRA DE NEGÓCIO: Mover jogador para a esquerda

        LÓGICA: Diminui posição X pela velocidade
        VALIDAÇÃO: Property x do Jogador garante que não sai da tela

        ENCAPSULAMENTO:
        - Usa property: jogador.x -= velocidade
        - Property valida limites automaticamente
        - Se tentar sair da tela, property corrige para 0

        Args:
            largura_tela (int): Largura da tela (não usado, mas mantido para interface)
        """
        self.jogador.x -= self.velocidade

    def mover_direita(self, largura_tela):
        """
        REGRA DE NEGÓCIO: Mover jogador para a direita

        LÓGICA: Aumenta posição X pela velocidade
        VALIDAÇÃO: Property x do Jogador garante que não sai da tela

        Args:
            largura_tela (int): Largura da tela (não usado, mas mantido para interface)
        """
        self.jogador.x += self.velocidade

    def mover_cima(self):
        """
        REGRA DE NEGÓCIO: Mover jogador para cima

        LÓGICA: Diminui posição Y pela velocidade
        VALIDAÇÃO: Property y do Jogador garante que não sai da tela
        """
        self.jogador.y -= self.velocidade

    def mover_baixo(self, altura_tela):
        """
        REGRA DE NEGÓCIO: Mover jogador para baixo

        LÓGICA: Aumenta posição Y pela velocidade
        VALIDAÇÃO: Property y do Jogador garante que não sai da tela

        Args:
            altura_tela (int): Altura da tela (não usado, mas mantido para interface)
        """
        self.jogador.y += self.velocidade
