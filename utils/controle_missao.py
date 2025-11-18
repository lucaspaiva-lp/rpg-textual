from models.inventario import Inventario, Item

# =====================================================
# ========== MENU DE MISSÃO ==========================
# =====================================================


def menu_missao(jogo) -> None:
    """
    Submenu de missões.
    Controla as escolhas e delega para funções específicas.
    """
    while True:
        print("\n=== Missão ===")
        print(f"Dificuldade atual: {jogo.missao_config['dificuldade']}")
        print(f"Cenário atual:     {jogo.missao_config['cenario']}")
        print("[1] Escolher dificuldade")
        print("[2] Escolher cenário")
        print("[3] Pré-visualizar missão")
        print("[4] Iniciar missão")
        print("[9] Ajuda")
        print("[0] Voltar")
        op = input("> ").strip()

        if op == "1":
            escolher_dificuldade(jogo)
        elif op == "2":
            escolher_cenario(jogo)
        elif op == "3":
            preview_missao(jogo)
        elif op == "4":
            iniciar_missao(jogo)
        elif op == "9":
            ajuda_missao()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


# -----------------------------------------------------
#               PARTE 1 — DIFICULDADE
# -----------------------------------------------------


def escolher_dificuldade(jogo) -> None:
    print("\nDificuldades:")
    print("[1] Fácil")
    print("[2] Média")
    print("[3] Difícil")
    op = input("> ").strip()
    mapa = {"1": "Fácil", "2": "Média", "3": "Difícil"}
    dif = mapa.get(op)

    if dif:
        jogo.missao_config["dificuldade"] = dif
        print(f"Dificuldade definida: {dif}")
    else:
        print("Opção inválida.")


# -----------------------------------------------------
#               PARTE 2 — CENÁRIO
# -----------------------------------------------------


def escolher_cenario(jogo) -> None:
    print("\nCenários:")
    print("[1] Trilha")
    print("[2] Floresta")
    print("[3] Caverna")
    print("[4] Ruínas")

    op = input("> ").strip()
    mapa = {"1": "Trilha", "2": "Floresta", "3": "Caverna", "4": "Ruínas"}
    cen = mapa.get(op)

    if cen:
        jogo.missao_config["cenario"] = cen
        print(f"Cenário definido: {cen}")
    else:
        print("Opção inválida.")


# -----------------------------------------------------
#             PRÉ-VISUALIZAÇÃO DA MISSÃO
# -----------------------------------------------------


def preview_missao(jogo) -> None:
    print("\nPré-visualização da Missão")
    print(f"- Dificuldade: {jogo.missao_config['dificuldade']}")
    print(f"- Cenário:     {jogo.missao_config['cenario']}")
    print("- Inimigos e recompensas: (em breve)")
    print("- Regras de combate: (em breve)")


# -----------------------------------------------------
#             PARTE 3 — COMBATE DINÂMICO
# -----------------------------------------------------


def iniciar_missao(jogo):
    if not jogo.personagem["nome"]:
        print("Crie um personagem antes de iniciar uma missão.")
        return

    # Inicializa inventário se não existir
    if (
        not hasattr(jogo.personagem_obj, "inventario")
        or jogo.personagem_obj.inventario is None
    ):
        jogo.personagem_obj.inventario = Inventario()
        # Itens iniciais
        jogo.personagem_obj.inventario.adicionar_item(Item("Poção de Cura", 30))
        jogo.personagem_obj.inventario.adicionar_item(Item("Poção de Cura", 30))

    jogador = jogo.personagem_obj

    inimigo = type(
        "InimigoSimulado", (), {"nome": "Goblin", "vida": 60, "ataque": 8, "defesa": 3}
    )()

    turno = 1
    print("\nIniciando missão...")
    jogo.logger.log_batalha(
        f"Missão iniciada — {jogo.missao_config['dificuldade']} / {jogo.missao_config['cenario']}"
    )

    while jogador.vida > 0 and inimigo.vida > 0:
        print(f"\n--- Turno {turno} ---")
        print(f"{jogador.nome} HP: {jogador.vida} | {inimigo.nome} HP: {inimigo.vida}")

        print("\nAção:")
        print("[1] Atacar")
        print("[2] Usar item")
        print("[3] Fugir")
        acao = input("> ").strip()

        if acao == "1":
            dano = max(jogador.ataque - inimigo.defesa, 0)
            inimigo.vida -= dano
            print(f"Você causou {dano} de dano!")
            jogo.logger.log_batalha(f"{jogador.nome} causou {dano} em {inimigo.nome}.")

        elif acao == "2":
            usar_item_em_combate(jogador, jogo)
            turno += 1
            continue  # inimigo não perde turno

        elif acao == "3":
            print("Você fugiu!")
            jogo.logger.log_batalha("Jogador fugiu da missão.")
            return

        else:
            print("Ação inválida!")
            continue

        # Ataque inimigo
        if inimigo.vida > 0:
            dano_inimigo = max(inimigo.ataque - jogador.defesa, 0)
            jogador.vida -= dano_inimigo
            print(f"{inimigo.nome} te atacou e causou {dano_inimigo}!")
            jogo.logger.log_batalha(
                f"{inimigo.nome} causou {dano_inimigo} em {jogador.nome}."
            )

        turno += 1

    resultado = "Vitória" if jogador.vida > 0 else "Derrota"
    print(f"\n=== Fim da Missão ===\nResultado: {resultado}")
    jogo.logger.log_batalha(f"Resultado: {resultado}")


# -----------------------------------------------------
#             USO DE ITENS DURANTE COMBATE
# -----------------------------------------------------


def usar_item_em_combate(jogador, jogo):
    inventario = jogador.inventario

    if not inventario.itens:
        print("Seu inventário está vazio!")
        return

    print("\n=== Inventário ===")
    for i, item in enumerate(inventario.itens, 1):
        print(f"[{i}] {item.nome} (cura {item.valor} HP)")
    print("[0] Cancelar")

    op = input("> ").strip()
    if op == "0":
        print("Você desistiu de usar um item.")
        return

    try:
        idx = int(op) - 1
        item = inventario.itens[idx]
    except:
        print("Item inválido!")
        return

    jogador.vida += item.valor
    print(f"Você usou {item.nome} e recuperou {item.valor} HP!")
    jogo.logger.log_batalha(f"{jogador.nome} usou {item.nome} (+{item.valor} HP).")
    inventario.remover_item(item)


# -----------------------------------------------------
#                     AJUDA
# -----------------------------------------------------


def ajuda_missao() -> None:
    print("\nAjuda — Missão")
    print("- Selecione dificuldade e cenário.")
    print("- Durante a missão, use [1] Atacar, [2] Usar item, [3] Fugir.")
    print("- Poções curam HP fixo.")
