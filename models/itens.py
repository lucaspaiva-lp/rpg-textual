from models.inventario import Item


class PocaoCura(Item):
    def __init__(self):
        super().__init__("Poção de Cura", 30)  # valor = cura


class PocaoForca(Item):
    def __init__(self):
        super().__init__("Poção de Força", 0)  # valor 0, buff será tratado no uso
