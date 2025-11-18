# =====================================================
# ========== IMPORTAÇÕES PRINCIPAIS ===================
# =====================================================
# Define compatibilidade futura e importa classes e libs
# usadas na persistência (salvar/carregar progresso).

from __future__ import annotations
import os
import json
from models.aventura_classes import Guerreiro, Mago


class Jogo:
    """Controla o núcleo do RPG textual e o fluxo principal do jogo.

    Gerencia menus, criação de personagens, configuração de missões e
    operações de salvamento e carregamento. Atua como ponto de entrada
    para integração com outras camadas do sistema (models e utils).
    """

    def __init__(self) -> None:
        """
        Inicializa o estado base do jogo em memória.
        Nenhum dado é persistido neste estágio.
        """
        self.personagem = {
            "nome": None,
            "arquetipo": None,  # ex.: "Guerreiro", "Mago"
        }
        self.missao_config = {
            "dificuldade": "Fácil",
            "cenario": "Trilha",
        }
        self._ultimo_save = None
        self._ultimo_load = None

    # =====================================================
    # ========== CRIAÇÃO DE PERSONAGEM - PROTOTICO ========
    # =====================================================

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
            print("\n=== Criar Personagem ===")
            print(f"Nome atual: {self.personagem['nome'] or '(não definido)'}")
            print(f"Arquétipo:  {self.personagem['arquetipo'] or '(não definido)'}")
            print("[1] Definir nome")
            print("[2] Escolher arquétipo")
            print("[3] Confirmar criação")
            print("[9] Ajuda")
            print("[0] Voltar")
            op = input("> ").strip()

            if op == "1":
                self._definir_nome()
            elif op == "2":
                self._escolher_arquetipo()
            elif op == "3":
                self._confirmar_criacao()
            elif op == "9":
                self._ajuda_criar_personagem()
            elif op == "0":
                break
            else:
                print("Opção inválida.")

    def _definir_nome(self) -> None:
        nome = input("Digite o nome do personagem: ").strip()
        if nome:
            self.personagem["nome"] = nome
            print(f"Nome definido: {nome}")
        else:
            print("Nome não alterado.")

    def _escolher_arquetipo(self) -> None:
        print("\nArquétipos disponíveis (apenas ilustrativos):")
        print("[1] Guerreiro")
        print("[2] Mago")
        print("[3] Arqueiro")
        print("[4] Curandeiro")
        print("[5] Personalizado")
        escolha = input("> ").strip()

        mapa = {
            "1": "Guerreiro",
            "2": "Mago",
            "3": "Arqueiro",
            "4": "Curandeiro",
            "5": "Personalizado",
        }
        arq = mapa.get(escolha)
        if arq:
            self.personagem["arquetipo"] = arq
            print(f"Arquétipo definido: {arq}")
        else:
            print("Opção inválida. Arquétipo não alterado.")

    def _confirmar_criacao(self) -> None:
        if not self.personagem["nome"]:
            print("Defina um nome antes de confirmar a criação.")
            return
        if not self.personagem["arquetipo"]:
            print("Escolha um arquétipo antes de confirmar a criação.")
            return
        print("\nPersonagem criado com sucesso!")
        print(
            f"Nome: {self.personagem['nome']} | Arquétipo: {self.personagem['arquetipo']}"
        )

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
        """
        Exibe os atributos atuais do personagem em memória.

        Se nenhum personagem tiver sido criado, notifica o usuário.
        """
        if hasattr(self, "personagem_obj"):
            p = self.personagem_obj
            print("\n=== Dados do Personagem ===")
            print(f"Nome: {p.nome}")
            print(f"Classe: {self.personagem['arquetipo']}")
            print(f"Vida: {p.vida}")
            print(f"Ataque: {p.ataque}")
            print(f"Defesa: {p.defesa}")
            print(f"Mana: {p.mana}")
            print(f"Inventário: {p.get_inventario()}")
        else:
            print("Nenhum personagem criado ainda.")

    # =====================================================
    # ========== MISSÕES - PROTOTICO DE TESTE =============
    # =====================================================

    def menu_missao(self) -> None:
        """
        Submenu de missões.

        Permite ao jogador configurar e visualizar detalhes da missão antes da execução.
        Os valores são armazenados em `self.missao_config`.
        """
        while True:
            print("\n=== Missão ===")
            print(f"Dificuldade atual: {self.missao_config['dificuldade']}")
            print(f"Cenário atual:     {self.missao_config['cenario']}")
            print("[1] Escolher dificuldade")
            print("[2] Escolher cenário")
            print("[3] Pré-visualizar missão")
            print("[4] Iniciar missão (placeholder)")
            print("[9] Ajuda")
            print("[0] Voltar")
            op = input("> ").strip()

            if op == "1":
                self._escolher_dificuldade()
            elif op == "2":
                self._escolher_cenario()
            elif op == "3":
                self._preview_missao()
            elif op == "4":
                self._iniciar_missao_placeholder()
            elif op == "9":
                self._ajuda_missao()
            elif op == "0":
                break
            else:
                print("Opção inválida.")

    def _escolher_dificuldade(self) -> None:
        """
        Atualiza o nível de dificuldade da missão.

        Mantém consistência com os valores permitidos:
        "Fácil", "Média" ou "Difícil".
        """
        print("\nDificuldades:")
        print("[1] Fácil")
        print("[2] Média")
        print("[3] Difícil")
        op = input("> ").strip()
        mapa = {"1": "Fácil", "2": "Média", "3": "Difícil"}
        dif = mapa.get(op)
        if dif:
            self.missao_config["dificuldade"] = dif
            print(f"Dificuldade definida: {dif}")
        else:
            print("Opção inválida.")

    def _escolher_cenario(self) -> None:
        """
        Define o cenário visual/temático da missão.

        Este método apenas altera o valor textual em `self.missao_config["cenario"]`.
        """
        print("\nCenários:")
        print("[1] Trilha")
        print("[2] Floresta")
        print("[3] Caverna")
        print("[4] Ruínas")
        op = input("> ").strip()
        mapa = {"1": "Trilha", "2": "Floresta", "3": "Caverna", "4": "Ruínas"}
        cen = mapa.get(op)
        if cen:
            self.missao_config["cenario"] = cen
            print(f"Cenário definido: {cen}")
        else:
            print("Opção inválida.")

    def _preview_missao(self) -> None:
        """
        Exibe uma prévia textual dos parâmetros atuais da missão.

        Placeholder — a lógica de geração de inimigos e recompensas
        será implementada em versões futuras.
        """
        print("\nPré-visualização da Missão")
        print(f"- Dificuldade: {self.missao_config['dificuldade']}")
        print(f"- Cenário:     {self.missao_config['cenario']}")
        print("- Inimigos e recompensas: (em breve)")
        print("- Regras de combate: (em breve)")

    def _iniciar_missao_placeholder(self) -> None:
        """
        Executa um placeholder de missão com combate simulado.

        Este método não depende da classe Missao neste estágio.
        Implementa um loop de combate simples entre o personagem
        e um inimigo fictício, exibindo o resultado ao final.
        """
        if not self.personagem["nome"]:
            print("Crie um personagem antes de iniciar uma missão.")
            return

        print("\nIniciando missão...")
        print(
            f"Configuração atual: {self.missao_config['dificuldade']} - {self.missao_config['cenario']}"
        )

        # Cria inimigo simulado (não depende de Missao)
        inimigo = type(
            "InimigoSimulado",
            (),
            {"nome": "Goblin", "vida": 60, "ataque": 8, "defesa": 3},
        )()

        jogador = self.personagem_obj
        turno = 1
        log_batalha = []

        # Loop de combate simples
        while jogador.vida > 0 and inimigo.vida > 0:
            print(f"\n--- Turno {turno} ---")

            # Ataque do jogador
            dano_jogador = max(jogador.ataque - inimigo.defesa, 0)
            inimigo.vida -= dano_jogador
            log_batalha.append(
                f"{jogador.nome} causou {dano_jogador} de dano em {inimigo.nome}."
            )

            if inimigo.vida <= 0:
                print(f"{inimigo.nome} foi derrotado!")
                break

            # Ataque do inimigo
            dano_inimigo = max(inimigo.ataque - jogador.defesa, 0)
            jogador.vida -= dano_inimigo
            log_batalha.append(
                f"{inimigo.nome} causou {dano_inimigo} de dano em {jogador.nome}."
            )

            print(
                f"🧙 {jogador.nome} HP: {jogador.vida} | ⚔️ {inimigo.nome} HP: {inimigo.vida}"
            )
            turno += 1

        # Exibição do resultado e log
        resultado = "✅ Vitória!" if jogador.vida > 0 else "💀 Derrota..."
        print(f"\n=== Fim da Missão ===\nResultado: {resultado}")

        print("\n=== Log de Batalha ===")
        for evento in log_batalha:
            print(evento)

        print("\nRetornando ao menu de Missão...")

    def _ajuda_missao(self) -> None:
        """Exibe orientações sobre o uso do submenu de missões."""
        print("\nAjuda — Missão")
        print("- Selecione dificuldade e cenário.")
        print("- A opção 'Iniciar missão' executará apenas um placeholder.")
        print(
            "- Uma futura implementação pode usar essas escolhas para montar encontros."
        )

    # =====================================================
    # ========== SALVAR E CARREGAR (PERSISTENTE) ==========
    # =====================================================

    def menu_salvar(self) -> None:
        """Submenu de salvamento do jogo."""
        os.makedirs("saves", exist_ok=True)

        while True:
            print("\n=== Salvar ===")
            print("[1] Salvar rápido")
            print("[2] Salvar com nome")
            print("[9] Ajuda")
            print("[0] Voltar")
            op = input("> ").strip()

            if op == "1":
                self._salvar_rapido()
            elif op == "2":
                self._salvar_nomeado()
            elif op == "9":
                self._ajuda_salvar()
            elif op == "0":
                break
            else:
                print("Opção inválida.")

    def _salvar_rapido(self) -> None:
        """Realiza um salvamento automático padrão."""
        caminho = os.path.join("saves", "quick_save.json")
        self._salvar_dados(caminho)
        self._ultimo_save = caminho
        print(f"✔ Progresso salvo em: {caminho}")

    def _salvar_nomeado(self) -> None:
        """Permite escolher o nome do arquivo de salvamento."""
        nome = input("Nome do arquivo (sem extensão): ").strip() or "meu_jogo"
        caminho = os.path.join("saves", f"{nome}.json")
        self._salvar_dados(caminho)
        self._ultimo_save = caminho
        print(f"✔ Progresso salvo em: {caminho}")

    def _salvar_dados(self, caminho: str) -> None:
        """Serializa os dados do jogo e grava em disco no formato JSON."""
        try:
            dados = {
                "personagem": self.personagem,
                "missao_config": self.missao_config,
            }
            if hasattr(self, "personagem_obj"):
                p = self.personagem_obj
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

    def _ajuda_salvar(self) -> None:
        """Exibe instruções sobre o menu de salvamento."""
        print("\nAjuda — Salvar")
        print("- Agora o jogo salva dados reais em formato JSON.")
        print("- Os arquivos ficam armazenados na pasta `saves/`.")
        print("- Use nomes curtos e sem espaços para evitar erros.")

    # =====================================================
    # ========== CARREGAR ================================
    # =====================================================

    def menu_carregar(self) -> None:
        """Submenu para carregamento real de progresso."""
        os.makedirs("saves", exist_ok=True)

        while True:
            print("\n=== Carregar ===")
            print("[1] Carregar último save")
            print("[2] Carregar por nome")
            print("[9] Ajuda")
            print("[0] Voltar")
            op = input("> ").strip()

            if op == "1":
                self._carregar_ultimo()
            elif op == "2":
                self._carregar_nomeado()
            elif op == "9":
                self._ajuda_carregar()
            elif op == "0":
                break
            else:
                print("Opção inválida.")

    def _carregar_ultimo(self) -> None:
        """Restaura o último save conhecido na sessão."""
        if not self._ultimo_save:
            print("Nenhum save encontrado nesta sessão.")
            return
        self._carregar_dados(self._ultimo_save)

    def _carregar_nomeado(self) -> None:
        """Permite carregar manualmente um arquivo de save."""
        nome = input("Nome do arquivo (sem extensão): ").strip()
        caminho = os.path.join("saves", f"{nome}.json")

        if not os.path.exists(caminho):
            print("Arquivo não encontrado.")
            return

        self._carregar_dados(caminho)

    def _carregar_dados(self, caminho: str) -> None:
        """Lê o arquivo JSON e restaura os dados do jogo na memória."""
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)

            self.personagem = dados.get("personagem", {})
            self.missao_config = dados.get("missao_config", {})

            if "personagem_detalhes" in dados:
                det = dados["personagem_detalhes"]
                arqu = self.personagem.get("arquetipo")
                nome = self.personagem.get("nome")

                if arqu == "Guerreiro":
                    self.personagem_obj = Guerreiro(nome)
                elif arqu == "Mago":
                    self.personagem_obj = Mago(nome)

                if hasattr(self, "personagem_obj"):
                    p = self.personagem_obj
                    p.vida = det.get("vida", p.vida)
                    p.ataque = det.get("ataque", p.ataque)
                    p.defesa = det.get("defesa", p.defesa)
                    p.mana = det.get("mana", p.mana)
                    p.inventario = det.get("inventario", [])

            self._ultimo_load = caminho
            print(f"✔ Jogo carregado com sucesso de: {caminho}")
        except Exception as e:
            print(f"❌ Erro ao carregar: {e}")

    def _ajuda_carregar(self) -> None:
        """Exibe orientações sobre o sistema de carregamento."""
        print("\nAjuda — Carregar")
        print("- Carrega arquivos JSON localizados na pasta `saves/`.")
        print("- Use o mesmo nome usado ao salvar (sem `.json`).")
        print("- Apenas arquivos válidos e bem formatados serão aceitos.")


# =====================================================
# ========== ENTRY POINT ==============================
# =====================================================

if __name__ == "__main__":
    """
    Entry point da aplicação.

    Instancia o núcleo do jogo e inicia o menu principal.
    """
    jogo = Jogo()
    jogo.menu_principal()
