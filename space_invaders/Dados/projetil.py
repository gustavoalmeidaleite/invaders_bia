# ============================================================================
# IMPORTAÇÕES
# ============================================================================
import pygame  # Biblioteca para desenvolvimento de jogos
from ..utils import COR_TIRO, COR_TIRO_INIMIGO, LARGURA_TELA, ALTURA_TELA

# ============================================================================
# CLASSE PROJETIL - CAMADA DE DADOS (MODEL)
# ============================================================================
class Projetil:
    """
    ========================================================================
    CLASSE PROJETIL - ENTIDADE DE DADOS
    ========================================================================

    PROPÓSITO:
    Esta classe representa um projétil (tiro) disparado pelo jogador ou
    pelos inimigos. É uma classe de DADOS pura, responsável apenas por
    armazenar o estado de um projétil individual.

    PRINCÍPIOS DE POO APLICADOS:

    1. ENCAPSULAMENTO:
       - Todos os atributos são PRIVADOS (prefixo __)
       - Acesso controlado através de PROPERTIES
       - Validação nos setters quando necessário

    2. ABSTRAÇÃO:
       - Esconde complexidade interna (pygame.Rect, cores)
       - Interface simples: x, y, largura, altura, tipo

    3. COESÃO:
       - Responsabilidade única: gerenciar dados de um projétil
       - NÃO contém lógica de movimento (isso é no Business)
       - NÃO contém lógica de renderização

    4. POLIMORFISMO (conceitual):
       - Mesmo tipo de objeto representa tiros do jogador E dos inimigos
       - Atributo __eh_inimigo diferencia comportamento
       - Cores diferentes baseadas no tipo

    RELACIONAMENTOS:
    - COMPOSIÇÃO: Contém um pygame.Rect (parte integral)
    - AGREGAÇÃO: Pode ter um sprite associado (opcional)
    - USADO POR: ProjetilBusiness (lógica de negócio)
    - USADO POR: Jogador (composição - jogador tem lista de tiros)

    ATRIBUTOS PRIVADOS:
    - __x: Posição horizontal na tela
    - __y: Posição vertical na tela
    - __largura: Largura do projétil em pixels
    - __altura: Altura do projétil em pixels
    - __rect: Retângulo pygame para detecção de colisão
    - __eh_inimigo: True se é tiro de inimigo, False se é do jogador
    - __cor_fallback: Cor usada se não houver sprite
    - __sprite: Imagem visual do projétil (pode ser None)
    ========================================================================
    """

    def __init__(self, x: int, y: int, largura: int = 6, altura: int = 15, eh_inimigo: bool = False):
        """
        CONSTRUTOR DA CLASSE PROJETIL

        Inicializa uma nova instância de Projétil.
        Pode representar tiro do jogador OU do inimigo (polimorfismo conceitual).

        ENCAPSULAMENTO:
        - Todos os atributos inicializados como PRIVADOS (__)

        LÓGICA CONDICIONAL:
        - Define cor diferente baseada em quem disparou
        - Tiro do jogador: amarelo
        - Tiro do inimigo: vermelho claro

        Args:
            x (int): Posição horizontal inicial do projétil
            y (int): Posição vertical inicial do projétil
            largura (int): Largura do projétil em pixels (padrão: 6)
            altura (int): Altura do projétil em pixels (padrão: 15)
            eh_inimigo (bool): True se é tiro de inimigo, False se é do jogador

        Exemplo de uso:
            # Tiro do jogador
            tiro_jogador = Projetil(400, 500, eh_inimigo=False)

            # Tiro do inimigo
            tiro_inimigo = Projetil(200, 100, eh_inimigo=True)
        """
        # ====================================================================
        # ATRIBUTOS PRIVADOS - ENCAPSULAMENTO
        # ====================================================================
        self.__x = x                    # Posição X (horizontal)
        self.__y = y                    # Posição Y (vertical)
        self.__largura = largura        # Largura do projétil
        self.__altura = altura          # Altura do projétil

        # COMPOSIÇÃO: Projetil "tem um" Rect (relacionamento forte)
        # Usado para detecção de colisão
        self.__rect = pygame.Rect(x, y, largura, altura)

        # Tipo do projétil (jogador ou inimigo)
        self.__eh_inimigo = eh_inimigo

        # AGREGAÇÃO: Sprite opcional
        self.__sprite = None

        # ====================================================================
        # LÓGICA CONDICIONAL - Define cor baseada no tipo
        # ====================================================================
        # Demonstra como um atributo pode determinar comportamento
        # Tiros de inimigos e jogadores têm cores diferentes
        if eh_inimigo:
            self.__cor_fallback = COR_TIRO_INIMIGO  # Vermelho claro
        else:
            self.__cor_fallback = COR_TIRO          # Amarelo

    # ========================================================================
    # PROPERTIES - ENCAPSULAMENTO
    # ========================================================================

    # ------------------------------------------------------------------------
    # PROPERTY X - POSIÇÃO HORIZONTAL SEM RESTRIÇÃO
    # ------------------------------------------------------------------------
    @property
    def x(self) -> int:
        """
        GETTER para posição X do projétil

        Returns:
            int: Posição horizontal atual
        """
        return self.__x

    @x.setter
    def x(self, novo_x: int):
        """
        SETTER para posição X SEM VALIDAÇÃO DE LIMITES

        Diferença importante:
        - Jogador/Inimigo: validam limites da tela
        - Projétil: NÃO valida limites

        Por quê?
        - Projéteis podem sair da tela (são removidos depois)
        - Não precisam ser contidos dentro dos limites
        - Simplifica lógica de movimento

        Args:
            novo_x (int): Nova posição horizontal
        """
        self.__x = novo_x
        self.__rect.x = novo_x  # Mantém sincronização com Rect

    # ------------------------------------------------------------------------
    # PROPERTY Y - POSIÇÃO VERTICAL SEM RESTRIÇÃO
    # ------------------------------------------------------------------------
    @property
    def y(self) -> int:
        """
        GETTER para posição Y do projétil

        Returns:
            int: Posição vertical atual
        """
        return self.__y

    @y.setter
    def y(self, novo_y: int):
        """
        SETTER para posição Y SEM VALIDAÇÃO DE LIMITES

        Permite que projétil saia da tela
        Lógica de remoção é responsabilidade do Business

        Args:
            novo_y (int): Nova posição vertical
        """
        self.__y = novo_y
        self.__rect.y = novo_y  # Mantém sincronização com Rect

    # ------------------------------------------------------------------------
    # PROPERTIES SOMENTE LEITURA (READ-ONLY)
    # ------------------------------------------------------------------------
    @property
    def largura(self) -> int:
        """
        GETTER para largura do projétil (SOMENTE LEITURA)

        Returns:
            int: Largura em pixels
        """
        return self.__largura

    @property
    def altura(self) -> int:
        """
        GETTER para altura do projétil (SOMENTE LEITURA)

        Returns:
            int: Altura em pixels
        """
        return self.__altura

    @property
    def rect(self) -> pygame.Rect:
        """
        GETTER para rect do projétil (SOMENTE LEITURA)

        Usado para detecção de colisão pelo pygame

        Returns:
            pygame.Rect: Retângulo de colisão
        """
        return self.__rect

    @property
    def eh_inimigo(self) -> bool:
        """
        GETTER para tipo do projétil (SOMENTE LEITURA)

        Determina:
        - Direção do movimento (cima ou baixo)
        - Cor do projétil
        - Com quem pode colidir

        IMUTÁVEL: Definido na criação e não muda

        Returns:
            bool: True se é tiro de inimigo, False se é do jogador
        """
        return self.__eh_inimigo

    @property
    def cor_fallback(self) -> tuple:
        """
        GETTER para cor de fallback (SOMENTE LEITURA)

        Cor usada quando não há sprite disponível
        Definida automaticamente baseada em eh_inimigo

        Returns:
            tuple: Cor RGB (ex: (255, 255, 0) para amarelo)
        """
        return self.__cor_fallback

    # ------------------------------------------------------------------------
    # PROPERTY SPRITE - AGREGAÇÃO
    # ------------------------------------------------------------------------
    @property
    def sprite(self):
        """
        GETTER para sprite do projétil

        AGREGAÇÃO: Sprite é opcional e gerenciado externamente

        Returns:
            pygame.Surface ou None: Imagem do projétil
        """
        return self.__sprite

    @sprite.setter
    def sprite(self, surface):
        """
        SETTER para sprite do projétil

        AGREGAÇÃO: Permite injeção de dependência
        Aceita qualquer Surface ou None

        Args:
            surface: pygame.Surface ou None
        """
        self.__sprite = surface

    # ========================================================================
    # MÉTODOS PÚBLICOS - INTERFACE DE CONVENIÊNCIA
    # ========================================================================

    def atualizar_posicao(self, nova_x: int, nova_y: int):
        """
        Atualiza posição X e Y simultaneamente

        MÉTODO DE CONVENIÊNCIA:
        - Alternativa para atualizar x e y separadamente
        - Usa as properties internamente (garante sincronização com Rect)
        - Mais legível que duas atribuições separadas

        Args:
            nova_x (int): Nova posição horizontal
            nova_y (int): Nova posição vertical

        Exemplo:
            # Em vez de:
            projetil.x = 100
            projetil.y = 200

            # Pode usar:
            projetil.atualizar_posicao(100, 200)
        """
        self.x = nova_x
        self.y = nova_y
