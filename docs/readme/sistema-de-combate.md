
# ⚔️ Sistema de Combate

**Documentação Técnica**

O sistema de combate implementa uma mecânica clássica de RPG baseada em turnos alternados, onde jogador e inimigo executam ações de forma intercalada até que um dos dois seja derrotado ou o jogador escolha fugir.

---

## 🧭 Visão Geral do Fluxo de Combate

1. A missão é iniciada e um inimigo é gerado dinamicamente.
2. O combate entra em um loop de turnos.
3. Em cada turno, o jogador escolhe uma das ações:
   * **Atacar**
   * **Usar Item**
   * **Fugir**
4. Após a ação do jogador, o inimigo realiza seu ataque (exceto se o jogador fugir).
5. O combate termina quando:
   * Vida do inimigo chega a 0 → ✔ **Vitória**
   * Vida do jogador chega a 0 → ❌ **Derrota**
   * O jogador seleciona fugir → 🏃 **Fuga**

---

## 🧩 Estrutura Técnica

O combate é controlado pelo arquivo:

<pre class="overflow-visible!" data-start="995" data-end="1028"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>models/controle_missao.py
</span></span></code></div></div></pre>

Função principal:

<pre class="overflow-visible!" data-start="1049" data-end="1088"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>def</span><span></span><span>iniciar_missao</span><span>(</span><span>jogo</span><span>):
</span></span></code></div></div></pre>

Essa função é responsável por:

* Configurar o cenário inicial
* Criar o inimigo
* Gerenciar turnos
* Aplicar dano
* Controlar o fluxo e encerramento da missão
* Registrar logs da batalha

---

## ⚔️ Ações do Jogador

---

### **1. 🗡️ Atacar**

Quando o jogador escolhe atacar:

<pre class="overflow-visible!" data-start="1382" data-end="1463"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>dano = </span><span>max</span><span>(jogador.ataque - inimigo.defesa, </span><span>1</span><span>)
inimigo.vida -= dano
</span></span></code></div></div></pre>

**Regras:**

* Sempre causa **mínimo de 1** de dano
* Fórmula:

  **ataque do jogador − defesa do inimigo**
* Log registrado automaticamente:

<pre class="overflow-visible!" data-start="1609" data-end="1698"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>jogo.logger.log_batalha(</span><span>f"{jogador.nome}</span><span> causou </span><span>{dano}</span><span> em </span><span>{inimigo.nome}</span><span>.")
</span></span></code></div></div></pre>

---

### **2. 🧪 Usar Item**

A ação chama:

<pre class="overflow-visible!" data-start="1745" data-end="1794"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>usar_item_em_combate(jogador, jogo)
</span></span></code></div></div></pre>

**Características:**

* Jogador pode consumir poções (ex.: Poção de Cura)
* Cura possui valor fixo (ex.: `30 pontos`)
* **Usar item consome o turno**
* **O inimigo ataca logo em seguida**

Exemplo de item:

<pre class="overflow-visible!" data-start="2003" data-end="2042"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>Item(</span><span>"Poção de Cura"</span><span>, </span><span>30</span><span>)
</span></span></code></div></div></pre>

---

### **3. 🏃 Fugir**

<pre class="overflow-visible!" data-start="2070" data-end="2163"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>print</span><span>(</span><span>"Você fugiu!"</span><span>)
jogo.logger.log_batalha(</span><span>"Jogador fugiu da missão."</span><span>)
</span><span>return</span><span>
</span></span></code></div></div></pre>

**Regras:**

* Encerramento instantâneo do combate
* O inimigo **não** ataca
* Resultado final: **Fuga**

---

## 💥 Ataque do Inimigo

Se ainda estiver vivo, o inimigo contra-ataca no mesmo turno:

<pre class="overflow-visible!" data-start="2368" data-end="2465"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>dano_inimigo = </span><span>max</span><span>(inimigo.ataque - jogador.defesa, </span><span>1</span><span>)
jogador.vida -= dano_inimigo
</span></span></code></div></div></pre>

**Regras:**

* Dano mínimo = **1**
* Fórmula:

  **ataque do inimigo − defesa do jogador**
* Log registrado pelo sistema

---

## 🔄 Exemplo de Turno Completo

<pre class="overflow-visible!" data-start="2628" data-end="2782"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>---</span><span></span><span>Turno</span><span></span><span>3</span><span></span><span>---</span><span>
</span><span>Uraraka</span><span></span><span>HP</span><span>: </span><span>54</span><span> | </span><span>Goblin</span><span></span><span>HP</span><span>: </span><span>20</span><span>

</span><span>A</span><span>çã</span><span>o</span><span>:
</span><span>[1]</span><span></span><span>Atacar</span><span>
</span><span>[2]</span><span></span><span>Usar</span><span></span><span>item</span><span>
</span><span>[3]</span><span></span><span>Fugir</span><span>
> </span><span>1</span><span>

</span><span>Voc</span><span>ê </span><span>causou</span><span></span><span>12</span><span></span><span>de</span><span></span><span>dano</span><span>!
</span><span>Goblin</span><span></span><span>te</span><span></span><span>atacou</span><span></span><span>e</span><span></span><span>causou</span><span></span><span>4</span><span>!
</span></span></code></div></div></pre>

---

## 🎯 Condições de Encerramento

<pre class="overflow-visible!" data-start="2822" data-end="2892"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>resultado = </span><span>"Vitória"</span><span></span><span>if</span><span> jogador.vida > </span><span>0</span><span></span><span>else</span><span></span><span>"Derrota"</span><span>
</span></span></code></div></div></pre>

Possíveis resultados:

* ✔ **Vitória**
* ❌ **Derrota**
* 🏃 **Fuga**

---

## 📝 Registro de Logs

Eventos importantes são registrados com:

<pre class="overflow-visible!" data-start="3035" data-end="3077"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>jogo.logger.log_batalha(...)
</span></span></code></div></div></pre>

Os logs são armazenados:

* No arquivo de save (JSON)
* No histórico interno da sessão

---

## 🧱 Estrutura de Dados

### 📍 Objeto Jogador

Atributos principais:

* **vida**
* **ataque**
* **defesa**
* **inventario**
* **mana**
* **nome**
* **arquetipo**

O jogador é criado a partir das classes:

<pre class="overflow-visible!" data-start="3380" data-end="3408"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>models/personagem.py
</span></span></code></div></div></pre>

### 📍 Objeto Inimigo

Criado dinamicamente:

<pre class="overflow-visible!" data-start="3457" data-end="3578"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>inimigo = </span><span>type</span><span>(
    </span><span>"InimigoSimulado"</span><span>, (),
    {</span><span>"nome"</span><span>: </span><span>"Goblin"</span><span>, </span><span>"vida"</span><span>: </span><span>60</span><span>, </span><span>"ataque"</span><span>: </span><span>8</span><span>, </span><span>"defesa"</span><span>: </span><span>3</span><span>}
)()
</span></span></code></div></div></pre>

### 📍 Itens

Exemplo de item padrão:

<pre class="overflow-visible!" data-start="3619" data-end="3658"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>Item(</span><span>"Poção de Cura"</span><span>, </span><span>30</span><span>)
</span></span></code></div></div></pre>

---

## 🔧 Responsabilidades por Arquivo

| Arquivo                             | Função                                 |
| ----------------------------------- | ---------------------------------------- |
| **models/controle_missao.py** | Lógica do combate e fluxo da missão    |
| **models/personagem.py**      | Atributos e comportamento do jogador     |
| **models/inventario.py**      | Armazena e gerencia itens do inventário |
| **models/salvamento.py**      | Salva e restaura o estado do jogo        |
| **models/logger.py**          | Armazena e exporta logs da missão       |
