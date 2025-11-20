from __future__ import annotations
import random
from models.inventario import Inventario  # ← necessário


class Aventureiro:
    def __init__(self, nome, vida, ataque, defesa, mana=0):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.defesa = defesa
        self.mana = mana
        self.mana_max = mana
        self.inventario = Inventario()  # ← corrigido
        self.nivel = 1
        self.xp = 0

    def get_ataque(self):
        return self.ataque

    def get_mana(self):
        return self.mana

    def set_mana(self, mana):
        self.mana = min(mana, self.mana_max)

    def get_inventario(self):
        return self.inventario

    def adicionar_item(self, item):
        self.inventario.adicionar_item(item)  # ← corrigido

    def remover_item(self, item):
        self.inventario.remover_item(item)  # ← corrigido

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        if self.vida < 0:
            self.vida = 0
            return False
        return True

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def calcular_dano_basico(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.receber_dano(dano)
        return dano

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        xp_para_proximo = self.nivel * 100

        if self.xp >= xp_para_proximo:
            self.xp -= xp_para_proximo
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.vida_max = int(self.vida_max * 1.10)
        self.ataque = int(self.ataque * 1.10)
        self.defesa = int(self.defesa * 1.10)
        self.mana_max = int(self.mana_max * 1.10)

        self.vida = self.vida_max
        self.mana = self.mana_max

    def usar_item(self, nome_item: str):
        """Tenta usar um item do inventário."""
        for item in self.inventario.itens:  # ← corrigido
            if item.nome.lower() == nome_item.lower():
                if hasattr(item, "usar"):
                    cura = item.usar(self)
                    self.inventario.remover_item(item)  # ← corrigido
                    return f"Você usou {item.nome} e recuperou {cura} de vida."
                return "Este item não pode ser usado."
        return "Item não encontrado no inventário."


class Guerreiro(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome, vida=120, ataque=15, defesa=10)
        self.pode_usar_habilidade = True

    def golpe_poderoso(self, alvo):
        dano_especial = self.get_ataque() * 1.5
        dano_final = max(0, dano_especial - (alvo.defesa / 2))
        alvo.receber_dano(dano_final)
        return dano_final

    def ataque_duplo(self, alvo):
        dano1 = self.calcular_dano_basico(alvo)
        dano2 = self.calcular_dano_basico(alvo)
        return dano1 + dano2

    def habilidade_especial(self, alvo):
        if not self.pode_usar_habilidade:
            return self.calcular_dano_basico(alvo)

        escolha = random.choice(["golpe", "duplo"])
        self.pode_usar_habilidade = False

        if escolha == "golpe":
            return self.golpe_poderoso(alvo)
        else:
            return self.ataque_duplo(alvo)

    def atacar(self, alvo):
        if self.pode_usar_habilidade:
            dano = self.habilidade_especial(alvo)
        else:
            dano = self.calcular_dano_basico(alvo)
            self.pode_usar_habilidade = True
        return dano


class Mago(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome, vida=80, ataque=10, defesa=5, mana=100)

    def bola_de_fogo(self, alvo):
        if self.mana < 20:
            return 0
        self.set_mana(self.mana - 20)
        dano = self.ataque * 2.5
        alvo.receber_dano(dano)
        return dano

    def raio_mistico(self, alvo):
        if self.mana < 10:
            return 0
        self.set_mana(self.mana - 10)
        dano = self.ataque * 1.5
        alvo.receber_dano(dano)
        return dano

    def habilidade_especial(self, alvo):
        escolha = random.choice(["fogo", "raio"])

        if escolha == "fogo":
            return self.bola_de_fogo(alvo)
        else:
            return self.raio_mistico(alvo)

    def atacar(self, alvo):
        dano = self.habilidade_especial(alvo)
        if dano > 0:
            return dano
        return self.calcular_dano_basico(alvo)


class Arqueiro(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome, vida=90, ataque=13, defesa=6, mana=40)

    def flecha_critica(self, alvo):
        dano = self.ataque * 2
        alvo.receber_dano(dano)
        return dano

    def chuva_de_flechas(self, alvo):
        total = 0
        for _ in range(3):
            dano = max(0, (self.ataque // 2) - alvo.defesa)
            alvo.receber_dano(dano)
            total += dano
        return total

    def atacar(self, alvo):
        escolha = random.choice(["critico", "chuva"])
        if escolha == "critico":
            return self.flecha_critica(alvo)
        return self.chuva_de_flechas(alvo)


class Ladrao(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome, vida=85, ataque=12, defesa=4, mana=30)

    def ataque_furtivo(self, alvo):
        dano = self.ataque * 2.2
        alvo.receber_dano(dano)
        return dano

    def cortar_garganta(self, alvo):
        dano = self.ataque * 1.2
        alvo.receber_dano(dano)
        return dano

    def atacar(self, alvo):
        chance = random.random()
        if chance < 0.35:
            return self.ataque_furtivo(alvo)
        return self.cortar_garganta(alvo)
