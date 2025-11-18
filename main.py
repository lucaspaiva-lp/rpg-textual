from __future__ import annotations
from models.jogo import Jogo


def menu() -> None:
    """Exibe o menu principal do jogo e gerencia a navegação.

    Cria uma instância da classe `Jogo` e permite ao jogador acessar:
    - criação de personagem,
    - missões,
    - salvamento,
    - carregamento.

    Loop contínuo até que o usuário escolha sair.
    """
    jogo = Jogo()

    while True:
        print("\n=== RPG OO — Menu Principal ===")
        print("[1] Criar personagem")
        print("[2] Missão")
        print("[3] Salvar")
        print("[4] Carregar")
        print("[0] Sair")

        op = input("> ").strip()

        if op == "1":
            jogo.criar_personagem()
        elif op == "2":
            jogo.menu_missao()
        elif op == "3":
            jogo.menu_salvar()
        elif op == "4":
            jogo.menu_carregar()
        elif op == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    """Ponto de entrada principal do programa.

    Executa `menu()` caso o arquivo seja executado diretamente.
    """
    menu()
