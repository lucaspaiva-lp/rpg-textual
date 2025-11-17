from __future__ import annotations
from .base import Entidade, Atributos


class Inimigo(Entidade):
    class inimigo:
    def_init_(self,nome, vida, ataque, defesa, efeitos):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.efeitos = {"sangramento": {"dano": 2, "turnos": 3}}


    def calcular_dano_base(self):
        return self.ataque
     
    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        if self.vida <0:
        self.vida = 0
        return dano_final
               
    def esta_vivo(self):
        return self.vida > 0
     
class goblin(Inimigo):
    def_init_(self, nome):
        super()._init_(nome, vida = 90, ataque = 7, defesa = 7)
        
    def habilidade_especial(self, alvo):
    #Furia goblin: o goblin se enfurece reduzindo sua defesa em -2 , e aumentando seu ataque em +2.
    if  self.defesa = 7:
        self.defesa -= 2
        self.ataque += 2
        
    def alvo.receber_dano(ataque)
    return self.ataque

class ladrao(Inimigo):
    def_init_(self, nome):
        super()._init_(nome, vida = 110, ataque = 11, defesa = 3)
    def_habilidade_especial(self, alvo):
    # Disparo de Adaga: o ladrao arremessa uma de suas adagas
    # acertando o seu alvo e causando sangramento de -2 de hp por turno
    dano_base

    def __init__(self, nome: str, vida: int, ataque: int, defesa: int):
        super().__init__(nome, Atributos(vida=vida, ataque=ataque, defesa=defesa, vida_max=vida))

