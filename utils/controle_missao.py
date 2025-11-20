from models.inventario import Inventario, Item
from models.inimigo import Goblin, Ladrao, Golem, Demonio
from models.itens import PocaoCura, PocaoForca
import random

# =====================================================
# ========== MENU DE MISSÃO ==========================
# =====================================================


def menu_missao(jogo) -> None:
    """Submenu de missões."""
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
#        GERADOR DE INIMIGOS POR CENÁRIO
# -----------------------------------------------------


def gerar_inimigo_por_cenario(cenario):
    mapa = {
        "Trilha": [Goblin],
        "Floresta": [Goblin, Ladrao],
        "Caverna": [Ladrao, Golem],
        "Ruínas": [Golem, Demonio],
    }

    lista = mapa.get(cenario, [Goblin])
    classe_escolhida = random.choice(lista)
    return classe_escolhida()


# -----------------------------------------------------
#        APLICAR DIFICULDADE
# -----------------------------------------------------


def aplicar_dificuldade(inimigo, dificuldade):
    if dificuldade == "Média":
        inimigo.vida = int(inimigo.vida * 1.2)
        inimigo.ataque = int(inimigo.ataque * 1.2)
        inimigo.defesa = int(inimigo.defesa * 1.2)

    elif dificuldade == "Difícil":
        inimigo.vida = int(inimigo.vida * 1.5)
        inimigo.ataque = int(inimigo.ataque * 1.5)
        inimigo.defesa = int(inimigo.defesa * 1.5)

    return inimigo


# -----------------------------------------------------
#             PRÉ-VISUALIZAÇÃO DA MISSÃO
# -----------------------------------------------------


def preview_missao(jogo) -> None:
    print("\nPré-visualização da Missão")
    print(f"- Dificuldade: {jogo.missao_config['dificuldade']}")
    print(f"- Cenário:     {jogo.missao_config['cenario']}")
    print("- Inimigos e recompensas: Gerados dinamicamente")
    print("- Regras de combate: Turnos alternados e uso de itens")


# -----------------------------------------------------
#                 COMBATE DINÂMICO
# -----------------------------------------------------


def iniciar_missao(jogo):
    if not jogo.personagem["nome"]:
        print("Crie um personagem antes de iniciar uma missão.")
        return

    jogador = jogo.personagem_obj
    inventario = jogador.inventario

    # Poções iniciais caso inventário esteja vazio
    if len(inventario.itens) == 0:
        inventario.adicionar_item(Item("Poção de Cura", 30))
        inventario.adicionar_item(Item("Poção de Cura", 30))

    # Gerar inimigo real
    cenario = jogo.missao_config["cenario"]
    dificuldade = jogo.missao_config["dificuldade"]

    inimigo = gerar_inimigo_por_cenario(cenario)
    inimigo = aplicar_dificuldade(inimigo, dificuldade)

    print(f"\nVocê encontrou um {inimigo.nome}!")

    turno = 1
    jogo.logger.log_batalha(
        f"Missão iniciada — {dificuldade} / {cenario} — Inimigo: {inimigo.nome}"
    )

    # ===== LOOP DO COMBATE =====
    while jogador.vida > 0 and inimigo.vida > 0:
        print(f"\n--- Turno {turno} ---")
        print(f"{jogador.nome} HP: {jogador.vida} | {inimigo.nome} HP: {inimigo.vida}")

        print("\nAção:")
        print("[1] Atacar")
        print("[2] Usar item")
        print("[3] Fugir")

        acao = input("> ").strip()

        # ----------------------------------
        # ATAQUE DO JOGADOR
        # ----------------------------------
        if acao == "1":
            dano = max(jogador.ataque - inimigo.defesa, 0)
            inimigo.vida -= dano
            print(f"Você causou {dano} de dano!")
            jogo.logger.log_batalha(f"{jogador.nome} causou {dano} em {inimigo.nome}.")

        elif acao == "2":
            usar_item_em_combate(jogador, jogo)
            turno += 1
            continue

        elif acao == "3":
            print("Você fugiu!")
            jogo.logger.log_batalha("Jogador fugiu da missão.")
            return

        else:
            print("Ação inválida!")
            continue

        # ----------------------------------
        # ATAQUE DO INIMIGO
        # ----------------------------------
        if inimigo.vida > 0:
            dano_inimigo = max(inimigo.ataque - jogador.defesa, 1)
            jogador.vida -= dano_inimigo
            print(f"{inimigo.nome} te atacou e causou {dano_inimigo}!")
            jogo.logger.log_batalha(
                f"{inimigo.nome} causou {dano_inimigo} em {jogador.nome}."
            )

        turno += 1

    # ----------------------------------
    # RESULTADO FINAL
    # ----------------------------------
    resultado = "Vitória" if jogador.vida > 0 else "Derrota"
    print(f"\n=== Fim da Missão ===\nResultado: {resultado}")
    jogo.logger.log_batalha(f"Resultado: {resultado}")

    # 👉 Recompensa somente se vencer
    if resultado == "Vitória":
        recompensar_jogador(jogador, dificuldade)


def recompensar_jogador(jogador, dificuldade):
    print("\n🎁 Recompensas da missão:")

    dif = dificuldade.lower()

    if dif == "fácil":
        jogador.adicionar_item(PocaoCura())
        print("→ 1x Poção de Cura")

    elif dif == "média":
        jogador.adicionar_item(PocaoCura())
        jogador.adicionar_item(PocaoForca())
        print("→ 1x Poção de Cura")
        print("→ 1x Poção de Força")

    elif dif == "difícil":
        jogador.adicionar_item(PocaoForca())
        jogador.adicionar_item(PocaoForca())
        print("→ 2x Poção de Força")

    else:
        print("Nenhuma recompensa para essa dificuldade.")

    print("✔ Recompensas adicionadas ao inventário!")


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
        if item.nome == "Poção de Força":
            print(f"[{i}] {item.nome} (+5 ATK)")
        else:
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

    # Poção de força
    if item.nome == "Poção de Força":
        jogador.ataque += 5
        print("💥 Seu ataque aumentou em +5 temporariamente!")
        jogo.logger.log_batalha(f"{jogador.nome} usou Poção de Força (+5 ATK).")

    # Poções de cura normais
    else:
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
    print("- Cada cenário tem seus inimigos específicos.")
    print("- Dificuldade aumenta vida, ataque e defesa do inimigo.")
    print("- Use poções no combate quando necessário.")
