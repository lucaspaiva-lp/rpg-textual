from __future__ import annotations


class Inimigo:
    def __init__(self, nome, vida, ataque, defesa, nome_ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.nome_ataque = nome_ataque

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        if self.vida < 0:
            self.vida = 0
        return dano_final

    def esta_vivo(self):
        return self.vida > 0

    def calcular_ataque(self):
        return self.ataque


# ===========================================================
# INIMIGOS ESPECÍFICOS
# ===========================================================


class Goblin(Inimigo):
    def __init__(self):
        super().__init__(
            nome="Goblin", vida=60, ataque=8, defesa=3, nome_ataque="Fúria Goblin"
        )


class Ladrao(Inimigo):
    def __init__(self):
        super().__init__(
            nome="Ladrão", vida=80, ataque=11, defesa=2, nome_ataque="Disparo de Adaga"
        )


class Golem(Inimigo):
    def __init__(self):
        super().__init__(
            nome="Golem", vida=120, ataque=16, defesa=10, nome_ataque="Soco de Pedra"
        )


class Demonio(Inimigo):
    def __init__(self):
        super().__init__(
            nome="Demônio", vida=150, ataque=22, defesa=12, nome_ataque="Chama Profunda"
        )
