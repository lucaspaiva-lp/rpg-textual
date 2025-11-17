from __future__ import annotations
from models.jogo import Jogo


def menu() -> None:
    """Exibe o menu principal do jogo e gerencia a navegação entre opções.

    Cria uma instância da classe `Jogo` e permite que o jogador interaja
    com as principais funcionalidades do sistema, como criação de personagem,
    seleção de missões e simulação de salvamento/carregamento.

    Loop contínuo até que o usuário opte por encerrar o programa.
    """
    jogo = Jogo()

    while True:
        print("\n=== RPG OO — Menu Principal ===")
        print("[1] Criar personagem")
        print("[2] Encarar missão")
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

    Executa a função `menu()` caso o script seja chamado diretamente,
    inicializando o fluxo principal do jogo.
    """
    menu()
