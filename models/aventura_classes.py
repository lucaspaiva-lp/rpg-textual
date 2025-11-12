class Guerreiro:
    """
    Representa o arquétipo de personagem Guerreiro.

    Caracteriza-se por alta vida e defesa, com foco em ataque físico.
    Possui inventário simples inicializado vazio.
    """

    def __init__(self, nome: str) -> None:
        """
        Inicializa uma nova instância de Guerreiro.

        Args:
            nome (str): Nome atribuído ao personagem.

        Atributos:
            nome (str): Identificação textual do personagem.
            vida (int): Pontos de vida base.
            ataque (int): Valor de ataque físico.
            defesa (int): Capacidade de reduzir dano recebido.
            mana (int): Pontos de energia mágica (0 para Guerreiro).
            inventario (list): Lista de itens possuídos pelo personagem.
        """
        self.nome = nome
        self.vida = 120
        self.ataque = 15
        self.defesa = 10
        self.mana = 0
        self.inventario = []

    def get_inventario(self) -> list:
        """
        Retorna o inventário atual do personagem.

        Returns:
            list: Lista de itens contidos no inventário.
        """
        return self.inventario


class Mago:
    """
    Representa o arquétipo de personagem Mago.

    Caracteriza-se por menor vida e defesa, compensadas por alto poder mágico (mana).
    Possui inventário simples inicializado vazio.
    """

    def __init__(self, nome: str) -> None:
        """
        Inicializa uma nova instância de Mago.

        Args:
            nome (str): Nome atribuído ao personagem.

        Atributos:
            nome (str): Identificação textual do personagem.
            vida (int): Pontos de vida base.
            ataque (int): Valor de ataque físico (baixo).
            defesa (int): Capacidade defensiva reduzida.
            mana (int): Pontos de energia mágica.
            inventario (list): Lista de itens possuídos pelo personagem.
        """
        self.nome = nome
        self.vida = 80
        self.ataque = 10
        self.defesa = 5
        self.mana = 50
        self.inventario = []

    def get_inventario(self) -> list:
        """
        Retorna o inventário atual do personagem.

        Returns:
            list: Lista de itens contidos no inventário.
        """
        return self.inventario
