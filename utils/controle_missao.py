# =====================================================
# ========== MISSÕES - PROTÓTIPO DE TESTE =============
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
        print("[4] Iniciar missão (placeholder)")
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
            iniciar_missao_placeholder(jogo)
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
#             PARTE 3 — COMBATE PLACEHOLDER
# -----------------------------------------------------


def iniciar_missao_placeholder(jogo) -> None:
    if not jogo.personagem["nome"]:
        print("Crie um personagem antes de iniciar uma missão.")
        return

    print("\nIniciando missão...")
    jogo.logger.log(
        f"Missão iniciada — {jogo.missao_config['dificuldade']} / {jogo.missao_config['cenario']}"
    )

    inimigo = type(
        "InimigoSimulado",
        (),
        {"nome": "Goblin", "vida": 60, "ataque": 8, "defesa": 3},
    )()

    jogador = jogo.personagem_obj
    turno = 1

    while jogador.vida > 0 and inimigo.vida > 0:
        print(f"\n--- Turno {turno} ---")
        jogo.logger.log_batalha(f"--- Turno {turno} ---")

        # Ataque do jogador
        dano_jogador = max(jogador.ataque - inimigo.defesa, 0)
        inimigo.vida -= dano_jogador

        evento_jogador = (
            f"{jogador.nome} causou {dano_jogador} de dano em {inimigo.nome}."
        )
        print(evento_jogador)
        jogo.logger.log_batalha(evento_jogador)

        if inimigo.vida <= 0:
            jogo.logger.log_batalha(f"{inimigo.nome} foi derrotado!")
            print(f"{inimigo.nome} foi derrotado!")
            break

        # Ataque do inimigo
        dano_inimigo = max(inimigo.ataque - jogador.defesa, 0)
        jogador.vida -= dano_inimigo

        evento_inimigo = (
            f"{inimigo.nome} causou {dano_inimigo} de dano em {jogador.nome}."
        )
        print(evento_inimigo)
        jogo.logger.log_batalha(evento_inimigo)

        print(
            f"🧙 {jogador.nome} HP: {jogador.vida} | ⚔️ {inimigo.nome} HP: {inimigo.vida}"
        )
        jogo.logger.log_batalha(
            f"HP — {jogador.nome}: {jogador.vida} | {inimigo.nome}: {inimigo.vida}"
        )

        turno += 1

    # Resultado final
    resultado = "Vitória" if jogador.vida > 0 else "Derrota"
    jogo.logger.log_batalha(f"Resultado: {resultado}")

    print(f"\n=== Fim da Missão ===\nResultado: {resultado}")
    print("\nRetornando ao menu...")


# -----------------------------------------------------
#                     AJUDA
# -----------------------------------------------------


def ajuda_missao() -> None:
    print("\nAjuda — Missão")
    print("- Selecione dificuldade e cenário.")
    print("- A opção 'Iniciar missão' executará apenas um placeholder.")
    print("- Futuras versões podem usar essas escolhas para montar encontros.")
