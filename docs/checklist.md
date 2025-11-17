## **SEMANA 1 — Fundamentos de POO**

### **Objetivo geral:**

Criar a base estrutural do jogo utilizando conceitos fundamentais de Programação Orientada a Objetos — classes, atributos, métodos e menu principal.

---

### **CHECKLIST SEMANA 1**

#### **Implementar as classes básicas (Personagem, Inimigo, Missão, Jogo)**

* [X] Estrutura da classe `Jogo` criada (menu, placeholders de métodos).
* [ ] Estrutura da classe `Missao` criada (com construtor e método `executar`).
* [X] Estrutura base `Entidade` criada corretamente (vida, ataque, defesa, etc.).
* [ ] Classe `Personagem` implementada com erros — métodos `__init__`, `calcular_dano_base` e `habilidade_especial` precisam ser corrigidos e finalizados.
* [X] Classe `Inimigo` implementada com erros de sintaxe (`def_init_`, `super()._init_`) e precisa ser revisada para rodar corretamente.
* [ ] Classes derivadas (`Guerreiro`, `Mago`, `Goblin`, `Ladrão`) ainda precisam de ajustes de sintaxe e integração funcional.

---

#### **Utilizar construtores (`__init__`), atributos e métodos**

* [X] Uso correto em `Entidade`, `Missao` e `Jogo`.
* [ ] Construtores incorretos em `Personagem` e `Inimigo` — precisam de revisão de nome e uso do `super()`.
* [ ] Métodos principais (`atacar`, `receber_dano`, `habilidade_especial`) precisam ser implementados de forma funcional, não apenas declarados.

---

#### **Criar um menu inicial com opções**

* [X] Criar personagem — opção presente no menu e chama o método correspondente.
* [X] Encarar missão — opção presente, ainda que simule o resultado.
* [X] Salvar / Carregar jogo — opções já incluídas no menu (mesmo que sejam placeholders).
* [X] Sair — opção funcional e encerrando o loop principal.

---

#### **Entregável da Semana 1**

> **Versão funcional do jogo com personagens e missões simples.**

* [X] Estrutura do jogo funcional (menu roda sem erro).
* [ ] Implementações internas incompletas (combate e métodos das classes).
* [ ] Falta o mínimo de jogabilidade real — tudo ainda é simulado.

---

## **SEMANA 2 — Regras, Coleções e Funções**

### Objetivo geral:

Aprimorar o sistema de combate, inventário e missões, além de começar a estruturar a lógica do jogo (sem herança complexa ainda).

---

### **CHECKLIST SEMANA 2**

#### Organização e Estrutura

* [ ] Criar listas e dicionários para organizar:
  * [ ] Inimigos disponíveis.
  * [ ] Itens e recompensas.
  * [ ] Missões disponíveis (por dificuldade ou local).

#### Funções e Utilidades

* [ ] Criar funções auxiliares para:
  * [ ] Sorteio de inimigos (módulo `random`).
  * [ ] Sorteio de missões e recompensas.
  * [ ] Validação de entradas (ex.: checar se input é número ou string válida).
* [ ] Criar funções de tratamento de erro para inputs incorretos.

#### Sistema de Combate

* [ ] Exibir dados de combate:
  * [ ] HP atual e dano sofrido.
  * [ ] Turnos e ações realizadas.
  * [ ] Vitória ou derrota ao final.
* [ ] Criar logs simples de turnos (mensagens informativas durante o combate).

#### Inventário e Itens

* [ ] Implementar inventário funcional no personagem:
  * [ ] Adicionar/Remover itens.
  * [ ] Criar itens de cura e mana.
  * [ ] Permitir uso dos itens durante o combate.

#### Missões

* [ ] Criar 4 locais básicos com missões de diferentes dificuldades.
* [ ] Associar cada local a tipos de inimigos específicos.
* [ ] Permitir escolha da dificuldade no menu antes da missão.

#### Inimigos

* [ ] Criar variedade de inimigos comuns (mínimo 10 para esta fase).
* [ ] Definir atributos básicos e pequenas variações (vida, ataque, defesa).
* [ ] Criar um sistema de rotação aleatória de inimigos.

#### Menu

* [ ] Atualizar o menu para:
  * [ ] Exibir opções dinâmicas de combate.
  * [ ] Mostrar estado atual do personagem (vida, mana, itens).

#### Entregável Semana 2

> Versão com múltiplos inimigos, missões e inventário funcional, incluindo logs de turnos de batalha.

---

## **SEMANA 3 — Polimorfismo, Herança e Persistência**

### Objetivo geral:

Finalizar a hierarquia de classes, adicionar herança real entre personagens e inimigos, implementar persistência (salvar/carregar) e logs completos.

---

### **CHECKLIST SEMANA 3**

#### Herança e Polimorfismo

* [ ] Criar subclasses de Personagem:
  * [ ] Arqueiro.
  * [ ] Ladino.
  * [ ] Curandeiro/Paladino.
* [ ] Criar subclasses de Inimigo:
  * [ ] Chefões (Inimigos únicos).
  * [ ] Inimigos mágicos (com mana e ataques especiais).
* [ ] Implementar métodos sobrescritos:
  * [ ] `atacar()` com comportamento distinto.
  * [ ] `habilidade_especial()` com efeito único.

#### Persistência

* [ ] Implementar salvamento e carregamento de dados com `json`:
  * [ ] Personagem (nome, atributos, inventário).
  * [ ] Progresso de missões.
  * [ ] Itens obtidos e inimigos derrotados.

#### Logs e Histórico

* [ ] Criar sistema de log real (usando `utils/logger.py`).
* [ ] Registrar eventos importantes:
  * [ ] Início e fim de combate.
  * [ ] Vitória e derrota.
  * [ ] Itens coletados e missões concluídas.

#### Ajustes Finais

* [ ] Revisar estrutura de diretórios e código (`main.py`, `jogo.py`).
* [ ] Garantir integração entre as classes e o menu.
* [ ] Testar persistência e reabertura de jogo salvo.

#### Entregável Semana 3

> Versão final do jogo com hierarquia de classes (POO completa), logs detalhados e persistência de dados (salvar/carregar jogo).
