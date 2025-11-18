from __future__ import annotations

from utils import controle_personagem
from utils import controle_missao
from utils import salvamento
from models.logger import Logger


class Jogo:
    """
    Núcleo do jogo. Apenas mantém o estado global e encaminha chamadas
    para os módulos especializados dentro de utils/.
    """

    def __init__(self) -> None:
        # ==================================================
        # Inicializa logger da sessão (ESSENCIAL)
        # ==================================================
        self.logger = Logger()

        # Estado do personagem
        self.personagem = {"nome": None, "arquetipo": None}

        # Objeto completo do personagem (classe Guerreiro/Mago)
        self.personagem_obj = None

        # Estado da missão
        self.missao_config = {"dificuldade": "Fácil", "cenario": "Trilha"}

        # Repositório de salvamento (importado do módulo utils/salvamento)
        self.repo = salvamento.repo

        # Últimos caminhos usados
        self._ultimo_save = None
        self._ultimo_load = None

    # ================================================================
    #           ROTAS (encaminham chamadas a módulos externos)
    # ================================================================

    def criar_personagem(self) -> None:
        try:
            controle_personagem.criar_personagem(self)
        except Exception as e:
            print(f"[ERRO] criar_personagem: {e}")

    def ver_personagem(self) -> None:
        try:
            if hasattr(controle_personagem, "ver_personagem"):
                return controle_personagem.ver_personagem(self)
            print("[AVISO] ver_personagem() não existe em controle_personagem.")
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
