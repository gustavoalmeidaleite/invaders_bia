# ============================================================================
# IMPORTAÇÕES
# ============================================================================
import pygame  # Biblioteca para desenvolvimento de jogos
from ..utils import VELOCIDADE_JOGADOR, LARGURA_TELA, ALTURA_TELA  # Constantes

# ============================================================================
# CLASSE JOGADOR - CAMADA DE DADOS (MODEL)
# ============================================================================
class Jogador:
    """
    ========================================================================
    CLASSE JOGADOR - ENTIDADE DE DADOS
    ========================================================================

    PROPÓSITO:
    Esta classe representa o jogador (nave espacial) no jogo Space Invaders.
    É uma classe de DADOS pura, responsável apenas por armazenar e
    gerenciar o estado do jogador.

    PRINCÍPIOS DE POO APLICADOS:

    1. ENCAPSULAMENTO:
       - Todos os atributos são PRIVADOS (prefixo __)
       - Acesso controlado através de PROPERTIES (getters/setters)
       - Validação rigorosa nos setters (ex: não sair da tela)
       - Lista de tiros protegida com métodos específicos

    2. ABSTRAÇÃO:
       - Esconde complexidade interna (pygame.Rect, lista de tiros)
       - Interface simples e clara para uso externo
       - Detalhes de implementação ocultos

    3. COESÃO:
       - Responsabilidade única: gerenciar dados do jogador
       - NÃO contém lógica de negócio (movimento, disparo)
       - NÃO contém lógica de renderização

    4. COMPOSIÇÃO:
       - Jogador "tem uma" lista de tiros (relacionamento forte)
       - Jogador "tem um" Rect (relacionamento forte)
       - Se Jogador é destruído, seus tiros também são

    RELACIONAMENTOS:
    - COMPOSIÇÃO: Contém pygame.Rect e lista de Projetil
    - AGREGAÇÃO: Pode ter um sprite associado (opcional)
    - USADO POR: JogadorBusiness (lógica de negócio)
    - USADO POR: Jogo/JogoHeadless (controladores)

    ATRIBUTOS PRIVADOS:
    - __x: Posição horizontal na tela
    - __y: Posição vertical na tela
    - __largura: Largura da nave em pixels
    - __altura: Altura da nave em pixels
    - __velocidade: Velocidade de movimento
    - __rect: Retângulo pygame para detecção de colisão
    - __tiros: Lista de projéteis disparados pelo jogador
    - __sprite: Imagem visual da nave (pode ser None)
    ========================================================================
    """

    def __init__(self, x: int, y: int, largura: int = 50, altura: int = 30):
        """
        CONSTRUTOR DA CLASSE JOGADOR

        Inicializa uma nova instância de Jogador (nave espacial).
        Este método é chamado automaticamente ao criar um objeto:
        jogador = Jogador(400, 550)

        ENCAPSULAMENTO EM AÇÃO:
        - Todos os atributos inicializados como PRIVADOS (__)
        - Impede acesso direto: jogador.__x (gera erro)
        - Força uso de properties: jogador.x (controlado e validado)

        COMPOSIÇÃO EM AÇÃO:
        - Cria internamente um pygame.Rect (parte integral)
        - Cria internamente uma lista de tiros (parte integral)
        - Estes objetos pertencem ao Jogador e são destruídos com ele

        Args:
            x (int): Posição horizontal inicial (centro da tela geralmente)
            y (int): Posição vertical inicial (parte inferior da tela)
            largura (int): Largura da nave em pixels (padrão: 50)
            altura (int): Altura da nave em pixels (padrão: 30)

        Exemplo de uso:
            # Cria jogador no centro inferior da tela
            jogador = Jogador(LARGURA_TELA // 2 - 25, ALTURA_TELA - 50)
        """
        # ====================================================================
        # ATRIBUTOS PRIVADOS - ENCAPSULAMENTO
        # ====================================================================
        # Prefixo __ torna atributos PRIVADOS (name mangling)

        self.__x = x                            # Posição X (horizontal)
        self.__y = y                            # Posição Y (vertical)
        self.__largura = largura                # Largura da nave
        self.__altura = altura                  # Altura da nave
        self.__velocidade = VELOCIDADE_JOGADOR  # Velocidade de movimento

        # COMPOSIÇÃO: Jogador "tem um" Rect (relacionamento forte)
        # O Rect é criado e gerenciado pela classe Jogador
        # Usado para detecção de colisão com projéteis inimigos
        self.__rect = pygame.Rect(x, y, largura, altura)

        # COMPOSIÇÃO: Jogador "tem uma" lista de tiros (relacionamento forte)
        # A lista é criada vazia e gerenciada pela classe
        # Armazena objetos Projetil disparados pelo jogador
        self.__tiros = []

        # AGREGAÇÃO: Jogador "pode ter" um sprite (relacionamento fraco)
        # O sprite é opcional e definido externamente
        self.__sprite = None

    # ========================================================================
    # PROPERTIES - ENCAPSULAMENTO COM VALIDAÇÃO
    # ========================================================================
    # Properties implementam ENCAPSULAMENTO em Python
    # Permitem controlar acesso aos atributos privados
    # Sintaxe limpa: jogador.x (parece atributo, mas executa método)

    # ------------------------------------------------------------------------
    # PROPERTY X - POSIÇÃO HORIZONTAL COM VALIDAÇÃO RIGOROSA
    # ------------------------------------------------------------------------
    @property
    def x(self) -> int:
        """
        GETTER para posição X do jogador

        ENCAPSULAMENTO: Permite LEITURA controlada do atributo privado __x

        Returns:
            int: Posição horizontal atual do jogador

        Exemplo:
            posicao_atual = jogador.x  # Chama este getter
        """
        return self.__x

    @x.setter
    def x(self, novo_x: int):
        """
        SETTER para posição X com VALIDAÇÃO RIGOROSA

        ENCAPSULAMENTO: Permite ESCRITA controlada do atributo privado __x
        VALIDAÇÃO FORTE: Garante que jogador NUNCA saia da tela

        Diferença do Inimigo:
        - Inimigo: permite sair parcialmente da tela
        - Jogador: NUNCA sai da tela (correção automática)

        Demonstra VALIDAÇÃO DEFENSIVA:
        - Se valor válido: aceita
        - Se valor inválido: corrige automaticamente para limite mais próximo
        - Nunca permite estado inválido

        Args:
            novo_x (int): Nova posição horizontal desejada

        Comportamento:
            - Se 0 <= novo_x <= LARGURA_TELA - largura: aceita valor
            - Se novo_x < 0: força para 0 (borda esquerda)
            - Se novo_x > limite: força para limite (borda direita)

        Exemplo:
            jogador.x = 100      # OK: dentro dos limites
            jogador.x = -50      # Corrigido para 0
            jogador.x = 10000    # Corrigido para LARGURA_TELA - largura
        """
        if 0 <= novo_x <= LARGURA_TELA - self.__largura:
            # Valor válido: aceita normalmente
            self.__x = novo_x
            self.__rect.x = novo_x
        else:
            # Valor inválido: corrige automaticamente
            if novo_x < 0:
                # Tentou sair pela esquerda: fixa na borda esquerda
                self.__x = 0
                self.__rect.x = 0
            else:
                # Tentou sair pela direita: fixa na borda direita
                self.__x = LARGURA_TELA - self.__largura
                self.__rect.x = self.__x

    # ------------------------------------------------------------------------
    # PROPERTY Y - POSIÇÃO VERTICAL COM VALIDAÇÃO RIGOROSA
    # ------------------------------------------------------------------------
    @property
    def y(self) -> int:
        """
        GETTER para posição Y do jogador

        ENCAPSULAMENTO: Permite LEITURA controlada do atributo privado __y

        Returns:
            int: Posição vertical atual do jogador

        Exemplo:
            altura = jogador.y  # Chama este getter
        """
        return self.__y

    @y.setter
    def y(self, novo_y: int):
        """
        SETTER para posição Y com VALIDAÇÃO RIGOROSA

        ENCAPSULAMENTO: Permite ESCRITA controlada do atributo privado __y
        VALIDAÇÃO FORTE: Garante que jogador NUNCA saia da tela verticalmente

        Mesma lógica de validação defensiva do setter X:
        - Aceita valores válidos
        - Corrige automaticamente valores inválidos
        - Mantém sincronização com pygame.Rect

        Args:
            novo_y (int): Nova posição vertical desejada

        Comportamento:
            - Se 0 <= novo_y <= ALTURA_TELA - altura: aceita valor
            - Se novo_y < 0: força para 0 (borda superior)
            - Se novo_y > limite: força para limite (borda inferior)

        Exemplo:
            jogador.y = 500      # OK: dentro dos limites
            jogador.y = -10      # Corrigido para 0
            jogador.y = 9999     # Corrigido para ALTURA_TELA - altura
        """
        if 0 <= novo_y <= ALTURA_TELA - self.__altura:
            # Valor válido: aceita normalmente
            self.__y = novo_y
            self.__rect.y = novo_y
        else:
            # Valor inválido: corrige automaticamente
            if novo_y < 0:
                # Tentou sair por cima: fixa na borda superior
                self.__y = 0
                self.__rect.y = 0
            else:
                # Tentou sair por baixo: fixa na borda inferior
                self.__y = ALTURA_TELA - self.__altura
                self.__rect.y = self.__y

    # ------------------------------------------------------------------------
    # PROPERTIES SOMENTE LEITURA (READ-ONLY)
    # ------------------------------------------------------------------------
    # Estas properties NÃO têm setter, apenas getter
    # Implementam atributos IMUTÁVEIS após criação
    # Demonstra controle fino: alguns atributos podem ser lidos mas não modificados

    @property
    def largura(self) -> int:
        """
        GETTER para largura do jogador (SOMENTE LEITURA)

        Não possui setter - largura é IMUTÁVEL após criação
        Demonstra ENCAPSULAMENTO: podemos ler, mas não modificar

        Returns:
            int: Largura da nave em pixels
        """
        return self.__largura

    @property
    def altura(self) -> int:
        """
        GETTER para altura do jogador (SOMENTE LEITURA)

        Não possui setter - altura é IMUTÁVEL após criação

        Returns:
            int: Altura da nave em pixels
        """
        return self.__altura

    # ------------------------------------------------------------------------
    # PROPERTY VELOCIDADE - COM VALIDAÇÃO DE LIMITES
    # ------------------------------------------------------------------------
    @property
    def velocidade(self) -> int:
        """
        GETTER para velocidade do jogador

        Returns:
            int: Velocidade de movimento em pixels por frame
        """
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, nova_velocidade: int):
        """
        SETTER para velocidade com VALIDAÇÃO DE LIMITES

        VALIDAÇÃO: Garante velocidade dentro de limites razoáveis
        - Mínimo: 0 (parado)
        - Máximo: 20 (muito rápido)

        Demonstra validação para manter jogabilidade equilibrada

        Args:
            nova_velocidade (int): Nova velocidade desejada

        Comportamento:
            - Se < 0: força para 0
            - Se > 20: força para 20
            - Caso contrário: aceita valor

        Exemplo:
            jogador.velocidade = 10   # OK
            jogador.velocidade = -5   # Corrigido para 0
            jogador.velocidade = 100  # Corrigido para 20
        """
        if nova_velocidade < 0:
            self.__velocidade = 0
        elif nova_velocidade > 20:  # Limite máximo razoável para jogabilidade
            self.__velocidade = 20
        else:
            self.__velocidade = nova_velocidade

    # ------------------------------------------------------------------------
    # PROPERTY RECT - SOMENTE LEITURA
    # ------------------------------------------------------------------------
    @property
    def rect(self) -> pygame.Rect:
        """
        GETTER para rect do jogador (SOMENTE LEITURA)

        Retorna o pygame.Rect usado para detecção de colisão
        IMPORTANTE: Retorna referência ao objeto interno (não cópia)
        Usado pelo sistema de colisão do pygame

        Returns:
            pygame.Rect: Retângulo de colisão do jogador
        """
        return self.__rect

    # ------------------------------------------------------------------------
    # PROPERTY TIROS - ACESSO CONTROLADO (PROTEÇÃO ESPECIAL)
    # ------------------------------------------------------------------------
    @property
    def tiros(self) -> list:
        """
        GETTER para lista de tiros (RETORNA CÓPIA)

        ENCAPSULAMENTO AVANÇADO:
        - Retorna CÓPIA da lista, não a lista original
        - Impede modificação direta: jogador.tiros.append() não afeta lista real
        - Força uso dos métodos adicionar_tiro() e remover_tiro()

        Por que retornar cópia?
        - Protege integridade da lista interna
        - Garante que modificações passem por validação
        - Evita efeitos colaterais indesejados

        Returns:
            list: Cópia da lista de projéteis do jogador

        Exemplo:
            tiros = jogador.tiros  # Recebe cópia
            tiros.append(x)        # Modifica cópia, não afeta jogador
            # Para adicionar de verdade, use: jogador.adicionar_tiro(x)
        """
        return self.__tiros.copy()

    # ------------------------------------------------------------------------
    # PROPERTY SPRITE - AGREGAÇÃO
    # ------------------------------------------------------------------------
    @property
    def sprite(self):
        """
        GETTER para sprite (imagem) do jogador

        AGREGAÇÃO: O sprite é opcional e gerenciado externamente
        Pode ser None (usa cor sólida) ou pygame.Surface (usa imagem)

        Returns:
            pygame.Surface ou None: Imagem da nave
        """
        return self.__sprite

    @sprite.setter
    def sprite(self, surface):
        """
        SETTER para sprite do jogador

        AGREGAÇÃO: Permite injeção de dependência (sprite externo)
        Aceita qualquer Surface compatível ou None

        Padrão de design: Injeção de Dependência
        - Sprite é criado externamente e injetado
        - Classe não depende de detalhes de carregamento de imagem

        Args:
            surface: pygame.Surface ou None
        """
        self.__sprite = surface

    # ========================================================================
    # MÉTODOS PÚBLICOS - INTERFACE CONTROLADA PARA MANIPULAR TIROS
    # ========================================================================
    # Estes métodos fornecem acesso CONTROLADO à lista privada __tiros
    # Demonstram ENCAPSULAMENTO: operações específicas em vez de acesso direto

    def adicionar_tiro(self, tiro):
        """
        Adiciona um tiro à lista de forma CONTROLADA

        ENCAPSULAMENTO: Substitui acesso direto à lista
        Permite adicionar validação futura se necessário

        Por que método em vez de acesso direto?
        - Ponto único de controle para adição
        - Facilita adicionar validação/logging no futuro
        - Mantém encapsulamento da lista privada

        Args:
            tiro: Objeto Projetil a ser adicionado

        Exemplo:
            novo_tiro = Projetil(x, y)
            jogador.adicionar_tiro(novo_tiro)
        """
        self.__tiros.append(tiro)

    def remover_tiro(self, tiro):
        """
        Remove um tiro da lista de forma CONTROLADA

        ENCAPSULAMENTO: Substitui acesso direto à lista
        VALIDAÇÃO: Verifica se tiro existe antes de remover

        Evita erro se tentar remover tiro que não existe

        Args:
            tiro: Objeto Projetil a ser removido

        Exemplo:
            jogador.remover_tiro(tiro_antigo)
        """
        if tiro in self.__tiros:
            self.__tiros.remove(tiro)

    def limpar_tiros(self):
        """
        Remove TODOS os tiros da lista

        ENCAPSULAMENTO: Operação específica para limpar lista
        Útil ao reiniciar jogo ou trocar de fase

        Exemplo:
            jogador.limpar_tiros()  # Remove todos os tiros
        """
        self.__tiros.clear()
