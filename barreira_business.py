from barreira import Barreira

class BarreiraBusiness:
    def __init__(self, barreiras):
        self.barreiras = barreiras

    def dano_barreira(self, barreira):
        barreira.vida -= 1
        if barreira.vida <= 0:
            self.barreiras.remove(barreira)