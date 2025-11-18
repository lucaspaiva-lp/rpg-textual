import os
import json
from models.personagem import Guerreiro, Mago


# =====================================================
# ========== MENU DE SALVAR ============================
# =====================================================


def menu_salvar(jogo) -> None:
    os.makedirs("saves", exist_ok=True)

    while True:
        print("\n=== Salvar ===")
        print("[1] Salvar rápido")
        print("[2] Salvar com nome")
        print("[9] Ajuda")
        print("[0] Voltar")

        op = input("> ").strip()

        if op == "1":
            salvar_rapido(jogo)
        elif op == "2":
            salvar_nomeado(jogo)
        elif op == "9":
            ajuda_salvar()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


# -----------------------------------------------------
#                 SALVAR RÁPIDO
# -----------------------------------------------------


def salvar_rapido(jogo) -> None:
    caminho = os.path.join("saves", "quick_save.json")
    salvar_dados(jogo, caminho)
    jogo._ultimo_save = caminho
    print(f"✔ Progresso salvo em: {caminho}")


# -----------------------------------------------------
#              SALVAR COM NOME MANUAL
# -----------------------------------------------------


def salvar_nomeado(jogo) -> None:
    nome = input("Nome do arquivo (sem extensão): ").strip() or "meu_jogo"
    caminho = os.path.join("saves", f"{nome}.json")
    salvar_dados(jogo, caminho)
    jogo._ultimo_save = caminho
    print(f"✔ Progresso salvo em: {caminho}")


# -----------------------------------------------------
#                   SALVAR DADOS
# -----------------------------------------------------


def salvar_dados(jogo, caminho: str) -> None:
    try:
        dados = {
            "personagem": jogo.personagem,
            "missao_config": jogo.missao_config,
        }

        if hasattr(jogo, "personagem_obj"):
            p = jogo.personagem_obj
            dados["personagem_detalhes"] = {
                "vida": p.vida,
                "ataque": p.ataque,
                "defesa": p.defesa,
                "mana": p.mana,
                "inventario": p.get_inventario(),
            }

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")


# -----------------------------------------------------
#                        AJUDA
# -----------------------------------------------------


def ajuda_salvar() -> None:
    print("\nAjuda — Salvar")
    print("- Os saves são gravados como JSON dentro da pasta `saves/`.")
    print("- 'Salvar rápido' sobrescreve quick_save.json.")
    print("- 'Salvar com nome' permite criar arquivos diferentes.")
    print("- Evite usar espaços ou acentos no nome do arquivo.")


# =====================================================
# ========== MENU DE CARREGAR ==========================
# =====================================================


def menu_carregar(jogo) -> None:
    os.makedirs("saves", exist_ok=True)

    while True:
        print("\n=== Carregar ===")
        print("[1] Carregar último save da sessão")
        print("[2] Carregar por nome")
        print("[9] Ajuda")
        print("[0] Voltar")

        op = input("> ").strip()

        if op == "1":
            carregar_ultimo(jogo)
        elif op == "2":
            carregar_nomeado(jogo)
        elif op == "9":
            ajuda_carregar()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


# -----------------------------------------------------
#               CARREGAR ÚLTIMO SAVE
# -----------------------------------------------------


def carregar_ultimo(jogo) -> None:
    if not jogo._ultimo_save:
        print("Nenhum save carregado ou salvo nesta sessão.")
        return

    carregar_dados(jogo, jogo._ultimo_save)


# -----------------------------------------------------
#               CARREGAR POR NOME
# -----------------------------------------------------


def carregar_nomeado(jogo) -> None:
    nome = input("Nome do arquivo (sem extensão): ").strip()
    caminho = os.path.join("saves", f"{nome}.json")

    if not os.path.exists(caminho):
        print("Arquivo não encontrado.")
        return

    carregar_dados(jogo, caminho)


# -----------------------------------------------------
#                CARREGAR DADOS
# -----------------------------------------------------


def carregar_dados(jogo, caminho: str) -> None:
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        jogo.personagem = dados.get("personagem", {})
        jogo.missao_config = dados.get("missao_config", {})

        # Restaurar classe do personagem
        if "personagem_detalhes" in dados:
            det = dados["personagem_detalhes"]

            arqu = jogo.personagem.get("arquetipo")
            nome = jogo.personagem.get("nome")

            if arqu == "Guerreiro":
                jogo.personagem_obj = Guerreiro(nome)
            elif arqu == "Mago":
                jogo.personagem_obj = Mago(nome)
            else:
                # fallback
                jogo.personagem_obj = Guerreiro(nome or "SemNome")

            # Restaurar atributos
            p = jogo.personagem_obj
            p.vida = det.get("vida", p.vida)
            p.ataque = det.get("ataque", p.ataque)
            p.defesa = det.get("defesa", p.defesa)
            p.mana = det.get("mana", p.mana)
            p.inventario = det.get("inventario", [])

        jogo._ultimo_load = caminho

        print(f"✔ Jogo carregado de: {caminho}")

    except Exception as e:
        print(f"❌ Erro ao carregar: {e}")


# -----------------------------------------------------
#                        AJUDA
# -----------------------------------------------------


def ajuda_carregar() -> None:
    print("\nAjuda — Carregar")
    print("- Carrega arquivos JSON da pasta `saves/`.")
    print("- Digite somente o nome (sem .json) ao carregar por nome.")
    print("- Apenas saves válidos funcionarão.")
