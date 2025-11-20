# 🏛️ Arquitetura do Projeto

### _Visão Geral Profissional_

Este documento descreve a arquitetura do sistema do jogo **RPG Orientado a Objetos**, estruturado em Python.

O projeto utiliza uma combinação de boas práticas arquiteturais adequadas para jogos de terminal, incluindo **MVC,** **Arquitetura em Camadas**, **Repository Pattern**, módulos de serviço e princípios de POO.

---

# 1. Arquitetura Predominante: **MVC (Model–View–Controller)**

Mesmo sem frameworks, o projeto segue de forma clara o padrão **MVC**, separando responsabilidades entre:

---

## **Model — Lógica de Negócio**

Onde ficam as regras principais do jogo, estados e comportamentos.

Localizados na pasta:

<pre class="overflow-visible!" data-start="961" data-end="976"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>models/
</span></span></code></div></div></pre>

Inclui:

- `personagem.py` → classes como **Guerreiro**, **Mago**, etc.
- `inventario.py` → controle de itens, equipamentos e consumo.
- `itens.py` e `equipamentos.py` → estrutura de itens do jogo.
- `inimigo.py` → inimigos, chefes, atributos e regras.
- `jogo.py` (parte do domínio) → lógica estrutural do jogo.
- `logger.py` → regras de registro de eventos.

### ✨ Responsabilidades do Model:

- Atributos e estados do jogo
- Regras de combate
- Regras de missão
- Cálculo de dano/defesa
- Manipulação de inventário
- Classes e heranças do personagem

---

## **📌 View — Interface / Exibição**

A interface atual é baseada no terminal:

- `print()` para exibir informações
- `input()` para coletar ações do jogador

Origem:

- Menus (arquivos de menu)
- Exibição de combate
- Exibição de status
- Mensagens de missão

### ✨ Responsabilidades da View:

- Mostrar informações ao jogador
- Receber entrada do usuário
- Não contém lógica de negócio

---

## **📌 Controller — Fluxo / Mediação**

Responsável por “ligar” Model e View.

Exemplos claros:

- `jogo.py` → controla o loop principal, mudanças de menu, criação de personagem
- `controle_missao.py` → gerencia turnos, combate, escolha do jogador
- Funções que interpretam inputs e aplicam ações

### ✨ Responsabilidades do Controller:

- Interpretar ações do usuário
- Chamar métodos do Model
- Atualizar a View
- Controlar fluxo do jogo

---

# 2. Arquitetura de 3 Camadas (Layered Architecture)

O projeto também se organiza muito bem em camadas:

---

## **🔹 Camada 1 — Domínio (Regras do Jogo)**

Representa o **coração da lógica**.

Inclui:

- Personagens
- Inimigos
- Itens e Inventário
- Classes de Missões
- Sistema de Combate
- Logger

---

## **🔹 Camada 2 — Aplicação (Serviços / Controle)**

Coordena o funcionamento do jogo.

Inclui:

- `jogo.py` → gerencia estados e navegação
- `repositorio_jogo.py` → salva/carrega jogo
- `controle_missao.py` → fluxo de missões e combate

---

## **🔹 Camada 3 — Interface (UI)**

Toda a interface de texto:

- Menus
- Entrada de usuário
- Impressões no terminal

---

# 3. Padrões Adicionais Existentes

Além de MVC e camadas, o projeto utiliza outros padrões profissionais:

---

## **📌 Repository Pattern**

Arquivo:

<pre class="overflow-visible!" data-start="3296" data-end="3323"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>repositorio_jogo.py
</span></span></code></div></div></pre>

Funções:

- Serialização de objetos
- Deserialização
- Salvamento em JSON
- Carregamento do progresso

Equivale a:

✔ Repository Pattern

✔ Data Mapper (transforma objetos ↔ JSON)

---

## **📌 Injeção de Dependências (Simplificada)**

Módulos recebem objetos do jogo como parâmetro, evitando dependências fixas e facilitando testes.

---

## **📌 Service Pattern (Implícito)**

O módulo:

<pre class="overflow-visible!" data-start="3726" data-end="3752"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>controle_missao.py
</span></span></code></div></div></pre>

age como um **serviço**, centralizando:

- Regras de combate
- Turnos
- Ações possíveis
- Validação de escolhas
- Interação personagem ↔ inimigo

---

# 4. Conclusão da Arquitetura

A arquitetura do sistema combina diferentes padrões modernos, resultando em um projeto modular, sustentável e apropriado para jogos via terminal.

### **Resumo Final**

| Parte                      | Responsabilidade          | Exemplos                        |
| -------------------------- | ------------------------- | ------------------------------- |
| **Model (Domínio)**        | Regras, estados e objetos | Personagem, Inimigo, Inventário |
| **Controller (Aplicação)** | Fluxo do jogo             | jogo.py, controle_missao        |
| **View (Interface)**       | Interação usuário         | prints, menus                   |
| **Repository Pattern**     | Salvamento                | repositorio_jogo                |
| **Service-like Modules**   | Combate/Missões           | controle_missao                 |

Essa arquitetura permite fácil expansão futura: novas classes, novos inimigos, novos menus — tudo sem quebrar o funcionamento existente.
