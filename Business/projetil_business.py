import pygame
from Dados.projetil import Projetil
from utils import ALTURA_TELA, VELOCIDADE_TIRO, EfeitoExplosao

class ProjetilBusiness:
    """
    Classe para gerenciar as regras de negócio relacionadas aos projéteis.
    Implementa as lógicas de movimento, colisão e comportamento dos projéteis.
    Segue os princípios de POO: separação entre dados e regras de negócio.
    """
    def __init__(self, projeteis_jogador, projeteis_inimigo, altura_tela=ALTURA_TELA):
        self.projeteis_jogador = projeteis_jogador
        self.projeteis_inimigo = projeteis_inimigo
        self.altura_tela = altura_tela

    def mover_projetil(self, projetil):
        """
        Regra de negócio: Movimento dos projéteis.
        Projéteis inimigos descem, projéteis do jogador sobem.
        """
        if projetil.eh_inimigo:
            nova_y = projetil.y + VELOCIDADE_TIRO  # Tiros inimigos descem
        else:
            nova_y = projetil.y - VELOCIDADE_TIRO  # Tiros do jogador sobem

        projetil.atualizar_posicao(projetil.x, nova_y)

    def mover_todos_projeteis(self):
        """
        Regra de negócio: Mover todos os projéteis ativos.
        Aplica movimento para todos os projéteis nas listas.
        """
        # Move projéteis do jogador
        for projetil in self.projeteis_jogador:
            self.mover_projetil(projetil)

        # Move projéteis dos inimigos
        for projetil in self.projeteis_inimigo:
            self.mover_projetil(projetil)

    def remover_projeteis_fora_tela(self):
        """
        Regra de negócio: Remover projéteis que saíram da tela.
        Otimização de performance e limpeza de memória.
        """
        # Remove projéteis do jogador que saíram pela parte superior
        self.projeteis_jogador[:] = [
            p for p in self.projeteis_jogador
            if p.y > -p.altura
        ]

        # Remove projéteis dos inimigos que saíram pela parte inferior
        self.projeteis_inimigo[:] = [
            p for p in self.projeteis_inimigo
            if p.y < self.altura_tela
        ]

    def verificar_colisao_projeteis(self, efeitos_explosao, pontuacao_business):
        """
        Regra de negócio: Verificar colisões entre projéteis do jogador e dos inimigos.
        Cria efeitos de explosão quando há colisão e aplica bônus de pontuação.
        """
        for tiro_jogador in self.projeteis_jogador[:]:
            for tiro_inimigo in self.projeteis_inimigo[:]:
                if tiro_jogador.rect.colliderect(tiro_inimigo.rect):
                    # Calcula posição central da colisão
                    pos_x = (tiro_jogador.x + tiro_inimigo.x) // 2
                    pos_y = (tiro_jogador.y + tiro_inimigo.y) // 2

                    # Cria efeito de explosão
                    explosao = EfeitoExplosao(pos_x, pos_y, tamanho=15)
                    efeitos_explosao.append(explosao)

                    # Remove ambos os projéteis
                    self.projeteis_jogador.remove(tiro_jogador)
                    self.projeteis_inimigo.remove(tiro_inimigo)

                    # Utiliza a regra de negócio para bônus de interceptação
                    pontuacao_business.adicionar_bonus_interceptacao()

                    break  # Sai do loop interno para evitar erro de lista modificada

    def verificar_colisoes_com_objetos(self, jogador, inimigos, pontuacao_business):
        """
        Regra de negócio: Verificar colisões de projéteis com objetos do jogo.
        Agora utiliza PontuacaoBusiness para aplicar regras de pontuação.
        """
        # Tiros do jogador acertando inimigos
        for tiro in self.projeteis_jogador[:]:
            for inimigo in inimigos[:]:
                if tiro.rect.colliderect(inimigo.rect):
                    self.projeteis_jogador.remove(tiro)
                    inimigos.remove(inimigo)
                    # Utiliza a regra de negócio de pontuação
                    pontuacao_business.adicionar_pontos_inimigo(inimigo.tipo)
                    break

        # Tiros dos inimigos acertando o jogador
        for tiro in self.projeteis_inimigo[:]:
            if tiro.rect.colliderect(jogador.rect):
                self.projeteis_inimigo.remove(tiro)
                # Utiliza a regra de negócio de pontuação
                pontuacao_business.perder_vida()
                break