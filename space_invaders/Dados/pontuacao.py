# ============================================================================
# CLASSE PONTUACAO - CAMADA DE DADOS (MODEL)
# ============================================================================
class Pontuacao:
    """
    ========================================================================
    CLASSE PONTUACAO - ENTIDADE DE DADOS
    ========================================================================

    PROPÓSITO:
    Esta classe representa os dados de pontuação e vidas do jogador.
    É uma classe de DADOS simples, focada em armazenar estado do jogo.

    PRINCÍPIOS DE POO APLICADOS:

    1. ENCAPSULAMENTO:
       - Atributos privados (__pontos, __vidas_jogador)
       - Acesso controlado via properties com validação
       - Impede valores inválidos (pontos/vidas negativos)

    2. ABSTRAÇÃO:
       - Interface simples: pontos e vidas
       - Esconde detalhes de armazenamento interno

    3. COESÃO:
       - Responsabilidade única: gerenciar pontuação e vidas
       - NÃO contém lógica de negócio (cálculo de pontos)
       - NÃO contém lógica de renderização

    4. MÉTODOS ESPECIAIS:
       - __str__: Representação em string (para debug)
       - __eq__: Comparação de igualdade entre objetos

    RELACIONAMENTOS:
    - USADO POR: PontuacaoBusiness (lógica de negócio)
    - USADO POR: Jogo/JogoHeadless (controladores)

    ATRIBUTOS PRIVADOS:
    - __pontos: Pontuação atual do jogador
    - __vidas_jogador: Número de vidas restantes
    ========================================================================
    """

    def __init__(self, pontos_iniciais: int = 0, vidas_iniciais: int = 3):
        """
        CONSTRUTOR DA CLASSE PONTUACAO

        Inicializa uma nova instância de Pontuacao com valores padrão.

        ENCAPSULAMENTO:
        - Atributos inicializados como PRIVADOS (__)
        - Valores padrão: 0 pontos, 3 vidas

        Args:
            pontos_iniciais (int): Pontuação inicial (padrão: 0)
            vidas_iniciais (int): Número inicial de vidas (padrão: 3)

        Exemplo de uso:
            pontuacao = Pontuacao()              # 0 pontos, 3 vidas
            pontuacao = Pontuacao(100, 5)        # 100 pontos, 5 vidas
        """
        # ====================================================================
        # ATRIBUTOS PRIVADOS - ENCAPSULAMENTO
        # ====================================================================
        self.__pontos = pontos_iniciais          # Pontuação atual
        self.__vidas_jogador = vidas_iniciais    # Vidas restantes

    # ========================================================================
    # PROPERTIES - ENCAPSULAMENTO COM VALIDAÇÃO
    # ========================================================================

    # ------------------------------------------------------------------------
    # PROPERTY PONTOS - COM VALIDAÇÃO
    # ------------------------------------------------------------------------
    @property
    def pontos(self) -> int:
        """
        GETTER para pontos do jogador

        Returns:
            int: Pontuação atual do jogador
        """
        return self.__pontos

    @pontos.setter
    def pontos(self, novos_pontos: int):
        """
        SETTER para pontos com VALIDAÇÃO

        VALIDAÇÃO: Garante que pontos nunca sejam negativos
        Se valor negativo for passado, corrige para 0

        Args:
            novos_pontos (int): Nova pontuação

        Comportamento:
            - Se >= 0: aceita valor
            - Se < 0: força para 0

        Exemplo:
            pontuacao.pontos = 100   # OK
            pontuacao.pontos = -50   # Corrigido para 0
        """
        if novos_pontos < 0:
            self.__pontos = 0
        else:
            self.__pontos = novos_pontos

    # ------------------------------------------------------------------------
    # PROPERTY VIDAS_JOGADOR - COM VALIDAÇÃO DE LIMITES
    # ------------------------------------------------------------------------
    @property
    def vidas_jogador(self) -> int:
        """
        GETTER para vidas do jogador

        Returns:
            int: Número de vidas restantes
        """
        return self.__vidas_jogador

    @vidas_jogador.setter
    def vidas_jogador(self, novas_vidas: int):
        """
        SETTER para vidas com VALIDAÇÃO DE LIMITES

        VALIDAÇÃO: Garante vidas entre 0 e 99
        - Mínimo: 0 (game over)
        - Máximo: 99 (limite razoável para display)

        Args:
            novas_vidas (int): Novo número de vidas

        Comportamento:
            - Se < 0: força para 0
            - Se > 99: força para 99
            - Caso contrário: aceita valor

        Exemplo:
            pontuacao.vidas_jogador = 3    # OK
            pontuacao.vidas_jogador = -1   # Corrigido para 0
            pontuacao.vidas_jogador = 200  # Corrigido para 99
        """
        if novas_vidas < 0:
            self.__vidas_jogador = 0
        elif novas_vidas > 99:  # Limite máximo razoável para display
            self.__vidas_jogador = 99
        else:
            self.__vidas_jogador = novas_vidas

    # ========================================================================
    # MÉTODOS PÚBLICOS - INTERFACE ALTERNATIVA
    # ========================================================================
    # Estes métodos fornecem interface alternativa para modificar valores
    # Internamente usam as properties, garantindo validação

    def definir_pontos(self, pontos: int):
        """
        Define pontos usando a property (garante validação)

        Método alternativo para: pontuacao.pontos = valor
        Útil para manter consistência de interface

        Args:
            pontos (int): Nova pontuação
        """
        self.pontos = pontos

    def definir_vidas(self, vidas: int):
        """
        Define vidas usando a property (garante validação)

        Método alternativo para: pontuacao.vidas_jogador = valor
        Útil para manter consistência de interface

        Args:
            vidas (int): Novo número de vidas
        """
        self.vidas_jogador = vidas

    # ========================================================================
    # MÉTODOS ESPECIAIS (DUNDER METHODS)
    # ========================================================================
    # Métodos especiais do Python que começam e terminam com __
    # Permitem customizar comportamento de operadores e funções built-in

    def __str__(self) -> str:
        """
        MÉTODO ESPECIAL: Representação em string do objeto

        Chamado automaticamente por:
        - print(pontuacao)
        - str(pontuacao)
        - f"{pontuacao}"

        Útil para DEBUG e logging

        Returns:
            str: Representação legível do objeto

        Exemplo:
            pontuacao = Pontuacao(100, 3)
            print(pontuacao)  # Saída: Pontuacao(pontos=100, vidas=3)
        """
        return f"Pontuacao(pontos={self.__pontos}, vidas={self.__vidas_jogador})"

    def __eq__(self, other) -> bool:
        """
        MÉTODO ESPECIAL: Comparação de igualdade

        Chamado automaticamente por:
        - pontuacao1 == pontuacao2
        - pontuacao1 != pontuacao2

        Permite comparar dois objetos Pontuacao
        Dois objetos são iguais se têm mesmos pontos E mesmas vidas

        Args:
            other: Outro objeto para comparar

        Returns:
            bool: True se objetos são iguais, False caso contrário

        Exemplo:
            p1 = Pontuacao(100, 3)
            p2 = Pontuacao(100, 3)
            p3 = Pontuacao(200, 3)
            print(p1 == p2)  # True (mesmos valores)
            print(p1 == p3)  # False (pontos diferentes)
        """
        # Verifica se other é instância de Pontuacao
        if not isinstance(other, Pontuacao):
            return False
        # Compara atributos privados
        return (self.__pontos == other.__pontos and
                self.__vidas_jogador == other.__vidas_jogador)