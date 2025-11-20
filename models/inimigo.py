from __future__ import annotations
from .base import Entidade


class Inimigo(Entidade):
    def __init__(self, nome, vida, ataque, defesa, efeitos, nome_ataque, drop_item):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.efeitos = {"Sangramento": {"dano": 2, "turnos": 3}}
        self.nome_ataque = nome_ataque
        self drop_item = drop_item

        self.tabela_drop = [
            {"item:" Item("Poção de Vida", 30), "chance:" 50},
            {"item:" Item("Poção Forte", 60), "chance:" 25},
            {"item:" Item("Moeda Antiga", 0), "chance:" 10},
            {"item:" Item("Adaga do ladrão", 1), "chance:" 33},
            {"item:" Item("Chifre do demônio", 1), "chance:" 12}
        ]

    def calcular_dano_base(self):

        return self.ataque

    def receber_dano(self, dano):

        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final

        if self.vida < 0:
            self.vida = 0

            return dano_final

    def esta_vivo(self):

        return self.vida > 0


    def tabela_drop(self)
        return self._tabela_drop


class Goblin(Inimigo):

    def __init__(self, nome, nome_ataque):

        super.__init__(
            nome="Goblin", vida=100, ataque=7, defesa=7, nome_ataque="Furia Goblin"
        )

    def habilidade_especial(self, alvo):

        if self.defesa == 7:

            self.defesa -= 2
            self.ataque += 2
            print(
                "{self.nome} usou {self.nome_ataque}, ao usar seu poder seu ataque ficou pra {self.ataque} e sua defesa {self.defesa} ."
            )

        else:
            print("{self.nome} sentiu medo do oponente e fugiu da batalha.")

            return self.ataque


class Ladrao(Inimigo):

    def __init__(self, nome, nome_ataque):

        super.__init__(
            nome="Ladrão", vida=100, ataque=11, defesa=3, nome_ataque="Disparo de adaga"
        )

    def habilidade_especial(self, alvo):

        if self.ataque == 11:

            print("{self.nome} usou {self.nome_ataque} . ")
            return self.ataque * 2

        else:
            print("{self.nome} Fugiu da batalha!")


class Golen(Inimigo):

    def __init__(self, nome, nome_ataque):
        super.__init__(
            nome="Golen", vida=100, ataque=20, defesa=15, nome_ataque="Soco de pedra"
        )

    def habilidade_especial(self, alvo):

        if self.ataque == 20:
            print("{self.nome} usou {self.nome_ataque} .")

            return self.ataque

        else:

            print("{self.nome} fugiu da batalha")


class Demonio(Inimigo):
    def __init__(self, nome, nome_ataque):

        super.__init__(
            nome="Trigon",
            vida=100,
            ataque=50,
            defesa=50,
            nome_ataque="Passeio no inferno",
        )

    def habilidade_especial(self, alvo):

        if self.ataque == 50:
            print("{self.nome} usou {self.nome_ataque} .")

            return self.ataque    
        