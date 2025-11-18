# ============================================
# PERSONAGENS DO JOGO (versão estável)
# ============================================


class Aventureiro:
    """
    Classe base usada pelo SEU jogo.
    Todos os personagens jogáveis herdam dela.
    """

    def __init__(self, nome: str, vida: int, ataque: int, defesa: int, mana: int = 0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.mana = mana

        # Inventário é fundamental para evitar o erro no salvamento
        self.inventario: list = []

    # -------------------------
    # GETTERS E UTILIDADES
    # -------------------------

    def get_ataque(self) -> int:
        return self.ataque

    def get_mana(self) -> int:
        return self.mana

    def set_mana(self, valor: int) -> None:
        self.mana = valor

    def get_inventario(self) -> list:
        return self.inventario

    # -------------------------
    # INVENTÁRIO
    # -------------------------

    def adicionar_item(self, item):
        self.inventario.append(item)

    def remover_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)

    # -------------------------
    # COMBATE
    # -------------------------

    def receber_dano(self, dano: float) -> bool:
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final

        if self.vida <= 0:
            self.vida = 0
            return False
        return True

    def esta_vivo(self) -> bool:
        return self.vida > 0


# ============================================
#           CLASSES ESPECÍFICAS
# ============================================


class Guerreiro(Aventureiro):
    """
    Personagem focado em força e defesa.
    Golpe Especial: golpe poderoso com mitigação parcial da defesa do inimigo.
    """

    def __init__(self, nome: str):
        super().__init__(nome, vida=120, ataque=15, defesa=10)

    def habilidade_especial(self, alvo: Aventureiro) -> float:
        dano = self.ataque * 1.5
        dano_final = max(0, dano - (alvo.defesa * 0.5))
        alvo.receber_dano(dano_final)
        return dano_final


class Mago(Aventureiro):
    """
    Personagem focado em mana e dano mágico.
    Golpe Especial: feitiço de alto dano que custa mana.
    """

    def __init__(self, nome: str):
        super().__init__(nome, vida=80, ataque=10, defesa=5, mana=100)

    def habilidade_especial(self, alvo: Aventureiro) -> float:
        if self.mana < 20:
            print("⚠ Mana insuficiente para lançar magia especial!")
            return 0

        self.mana -= 20
        dano_magico = self.ataque * 2.5
        alvo.receber_dano(dano_magico)
        return dano_magico
