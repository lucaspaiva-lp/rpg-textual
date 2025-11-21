-

# 🧙‍♂️ RPG Orientado a Objetos (POO)

## 📘 Sobre o Projeto

Este projeto é um **RPG textual desenvolvido em Python**, estruturado com **Programação Orientada a Objetos (POO)**.

O objetivo é criar uma arquitetura modular e escalável, utilizando conceitos como **herança**, **polimorfismo**, **abstração** e **encapsulamento.**

O jogo permite criar personagens, enfrentar inimigos, realizar missões e salvar/carregar o progresso, tudo de forma colaborativa e organizada entre equipes.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Paradigma:** Programação Orientada a Objetos (POO)
- **Bibliotecas padrão:**
  - `dataclasses`
  - `random`
  - `json` (modelo de persistência)
- **Estrutura modular:**
  - `models/`
  - `utils/`
  - `docs/`

---

## 💻 Como Rodar o Projeto (Código-fonte)

Caso você esteja utilizando a versão em **Python** (não o executável):

1. Certifique-se de ter **Python 3.10 ou superior** instalado.
2. Clone o repositório:
   <pre class="overflow-visible!" data-start="522" data-end="570"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> <URL_DO_REPOSITORIO>
   </span></span></code></div></div></pre>
3. Acesse o diretório do projeto:
   <pre class="overflow-visible!" data-start="608" data-end="636"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>cd</span><span> rpg-textual
   </span></span></code></div></div></pre>
4. Execute o jogo:
   <pre class="overflow-visible!" data-start="659" data-end="691"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python main.py
   </span></span></code></div></div></pre>

---

## 💾 Como Rodar o Jogo (Executáveis da Release)

Escolha o arquivo conforme o seu sistema operacional:

### 🪟 **Windows**

Baixe o arquivo:

* **rpg-v1.0.0-windows.exe**

E execute com um clique —  **não é necessário ter Python instalado** .

---

### 🐧 **Linux**

Baixe o arquivo:

* **rpg-v1.0.0-linux**

Dê permissão de execução (apenas na primeira vez):

<pre class="overflow-visible!" data-start="1113" data-end="1150"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>chmod</span><span> +x rpg-v1.0.0-linux
</span></span></code></div></div></pre>

Depois execute normalmente:

<pre class="overflow-visible!" data-start="1181" data-end="1211"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>./rpg-v1.0.0-linux
</span></span></code></div></div></pre>

---

### 🧩 Código-fonte (para desenvolvedores)

Na seção *Assets* você também encontrará:

* **Source code (zip)**
* **Source code (tar.gz)**

Essas versões contêm o código completo e exigem Python para executar.

---

## 🧩 Funcionalidades

- **Criação de Personagem** : classes, atributos e escolha inicial.
- **Sistema de Combate Dinâmico** : atacar, usar item e fugir.
- **Sistema de Inimigos** : múltiplos tipos, níveis e habilidades.
- **Missões** : três níveis de dificuldade com diferentes recompensas.
- **Menu Principal** : criação, carregamento, combate e navegação.
- **Sistema de Salvamento (POO)** : repositório orientado a objetos para persistência.
- **Logs de Jogo** : registro de ações e eventos.

---

## 🗂️ Estrutura Básica do Projeto

<pre class="overflow-visible!" data-start="1787" data-end="2176"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>├─ README.md
├─ main.py
├─ jogo.py
├─ models/
│  ├─ </span><span>base</span><span>.py
│  ├─ personagem.py
│  ├─ classes.py
│  ├─ inimigo.py
│  └─ missao.py
├─ utils/
│  ├─ repositorio.py
│  └─ logger.py
└─ docs/
   ├─ gerais/
   │  ├─ checklist.md
   │  ├─ escolpo.md
   │  ├─ explicacao_classes.md
   │  ├─ times.md
   │  ├─ Trabalho_de_Paradigmas.pdf
   ├─ readme/
   │  ├─ arquitetura.md
   │  ├─ combate.md
   │  ├─ personagens.md
   │  ├─ inimigos.md
   │  ├─ missoes.md
   │  ├─ salvamento.md
   │  └─ roadmap.md
   ├─ split.md
   └─ times.md
</span></span></code></div></div></pre>

---

## 👥 Equipe

**[@Mateus Alves](https://github.com/AlvesTK)** — Desenvolvimento de Personagens

**[@Rodrigo Moraes](https://github.com/RodrigoDevBack)** — Desenvolvimento Geral, Refatoração e Github

**[@Guilherme da Silva](https://github.com/Gohanphp)** — Desenvolvimento de Inimigos

**[@Lucas Paiva](https://github.com/lucaspaiva-lp-lp)** — Desenvolvimento Geral, Refatoração, Organização, Integração, Documentação

**[@Maria Eduarda](https://github.com/mariaeduarda63)** — Desenvolvimento de Missões

**[@Nicolas](https://github.com/nicolas021007)** — Desenvolvimento de Inimigos

**[@Rian Alves](https://github.com/RianAlvesTi)** — Desenvolvimento de Missões

**[@Alexandre Arcanjo](https://github.com/alexandrexande)** — Desenvolvimento do Menu

**[@Felipe Gonçalves](https://github.com/FIGFelip)** — Desenvolvimento de Personagens

**[@Cauan Arnoldo](https://github.com/Camp-1)** — Desenvolvimento de Inimigos

---

## 📚 Documentação Completa

Para informações detalhadas sobre cada módulo, consulte a pasta `docs/readme/`:

- **[Arquitetura](/docs/readme/arquitetura.md)**
- **[Sistema de Combate](/docs/readme/sistema-de-combate.md)**
- **[Personagens](/docs/readme/personagens.md)**
- **[Inimigos]()**
- **[Missões](/docs/readme/missao.md)**
- **[Sistema de Salvamento](/docs/readme/salvamento.md)**
- **[Roadmap](/docs/readme/roadmap.md)**
