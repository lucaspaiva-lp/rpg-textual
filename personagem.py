from __future__ import annotations
import random
from typing import Optional, List, Tuple


class Aventureiro:
    def __init__(self, nome: str, vida: int, ataque: float, defesa: float, mana: float):
        self._nome = nome
        self._vida_max = int(vida)
        self._vida = int(vida)
        self._ataque = float(ataque)
        self._defesa = float(defesa)
        self._mana_max = float(mana)
        self._mana = float(mana)
        self._nivel = 1
        self._xp = 0
        self._xp_para_prox = 100
        self._habilidades: List[str] = []
        self._ponto_habilidade = False
        self._cooldowns: dict[str, int] = {}
        self._flags: dict[str, bool] = {}
        self._dots: List[Tuple[int, int]] = []

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def vida(self) -> int:
        return int(self._vida)

    @vida.setter
    def vida(self, valor: int):
        self._vida = max(0, int(valor))

    @property
    def vida_max(self) -> int:
        return int(self._vida_max)

    @vida_max.setter
    def vida_max(self, valor: int):
        self._vida_max = max(1, int(valor))

    @property
    def ataque(self) -> float:
        return float(self._ataque)

    @ataque.setter
    def ataque(self, valor: float):
        self._ataque = max(0.0, float(valor))

    @property
    def defesa(self) -> float:
        return float(self._defesa)

    @defesa.setter
    def defesa(self, valor: float):
        self._defesa = max(0.0, float(valor))

    @property
    def mana(self) -> float:
        return float(self._mana)

    @mana.setter
    def mana(self, valor: float):
        self._mana = max(0.0, float(valor))

    @property
    def mana_max(self) -> float:
        return float(self._mana_max)

    @mana_max.setter
    def mana_max(self, valor: float):
        self._mana_max = max(0.0, float(valor))

    @property
    def nivel(self) -> int:
        return int(self._nivel)

    @nivel.setter
    def nivel(self, valor: int):
        if valor < 1:
            return
        self._nivel = int(valor)

    @property
    def xp(self) -> int:
        return int(self._xp)

    @xp.setter
    def xp(self, valor: int):
        self._xp = max(0, int(valor))

    @property
    def habilidades(self) -> List[str]:
        return list(self._habilidades)

    @property
    def ponto_habilidade(self) -> bool:
        return bool(self._ponto_habilidade)

    @property
    def cooldowns(self) -> dict:
        return dict(self._cooldowns)

    def calcular_dano_base(self) -> int:
        base = int(self._ataque + random.randint(-2, 2))
        return max(0, base)

    def chance_critico(self) -> float:
        return 0.0

    def pode_critar(self) -> bool:
        return True

    def tentar_critico(self) -> bool:
        if not self.pode_critar():
            return False
        return random.random() < self.chance_critico()

    def aplicar_critico(self, dano: int) -> int:
        if self.tentar_critico():
            self._flags["ultimo_critico"] = True
            return int(dano * 2)
        self._flags["ultimo_critico"] = False
        return int(dano)

    def receber_dano(self, dano: float) -> int:
        reducao = self._defesa / 2
        dano_final = max(0, dano - reducao)
        self._vida -= int(dano_final)
        if self._vida < 0:
            self._vida = 0
        return int(dano_final)

    def receber_dano_ignora_defesa(self, dano: float) -> int:
        dano_final = max(0, dano)
        self._vida -= int(dano_final)
        if self._vida < 0:
            self._vida = 0
        return int(dano_final)

    def aplicar_dots(self):
        novos: List[Tuple[int, int]] = []
        for dano, turnos in self._dots:
            if turnos > 0:
                self.receber_dano(dano)
                if turnos - 1 > 0:
                    novos.append((dano, turnos - 1))
        self._dots = novos

    def reduzir_cooldowns(self):
        chaves = list(self._cooldowns.keys())
        for k in chaves:
            if self._cooldowns[k] > 0:
                self._cooldowns[k] -= 1
            if self._cooldowns[k] <= 0:
                del self._cooldowns[k]

    def ganhar_xp(self, qtd: int):
        self._xp += int(qtd)
        while self._xp >= self._xp_para_prox:
            self._xp -= self._xp_para_prox
            self.subir_nivel()

    def subir_nivel(self):
        self._nivel += 1
        self._ataque *= 1.1
        self._defesa *= 1.1
        self._mana_max *= 1.1
        self._mana = int(self._mana_max)
        self._vida_max = int(self._vida_max * 1.1)
        self._vida = int(self._vida_max)
        self._xp_para_prox = self._nivel * 100
        if self._nivel % 5 == 0:
            self._ponto_habilidade = True

    def escolher_habilidade(self, nome: str) -> bool:
        nome = nome.lower()
        if not self._ponto_habilidade:
            return False
        if nome in self._habilidades:
            return False
        self._habilidades.append(nome)
        self._ponto_habilidade = False
        return True

    def usar_habilidade(self, nome: str, alvo: Optional['Aventureiro'] = None, **kwargs):
        raise NotImplementedError


class Guerreiro(Aventureiro):
    class Summon:
        def __init__(self, dono: 'Guerreiro', duracao: int):
            self.dono = dono
            self.turnos = duracao
            self.dano_por_turno = int(dono.ataque * 0.5)

        def tick(self, inimigo: Aventureiro) -> bool:
            if self.turnos <= 0:
                return False
            inimigo.receber_dano(self.dano_por_turno)
            self.turnos -= 1
            return self.turnos > 0

    def __init__(self, nome: str):
        super().__init__(nome, vida=180, ataque=25, defesa=12, mana=40)
        self._cooldowns = {
            "ataque_duplo": 0,
            "fortificacao": 0,
            "ataque_de_cima": 0,
            "levantar_defesas": 0,
            "contra_ataque": 0,
            "tudo_ou_nada": 0,
            "invocar_tropa": 0,
            "ponto_vital": 0,
        }
        self._turnos_fortificacao = 0
        self._fortificacao_bonus = 15
        self._berserker_ativo = False
        self._vontade_de_ferro_ativa = True
        self._soldier: Optional[Guerreiro.Summon] = None
        self._flags["ultimo_critico"] = False

    def chance_critico(self) -> float:
        return 0.20

    def receber_dano(self, dano: float) -> int:
        if self._turnos_fortificacao > 0:
            reducao = self._defesa
            dano_final = max(0, dano - reducao)
            self._vida -= int(dano_final)
            if self._vida < 0:
                self._vida = 0
        elif self._berserker_ativo:
            dano_final = max(0, dano)
            self._vida -= int(dano_final)
            if self._vida < 0:
                self._vida = 0
        else:
            return super().receber_dano(dano)
        if self._vida <= 0 and self._vontade_de_ferro_ativa and "vontade_de_ferro" in self._habilidades:
            self._vontade_de_ferro_ativa = False
            self._vida = int(self._vida_max * 0.25)
            self._mana = 0.0
        return int(dano_final)

    def usar_habilidade(self, nome: str, alvo: Optional[Aventureiro] = None, **kwargs):
        key = nome.lower()
        if key == "ataque_duplo":
            return self._ataque_duplo(alvo, kwargs.get("modo_forte", False))
        if key == "fortificacao":
            return self._fortificacao()
        if key == "berserker":
            return self._berserker()
        if key in ("vontade_de_ferro", "vontade de ferro"):
            return None
        if key == "ataque_de_cima":
            return self._ataque_de_cima(alvo)
        if key == "levantar_defesas":
            return self._levantar_defesas()
        if key == "contra_ataque":
            return self._contra_ataque(alvo)
        if key == "ponto_vital":
            return self._ponto_vital(alvo)
        if key == "invocar_tropa":
            return self._invocar_tropa()
        if key == "tudo_ou_nada":
            return self._tudo_ou_nada(alvo)
        raise ValueError("Habilidade desconhecida")

    def _ataque_duplo(self, alvo: Optional[Aventureiro], modo_forte: bool = False):
        if self._cooldowns.get("ataque_duplo", 0) > 0:
            return 0
        if modo_forte:
            custo = 20
            dano = int(self._ataque * 1.8)
            if self._mana < custo:
                return 0
            self._mana -= custo
            self._cooldowns["ataque_duplo"] = 1
            total = 0
            if alvo:
                alvo.receber_dano(dano)
                alvo.receber_dano(dano)
                total = int(dano * 2)
            return total
        else:
            custo = 5
            if self._mana < custo:
                return 0
            self._mana -= custo
            self._cooldowns["ataque_duplo"] = 1
            total = 0
            if alvo:
                d1 = int(self._ataque)
                d2 = int(self._ataque)
                alvo.receber_dano(d1)
                alvo.receber_dano(d2)
                total = d1 + d2
            return total

    def _fortificacao(self):
        if "fortificacao" not in self._habilidades:
            return False
        if self._cooldowns.get("fortificacao", 0) > 0:
            return False
        if self._berserker_ativo:
            return False
        custo = 10
        if self._mana < custo:
            return False
        self._mana -= custo
        self._defesa += self._fortificacao_bonus
        self._turnos_fortificacao = 3
        self._cooldowns["fortificacao"] = 5
        return True

    def _berserker(self):
        if "berserker" not in self._habilidades:
            return False
        if "fortificacao" in self._habilidades:
            return False
        if self._berserker_ativo:
            return False
        original_def = self._defesa
        self._defesa = 0.0
        self._ataque += original_def * 0.5
        self._berserker_ativo = True
        return True

    def _ataque_de_cima(self, alvo: Optional[Aventureiro]):
        if self._cooldowns.get("ataque_de_cima", 0) > 0:
            return 0
        custo = 15
        if self._mana < custo:
            return 0
        self._mana -= custo
        self._cooldowns["ataque_de_cima"] = 2
        if random.random() < 0.60:
            return 0
        dano = int(self._ataque * 2)
        if alvo:
            alvo.receber_dano(dano)
        self._flags["ultimo_critico"] = True
        return dano

    def _levantar_defesas(self):
        if self._cooldowns.get("levantar_defesas", 0) > 0:
            return False
        custo = 5
        if self._mana < custo:
            return False
        self._mana -= custo
        self._flags["bloqueia_turno"] = True
        self._cooldowns["levantar_defesas"] = 1
        return True

    def _contra_ataque(self, alvo: Optional[Aventureiro]):
        if self._cooldowns.get("contra_ataque", 0) > 0:
            return False
        custo = 25
        if self._mana < custo:
            return False
        if not alvo:
            return False
        self._mana -= custo
        self._cooldowns["contra_ataque"] = 3
        esperado = max(0, alvo.ataque - (alvo.defesa / 2))
        dano_retorno = int(min(self._ataque, esperado))
        alvo.receber_dano(dano_retorno)
        return dano_retorno

    def _ponto_vital(self, alvo: Optional[Aventureiro]):
        if "ponto_vital" not in self._habilidades:
            return 0
        if not self._flags.get("ultimo_critico", False):
            return 0
        custo = 20
        if self._mana < custo:
            return 0
        if not alvo:
            return 0
        self._mana -= custo
        dano_extra = int(self._ataque * 0.5)
        alvo.receber_dano(dano_extra)
        return dano_extra

    def _invocar_tropa(self):
        if self._cooldowns.get("invocar_tropa", 0) > 0:
            return False
        if self._soldier and self._soldier.turnos > 0:
            return False
        self._soldier = Guerreiro.Summon(self, 5)
        self._cooldowns["invocar_tropa"] = 6
        return True

    def _tudo_ou_nada(self, alvo: Optional[Aventureiro]):
        if self._cooldowns.get("tudo_ou_nada", 0) > 0:
            return 0
        custo = 30
        if self._mana < custo:
            return 0
        if not alvo:
            return 0
        self._mana -= custo
        self._cooldowns["tudo_ou_nada"] = 3
        total = 0
        for _ in range(3):
            dano = int(self._ataque)
            alvo.receber_dano(dano)
            total += dano
        recebido = int(total * 0.5)
        self._vida -= recebido
        if self._vida < 0:
            self._vida = 0
        return total


class Mago(Aventureiro):
    class Summon:
        def __init__(self, tipo: str, dono: 'Mago'):
            self.tipo = tipo
            self.dono = dono
            self.turnos = 3
            if tipo == "elefante":
                self.hp = int(dono.vida_max * 0.5)
            else:
                self.hp = None
            self.dano_por_turno = 0
            if tipo == "tigre":
                self.dano_por_turno = int(dono.ataque * 0.5)
            if tipo == "vespa":
                self.dano_por_turno = int(dono.ataque * 0.25)

        def tick(self, inimigo: Aventureiro) -> bool:
            if self.turnos <= 0:
                return False
            if self.tipo == "elefante":
                self.turnos -= 1
                return self.turnos > 0
            if self.tipo == "tigre":
                inimigo.receber_dano(self.dano_por_turno)
            if self.tipo == "vespa":
                for _ in range(3):
                    dano = self.dano_por_turno
                    if random.random() < 0.5:
                        dano *= 2
                    inimigo.receber_dano(int(dano))
            self.turnos -= 1
            return self.turnos > 0

        def sofre_dano(self, valor: float) -> bool:
            if self.tipo != "elefante":
                return False
            self.hp -= int(valor)
            if self.hp <= 0:
                return True
            return False

    def __init__(self, nome: str):
        super().__init__(nome, vida=120, ataque=15, defesa=8, mana=120)
        self._cooldowns = {
            "raio_mistico": 0,
            "mare_de_fogo": 0,
            "meteorito": 0,
            "raio_congelante": 0,
            "invocar_ser": 0,
            "escudo_magico": 0,
        }
        self._dano_continuo = 0
        self._turnos_fogo = 0
        self._armadura_arcana_ativa = False
        self._summon: Optional[Mago.Summon] = None
        self._escudo_ativo = False
        self._flags["raio_congelante_ativo"] = False
        self._flags["ultimo_critico"] = False
        self._visao_do_futuro = False

    def chance_critico(self) -> float:
        return 0.10

    def iniciar_passivas(self):
        if "saber_e_poder" in self._habilidades:
            self._ataque += self._ataque * 0.5
        if "visao_do_futuro" in self._habilidades:
            self._visao_do_futuro = True

    def receber_dano(self, dano: float) -> int:
        if self._summon and self._summon.tipo == "elefante" and self._summon.hp and self._summon.hp > 0:
            morto = self._summon.sofre_dano(dano)
            if morto:
                self._summon = None
            return 0
        if getattr(self, "_escudo_ativo", False):
            self._escudo_ativo = False
            return 0
        if self._flags.get("raio_congelante_ativo", False):
            self._flags["raio_congelante_ativo"] = False
            return super().receber_dano(dano * 0.5)
        return super().receber_dano(dano)

    def usar_habilidade(self, nome: str, alvo: Optional[Aventureiro] = None, **kwargs):
        key = nome.lower()
        if key == "raio_mistico":
            return self._raio_mistico(alvo)
        if key == "mare_de_fogo":
            return self._mare_de_fogo(alvo)
        if key == "armadura_arcana":
            return self._armadura_arcana()
        if key == "cortar":
            return self._cortar(alvo)
        if key == "meteorito":
            return self._meteorito(alvo)
        if key == "raio_congelante":
            return self._raio_congelante()
        if key == "invocar_ser":
            return self._invocar_ser(kwargs.get("tipo", "elefante"))
        if key == "escudo_magico":
            return self._escudo_magico()
        if key == "saber_e_poder":
            return None
        if key == "visao_do_futuro":
            return None
        raise ValueError("Habilidade desconhecida")

    def _raio_mistico(self, alvo: Optional[Aventureiro]):
        if self._cooldowns.get("raio_mistico", 0) > 0:
            return 0
        custo = 15
        if self._mana < custo:
            return 0
        self._mana -= custo
        self._cooldowns["raio_mistico"] = 1
        dano = int(self._ataque * 1.2)
        if alvo:
            alvo.receber_dano_ignora_defesa(dano)
        return dano

    def _mare_de_fogo(self, alvo: Optional[Aventureiro]):
        if self._cooldowns.get("mare_de_fogo", 0) > 0:
            return 0
        custo = 20
        if self._mana < custo:
            return 0
        self._mana -= custo
        self._cooldowns["mare_de_fogo"] = 3
        dano_inicial = int(self._ataque * 0.7)
        dano_dot = int(self._ataque * 0.4)
        if alvo:
            alvo.receber_dano(dano_inicial)
            alvo._dots.append((dano_dot, 2))
        return dano_inicial

    def _armadura_arcana(self):
        if "armadura_arcana" not in self._habilidades:
            return False
        if self._armadura_arcana_ativa:
            return False
        custo = 30
        if self._mana < custo:
            return False
        self._mana -= custo
        bonus = int(self._ataque * 0.5)
        self._defesa += bonus
        self._armadura_arcana_ativa = True
        return True

    def _cortar(self, alvo: Optional[Aventureiro]):
        if self._cooldowns.get("cortar", 0) > 0:
            return 0
        custo = 20
        if self._mana < custo:
            return 0
        self._mana -= custo
        self._cooldowns["cortar"] = 6
        dano_por_turno = int(self._ataque * 0.4)
        if alvo:
            alvo._dots.append((dano_por_turno, 5))
        return dano_por_turno

    def _meteorito(self, alvo: Optional[Aventureiro]):
        if self._cooldowns.get("meteorito", 0) > 0:
            return 0
        custo = 45
        if self._mana < custo:
            return 0
        self._mana -= custo
        self._cooldowns["meteorito"] = 3
        dano = int(self._ataque * 4)
        if alvo:
            alvo.receber_dano(dano)
        return dano

    def _raio_congelante(self):
        if self._cooldowns.get("raio_congelante", 0) > 0:
            return False
        custo = 20
        if self._mana < custo:
            return False
        self._mana -= custo
        self._cooldowns["raio_congelante"] = 2
        self._flags["raio_congelante_ativo"] = True
        return True

    def _invocar_ser(self, tipo: str):
        if self._cooldowns.get("invocar_ser", 0) > 0:
            return False
        custo = 30
        if self._mana < custo:
            return False
        if type(tipo) is not str or tipo not in ("elefante", "tigre", "vespa"):
            return False
        self._mana -= custo
        self._cooldowns["invocar_ser"] = 5
        self._summon = Mago.Summon(tipo, self)
        if tipo == "elefante":
            self._vida += int(self._vida_max * 0.5)
            if self._vida > self._vida_max:
                self._vida = self._vida_max
        return True

    def _escudo_magico(self):
        if self._cooldowns.get("escudo_magico", 0) > 0:
            return False
        custo = 10
        if self._mana < custo:
            return False
        self._mana -= custo
        self._cooldowns["escudo_magico"] = 1
        self._escudo_ativo = True
        return True
