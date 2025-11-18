from __future__ import annotations

# Importa os módulos controladores (cada um responsável por sua área)
from utils import controle_personagem
from utils import controle_missao
from utils import salvamento


class Jogo:
    """
    Núcleo do jogo. Armazena o estado global e delega todas as ações
    para os módulos especializados dentro de /utils.

    Este arquivo NÃO contém lógicas específicas do jogo;
    apenas mantém o estado e direciona chamadas.
    """

    def __init__(self) -> None:
        # Estado do personagem
        self.personagem = {"nome": None, "arquetipo": None}
        self.personagem_obj = None

        # Estado da missão
        self.missao_config = {"dificuldade": "Fácil", "cenario": "Trilha"}

        # Controles de persistência
        self._ultimo_save = None
        self._ultimo_load = None

    # ------------------------------------------------------------------
    #                        ROTAS / DELEGADORES
    # ------------------------------------------------------------------

    def criar_personagem(self) -> None:
        """Delegação direta para controle_personagem."""
        try:
            controle_personagem.criar_personagem(self)
        except Exception as e:
            print(f"[ERRO] criar_personagem: {e}")

    def ver_personagem(self) -> None:
        """Tenta delegar para o módulo. Caso não exista, avisa."""
        try:
            if hasattr(controle_personagem, "ver_personagem"):
                return controle_personagem.ver_personagem(self)
            print(
                "[AVISO] Função ver_personagem() não encontrada em controle_personagem."
            )
        except Exception as e:
            print(f"[ERRO] ver_personagem: {e}")

    def menu_missao(self) -> None:
        try:
            controle_missao.menu_missao(self)
        except Exception as e:
            print(f"[ERRO] menu_missao: {e}")

    def menu_salvar(self) -> None:
        try:
            salvamento.menu_salvar(self)
        except Exception as e:
            print(f"[ERRO] menu_salvar: {e}")

    def menu_carregar(self) -> None:
        try:
            salvamento.menu_carregar(self)
        except Exception as e:
            print(f"[ERRO] menu_carregar: {e}")
