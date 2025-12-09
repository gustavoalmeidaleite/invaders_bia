"""
Pacote Dados - Camada de Dados (Model/Entity)

Este pacote contém as classes que representam as ENTIDADES do jogo.
Seguindo os princípios de POO, estas classes:

1. ARMAZENAM DADOS usando atributos privados (encapsulamento)
2. CONTROLAM ACESSO via properties com validação
3. NÃO CONTÊM regras de negócio (delegadas para Business/)

Classes disponíveis:
- Jogador: Representa a nave do jogador
- Inimigo: Representa os invasores alienígenas
- Projetil: Representa tiros (do jogador ou inimigos)
- Pontuacao: Armazena pontos e vidas do jogador

Princípios aplicados: Encapsulamento, SRP (Responsabilidade Única)
"""