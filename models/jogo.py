from __future__ import annotations
import os
import json
from models.aventura_classes import Guerreiro, Mago
from equipamentos import PocaoDeVida

from utils import controle_personagem
from utils import controle_missao
from utils import salvamento
from models.logger import Logger


class Jogo:
    """
    Núcleo do jogo. Apenas mantém o estado global e encaminha chamadas
    para os módulos especializados dentro de utils/.
    """

    def __init__(self) -> None:
        # ==================================================
        # Inicializa logger da sessão (ESSENCIAL)
        # ==================================================
        self.logger = Logger()

        # Estado do personagem
        self.personagem = {"nome": None, "arquetipo": None}

 # menu personagem
    def menu_personagem(self):
        """
        Menu dedicado às operações relacionadas ao personagem:
        criar, ver, inventário, criação de itens.
        """
        while True:
            print("\n=== Menu de Personagem ===")
            print("[1] Criar personagem")
            print("[2] Ver personagem")
            print("[3] Checar inventário")
            print("[4] Criar item")
            print("[5] Usar item")
            print("[6] Adicionar item ao inventário")
            print("[0] Voltar ao menu principal")

        # Estado da missão
        self.missao_config = {"dificuldade": "Fácil", "cenario": "Trilha"}

        # Repositório de salvamento (importado do módulo utils/salvamento)
        self.repo = salvamento.repo

            elif op == "2":
                self.ver_personagem()

            elif op == "3":
                self.checar_inventario()

            elif op == "5":
                self.usar_item_personagem()

            elif op == "6":
                item = print("Informe o nome do item a adicionar:")
                self.personagem.adicionar_item(item)

            elif op == "0":
                break

            else:
                print("Opção inválida. Tente novamente.")

    # ================================================================
    #           ROTAS (encaminham chamadas a módulos externos)
    # ================================================================

    def criar_personagem(self) -> None:
        """
        Fluxo interativo de criação de personagem jogável.

        Responsável por instanciar e armazenar um objeto de personagem (Guerreiro ou Mago)
        com base na entrada do usuário. Garante consistência entre `personagem_obj`
        e o dicionário de metadados `self.personagem`.

        Rules:
                - O nome é obrigatório.
                - A classe é escolhida entre as opções implementadas (1 ou 2).
                - Nenhum dado é persistido neste estágio.

        Side effects:
                - Cria `self.personagem_obj`
                - Atualiza `self.personagem["nome"]` e `self.personagem["arquetipo"]`
        """
        print("=== Criação de Personagem ===")
        nome = input("Digite o nome do seu personagem: ").strip()

        print("\nEscolha uma classe:")
        print("[1] Guerreiro - Alta vida e defesa, ataque físico forte.")
        print("[2] Mago - Usa mana e ataques mágicos poderosos.")

        while True:
            escolha = input("> ").strip()
            if escolha == "1":
                personagem = Guerreiro(nome)
                break
            elif escolha == "2":
                personagem = Mago(nome)
                break
            else:
                print("Opção inválida. Escolha 1 ou 2.")

        print("\nPersonagem criado com sucesso!")
        print(f"Nome: {personagem.nome}")
        print(f"Classe: {'Guerreiro' if isinstance(personagem, Guerreiro) else 'Mago'}")
        print(f"Vida: {personagem.vida}")
        print(f"Ataque: {personagem.ataque}")
        print(f"Defesa: {personagem.defesa}")
        print(f"Mana: {personagem.mana}")

        self.personagem_obj = personagem
        self.personagem["nome"] = nome
        self.personagem["arquetipo"] = (
            "Guerreiro" if isinstance(personagem, Guerreiro) else "Mago"
        )


    # =====================================================
    # VER PERSONAGEM
    # =====================================================
    def ver_personagem(self):
        if not self.personagem_obj:
            print("Nenhum personagem criado ainda.")
            return

        p = self.personagem_obj
        print("\n=== Personagem Atual ===")
        print(f"Nome: {p.nome}")
        print(f"Vida: {p.vida}")
        print(f"Ataque: {p.ataque}")
        print(f"Defesa: {p.defesa}")
        if hasattr(p, "mana"):
            print(f"Mana: {p.mana}")

    # =====================================================
    # CHECAR INVENTÁRIO
    # =====================================================
    def checar_inventario(self):
        if not self.personagem_obj:
            print("Nenhum personagem criado.")
            return

        inventario = self.personagem_obj.inventario

        print("\n=== Inventário ===")
        if not inventario:
            print("(vazio)")
        else:
            for i, item in enumerate(inventario, 1):
                print(f"{i}. {item}")


    # =====================================================
    # USAR ITEM
    # =====================================================
    def usar_item_personagem(self):
        if not self.personagem_obj:
            print("Nenhum personagem criado.")
            return

        nome_item = input("Digite o nome do item a ser usado: ").strip()
        resultado = self.personagem_obj.usar_item(nome_item)
        print(resultado)

    # =====================================================
    # ========== MENU PRINCIPAL ===========================
    # =====================================================

    def menu_principal(self) -> None:
        """
        Loop principal de execução do jogo.

        Exibe o menu principal e redireciona o fluxo para os submenus:
        criação de personagem, missões, salvar/carregar e saída.

        Este método bloqueia a execução até que o usuário escolha sair.
        """
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("[1] Criar novo personagem")
            print("[2] Ver informações do personagem")
            print("[3] Missão")
            print("[4] Salvar Jogo (simulado)")
            print("[5] Carregar Jogo (simulado)")
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

    def ver_personagem(self) -> None:
        try:
            if hasattr(controle_personagem, "ver_personagem"):
                return controle_personagem.ver_personagem(self)
            print("[AVISO] ver_personagem() não existe em controle_personagem.")
        except Exception as e:
            print(f"[ERRO] ver_personagem: {e}")

    def menu_missao(self) -> None:
        try:
            controle_missao.menu_missao(self)
        except Exception as e:
            print(f"[ERRO] menu_missao: {e}")

    def menu_salvar(self) -> None:
        try:
            salvamento.menu_salvar(self)
        except Exception as e:
            print(f"[ERRO] menu_salvar: {e}")

    def menu_carregar(self) -> None:
        try:
            salvamento.menu_carregar(self)
        except Exception as e:
            print(f"[ERRO] menu_carregar: {e}")
