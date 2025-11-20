def menu_logs(jogo):
    if not hasattr(jogo, "logger") or jogo.logger is None:
        print("⚠ Logger não inicializado.")
        return

    while True:
        print("\n=== LOGS DO JOGO ===")
        print("[1] Ver todos os logs")
        print("[5] Limpar logs")
        print("[0] Voltar")

        op = input("> ").strip()

        if op == "1":
            exibir_logs(jogo.logger.eventos)

        elif op == "5":
            confirmar_limpar_logs(jogo)

        elif op == "0":
            break
        else:
            print("Opção inválida.")


# -----------------------------------------------------
#          EXIBIÇÃO E PAGINAÇÃO DE LOGS
# -----------------------------------------------------


def exibir_logs(lista_logs):
    if not lista_logs:
        print("\n(sem registros)")
        return

    tamanho = len(lista_logs)
    pagina = 0
    por_pagina = 10

    while True:
        inicio = pagina * por_pagina
        fim = inicio + por_pagina

        print("\n=== LOGS ===")
        for linha in lista_logs[inicio:fim]:
            print("- " + linha)

        print(f"\nPágina {pagina + 1} / {((tamanho - 1) // por_pagina) + 1}")
        print("[N] próxima página  |  [P] página anterior  |  [0] voltar")

        op = input("> ").strip().lower()

        if op == "n":
            if fim < tamanho:
                pagina += 1
        elif op == "p":
            if pagina > 0:
                pagina -= 1
        elif op == "0":
            break
        else:
            print("Opção inválida.")


# -----------------------------------------------------
#                LIMPAR LOGS
# -----------------------------------------------------


def confirmar_limpar_logs(jogo):
    print("\nTem certeza que deseja APAGAR todos os logs?")
    print("[1] Sim")
    print("[0] Não")
    op = input("> ").strip()

    if op == "1":
        jogo.logger.eventos.clear()
        print("✔ Todos os logs foram apagados.")
    else:
        print("Operação cancelada.")
