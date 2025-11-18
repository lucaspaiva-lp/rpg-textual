from __future__ import annotations
import os
import json

# Importa os módulos utilitários (delegação de responsabilidade)
from utils import controle_personagem as controle_personagem
from utils import controle_missao as controle_missao
from utils import salvamento as salvamento


class Jogo:
    """Controla o núcleo do RPG textual e o fluxo principal do jogo.

    Esta versão do arquivo mantém apenas o loop principal e fornece
    "rotas" (métodos) que delegam a lógica para os módulos em `utils`.
    Cada método tenta delegar a chamada ao util correspondente e, se
    não encontrado, apresenta uma mensagem clara para debug.
    """

    def __init__(self) -> None:
        self.personagem = {"nome": None, "arquetipo": None}
        self.personagem_obj = None
        self.missao_config = {"dificuldade": "Fácil", "cenario": "Trilha"}
        self._ultimo_save = None
        self._ultimo_load = None

    # ---------------------- Rotas / Delegadores ----------------------
    def criar_personagem(self) -> None:
        """Rota para criação de personagem.

        Tenta delegar para `utils.controle_personagem.criar_personagem(jogo)`.
        """
        try:
            # espera-se função: criar_personagem(jogo: Jogo) -> None
            controle_personagem.criar_personagem(self)
        except AttributeError:
            print("[ERRO] controle_personagem.criar_personagem não encontrada.")
        except Exception as e:
            print(f"[ERRO] Ao chamar criar_personagem: {e}")

    def ver_personagem(self) -> None:
        """Exibe dados do personagem ou delega ao util se disponível."""
        # Delegar se existir
        try:
            if hasattr(controle_personagem, "ver_personagem"):
                controle_personagem.ver_personagem(self)
                return
        except Exception:
            print("[AVISO] falha ao delegar ver_personagem para controle_personagem")

        # Fallback interno (leve)
        if getattr(self, "personagem_obj", None):
            p = self.personagem_obj
            print("\n=== Dados do Personagem ===")
            print(f"Nome: {p.nome}")
            print(f"Classe: {self.personagem.get('arquetipo')}")
            print(f"Vida: {getattr(p, 'vida', 'N/A')}")
            print(f"Ataque: {getattr(p, 'ataque', 'N/A')}")
            print(f"Defesa: {getattr(p, 'defesa', 'N/A')}")
            print(f"Mana: {getattr(p, 'mana', 'N/A')}")
            inv = getattr(p, "get_inventario", None)
            if callable(inv):
                print(f"Inventário: {p.get_inventario()}")
            else:
                print(f"Inventário: {getattr(p, 'inventario', [])}")
        else:
            print("Nenhum personagem criado ainda.")

    def menu_missao(self) -> None:
        """Rota para o menu de missões; delega para utils.controle_missao."""
        try:
            controle_missao.menu_missao(self)
        except AttributeError:
            print("[ERRO] controle_missao.menu_missao não encontrada.")
        except Exception as e:
            print(f"[ERRO] Ao chamar menu_missao: {e}")

    def menu_salvar(self) -> None:
        """Rota para salvar: delega para utils.salvamento."""
        try:
            salvamento.menu_salvar(self)
        except AttributeError:
            print("[ERRO] salvamento.menu_salvar não encontrada.")
        except Exception as e:
            print(f"[ERRO] Ao chamar menu_salvar: {e}")

    def menu_carregar(self) -> None:
        """Rota para carregar: delega para utils.salvamento."""
        try:
            salvamento.menu_carregar(self)
        except AttributeError:
            print("[ERRO] salvamento.menu_carregar não encontrada.")
        except Exception as e:
            print(f"[ERRO] Ao chamar menu_carregar: {e}")

    # ---------------------- Menu principal ----------------------
    def menu_principal(self) -> None:
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("[1] Criar novo personagem")
            print("[2] Ver informações do personagem")
            print("[3] Missão")
            print("[4] Salvar Jogo")
            print("[5] Carregar Jogo")
            print("[0] Sair")

            opcao = input("> ").strip()

            if opcao == "1":
                self.criar_personagem()
            elif opcao == "2":
                self.ver_personagem()
            elif opcao == "3":
                self.menu_missao()
            elif opcao == "4":
                self.menu_salvar()
            elif opcao == "5":
                self.menu_carregar()
            elif opcao == "0":
                print("Saindo do jogo...")
                break
            else:
                print("Opção inválida. Tente novamente.")


# ---------------------- ENTRY POINT ----------------------
if __name__ == "__main__":
    jogo = Jogo()
    jogo.menu_principal()
