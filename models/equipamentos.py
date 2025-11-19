class PocaoDeVida:
    def __init__(self, cura=50):
        self.nome = "Poção de Vida"
        self.cura = cura

    def usar(self, jogador):
        """Restaura a vida do jogador até o máximo permitido."""
        vida_antes = jogador.atributos.vida
        jogador.atributos.vida = min(
            jogador.atributos.vida + self.cura,
            jogador.atributos.vida_max
        )
        return jogador.atributos.vida - vida_antes