# 💾 **Sistema de Salvamento**

O módulo de salvamento é responsável por armazenar e recuperar todo o progresso do jogo de maneira orientada a objetos.

Ele utiliza JSON como formato de persistência e reconstrói completamente o personagem, inventário, atributos e logs.

Este documento descreve o comportamento do arquivo **repositorio_jogo.py**, incluindo as rotinas de salvar, carregar e os menus associados.

---

# **1. Visão Geral**

O sistema de salvamento foi projetado para:

- Salvar o estado atual do jogo (personagem, missão, inventário, logs)
- Permitir múltiplos saves nomeados
- Oferecer carregamento rápido
- Permitir restauração total do objeto Personagem
- Reconstruir corretamente os itens do inventário
- Exportar e importar logs da sessão
- Evitar erros de serialização com objetos complexos

Arquitetura principal:

<pre class="overflow-visible!" data-start="1159" data-end="1300"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>RepositorioJogo
 ├── </span><span>salvar_rapido</span><span>()
 ├── </span><span>salvar_com_nome</span><span>()
 ├── </span><span>salvar</span><span>()
 ├── </span><span>carregar</span><span>()
 ├── </span><span>_montar_dados</span><span>()  ← serialização segura
</span></span></code></div></div></pre>

E menus auxiliares:

<pre class="overflow-visible!" data-start="1323" data-end="1360"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>menu_salvar</span><span>()
</span><span>menu_carregar</span><span>()
</span></span></code></div></div></pre>

---

# **2. Estrutura do Repositório**

A classe base é:

<pre class="overflow-visible!" data-start="1423" data-end="1459"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>class</span><span></span><span>RepositorioJogo</span><span>:
</span></span></code></div></div></pre>

Ela controla:

- Pasta de saves (`/saves/`)
- Último arquivo utilizado
- Serialização e deserialização do jogo
- Tratamento de erros
- Compatibilidade com todo o projeto

O construtor:

<pre class="overflow-visible!" data-start="1647" data-end="1695"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>def</span><span></span><span>__init__</span><span>(</span><span>self, pasta="saves"</span><span>):
</span></span></code></div></div></pre>

- Cria automaticamente a pasta de saves
- Armazena o caminho do último save
- Permite sincronização com `jogo._ultimo_save`

---

# **3. Métodos de Salvamento**

### ✅ **3.1 Salvamento rápido**

<pre class="overflow-visible!" data-start="1895" data-end="1928"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>salvar_rapido(jogo)
</span></span></code></div></div></pre>

- Salva diretamente em `quick_save.json`
- Atualiza ponteiros internos de último save

---

### 📁 **3.2 Salvamento com nome**

<pre class="overflow-visible!" data-start="2058" data-end="2099"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>salvar_com_nome(jogo, nome)
</span></span></code></div></div></pre>

- O jogador define o nome do arquivo
- Arquivo gerado: `saves/<nome>.json`

---

### ⚙️ **3.3 Salvamento interno**

`salvar(jogo, caminho)` é o método de baixo nível responsável por gravar o JSON.

Fluxo:

1. Monta todos os dados com `_montar_dados`
2. Serializa em **UTF-8**
3. Salva com indentação (para leitura humana)
4. Trata exceções de forma amigável

---

# **4. Métodos de Carregar**

### 📂 `carregar(jogo, caminho)`

Responsável por restaurar **todo o estado do jogo** , incluindo:

- `jogo.personagem` (dados simplificados)
- `jogo.missao_config`
- **Reconstrução completa do objeto personagem**
- **Reconstrução do inventário**
- **Importação de logs de batalha**

Fluxo:

<pre class="overflow-visible!" data-start="2789" data-end="2936"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>abrir arquivo → ler </span><span>JSON</span><span> →
recriar personagem →
restaurar atributos →
reconstruir inventário →
restaurar logs →
atualizar caminhos internos
</span></span></code></div></div></pre>

---

# **5. Reconstrução do Personagem**

Quando o jogo é carregado, o repositório analisa:

<pre class="overflow-visible!" data-start="3034" data-end="3092"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>arquetipo = jogo.personagem.get(</span><span>"arquetipo"</span><span>)
</span></span></code></div></div></pre>

E instancia corretamente:

| Arquetipo salvo | Classe restaurada              |
| --------------- | ------------------------------ |
| "Guerreiro"     | `Guerreiro`                  |
| "Mago"          | `Mago`                       |
| Outros          | `Guerreiro`(fallback seguro) |

Depois restaura atributos:

<pre class="overflow-visible!" data-start="3322" data-end="3353"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>vida</span><span>
ataque
defesa
mana
</span></span></code></div></div></pre>

---

# **6. Reconstrução do Inventário**

O inventário salvo possui formato:

<pre class="overflow-visible!" data-start="3436" data-end="3552"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>"inventario"</span><span>:</span><span></span><span>[</span><span>
  </span><span>{</span><span></span><span>"nome"</span><span>:</span><span></span><span>"Poção de Cura"</span><span>,</span><span></span><span>"valor"</span><span>:</span><span></span><span>30</span><span></span><span>}</span><span>,</span><span>
  </span><span>{</span><span></span><span>"nome"</span><span>:</span><span></span><span>"Poção de Cura"</span><span>,</span><span></span><span>"valor"</span><span>:</span><span></span><span>30</span><span></span><span>}</span><span>
</span><span>]</span><span>
</span></span></code></div></div></pre>

A desserialização faz:

<pre class="overflow-visible!" data-start="3578" data-end="3694"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>p.inventario = Inventario()
</span><span>for</span><span> item </span><span>in</span><span> inventario:
    p.inventario.adicionar_item(Item(nome, valor))
</span></span></code></div></div></pre>

É 100% compatível com `Inventario.itens`.

---

# **7. Serialização do Inventário (salvamento)**

A montagem é feita em:

<pre class="overflow-visible!" data-start="3821" data-end="3992"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>inventario_serializado = []
</span><span>for</span><span> item </span><span>in</span><span> p.inventario.itens:
    inventario_serializado.append({
        </span><span>"nome"</span><span>: item.nome,
        </span><span>"valor"</span><span>: item.valor
    })
</span></span></code></div></div></pre>

Totalmente à prova de erros (usa `getattr` quando necessário).

---

# **8. Logs da Sessão**

Os logs são exportados e importados através de:

- `jogo.logger.exportar()`
- `jogo.logger.importar(lista)`

Garantindo total persistência dos eventos da batalha.

Formato salvo:

<pre class="overflow-visible!" data-start="4271" data-end="4362"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>"logs"</span><span>:</span><span></span><span>[</span><span>
    </span><span>"Jogador causou 10 em Goblin"</span><span>,</span><span>
    </span><span>"Goblin causou 3 em Jogador"</span><span>
</span><span>]</span><span>
</span></span></code></div></div></pre>

---

# **9. Menus Associados**

O módulo também fornece menus de operação:

---

## 📁 **menu_salvar()**

Opções:

| Opção | Função           |
| ------- | ------------------ |
| 1       | salvamento rápido |
| 2       | salvar com nome    |
| 9       | ajuda              |
| 0       | voltar             |

---

## 📂 **menu_carregar()**

Opções:

| Opção | Função                        |
| ------- | ------------------------------- |
| 1       | carrega último save da sessão |
| 2       | carrega arquivo por nome        |
| 9       | ajuda                           |
| 0       | voltar                          |

---

# **10. Tratamento de Erros**

Sistema robusto:

- Captura exceções de IO
- Captura erros de serialização
- Mostra mensagens amigáveis
- Evita crash completo do jogo

Exemplo:

<pre class="overflow-visible!" data-start="4963" data-end="5001"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>❌ </span><span>Erro</span><span></span><span>ao</span><span></span><span>carregar</span><span>: </span><span>[Mensagem]</span><span>
</span></span></code></div></div></pre>

---

# **11. Estrutura Final do JSON**

Save gerado:

<pre class="overflow-visible!" data-start="5060" data-end="5564"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
    </span><span>"personagem"</span><span>:</span><span></span><span>{</span><span>
        </span><span>"nome"</span><span>:</span><span></span><span>"Uraraka"</span><span>,</span><span>
        </span><span>"arquetipo"</span><span>:</span><span></span><span>"Guerreiro"</span><span>
    </span><span>}</span><span>,</span><span>
    </span><span>"missao_config"</span><span>:</span><span></span><span>{</span><span>
        </span><span>"dificuldade"</span><span>:</span><span></span><span>"Média"</span><span>,</span><span>
        </span><span>"cenario"</span><span>:</span><span></span><span>"Floresta"</span><span>
    </span><span>}</span><span>,</span><span>
    </span><span>"logs"</span><span>:</span><span></span><span>[</span><span>
        </span><span>"Missão iniciada — Média / Floresta"</span><span>,</span><span>
        </span><span>"Uraraka causou 12 em Goblin"</span><span>
    </span><span>]</span><span>,</span><span>
    </span><span>"personagem_detalhes"</span><span>:</span><span></span><span>{</span><span>
        </span><span>"vida"</span><span>:</span><span></span><span>88</span><span>,</span><span>
        </span><span>"ataque"</span><span>:</span><span></span><span>15</span><span>,</span><span>
        </span><span>"defesa"</span><span>:</span><span></span><span>6</span><span>,</span><span>
        </span><span>"mana"</span><span>:</span><span></span><span>10</span><span>,</span><span>
        </span><span>"inventario"</span><span>:</span><span></span><span>[</span><span>
            </span><span>{</span><span></span><span>"nome"</span><span>:</span><span></span><span>"Poção de Cura"</span><span>,</span><span></span><span>"valor"</span><span>:</span><span></span><span>30</span><span></span><span>}</span><span>
        </span><span>]</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

Esse é o “snapshot” completo do estado atual do jogo.
