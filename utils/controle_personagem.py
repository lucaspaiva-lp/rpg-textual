# =====================================================
# ========== CRIAÇÃO DE PERSONAGEM - PROTÓTIPO =========
# =====================================================


def criar_personagem(jogo) -> None:
    """
    Fluxo interativo de criação do personagem.
    Atualiza jogo.personagem e cria jogo.personagem_obj ao confirmar.
    """

    print("=== Criação de Personagem ===")

    while True:
        print("\n=== Criar Personagem ===")
        print(f"Nome atual: {jogo.personagem['nome'] or '(não definido)'}")
        print(f"Arquétipo:  {jogo.personagem['arquetipo'] or '(não definido)'}")

        print("[1] Definir nome")
        print("[2] Escolher arquétipo")
        print("[3] Confirmar criação")
        print("[9] Ajuda")
        print("[0] Voltar")

        op = input("> ").strip()

        if op == "1":
            definir_nome(jogo)
        elif op == "2":
            escolher_arquetipo(jogo)
        elif op == "3":
            confirmar_criacao(jogo)
        elif op == "9":
            ajuda_criar_personagem()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


# -----------------------------------------------------
#                DEFINIR NOME
# -----------------------------------------------------


def definir_nome(jogo) -> None:
    nome = input("Digite o nome do personagem: ").strip()
    if nome:
        jogo.personagem["nome"] = nome
        print(f"Nome definido: {nome}")
    else:
        print("Nome não alterado.")


# -----------------------------------------------------
#             ESCOLHER ARQUÉTIPO
# -----------------------------------------------------


def escolher_arquetipo(jogo) -> None:
    print("\nArquétipos disponíveis:")
    print("[1] Guerreiro")
    print("[2] Mago")
    print("[3] Arqueiro")
    print("[4] Curandeiro")
    print("[5] Personalizado")

    op = input("> ").strip()

    mapa = {
        "1": "Guerreiro",
        "2": "Mago",
        "3": "Arqueiro",
        "4": "Curandeiro",
        "5": "Personalizado",
    }

    arq = mapa.get(op)

    if arq:
        jogo.personagem["arquetipo"] = arq
        print(f"Arquétipo definido: {arq}")
    else:
        print("Opção inválida. Arquétipo não alterado.")


# -----------------------------------------------------
#             CONFIRMAR CRIAÇÃO
# -----------------------------------------------------


def confirmar_criacao(jogo) -> None:
    nome = jogo.personagem["nome"]
    arq = jogo.personagem["arquetipo"]

    if not nome:
        print("Defina um nome antes de confirmar a criação.")
        return
    if not arq:
        print("Escolha um arquétipo antes de confirmar a criação.")
        return

    print("\nPersonagem criado com sucesso!")
    print(f"Nome: {nome} | Arquétipo: {arq}")

    # Aqui você instancia a classe real do personagem
    # (Guerreiro, Mago, etc.)
    # Para já funcionar, deixei assim:
    from models.personagem import Guerreiro, Mago

    if arq == "Guerreiro":
        jogo.personagem_obj = Guerreiro(nome)
    elif arq == "Mago":
        jogo.personagem_obj = Mago(nome)
    else:
        # Para os que ainda não existem, cria um básico
        jogo.personagem_obj = Guerreiro(nome)

    print("Objeto do personagem criado com sucesso!")


# -----------------------------------------------------
#                     AJUDA
# -----------------------------------------------------


def ajuda_criar_personagem() -> None:
    print("\nAjuda — Criação de Personagem")
    print("- Defina um nome e um arquétipo.")
    print("- Apenas Guerreiro e Mago possuem classes próprias.")
    print("- A confirmação cria o objeto do personagem.")
