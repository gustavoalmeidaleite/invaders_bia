from utils import COR_TIRO, COR_TIRO_INIMIGO
from .entidade_jogo import EntidadeJogo

class Projetil(EntidadeJogo):
    """
    Classe para representar o tiro disparado pelo jogador ou inimigos - SUBCLASSE de EntidadeJogo.
    Implementa HERANÇA: herda atributos e métodos comuns da superclasse EntidadeJogo.
    Demonstra especialização: adiciona atributos específicos (eh_inimigo, cor_fallback).
    Segue os princípios das aulas do Dr. Edson Nascimento.

    HERANÇA IMPLEMENTADA:
    - Herda: x, y, largura, altura, rect, sprite da superclasse
    - Adiciona: eh_inimigo, cor_fallback (especialização)
    - Mantém: setters da superclasse (projéteis podem se mover livremente)
    """

    def __init__(self, x: int, y: int, largura: int = 6, altura: int = 15, eh_inimigo: bool = False):
        """
        Construtor da classe Projetil (subclasse).
        Chama o construtor da superclasse usando super() e adiciona atributos específicos.

        Args:
            x (int): Posição horizontal inicial
            y (int): Posição vertical inicial
            largura (int): Largura do projétil
            altura (int): Altura do projétil
            eh_inimigo (bool): True se é projétil de inimigo, False se é do jogador
        """
        # Determina o sprite baseado no tipo antes de chamar super()
        if eh_inimigo:
            sprite_name = "bullet_enemy.png"
            cor_fallback = COR_TIRO_INIMIGO
        else:
            sprite_name = "bullet_player.png"
            cor_fallback = COR_TIRO

        # Chama o construtor da superclasse (HERANÇA)
        super().__init__(x, y, largura, altura, sprite_name)

        # Atributos específicos da subclasse (ESPECIALIZAÇÃO)
        self.__eh_inimigo = eh_inimigo
        self.__cor_fallback = cor_fallback

    # HERANÇA: Usa os setters da superclasse sem sobrescrita
    # Projéteis podem se mover livremente, então não precisam de validação especial
    # As properties x, y, largura, altura, rect, sprite são herdadas da superclasse

    # Properties específicas da subclasse Projetil (ESPECIALIZAÇÃO)
    @property
    def eh_inimigo(self) -> bool:
        """Getter para tipo do projétil (atributo específico da subclasse, somente leitura)."""
        return self.__eh_inimigo

    @property
    def cor_fallback(self) -> tuple:
        """Getter para cor de fallback do projétil (atributo específico da subclasse, somente leitura)."""
        return self.__cor_fallback

    # Properties herdadas (sprite) não precisam ser redefinidas - HERANÇA!

    # Método específico da subclasse que usa método herdado da superclasse
    def atualizar_posicao(self, nova_x: int, nova_y: int):
        """
        Método para atualizar posição do projétil.
        Usa o método herdado da superclasse EntidadeJogo.
        """
        super().atualizar_posicao(nova_x, nova_y)

    # Sobrescrita do método __str__ da superclasse (HERANÇA + ESPECIALIZAÇÃO)
    def __str__(self) -> str:
        """
        Representação em string específica do projétil.
        Sobrescreve o método da superclasse para incluir informações específicas.
        """
        tipo_str = "Inimigo" if self.__eh_inimigo else "Jogador"
        return f"Projetil(x={self.x}, y={self.y}, tipo={tipo_str})"

