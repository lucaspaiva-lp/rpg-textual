from __future__ import annotations
from .base import Entidade, Atributos


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
        raise NotImplementedError("Implementar cálculo de dano base do Personagem.")

    def habilidade_especial(self) -> int:
        """
        Deve retornar dano especial (ou 0 se indisponível).
        (ex.: consumir self._atrib.mana e aplicar bônus de dano)
        """
        raise NotImplementedError("Implementar habilidade especial do Personagem.")



        class Aventureiro:
    def init(self, nome, vida, ataque, defesa, mana=0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.mana = mana
        self.inventario = []
        
    def get_ataque(self) -> int:
        return self.ataque
    
    def get_mana(self) -> int:
        return self.mana
    
    def set_mana(self, mana) -> None:
        self.mana = mana
    
    def get_inventario(self) -> list:
        return self.inventario
    
    def adicionar_item(self, item):
        self.inventario.append(item)

    def remover_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)

    def receber_dano(self, dano) -> bool:
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        # Se tiver vida retorn True se não retorna False
        if self.vida < 0:
            self.vida = 0
            return False
        return True

    def esta_vivo(self):
        return self.vida > 0


class Guerreiro(Aventureiro):
    def init(self, nome):
        super().init(nome, vida=120, ataque=15, defesa=10)

    def habilidade_especial(self, alvo:Aventureiro):
        # Golpe poderoso: ignora metade da defesa do alvo
        dano_base = self.get_ataque()
        dano_especial = dano_base * 1.5
        dano_final = max(0, dano_especial - (alvo.defesa/2))
        alvo.receber_dano(dano_final)
        return dano_final

class Mago(Aventureiro):
    def init(self, nome):
        super().init(nome, vida=80, ataque=10, defesa=5, mana=100)

    def habilidade_especial(self, alvo:Aventureiro):
        # Bola de fogo: consome 20 de mana e causa alto dano mágico
        mana = self.get_mana()
        ataque = self.get_ataque()
        if mana >=20:
            mana -= 20
            self.set_mana(mana)
            dano_magico = ataque * 2.5
            alvo.receber_dano(dano_magico)
            return dano_magico
        else:
            return 0 #sem mana suficiente
