# Data layer package
# Implementa HERANÇA: EntidadeJogo é a superclasse, outras são subclasses

from .entidade_jogo import EntidadeJogo
from .jogador import Jogador
from .inimigo import Inimigo
from .projetil import Projetil
from .pontuacao import Pontuacao

__all__ = ['EntidadeJogo', 'Jogador', 'Inimigo', 'Projetil', 'Pontuacao']