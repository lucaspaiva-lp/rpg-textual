from __future__ import annotations
from .base import Entidade, Atributos


class Inimigo(Entidade):
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int):
        super().__init__(nome, Atributos(vida=vida, ataque=ataque, defesa=defesa, vida_max=vida))

    def get_vida(self):
        return self._atrib.vida

    def set_vida(self, nova_vida: int) -> None:
            self._atrib.vida = nova_vida


    def get_ataque(self):
        return self._atrib.ataque
    
    def set_ataque(self,novo_ataque):
        self._atrib.ataque = novo_ataque
    

    def get_defesa(self):
        return self._atrib.defesa
    
    def set_defesa(self,nova_defesa):
        self._atrib.defesa = nova_defesa
     
    def receber_dano(self, dano):
        dano_final = max(0, dano - self._atrib.defesa)
        self._atrib.vida -= dano_final

        if self._atrib.vida <0:
             self._atrib.vida = 0
        return dano_final
               
    def esta_vivo(self):
        return self._atrib.vida > 0
     
class goblin(Inimigo):
    def __init__(self, nome):
        super().__init__(nome, vida = 90, ataque = 5, defesa = 7)
    def furia(self):
        self._atrib.defesa()
        self.set_defesa(nova_defesa = - 2)
        self._atrib.ataque()
        self.set_ataque(novo_ataque = + 2)

    #Furia goblin: o goblin se enfurece reduzindo sua defesa em -2 , e aumentando seu ataque em +2.
 

class ladrao(Inimigo):
    def __init__(self, nome):
        super().__init__(nome, vida = 110, ataque = 11, defesa = 3)
   
    # Disparo de Adaga: o ladrao arremessa uma de suas adagas
    # acertando o seu alvo e causando sangramento de -2 de hp por turno
   

    

