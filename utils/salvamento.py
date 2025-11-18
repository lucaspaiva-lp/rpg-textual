import os
import json
from models.personagem import Guerreiro, Mago, Aventureiro
from models.inventario import Inventario, Item
from models.logger import Logger


class RepositorioJogo:
    """
    Repositório responsável por SALVAR e CARREGAR o progresso.
    Totalmente orientado a objetos e compatível com o projeto atual.
    """

    def __init__(self, pasta="saves"):
        self.pasta = pasta
        os.makedirs(self.pasta, exist_ok=True)
        self.ultimo_save = None  # espelho do jogo._ultimo_save se quiser sincronizar

    # =========================================================
    #                      SALVAR
    # =========================================================

    def salvar_rapido(self, jogo):
        caminho = os.path.join(self.pasta, "quick_save.json")
        self.salvar(jogo, caminho)
        self.ultimo_save = caminho
        jogo._ultimo_save = caminho

    def salvar_com_nome(self, jogo, nome):
        caminho = os.path.join(self.pasta, f"{nome}.json")
        self.salvar(jogo, caminho)
        self.ultimo_save = caminho
        jogo._ultimo_save = caminho

    def salvar(self, jogo, caminho):
        try:
            dados = self._montar_dados(jogo)
            with open(caminho, "w", encoding="utf-8") as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)
            print(f"✔ Progresso salvo em: {caminho}")
        except Exception as e:
            print(f"❌ Erro ao salvar: {e}")

    # =========================================================
    #                      CARREGAR
    # =========================================================

    def carregar(self, jogo, caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)

            jogo.personagem = dados.get("personagem", {})
            jogo.missao_config = dados.get("missao_config", {})

            # -------------------------
            #       RECRIAR PERSONAGEM
            # -------------------------
            if "personagem_detalhes" in dados:
                det = dados["personagem_detalhes"]
                nome = jogo.personagem.get("nome")
                arq = jogo.personagem.get("arquetipo")

                # recria a classe correta
                if arq == "Guerreiro":
                    jogo.personagem_obj = Guerreiro(nome)
                elif arq == "Mago":
                    jogo.personagem_obj = Mago(nome)
                else:
                    jogo.personagem_obj = Guerreiro(nome or "SemNome")

                p: Aventureiro = jogo.personagem_obj

                # restaura atributos básicos
                p.vida = det.get("vida", p.vida)
                p.ataque = det.get("ataque", p.ataque)
                p.defesa = det.get("defesa", p.defesa)
                p.mana = det.get("mana", p.mana)

                # reconstrói o inventário
                p.inventario = Inventario()
                for item_data in det.get("inventario", []):
                    p.inventario.adicionar_item(
                        Item(item_data["nome"], item_data["valor"])
                    )

            # -------------------------
            #       RESTAURAR LOGS
            # -------------------------
            if hasattr(jogo, "logger") and "logs" in dados:
                jogo.logger.importar(dados["logs"])

            self.ultimo_save = caminho
            jogo._ultimo_load = caminho
            print(f"✔ Jogo carregado de: {caminho}")

        except Exception as e:
            print(f"❌ Erro ao carregar: {e}")

    # =========================================================
    #                MONTAGEM DOS DADOS (JSON)
    # =========================================================

    def _montar_dados(self, jogo):
        dados = {
            "personagem": jogo.personagem,
            "missao_config": jogo.missao_config,
        }

        # -----------------------
        # Salvar LOGS
        # -----------------------
        if hasattr(jogo, "logger") and jogo.logger is not None:
            dados["logs"] = jogo.logger.exportar()
        else:
            dados["logs"] = []

        # -----------------------
        # Detalhes do personagem
        # -----------------------
        if jogo.personagem_obj:
            p: Aventureiro = jogo.personagem_obj

            # Serializa inventário de forma segura
            inventario_serializado = []
            if hasattr(p, "inventario") and hasattr(p.inventario, "itens"):
                for item in p.inventario.itens:
                    inventario_serializado.append(
                        {
                            "nome": getattr(item, "nome", "Item Desconhecido"),
                            "valor": getattr(item, "valor", 0),
                        }
                    )

            dados["personagem_detalhes"] = {
                "vida": getattr(p, "vida", 100),
                "ataque": getattr(p, "ataque", 10),
                "defesa": getattr(p, "defesa", 5),
                "mana": getattr(p, "mana", 0),
                "inventario": inventario_serializado,
            }

            # salva arquetipo para recriar corretamente
            dados["personagem"]["arquetipo"] = p.__class__.__name__

        return dados


# =====================================================
#           MENUS — CHAMAM O REPOSITORIO
# =====================================================

repo = RepositorioJogo()


def menu_salvar(jogo):
    while True:
        print("\n=== Salvar ===")
        print("[1] Salvar rápido")
        print("[2] Salvar com nome")
        print("[9] Ajuda")
        print("[0] Voltar")

        op = input("> ").strip()

        if op == "1":
            repo.salvar_rapido(jogo)
        elif op == "2":
            nome = input("Nome do arquivo (sem extensão): ").strip() or "meu_jogo"
            repo.salvar_com_nome(jogo, nome)
        elif op == "9":
            ajuda_salvar()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_carregar(jogo):
    while True:
        print("\n=== Carregar ===")
        print("[1] Carregar último da sessão")
        print("[2] Carregar por nome")
        print("[9] Ajuda")
        print("[0] Voltar")

        op = input("> ").strip()

        if op == "1":
            if repo.ultimo_save:
                repo.carregar(jogo, repo.ultimo_save)
            else:
                print("Nenhum save na sessão.")
        elif op == "2":
            nome = input("Nome do arquivo (sem extensão): ").strip()
            caminho = os.path.join("saves", f"{nome}.json")
            if os.path.exists(caminho):
                repo.carregar(jogo, caminho)
            else:
                print("Arquivo não encontrado.")
        elif op == "9":
            ajuda_carregar()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


# =====================================================
# Funções de ajuda
# =====================================================


def ajuda_salvar():
    print("\nAjuda — Salvar")
    print("- [1] Salvar rápido: salva em 'quick_save.json'.")
    print("- [2] Salvar com nome: permite escolher o nome do arquivo.")


def ajuda_carregar():
    print("\nAjuda — Carregar")
    print("- [1] Carregar último da sessão.")
    print("- [2] Carregar por nome de arquivo.")
