from __future__ import annotations

from utils import controle_personagem
from utils import controle_missao
from utils import salvamento


class Jogo:
    """
    Núcleo do jogo. Apenas mantém o estado global e encaminha chamadas
    para os módulos especializados dentro de utils/.
    """

    def __init__(self) -> None:
        # Estado do personagem
        self.personagem = {"nome": None, "arquetipo": None}

        # Objeto do personagem (instância de Guerreiro ou Mago)
        self.personagem_obj = None

        # Estado da missão
        self.missao_config = {"dificuldade": "Fácil", "cenario": "Trilha"}

        # Dados de persistência
        self._ultimo_save = None
        self._ultimo_load = None

    # ================================================================
    #           ROTAS (encaminham chamadas a módulos externos)
    # ================================================================

    def criar_personagem(self) -> None:
        """Chama o módulo controle_personagem."""
        try:
            controle_personagem.criar_personagem(self)
        except Exception as e:
            print(f"[ERRO] criar_personagem: {e}")

    def ver_personagem(self) -> None:
        """Exibe informações do personagem, se o módulo possuir essa função."""
        try:
            if hasattr(controle_personagem, "ver_personagem"):
                return controle_personagem.ver_personagem(self)
            print("[AVISO] ver_personagem() não existe em controle_personagem.")
        except Exception as e:
            print(f"[ERRO] ver_personagem: {e}")

    def menu_missao(self) -> None:
        """Chama o módulo de missões."""
        try:
            controle_missao.menu_missao(self)
        except Exception as e:
            print(f"[ERRO] menu_missao: {e}")

    def menu_salvar(self) -> None:
        """Encaminha para o sistema de salvamento."""
        try:
            salvamento.menu_salvar(self)
        except Exception as e:
            print(f"[ERRO] menu_salvar: {e}")

    def menu_carregar(self) -> None:
        """Encaminha para o sistema de carregamento."""
        try:
            salvamento.menu_carregar(self)
        except Exception as e:
            print(f"[ERRO] menu_carregar: {e}")
