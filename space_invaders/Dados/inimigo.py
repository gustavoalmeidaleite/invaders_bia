# ============================================================================
# IMPORTAÇÕES
# ============================================================================
import pygame  # Biblioteca para desenvolvimento de jogos
from ..utils import LARGURA_TELA, ALTURA_TELA  # Constantes globais do jogo

# ============================================================================
# CLASSE INIMIGO - CAMADA DE DADOS (MODEL)
# ============================================================================
class Inimigo:
    """
    ========================================================================
    CLASSE INIMIGO - ENTIDADE DE DADOS
    ========================================================================

    PROPÓSITO:
    Esta classe representa um inimigo (alien) no jogo Space Invaders.
    É uma classe de DADOS pura, responsável apenas por armazenar e
    gerenciar o estado de um inimigo individual.

    PRINCÍPIOS DE POO APLICADOS:

    1. ENCAPSULAMENTO:
       - Todos os atributos são PRIVADOS (prefixo __)
       - Acesso controlado através de PROPERTIES (getters/setters)
       - Validação de dados nos setters para garantir integridade
       - Protege o estado interno da classe contra modificações indevidas

    2. ABSTRAÇÃO:
       - Esconde a complexidade interna (como pygame.Rect)
       - Expõe apenas interface necessária (x, y, largura, altura, etc.)
       - Cliente da classe não precisa saber detalhes de implementação

    3. COESÃO:
       - Responsabilidade única: gerenciar dados de um inimigo
       - NÃO contém lógica de negócio (movimento, tiro, etc.)
       - NÃO contém lógica de renderização

    RELACIONAMENTOS:
    - COMPOSIÇÃO: Contém um pygame.Rect (parte integral do inimigo)
    - AGREGAÇÃO: Pode ter um sprite associado (opcional)
    - USADO POR: InimigoBusiness (lógica de negócio)
    - USADO POR: Jogo/JogoHeadless (controladores)

    ATRIBUTOS PRIVADOS:
    - __x: Posição horizontal na tela
    - __y: Posição vertical na tela
    - __largura: Largura do inimigo em pixels
    - __altura: Altura do inimigo em pixels
    - __rect: Retângulo pygame para detecção de colisão
    - __direcao: Direção do movimento (1=direita, -1=esquerda)
    - __tipo: Tipo do inimigo (1, 2 ou 3 - diferentes pontuações)
    - __sprite: Imagem visual do inimigo (pode ser None)
    ========================================================================
    """

    def __init__(self, x: int, y: int, largura: int = 40, altura: int = 25, tipo: int = 1):
        """
        CONSTRUTOR DA CLASSE INIMIGO

        Inicializa uma nova instância de Inimigo com os parâmetros fornecidos.
        Este é o método especial __init__ que é chamado automaticamente
        quando criamos um novo objeto: inimigo = Inimigo(100, 50)

        ENCAPSULAMENTO EM AÇÃO:
        - Todos os atributos são inicializados como PRIVADOS (__)
        - Isso impede acesso direto: inimigo.__x (gera erro)
        - Força uso de properties: inimigo.x (controlado)

        Args:
            x (int): Posição horizontal inicial do inimigo na tela
            y (int): Posição vertical inicial do inimigo na tela
            largura (int): Largura do inimigo em pixels (padrão: 40)
            altura (int): Altura do inimigo em pixels (padrão: 25)
            tipo (int): Tipo do inimigo (1, 2 ou 3 para diferentes sprites e pontuações)

        Exemplo de uso:
            inimigo1 = Inimigo(100, 50, tipo=1)  # Cria inimigo tipo 1 na posição (100, 50)
            inimigo2 = Inimigo(200, 50, tipo=2)  # Cria inimigo tipo 2 na posição (200, 50)
        """
        # ====================================================================
        # ATRIBUTOS PRIVADOS - ENCAPSULAMENTO
        # ====================================================================
        # O prefixo __ (duplo underscore) torna o atributo PRIVADO
        # Python aplica "name mangling": __x vira _Inimigo__x internamente
        # Isso dificulta (mas não impossibilita) acesso externo direto

        self.__x = x                    # Posição X (horizontal)
        self.__y = y                    # Posição Y (vertical)
        self.__largura = largura        # Largura do inimigo
        self.__altura = altura          # Altura do inimigo

        # COMPOSIÇÃO: Inimigo "tem um" Rect (relacionamento forte)
        # O Rect é criado e gerenciado internamente pela classe
        # Se o Inimigo for destruído, o Rect também é destruído
        self.__rect = pygame.Rect(x, y, largura, altura)

        self.__direcao = 1              # Direção do movimento: 1 = direita, -1 = esquerda
        self.__tipo = tipo              # Tipo do inimigo (afeta pontuação e sprite)

        # AGREGAÇÃO: Inimigo "pode ter" um sprite (relacionamento fraco)
        # O sprite é opcional e pode ser definido externamente
        self.__sprite = None            # Inicialmente sem sprite (será definido depois)

    # ========================================================================
    # PROPERTIES - ENCAPSULAMENTO ATRAVÉS DE GETTERS E SETTERS
    # ========================================================================
    # Properties são o mecanismo Python para implementar ENCAPSULAMENTO
    # Permitem controlar acesso aos atributos privados com validação
    # Sintaxe: objeto.x (parece atributo público, mas executa método)

    # ------------------------------------------------------------------------
    # PROPERTY X - POSIÇÃO HORIZONTAL COM VALIDAÇÃO
    # ------------------------------------------------------------------------
    @property
    def x(self) -> int:
        """
        GETTER para posição X do inimigo

        ENCAPSULAMENTO: Permite LEITURA controlada do atributo privado __x

        Returns:
            int: Posição horizontal atual do inimigo

        Exemplo:
            posicao = inimigo.x  # Chama este getter automaticamente
        """
        return self.__x

    @x.setter
    def x(self, novo_x: int):
        """
        SETTER para posição X com VALIDAÇÃO

        ENCAPSULAMENTO: Permite ESCRITA controlada do atributo privado __x
        VALIDAÇÃO: Garante que o inimigo não saia completamente da tela

        Este setter demonstra um princípio importante de POO:
        - Não apenas armazena o valor, mas VALIDA antes
        - Mantém consistência: atualiza __x E __rect.x juntos
        - Protege a integridade dos dados da classe

        Args:
            novo_x (int): Nova posição horizontal

        Validação:
            - Permite valores entre -largura e LARGURA_TELA
            - Permite inimigo sair parcialmente da tela (para efeitos visuais)

        Exemplo:
            inimigo.x = 150  # Chama este setter automaticamente
            inimigo.x += 5   # Move 5 pixels para direita
        """
        # Validação de limites
        if -self.__largura <= novo_x <= LARGURA_TELA:
            self.__x = novo_x
            # IMPORTANTE: Mantém sincronização entre __x e __rect.x
            self.__rect.x = novo_x

    # ------------------------------------------------------------------------
    # PROPERTY Y - POSIÇÃO VERTICAL COM VALIDAÇÃO
    # ------------------------------------------------------------------------
    @property
    def y(self) -> int:
        """
        GETTER para posição Y do inimigo

        ENCAPSULAMENTO: Permite LEITURA controlada do atributo privado __y

        Returns:
            int: Posição vertical atual do inimigo

        Exemplo:
            altura_atual = inimigo.y  # Chama este getter
        """
        return self.__y

    @y.setter
    def y(self, novo_y: int):
        """
        SETTER para posição Y com VALIDAÇÃO

        ENCAPSULAMENTO: Permite ESCRITA controlada do atributo privado __y
        VALIDAÇÃO: Garante que o inimigo permaneça dentro dos limites

        Args:
            novo_y (int): Nova posição vertical

        Validação:
            - Permite valores entre -altura e ALTURA_TELA
            - Mantém sincronização com pygame.Rect

        Exemplo:
            inimigo.y = 200  # Chama este setter
            inimigo.y += 20  # Move 20 pixels para baixo
        """
        if -self.__altura <= novo_y <= ALTURA_TELA:
            self.__y = novo_y
            self.__rect.y = novo_y

    # ------------------------------------------------------------------------
    # PROPERTIES SOMENTE LEITURA (READ-ONLY)
    # ------------------------------------------------------------------------
    # Estas properties NÃO têm setter, apenas getter
    # Implementam atributos IMUTÁVEIS após criação do objeto
    # Demonstra controle fino sobre o que pode ser modificado

    @property
    def largura(self) -> int:
        """
        GETTER para largura do inimigo (SOMENTE LEITURA)

        Não possui setter - largura é IMUTÁVEL após criação
        Demonstra ENCAPSULAMENTO: podemos ler, mas não modificar

        Returns:
            int: Largura do inimigo em pixels
        """
        return self.__largura

    @property
    def altura(self) -> int:
        """
        GETTER para altura do inimigo (SOMENTE LEITURA)

        Não possui setter - altura é IMUTÁVEL após criação

        Returns:
            int: Altura do inimigo em pixels
        """
        return self.__altura

    @property
    def rect(self) -> pygame.Rect:
        """
        GETTER para rect do inimigo (SOMENTE LEITURA)

        Retorna o pygame.Rect usado para detecção de colisão
        IMPORTANTE: Retorna referência ao objeto interno (não cópia)
        Usado pelo sistema de colisão do pygame

        Returns:
            pygame.Rect: Retângulo de colisão do inimigo
        """
        return self.__rect

    # ------------------------------------------------------------------------
    # PROPERTY DIREÇÃO - COM VALIDAÇÃO RIGOROSA
    # ------------------------------------------------------------------------
    @property
    def direcao(self) -> int:
        """
        GETTER para direção do movimento do inimigo

        Returns:
            int: 1 para direita, -1 para esquerda
        """
        return self.__direcao

    @direcao.setter
    def direcao(self, nova_direcao: int):
        """
        SETTER para direção com VALIDAÇÃO RIGOROSA

        VALIDAÇÃO: Aceita APENAS -1 ou 1
        Lança exceção se valor inválido (fail-fast)

        Demonstra validação forte para garantir integridade dos dados

        Args:
            nova_direcao (int): Nova direção (-1 ou 1)

        Raises:
            ValueError: Se direção não for -1 ou 1

        Exemplo:
            inimigo.direcao = 1   # OK: move para direita
            inimigo.direcao = -1  # OK: move para esquerda
            inimigo.direcao = 0   # ERRO: ValueError
        """
        if nova_direcao in [-1, 1]:
            self.__direcao = nova_direcao
        else:
            raise ValueError("Direção deve ser -1 (esquerda) ou 1 (direita)")

    # ------------------------------------------------------------------------
    # PROPERTY TIPO - SOMENTE LEITURA
    # ------------------------------------------------------------------------
    @property
    def tipo(self) -> int:
        """
        GETTER para tipo do inimigo (SOMENTE LEITURA)

        O tipo determina:
        - Qual sprite é usado (visual)
        - Quantos pontos vale ao ser destruído

        Tipo é IMUTÁVEL - definido na criação e não muda

        Returns:
            int: Tipo do inimigo (1, 2 ou 3)
        """
        return self.__tipo

    # ------------------------------------------------------------------------
    # PROPERTY SPRITE - AGREGAÇÃO
    # ------------------------------------------------------------------------
    @property
    def sprite(self):
        """
        GETTER para sprite (imagem) do inimigo

        AGREGAÇÃO: O sprite é opcional e gerenciado externamente
        Pode ser None (usa cor sólida) ou pygame.Surface (usa imagem)

        Returns:
            pygame.Surface ou None: Imagem do inimigo
        """
        return self.__sprite

    @sprite.setter
    def sprite(self, surface):
        """
        SETTER para sprite do inimigo

        AGREGAÇÃO: Permite injeção de dependência (sprite externo)
        Aceita qualquer Surface compatível ou None

        Padrão de design: Injeção de Dependência
        - Sprite é criado externamente e injetado
        - Classe não depende de detalhes de carregamento de imagem

        Args:
            surface: pygame.Surface ou None
        """
        self.__sprite = surface
