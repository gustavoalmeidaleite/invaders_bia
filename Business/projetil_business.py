import pygame
from Dados.projetil import Projetil
from utils import ALTURA_TELA, EfeitoExplosao

class ProjetilBusiness:
    def __init__(self, projeteis_jogador, projeteis_inimigo, altura_tela=ALTURA_TELA):
        self.projeteis_jogador = projeteis_jogador
        self.projeteis_inimigo = projeteis_inimigo
        self.altura_tela = altura_tela

    def mover_projeteis(self):
        # Mover projéteis do jogador
        for projetil in self.projeteis_jogador[:]:
            projetil.mover()
            if projetil.y < -projetil.altura:
                self.projeteis_jogador.remove(projetil)

        # Mover projéteis dos inimigos
        for projetil in self.projeteis_inimigo[:]:
            projetil.mover()
            if projetil.y > self.altura_tela:
                self.projeteis_inimigo.remove(projetil)

    def verificar_colisao_projeteis(self, efeitos_explosao, pontuacao):
        """
        Verifica colisões entre projéteis do jogador e dos inimigos.
        Cria efeitos de explosão quando há colisão.
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

                    # Adiciona pontos bônus por interceptar projétil inimigo
                    pontuacao.adicionar_pontos(5)

                    break  # Sai do loop interno para evitar erro de lista modificada

    def verificar_colisoes_com_objetos(self, jogador, inimigos, pontuacao):
        """
        Verifica colisões de projéteis com jogador, inimigos e jogador.
        """
        # Tiros do jogador acertando inimigos
        for tiro in self.projeteis_jogador[:]:
            for inimigo in inimigos[:]:
                if tiro.rect.colliderect(inimigo.rect):
                    self.projeteis_jogador.remove(tiro)
                    inimigos.remove(inimigo)
                    # Adiciona pontos baseado no tipo do inimigo
                    pontos = {1: 30, 2: 20, 3: 10}
                    pontuacao.adicionar_pontos(pontos.get(inimigo.tipo, 10))
                    break

        # Tiros dos inimigos acertando o jogador
        for tiro in self.projeteis_inimigo[:]:
            if tiro.rect.colliderect(jogador.rect):
                self.projeteis_inimigo.remove(tiro)
                pontuacao.perder_vida()
                break