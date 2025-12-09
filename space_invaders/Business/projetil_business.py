# ============================================================================
# IMPORTAÇÕES
# ============================================================================
from ..Dados.projetil import Projetil  # Classe de dados Projetil
from ..utils import ALTURA_TELA, VELOCIDADE_TIRO, EfeitoExplosao  # Constantes e classes utilitárias

# ============================================================================
# CLASSE PROJETILBUSINESS - CAMADA DE LÓGICA DE NEGÓCIO (BUSINESS)
# ============================================================================
class ProjetilBusiness:
    """
    ========================================================================
    CLASSE PROJETILBUSINESS - LÓGICA DE NEGÓCIO
    ========================================================================

    PROPÓSITO:
    Esta classe contém as REGRAS DE NEGÓCIO relacionadas aos projéteis.
    Gerencia movimento, colisões e comportamento de TODOS os projéteis do jogo.

    PRINCÍPIOS DE POO APLICADOS:

    1. SEPARAÇÃO DE RESPONSABILIDADES (SRP):
       - Dados: Classe Projetil (armazena estado de um projétil)
       - Lógica: Classe ProjetilBusiness (gerencia comportamento de todos)

    2. COESÃO:
       - Responsabilidade única: gerenciar comportamento de projéteis
       - Movimento, colisões, remoção de projéteis
       - NÃO contém renderização

    3. POLIMORFISMO (conceitual):
       - Trata projéteis do jogador E dos inimigos
       - Comportamento diferente baseado em projetil.eh_inimigo

    RELACIONAMENTOS:
    - USA: Projetil (lê e modifica via interface pública)
    - USA: PontuacaoBusiness (para adicionar pontos)
    - USA: EfeitoExplosao (cria efeitos visuais)
    - USADO POR: Jogo/JogoHeadless (controladores)

    ATRIBUTOS:
    - projeteis_jogador: Lista de projéteis do jogador
    - projeteis_inimigo: Lista de projéteis dos inimigos
    - jogador: Referência ao jogador (para sincronização)
    - altura_tela: Altura da tela (para detectar saída)
    - sprite_explosao: Sprite para efeitos de explosão
    ========================================================================
    """

    def __init__(self, projeteis_jogador, projeteis_inimigo, jogador=None, altura_tela=ALTURA_TELA, sprite_explosao=None):
        """
        CONSTRUTOR DA CLASSE PROJETILBUSINESS

        AGREGAÇÃO: Recebe listas de projéteis existentes

        Args:
            projeteis_jogador (list): Lista de projéteis do jogador
            projeteis_inimigo (list): Lista de projéteis dos inimigos
            jogador (Jogador, optional): Referência ao jogador
            altura_tela (int): Altura da tela
            sprite_explosao: Sprite para explosões
        """
        self.projeteis_jogador = projeteis_jogador
        self.projeteis_inimigo = projeteis_inimigo
        self.jogador = jogador
        self.altura_tela = altura_tela
        self.sprite_explosao = sprite_explosao

    # ========================================================================
    # MÉTODOS DE LÓGICA DE NEGÓCIO - MOVIMENTO
    # ========================================================================

    def mover_projetil(self, projetil):
        """
        REGRA DE NEGÓCIO: Movimento de um projétil

        POLIMORFISMO CONCEITUAL:
        - Mesmo método trata projéteis do jogador E dos inimigos
        - Comportamento diferente baseado em projetil.eh_inimigo

        LÓGICA:
        - Projéteis do jogador: sobem (Y diminui)
        - Projéteis dos inimigos: descem (Y aumenta)

        Args:
            projetil (Projetil): Projétil a mover
        """
        if projetil.eh_inimigo:
            # Tiros inimigos descem (Y aumenta)
            nova_y = projetil.y + VELOCIDADE_TIRO
        else:
            # Tiros do jogador sobem (Y diminui)
            nova_y = projetil.y - VELOCIDADE_TIRO

        # Atualiza posição via método (mantém sincronização com Rect)
        projetil.atualizar_posicao(projetil.x, nova_y)

    def mover_todos_projeteis(self):
        """
        REGRA DE NEGÓCIO: Mover todos os projéteis ativos

        Aplica movimento para TODOS os projéteis do jogo
        Chamado a cada frame do jogo

        REUTILIZAÇÃO: Usa mover_projetil() para cada projétil
        """
        # Move projéteis do jogador
        for projetil in self.projeteis_jogador:
            self.mover_projetil(projetil)

        # Move projéteis dos inimigos
        for projetil in self.projeteis_inimigo:
            self.mover_projetil(projetil)

    def remover_projeteis_fora_tela(self):
        """
        REGRA DE NEGÓCIO: Remover projéteis que saíram da tela

        OTIMIZAÇÃO:
        - Evita processar projéteis invisíveis
        - Libera memória de objetos não usados
        - Melhora performance do jogo

        LÓGICA:
        - Projéteis do jogador: saem pela parte SUPERIOR (y < 0)
        - Projéteis dos inimigos: saem pela parte INFERIOR (y > altura_tela)
        """
        # Remove projéteis do jogador que saíram pela parte superior
        projeteis_em_tela = []
        for projetil in self.projeteis_jogador:
            # Verifica se ainda está visível
            if projetil.y > -projetil.altura:
                projeteis_em_tela.append(projetil)
            else:
                # Remove também da lista do jogador (sincronização)
                self._remover_tiro_jogador(projetil)
        # Substitui lista por versão filtrada
        self.projeteis_jogador[:] = projeteis_em_tela

        # Remove projéteis dos inimigos que saíram pela parte inferior
        # List comprehension: forma concisa de filtrar lista
        self.projeteis_inimigo[:] = [
            p for p in self.projeteis_inimigo
            if p.y < self.altura_tela
        ]

    # ========================================================================
    # MÉTODOS DE LÓGICA DE NEGÓCIO - COLISÕES
    # ========================================================================

    def verificar_colisao_projeteis(self, efeitos_explosao, pontuacao_business):
        """
        REGRA DE NEGÓCIO: Colisão entre projéteis (jogador vs inimigo)

        LÓGICA IMPLEMENTADA:
        1. Detecta colisão entre tiro do jogador e tiro do inimigo
        2. Cria efeito visual de explosão
        3. Remove ambos os projéteis
        4. Adiciona bônus de pontuação (+5 pontos)

        SEPARAÇÃO DE RESPONSABILIDADES:
        - ProjetilBusiness: detecta colisão e coordena ações
        - EfeitoExplosao: gerencia efeito visual
        - PontuacaoBusiness: gerencia pontuação

        Args:
            efeitos_explosao (list): Lista para adicionar efeitos
            pontuacao_business (PontuacaoBusiness): Para adicionar pontos
        """
        # Itera sobre cópias das listas (permite remoção segura)
        for tiro_jogador in self.projeteis_jogador[:]:
            for tiro_inimigo in self.projeteis_inimigo[:]:
                # Detecta colisão usando pygame.Rect.colliderect()
                if tiro_jogador.rect.colliderect(tiro_inimigo.rect):
                    # Calcula posição central da colisão para explosão
                    pos_x = (tiro_jogador.x + tiro_inimigo.x) // 2
                    pos_y = (tiro_jogador.y + tiro_inimigo.y) // 2

                    # Cria efeito de explosão
                    explosao = EfeitoExplosao(pos_x, pos_y, tamanho=15)
                    if self.sprite_explosao:
                        explosao.sprite = self.sprite_explosao
                    efeitos_explosao.append(explosao)

                    # Remove ambos os projéteis
                    self.projeteis_jogador.remove(tiro_jogador)
                    self._remover_tiro_jogador(tiro_jogador)  # Sincroniza com jogador
                    self.projeteis_inimigo.remove(tiro_inimigo)

                    # Adiciona bônus de interceptação via PontuacaoBusiness
                    # Demonstra SEPARAÇÃO DE RESPONSABILIDADES
                    pontuacao_business.adicionar_bonus_interceptacao()

                    break  # Sai do loop interno (tiro já foi removido)

    def verificar_colisoes_com_objetos(self, jogador, inimigos, pontuacao_business):
        """
        REGRA DE NEGÓCIO: Colisões de projéteis com jogador e inimigos

        LÓGICA IMPLEMENTADA:
        1. Tiros do jogador acertando inimigos:
           - Remove tiro e inimigo
           - Adiciona pontos baseado no tipo do inimigo

        2. Tiros dos inimigos acertando jogador:
           - Remove tiro
           - Jogador perde uma vida

        SEPARAÇÃO DE RESPONSABILIDADES:
        - ProjetilBusiness: detecta colisões
        - PontuacaoBusiness: gerencia pontuação e vidas

        Args:
            jogador (Jogador): Objeto jogador
            inimigos (list): Lista de inimigos
            pontuacao_business (PontuacaoBusiness): Para gerenciar pontuação
        """
        # ====================================================================
        # COLISÃO: Tiros do jogador acertando inimigos
        # ====================================================================
        for tiro in self.projeteis_jogador[:]:
            for inimigo in inimigos[:]:
                # Detecta colisão
                if tiro.rect.colliderect(inimigo.rect):
                    # Remove tiro
                    self.projeteis_jogador.remove(tiro)
                    self._remover_tiro_jogador(tiro)  # Sincroniza com jogador

                    # Remove inimigo
                    inimigos.remove(inimigo)

                    # Adiciona pontos via PontuacaoBusiness
                    # Pontos variam baseado no tipo do inimigo
                    pontuacao_business.adicionar_pontos_inimigo(inimigo.tipo)

                    break  # Tiro já foi removido

        # ====================================================================
        # COLISÃO: Tiros dos inimigos acertando jogador
        # ====================================================================
        for tiro in self.projeteis_inimigo[:]:
            # Detecta colisão com jogador
            if tiro.rect.colliderect(jogador.rect):
                # Remove tiro
                self.projeteis_inimigo.remove(tiro)

                # Jogador perde vida via PontuacaoBusiness
                pontuacao_business.perder_vida()

                break  # Tiro já foi removido

    # ========================================================================
    # MÉTODOS PRIVADOS - AUXILIARES
    # ========================================================================

    def _remover_tiro_jogador(self, projetil):
        """
        MÉTODO PRIVADO: Remove projétil da lista do jogador

        SINCRONIZAÇÃO:
        - Projétil está em duas listas: projeteis_jogador E jogador.tiros
        - Precisa remover de ambas para manter consistência

        ENCAPSULAMENTO:
        - Usa método público do Jogador: remover_tiro()

        Args:
            projetil (Projetil): Projétil a remover
        """
        if self.jogador:
            self.jogador.remover_tiro(projetil)
