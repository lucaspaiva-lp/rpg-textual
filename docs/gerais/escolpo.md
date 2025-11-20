# **Documento de Escopo — RPG POO**

## **1. Essencial / Obrigatório**

### **Classes Principais (Núcleo do Projeto)**

* **Personagem:** representa o jogador, contendo nome, atributos e inventário.
* **Guerreiro e Mago:** subclasses com habilidades específicas de ataque e defesa.
* **Inimigo:** classe base genérica para os oponentes, com subclasses como **Goblin** e  **Lobo** .
* **Missao:** define o desafio, inimigos envolvidos e recompensas; executa o combate básico.
* **Jogo:** controla o fluxo do programa (menus, combate, salvar, carregar, etc.).
* **Repositorio:** gerencia a persistência dos dados (salvar e carregar em JSON).
* **Logger:** registra eventos e resultados em arquivo `.log`.

---

### **Semana 1 — Fundamentos de POO**

**Objetivos:**

* Implementar as classes básicas ( **Personagem** ,  **Inimigo** ,  **Missao** ,  **Jogo** ).
* Usar construtores `__init__`, atributos e métodos corretamente.
* Criar menu inicial com as opções:
  * Criar personagem
  * Encarar missão
  * Salvar / Carregar jogo
  * Sair

**Entregável:**

Versão funcional inicial com personagens e missões simples, já navegável pelo menu principal.

---

### **Semana 2 — Regras, Coleções e Funções**

**Objetivos:**

* Utilizar **listas e dicionários** para organizar inimigos, itens e missões.
* Adicionar **funções auxiliares** e controle de fluxo para validação de entradas.
* Implementar **uso do módulo random** (sorteio de inimigos, recompensas, locais).
* Criar **inventário funcional** com itens e sistema de cura/mana.
* Validar ações do jogador e exibir **dados de combate** (HP, dano, turnos, vitória e derrota).

**Entregável:**

Versão aprimorada com múltiplos inimigos, missões variadas, inventário funcional e logs simples de turnos de batalha.

---

### **Semana 3 — Polimorfismo, Herança e Persistência**

**Objetivos:**

* Criar novas subclasses ( **Arqueiro** ,  **Chefão** , etc.) com habilidades próprias.
* Implementar **métodos sobrescritos** (como `atacar()` e `habilidade_especial()`).
* Usar **módulo json** para salvar e carregar progresso de forma persistente.
* Implementar **logs de eventos** (vitórias, derrotas, itens coletados).
* Aplicar princípios de **polimorfismo** entre as classes de personagem e inimigos.

**Entregável:**

Versão final do jogo com hierarquia de classes completa, persistência de dados e sistema de logs.

---

## **2. Opcional / Expansões e Melhorias**

Esses pontos **não são obrigatórios** para o escopo mínimo, mas agregam valor, estética e profundidade ao projeto:

### **Aprimoramentos de Interface e Estilo**

* Estilizar o menu para torná-lo mais  **dinâmico durante o combate** , exibindo barras de HP e Mana.
* Incluir **mensagens narrativas** ou descrições textuais do progresso do personagem.

### **Diversidade de Personagens**

* Criar **5 classes únicas** no total (além de Guerreiro e Mago, incluir Arqueiro e outras 2 especiais).
* Cada classe deve ter  **estilo de jogo próprio** , com mecânicas e habilidades distintas.

### **Variedade de Inimigos**

* Desenvolver cerca de **20 inimigos comuns** e **5 inimigos únicos** com habilidades exclusivas.
* Relacionar tipos de inimigos aos locais das missões (ex.: inimigos de floresta não aparecem em vulcões).
* Criar  **chefes com mecânicas especiais** , como roubo de vida ou resistência mágica.

### **Missões e Locais**

* Criar **4 locais distintos** (como Floresta, Vulcão, Montanha e Castelo) com inimigos e drops específicos.
* Recompensas devem ser  **coerentes com o inimigo derrotado** , usando uma  **tabela de drops aleatórios** .

### **Sistema de Itens e Progressão**

* Permitir que  **itens sejam compartilhados entre classes** , não exclusivos.
* Garantir equilíbrio — os itens  **não devem ser mais fortes que as habilidades de classe** .
* Ao subir de nível, o jogador pode **escolher novas habilidades** (ex.: a cada 5 níveis).
