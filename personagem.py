from __future__ import annotations
from .base import Entidade, Atributos
import random


class Personagem(Entidade):
    """
    Classe base única do jogador.
    Esta versão NÃO implementa a lógica principal de combate.
    """
    def __init__(self, nome: str, atrib: Atributos):
        super().__init__(nome, atrib)
        self.nivel = 1
        self.xp = 0

    def calcular_dano_base(self) -> int:
        """
        Deve retornar um inteiro com o dano base do personagem.
        (ex.: usar self._atrib.ataque, aplicar aleatoriedade/crítico/etc.)
        """
        dano = self._atrib.ataque + random.randint(-2, 2)
        critico = random.random() < 0.1
        if critico:
            dano*=2
        return max(0, int(dano))

    def habilidade_especial(self) -> int:
        """
        Deve retornar dano especial (ou 0 se indisponível).
        (ex.: consumir self._atrib.mana e aplicar bônus de dano)
        """
        if self._atrib.mana >=10:
            self._atrib.mana -=10
            dano = self._atrib.ataque *1.5
            return int(dano)
        return 0


class Aventureiro:
    def __init__(self, nome, vida, vida_max, ataque, defesa, mana=0):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida_max
        self.ataque = ataque
        self.defesa = defesa
        self.mana = mana
        self.inventario = []
# GETTERS E SETTERS
    def get_vida(self):
        return self.vida

    def set_vida(self, vida:int):
        self._vida = vida
        return None
    def get_ataque(self):
        return self.ataque

    def set_ataque(self, valor):
        self._ataque=valor

    def get_defesa(self):
        return self.defesa

    def set_defesa(self, valor):
        self._defesa=valor

    def get_mana(self):
        return self.mana

    def set_mana(self, valor):
        self._mana = max(0, valor)

    def get_inventario(self):
        return self.inventario

#-----------------------------------

    def adicionar_item(self, item):
        self.inventario.append(item)

    def remover_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)

    def calcular_dano_base(self):
        return self.get_ataque()

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -=dano_final
        if self.vida < 0:
            self.vida=0
            return False
        return True



    def esta_vivo(self):
        return self.vida() > 0


class Guerreiro(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome, vida=20, vida_max=20, ataque=5, defesa=8, mana=0)


    def habilidade_especial(self, alvo):
        # Golpe poderoso: ignora metade da defesa do alvo

        dano_base = self.get_ataque()
        dano_especial = dano_base * 1.5
        dano_final = max(0, dano_especial - (alvo.get_defesa()/2))
        alvo.receber_dano(dano_final)
        return dano_final




class Mago(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome, vida=12, vida_max=12, ataque=5, defesa=5, mana=20)

    def habilidade_especial(self, alvo):
        # Bola de fogo: consome 20 de mana e causa alto dano mágico
        mana = self.get_mana()
        ataque = self.get_ataque()
        if self.get_mana()>=10:
            mana -= 2
            self.set_mana(mana)
            dano_magico = ataque() * 2.5
            alvo.receber_dano(dano_magico)
            return dano_magico
        else:
            return 0 #sem mana suficiente

    # HABILIDADES DE CURA DE MANA E DE VIDA
    def cura_vida(self):
        mana = self.get_mana()
        vida = self.get_vida()
        if vida >0 and vida <12 and mana >= 20: # verifica se está com vida compatível
            vida+=3 # mais 3 pontos de vida
            mana -= 8 #ao custo de 8pts de mana
            self.set_mana(mana)
            self.set_vida(vida)
        else:
            return 0

    def cura_mana(self):
        mana = self.get_mana()
        vida = self.get_vida()
        if vida > 4 and vida <= 12 and mana >= 0 and mana <=20: #precisa de hp entre 4 e 12 e mana entre 0 e 20 para curar mana
            mana+=5 # mais 5 pts de mana
            vida-=2 #ao custo de 2pts de HP
            self.set_mana(mana)
            self.set_vida(vida)
        else:
            return 0






