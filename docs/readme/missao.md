# 🗺️ **Sistema de Missões**

Este documento descreve toda a estrutura, comportamento e fluxo do módulo responsável pelas missões do jogo.

Baseado integralmente no código do arquivo _menu_missao_ fornecido.

---

# **1. Visão Geral**

O sistema de missões fornece:

- Interface de seleção de dificuldade
- Escolha de cenário
- Pré-visualização da missão
- Inicialização do combate
- Sistema dinâmico de turnos
- Uso de inventário durante o combate
- Registro de logs de batalha
- Sistema simples de inimigo simulado

É um componente essencial conectado ao personagem, combate e inventário.

Estrutura do módulo:

<pre class="overflow-visible!" data-start="955" data-end="1127"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>menu_missao</span><span>()
 ├── </span><span>escolher_dificuldade</span><span>()
 ├── </span><span>escolher_cenario</span><span>()
 ├── </span><span>preview_missao</span><span>()
 ├── </span><span>iniciar_missao</span><span>()
 │      └── </span><span>usar_item_em_combate</span><span>()
 └── </span><span>ajuda_missao</span><span>()
</span></span></code></div></div></pre>

---

# **2. Configuração de Missão**

As opções de missão são lidas e modificadas através de:

<pre class="overflow-visible!" data-start="1227" data-end="1311"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>jogo.missao_config = {
    </span><span>"dificuldade"</span><span>: </span><span>"Fácil"</span><span>,
    </span><span>"cenario"</span><span>: </span><span>"Trilha"</span><span>
}
</span></span></code></div></div></pre>

O módulo oferece ao jogador a possibilidade de alterar:

### 🎚️ _Dificuldade_

Valores possíveis:

- Fácil
- Média
- Difícil

Seleção feita em `escolher_dificuldade()`.

### 🌲 _Cenário_

Opções disponíveis:

- Trilha
- Floresta
- Caverna
- Ruínas

Seleção feita em `escolher_cenario()`.

---

# **3. Menu Principal de Missão**

A função `menu_missao(jogo)` exibe um submenu permanente com opções:

| Opção | Ação                   |
| ----- | ---------------------- |
| 1     | Selecionar dificuldade |
| 2     | Selecionar cenário     |
| 3     | Pré-visualizar missão  |
| 4     | Iniciar missão         |
| 9     | Ajuda                  |
| 0     | Voltar                 |

É responsável por delegar ao restante do sistema.

---

# **4. Pré-visualização de missão**

`preview_missao(jogo)` exibe:

- Dificuldade atual
- Cenário selecionado
- Informação futura sobre inimigos
- Informação futura sobre recompensas
- Observações sobre as regras de combate

Atualmente é um placeholder para futuras expansões.

---

# **5. Início da Missão**

A função principal do módulo é **iniciar_missao(jogo)** .

Fluxo:

1. Verifica se existe personagem criado
2. Garante que o inventário exista (senão cria)
3. Adiciona duas poções iniciais caso seja a primeira missão
4. Cria um inimigo simulado
5. Inicia o loop de combate por turnos
6. Atualiza logs de batalha
7. Exibe o resultado final

---

# **6. Sistema de Inimigo**

O inimigo atual é gerado dinamicamente com:

<pre class="overflow-visible!" data-start="2713" data-end="2762"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>nome: Goblin</span><span>
</span><span>vida: 60</span><span>
</span><span>ataque: 8</span><span>
</span><span>defesa: 3</span><span>
</span></span></code></div></div></pre>

Implementado via `type()` para criar um objeto simples.

---

# **7. Loop de Combate**

O combate segue o ciclo:

<pre class="overflow-visible!" data-start="2881" data-end="3040"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Turno →
    Jogador escolhe </span><span>a</span><span>ção
         ↓
    Jogador executa </span><span>a</span><span>ção
         ↓
    Se inimigo estiver vivo → inimigo ataca
         ↓
    Avanç</span><span>a</span><span> turno
</span></span></code></div></div></pre>

Condições de parada:

- `jogador.vida <= 0`
- `inimigo.vida <= 0`
- Fugir

---

# **8. Ações do Jogador**

### ⚔️ **[1] Atacar**

Calcula dano:

<pre class="overflow-visible!" data-start="3190" data-end="3244"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>dano</span><span> = max(jogador.ataque - inimigo.defesa, </span><span>0</span><span>)
</span></span></code></div></div></pre>

Aplica dano e registra no log.

---

### 🧪 **[2] Usar Item**

Chama: `usar_item_em_combate(jogador, jogo)`

O jogador:

- Visualiza lista numerada dos itens
- Seleciona um deles
- Recupera HP conforme o valor do item
- Item é removido do inventário

⚠ **O inimigo NÃO age nesse turno.**

---

### 🏃 **[3] Fugir**

Finaliza a missão imediatamente.

---

# **9. Ataque do Inimigo**

Mesmo sistema de dano, mas garante:

<pre class="overflow-visible!" data-start="3677" data-end="3739"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>dano_inimigo</span><span> = max(inimigo.ataque - jogador.defesa, </span><span>1</span><span>)
</span></span></code></div></div></pre>

Ou seja, **sempre causa no mínimo 1 de dano** .

---

# **10. Resultado da Missão**

Após o combate:

- Exibe **Vitória** ou **Derrota**
- Registra no log interno do jogo

---

# **11. Uso de Itens em Combate**

A função `usar_item_em_combate()`:

1. Lista itens com índice
2. Permite cancelar com `0`
3. Recupera vida com `item.valor`
4. Remove o item do inventário
5. Registra evento no log

Formato de listagem:

<pre class="overflow-visible!" data-start="4176" data-end="4214"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>[1]</span><span> Poção de Cura (cura </span><span>30</span><span> HP)
</span></span></code></div></div></pre>

---

# **12. Ajuda**

O comando `ajuda_missao()` fornece:

- Resumo geral das mecânicas
- Explicação das opções
- Dicas básicas

---

# **13. Expansões Futuras Sinalizadas pelo Código**

Partes do sistema indicam pontos planejados para expansão:

- Tabelas de inimigos reais por dificuldade
- Recompensas de missão
- Regras de combate mais completas
- Eventos e encontros aleatórios
- Variação de atributos conforme o cenário
- Modificadores de loot
