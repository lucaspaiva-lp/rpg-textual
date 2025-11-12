from __future__ import annotations
from models.aventura_classes import Guerreiro, Mago


class Jogo:
	"""
	Núcleo de controle do RPG textual.

	Centraliza o fluxo principal do jogo, incluindo menus, criação de personagens,
	configuração de missões e operações simuladas de salvamento e carregamento.

	Esta classe atua como ponto de entrada para integração futura com as demais camadas:
	- models (Personagem, Inimigo, Missão)
	- utils (Logger, Repositório)
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
		print(f"Configuração atual: {self.missao_config['dificuldade']} - {self.missao_config['cenario']}")

		# Cria inimigo simulado (não depende de Missao)
		inimigo = type("InimigoSimulado", (), {
			"nome": "Goblin",
			"vida": 60,
			"ataque": 8,
			"defesa": 3
		})()

		jogador = self.personagem_obj
		turno = 1
		log_batalha = []

		# Loop de combate simples
		while jogador.vida > 0 and inimigo.vida > 0:
			print(f"\n--- Turno {turno} ---")

			# Ataque do jogador
			dano_jogador = max(jogador.ataque - inimigo.defesa, 0)
			inimigo.vida -= dano_jogador
			log_batalha.append(f"{jogador.nome} causou {dano_jogador} de dano em {inimigo.nome}.")

			if inimigo.vida <= 0:
				print(f"{inimigo.nome} foi derrotado!")
				break

			# Ataque do inimigo
			dano_inimigo = max(inimigo.ataque - jogador.defesa, 0)
			jogador.vida -= dano_inimigo
			log_batalha.append(f"{inimigo.nome} causou {dano_inimigo} de dano em {jogador.nome}.")

			print(f"🧙 {jogador.nome} HP: {jogador.vida} | ⚔️ {inimigo.nome} HP: {inimigo.vida}")
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
		print("- Uma futura implementação pode usar essas escolhas para montar encontros.")

	# =====================================================
	# ========== SALVAR E CARREGAR ========================
	# =====================================================

	def menu_salvar(self) -> None:
		"""
		Submenu de salvamento de progresso (simulado).

		Nenhuma gravação real em disco é feita neste estágio.
		"""
		while True:
			print("\n=== Salvar ===")
			print("[1] Salvar rápido (simulado)")
			print("[2] Salvar com nome (simulado)")
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
		"""Executa uma simulação de salvamento rápido em memória."""
		self._ultimo_save = "quick_save.json"
		print(f"✔ Salvo (simulado) em: {self._ultimo_save}")

	def _salvar_nomeado(self) -> None:
		"""Solicita um nome de arquivo e simula o salvamento."""
		nome = input("Nome do arquivo de save (ex.: meu_jogo.json): ").strip() or "save.json"
		self._ultimo_save = nome
		print(f"✔ Salvo (simulado) em: {self._ultimo_save}")

	def _ajuda_salvar(self) -> None:
		"""Exibe instruções sobre o menu de salvamento."""
		print("\nAjuda — Salvar")
		print("- Salvar rápido usa um nome padrão fictício.")
		print("- Salvar nomeado permite escolher um nome fictício.")
		print("- Não há escrita em disco nesta base — é apenas navegação.")

	def menu_carregar(self) -> None:
		"""Submenu para simular carregamento de progresso salvo."""
		while True:
			print("\n=== Carregar ===")
			print("[1] Carregar último save (simulado)")
			print("[2] Carregar por nome (simulado)")
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
		"""Recupera o último save simulado da sessão atual."""
		if self._ultimo_save:
			self._ultimo_load = self._ultimo_save
			print(f"✔ Carregado (simulado) de: {self._ultimo_load}")
		else:
			print("Nenhum save recente encontrado (simulado).")

	def _carregar_nomeado(self) -> None:
		"""Permite informar manualmente o nome de um arquivo para simular o carregamento."""
		nome = input("Nome do arquivo para carregar (ex.: meu_jogo.json): ").strip()
		if nome:
			self._ultimo_load = nome
			print(f"✔ Carregado (simulado) de: {self._ultimo_load}")
		else:
			print("Nome não informado.")

	def _ajuda_carregar(self) -> None:
		"""Exibe instruções sobre o submenu de carregamento."""
		print("\nAjuda — Carregar")
		print("- O carregamento aqui é apenas ilustrativo (sem leitura real).")
		print("- Use o nome que você “salvou” anteriormente para simular.")


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
