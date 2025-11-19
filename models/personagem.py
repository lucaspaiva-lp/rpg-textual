from models.inventario import Inventario, Item

# ============================================
# CLASSE BASE
# ============================================


class Aventureiro:
    """
    Classe base para todos os personagens jogáveis.
    Contém atributos comuns, inventário, métodos de combate e utilidades.
    """

    def __init__(self, nome: str, vida: int, ataque: int, defesa: int, mana: int = 0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.mana = mana

        # Inventário integrado
        self.inventario = Inventario()

    # -------------------------
    # COMBATE
    # -------------------------

    def receber_dano(self, dano: float) -> bool:
        """Aplica dano considerando defesa. Retorna False se morreu."""
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        if self.vida <= 0:
            self.vida = 0
            return False
        return True

    def esta_vivo(self) -> bool:
        return self.vida > 0

    # -------------------------
    # INVENTÁRIO
    # -------------------------

    def adicionar_item(self, item: Item):
        self.inventario.adicionar_item(item)

    def remover_item(self, item: Item):
        self.inventario.remover_item(item)

    def listar_inventario(self):
        return self.inventario.itens


# ============================================
# CLASSES ESPECÍFICAS
# ============================================


class Guerreiro(Aventureiro):
    """
    Personagem focado em vida, ataque físico e defesa.
    Golpe especial: dano aumentado com mitigação parcial da defesa do inimigo.
    """

    def __init__(self, nome: str):
        super().__init__(nome, vida=120, ataque=15, defesa=10, mana=0)
        # Inventário inicial com poções
        self.inventario.adicionar_item(Item("Poção de Cura", 30))
        self.inventario.adicionar_item(Item("Poção de Cura", 30))

    def habilidade_especial(self, alvo: Aventureiro) -> float:
        dano = self.ataque * 1.5
        dano_final = max(0, dano - (alvo.defesa * 0.5))
        alvo.receber_dano(dano_final)
        return dano_final


class Mago(Aventureiro):
    """
    Personagem focado em mana e dano mágico.
    Golpe especial: feitiço poderoso que consome mana.
    """

    def __init__(self, nome: str):
        super().__init__(nome, vida=80, ataque=10, defesa=5, mana=100)
        # Inventário inicial com poções
        self.inventario.adicionar_item(Item("Poção de Cura", 30))
        self.inventario.adicionar_item(Item("Poção de Cura", 30))

    def habilidade_especial(self, alvo: Aventureiro) -> float:
        if self.mana < 20:
            print("⚠ Mana insuficiente para lançar magia especial!")
            return 0
        self.mana -= 20
        dano_magico = self.ataque * 2.5
        alvo.receber_dano(dano_magico)
        return dano_magico
