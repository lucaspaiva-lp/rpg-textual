# 🧙‍♂️ RPG Orientado a Objetos (POO)

## 📘 Sobre o Projeto

Este projeto tem como objetivo o desenvolvimento de um **RPG textual em Python**, utilizando **conceitos de Programação Orientada a Objetos (POO)**, como herança, polimorfismo, abstração e encapsulamento.

O jogo permite **criar personagens**, **enfrentar missões**, **lutar contra inimigos** e **salvar/carregar o progresso**.

Ele está sendo desenvolvido de forma **colaborativa em equipe**, com divisão de tarefas por área (Personagem, Inimigo, Missão, Menu, etc).

---

## 🗂️ Estrutura do Projeto

<pre class="overflow-visible!" data-start="881" data-end="1065"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>├─ README.md
├─ main.py
├─ jogo.py
├─ models/
│  ├─ </span><span>base</span><span>.py
│  ├─ personagem.py
│  ├─ classes.py
│  ├─ inimigo.py
│  └─ missao.py
└─ utils/
   ├─ repositorio.py
   └─ logger.py
└─ docs/
   ├─ split.md
   └─ times.md
</span></span></code></div></div></pre>

---

## 🧩 Funcionalidades Principais

* **Criação de Personagem:** escolha de nome, classe e atributos.
* **Sistema de Inimigos:** múltiplos tipos com habilidades únicas.
* **Missões:** diferentes locais e dificuldades (Fácil, Média, Difícil).
* **Menu Principal:** interação do jogador com o jogo.
* **Salvar / Carregar:** simulado com placeholders para persistência futura.
* **Sistema de Combate (em desenvolvimento):** cálculo de dano, defesa e mana.

---

## 🧱 Estrutura de Times

### 🛡️ **Time 1 — Personagens (Heróis)**

**Integrantes:**

* @Mateus Alves
* @~Felipe Trabalho

**Responsabilidades:**

* Criar e ajustar as classes jogáveis (Guerreiro, Mago, Arqueiro, etc).
* Implementar atributos e habilidades especiais dos heróis.

---

### 👹 **Time 2 — Inimigos**

**Integrantes:**

* @~Gui Silva
* @nicolas
* @camp-1
* @gohan

**Responsabilidades:**

* Desenvolver inimigos comuns e únicos, com habilidades próprias.
* Preparar inimigos para integração com as missões.

---

### ⚔️ **Time 3 — Missões**

**Integrantes:**

* @~Maria Eduarda
* @~Rian Alves

**Responsabilidades:**

* Criar as classes de missões (Fácil, Média, Difícil).
* Associar inimigos, locais e recompensas conforme a dificuldade.

---

### 🧭 **Time 4 — Menu Principal**

**Integrante:**

* @~Alexandre

**Responsabilidades:**

* Implementar o menu principal e suas interações com as outras partes do jogo.
* Garantir a navegação entre as opções (criar personagem, missão, salvar/carregar).

---

### 🧱 **Time 5 — Organização e GitHub**

**Integrante:**

* @Lucas

**Responsabilidades:**

* Organizar o repositório no GitHub conforme o padrão definido.
* Criar e manter o arquivo `README.md`.

---

### ⚙️ **Time 6 — Suporte Master**

**Integrante:**

* @Rodrigo Moraes

**Responsabilidades:**

* Suporte técnico geral e integração entre os módulos.
* Revisão de código e orientação do grupo.

---

## 🗓️ Cronograma de Desenvolvimento

### **Semana 1 — Fundamentos de POO**

**Objetivos:**

* Implementar as classes básicas (`Personagem`, `Inimigo`, `Missao`, `Jogo`).
* Criar menu inicial com as opções principais.

**Status:**

✅ Estrutura básica implementada.

⚠️ Ajustes de sintaxe e integração ainda necessários.

---

### **Semana 2 — Regras, Coleções e Funções**

**Objetivos:**

* Adicionar funções auxiliares e listas de inimigos/missões.
* Implementar inventário e sistema de sorteio de inimigos.
* Exibir dados de combate e logs de turnos.

**Status:**

🛠️ Em desenvolvimento.

---

### **Semana 3 — Polimorfismo, Herança e Persistência**

**Objetivos:**

* Criar subclasses com habilidades próprias (ex.: Arqueiro, Chefão, etc).
* Implementar persistência com JSON e logs de eventos.
* Aplicar polimorfismo entre classes.

**Status:**

📅 Planejado.

---

## 💻 Como Executar

1. Certifique-se de ter o **Python 3.10+** instalado.
2. Clone o repositório:
   <pre class="overflow-visible!" data-start="3982" data-end="4030"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> <URL_DO_REPOSITORIO>
   </span></span></code></div></div></pre>
3. Acesse o diretório do projeto:
   <pre class="overflow-visible!" data-start="4068" data-end="4096"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>cd</span><span> RPG-POO
   </span></span></code></div></div></pre>
4. Execute o jogo:
   <pre class="overflow-visible!" data-start="4119" data-end="4151"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python main.py
   </span></span></code></div></div></pre>

---

## 📚 Tecnologias Utilizadas

* **Linguagem:** Python
* **Paradigma:** Programação Orientada a Objetos (POO)
* **Módulos utilizados:** `dataclasses`, `random`, `json` (futuro)

---

## 👥 Equipe

- **[@MateusAlves](https://github.com/AlvesTK)** — Desenvolvimento de Personagens
- **[@Rodrigo](https://github.com/RodrigoDevBack)** — Suporte Master e Github
- **[@GuiSilva](https://github.com/Gohanphp)** — Sistema de Inimigos
- **[@LucasPaiva](https://github.com/lucaspaiva-lp)** — Organização, GitHub e Sistema de Menu
- **[@MariaEduarda](https://github.com/mariaeduarda63)** — Sistema de Missões
- **[@Nicolas](https://github.com/nicolas021007)** — Sistema de Inimigos
- **[@Rian](https://github.com/RianAlvesTi)** — Sistema de Missões
- **[@Alexandre](https://github.com/alexandrexande)** — Sistema de Menu
- **[@Felipe](https://github.com/FIGFelip)** — Desenvolvimento de Personagens
- **[@Cauan](https://github.com/Camp-1)** — Sistema de Inimigos

## ✨ Créditos

Projeto desenvolvido pela equipe de  (nome da equipe) **- 2025** , como parte da disciplina de  **Paradigmas de linguagens de programação em python** .
