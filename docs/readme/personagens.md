# 🧙‍♂️ **Sistema de Personagens**

Este documento descreve a arquitetura, atributos, métodos e comportamentos dos personagens do jogo, conforme implementados no módulo `personagem.py`.

Ele serve como referência oficial para evolução do sistema.

---

# 📌 **1. Arquitetura Geral**

O sistema de personagens segue um modelo  **orientado a objetos** , onde:

* `Aventureiro` é a **classe base** para todos os personagens.
* `Guerreiro` e `Mago` são  **subclasses especializadas** .
* Habilidades são implementadas por polimorfismo, sobrescrevendo métodos como `atacar()`.
* Itens são armazenados em uma  **lista simples** , e não mais em uma classe Inventário.

Diagrama simplificado:

<pre class="overflow-visible!" data-start="919" data-end="963"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Aventureiro</span><span>
 ├── Guerreiro
 └── Mago
</span></span></code></div></div></pre>

---

# 📌 **2. Classe Base — Aventureiro**

A classe `Aventureiro` centraliza todos os atributos e comportamentos comuns.

## 🧱 **Atributos**

| Atributo       | Descrição                |
| -------------- | -------------------------- |
| `nome`       | Nome do personagem         |
| `vida`       | Vida atual                 |
| `vida_max`   | Vida máxima do personagem |
| `ataque`     | Valor de ataque            |
| `defesa`     | Defesa base                |
| `mana`       | Mana atual                 |
| `mana_max`   | Mana máxima               |
| `inventario` | Lista de itens             |
| `nivel`      | Nível atual               |
| `xp`         | Experiência acumulada     |

---

## 🧰 **Métodos Principais**

### 🎯 **get_ataque()**

Retorna o valor de ataque base.

### 🔮 **get_mana() / set_mana()**

Manipulação da barra de mana com limite máximo.

### 🎒 **Inventário**

* `adicionar_item(item)`
* `remover_item(item)`
* `usar_item(nome_item)`

A função `usar_item()` procura o item no inventário e, se possível, executa seu método interno `usar()`.

### ❤️ **receber_dano(dano)**

Reduz vida com base na defesa:

<pre class="overflow-visible!" data-start="1902" data-end="1944"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>dano_final</span><span> = max(</span><span>0</span><span>, da</span><span>no</span><span> - defesa)
</span></span></code></div></div></pre>

### ⚔️ **calcular_dano_basico(alvo)**

Sistema de ataque comum a todas as classes:

<pre class="overflow-visible!" data-start="2029" data-end="2072"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>dano</span><span> = max(</span><span>0</span><span>, ataque - alvo.defesa)
</span></span></code></div></div></pre>

### 📈 **ganhar_xp(quantidade)**

Acumula XP e verifica subida de nível:

<pre class="overflow-visible!" data-start="2147" data-end="2182"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>xp</span><span></span><span>necessária</span><span></span><span>=</span><span> nivel * </span><span>100</span><span>
</span></span></code></div></div></pre>

### ⬆️ **subir_nivel()**

Aumenta atributos em  **10%** , restaura vida e mana ao máximo.

---

# 📌 **3. Classe Guerreiro**

Especialização focada em dano físico consistente.

Possui alternância automática entre ataque normal e habilidades especiais.

---

## ⚙️ **Habilidades Especiais**

### 🪓 golpe_poderoso(alvo)

* Dano = ataque * **1.5**
* Defesa inimiga reduzida pela metade

### ⚔️ ataque_duplo(alvo)

* Executa **dois ataques básicos**
* Retorna a soma total do dano

### 🔥 habilidade_especial(alvo)

Escolhe aleatoriamente entre:

* `"golpe"` → golpe_poderoso
* `"duplo"` → ataque_duplo

Após usar, só volta a usar no próximo turno (cooldown).

---

## ⚔️ **Método atacar()**

O Guerreiro alterna automaticamente:

* Se a habilidade está disponível → usa especial
* Caso contrário → usa ataque básico e restaura a habilidade

---

# 📌 **4. Classe Mago**

Especialização focada em dano mágico e gerenciamento de mana.

---

## ✨ **Habilidades Mágicas**

### 🔥 bola_de_fogo(alvo)

* Custo: **20 mana**
* Dano: ataque × 2.5

### ⚡ raio_mistico(alvo)

* Custo: **10 mana**
* Dano: ataque × 1.5

### 🔮 habilidade_especial(alvo)

Escolhe **aleatoriamente** entre:

* `"fogo"` → bola_de_fogo
* `"raio"` → raio_mistico

Caso não tenha mana, retorna 0.

---

## ⚔️ **Método atacar()**

Fluxo:

1. Tenta usar uma magia aleatória.
2. Se a magia falhar (sem mana) → usa ataque básico.

---

# 📌 **5. Criação do Personagem**

A criação de personagem segue o fluxo definido em:

<pre class="overflow-visible!" data-start="3668" data-end="3698"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>criar_personagem</span><span>(jogo)
</span></span></code></div></div></pre>

Passos:

1. Jogador define o nome
2. Escolhe o arquétipo
3. O sistema instancia:

| Arquétipo | Classe Instanciada |
| ---------- | ------------------ |
| Guerreiro  | `Guerreiro`      |
| Mago       | `Mago`           |
| Arqueiro   | (indisponível)    |
| Curandeiro | (indisponível)    |

---

# 📌 **6. Exemplo de Instanciação**

<pre class="overflow-visible!" data-start="4006" data-end="4077"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>heroi = Guerreiro(</span><span>"Uraraka"</span><span>)
</span><span>print</span><span>(heroi.ataque)  </span><span># -> 15</span><span>
</span></span></code></div></div></pre>

Ou:

<pre class="overflow-visible!" data-start="4084" data-end="4146"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>mago = Mago(</span><span>"Merlin"</span><span>)
</span><span>print</span><span>(mago.mana)  </span><span># -> 100</span><span>
</span></span></code></div></div></pre>

---

# 📌 **7. Evolução do Personagem**

Subir de nível:

* +10% vida
* +10% ataque
* +10% defesa
* +10% mana máxima
* vida e mana restauradas

XP necessária cresce proporcional ao nível:

<pre class="overflow-visible!" data-start="4337" data-end="4361"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>XP</span><span> = nivel * </span><span>100</span><span>
</span></span></code></div></div></pre>

---

# 📌 **8. Inventário e Uso de Itens**

Itens são armazenados assim:

<pre class="overflow-visible!" data-start="4437" data-end="4471"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>self.inventario = []
</span></span></code></div></div></pre>

Para usar:

<pre class="overflow-visible!" data-start="4485" data-end="4547"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>mensagem = personagem.usar_item(</span><span>"Poção de Cura"</span><span>)
</span></span></code></div></div></pre>

Itens precisam implementar:

<pre class="overflow-visible!" data-start="4578" data-end="4644"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>def</span><span></span><span>usar</span><span>(</span><span>self, personagem</span><span>):
    </span><span>return</span><span> valor_da_cura
</span></span></code></div></div></pre>

---

# 📌 **9. Resumo das Diferenças Entre Classes**

| Característica   | Guerreiro                     | Mago                         |
| ----------------- | ----------------------------- | ---------------------------- |
| Vida              | Alta                          | Baixa                        |
| Ataque            | Alto                          | Médio                       |
| Defesa            | Alta                          | Baixa                        |
| Mana              | 0                             | Alta                         |
| Tipo de dano      | Físico                       | Mágico                      |
| Ataques especiais | Golpe Poderoso / Ataque Duplo | Bola de Fogo / Raio Místico |
| Custos            | Nenhum                        | Mana                         |
