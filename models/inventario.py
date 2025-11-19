# =====================================================
# CLASSE ITEM
# =====================================================
class Item:
    """
    Representa um item do jogo, por enquanto apenas poções de cura.
    """

    def __init__(self, nome: str, valor: int):
        """
        Args:
            nome (str): Nome do item.
            valor (int): Valor do efeito (ex: quantidade de HP que recupera).
        """
        self.nome = nome
        self.valor = valor

    def __repr__(self):
        return f"<Item: {self.nome}, Valor: {self.valor}>"


# =====================================================
# CLASSE INVENTÁRIO
# =====================================================
class Inventario:
    """
    Inventário de um personagem. Guarda itens e permite adicionar/remover.
    """

    def __init__(self):
        self.itens: list[Item] = []

    def adicionar_item(self, item: Item):
        """Adiciona um item ao inventário."""
        self.itens.append(item)

    def remover_item(self, item: Item):
        """Remove um item do inventário, se existir."""
        if item in self.itens:
            self.itens.remove(item)

    def listar_itens(self) -> list[Item]:
        """Retorna a lista de itens atuais."""
        return self.itens

    def esta_vazio(self) -> bool:
        """Retorna True se o inventário estiver vazio."""
        return len(self.itens) == 0
