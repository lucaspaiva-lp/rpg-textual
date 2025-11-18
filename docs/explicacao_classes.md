# Explicação Completa das Classes: Aventureiro, Guerreiro e Mago

## 1. Classe Aventureiro (Base)

A classe **Aventureiro** representa a base de todas as outras classes.\
Ela contém apenas os elementos essenciais que **todos os personagens**
devem ter:

### Propriedades básicas:

-   **nome**: Nome do personagem.
-   **vida** e **vida_max**: Saúde atual e máxima.
-   **ataque**: Valor de ataque básico.
-   **defesa**: Valor de defesa básico.
-   **mana**: Recurso utilizado por habilidades.
-   **inventario**: Lista de itens.

### Métodos:

-   `get_vida()`, `set_vida()`
-   `get_ataque()`, `set_ataque()`
-   `get_defesa()`, `set_defesa()`
-   `get_mana()`, `set_mana()`
-   `get_inventario()`
-   `adicionar_item()`, `remover_item()`
-   `calcular_dano_base()`: Retorna dano básico físico.
-   `receber_dano(dano)`: Calcula dano reduzindo pela **metade da
    defesa**.
-   `esta_vivo()`: Indica se o personagem está vivo.

------------------------------------------------------------------------

## 2. Classe Guerreiro

A classe **Guerreiro** herda de **Aventureiro** e representa um lutador
físico especializado.

### Características gerais:

-   Alta defesa
-   Ataques físicos poderosos
-   Baixa mana
-   Chance crítica: **20%**

### Habilidades especiais (cada uma com cooldown e custo):

-   **Fortificação**
    -   Substitui redução de dano por metade da defesa → passa a usar
        **100% da defesa** por 3 turnos.
-   **Vontade de Ferro**
    -   Primeira vez que morre no combate, retorna com **25% de HP**,
        mas perde toda a mana.
-   **Ataque Duplo**
    -   Ataca duas vezes.\
    -   Sem chance crítica.\
    -   Se combinado com habilidade especial, o custo aumenta.
-   **Berserker**
    -   Troca defesa por ataque.\
    -   Não pode ser escolhida com Fortificação.
-   **Ataque de Cima**
    -   60% de chance de errar, mas acerta com crítico garantido.
-   **Levantar Defesas**
    -   Não leva dano no turno, mas não ataca.
-   **Contra-Ataque**
    -   Reduz dano recebido com seu ataque e devolve o dano ao inimigo.
-   **Ponto Vital**
    -   Pode ser usado após um crítico para aumentar ainda mais o dano.
-   **Invocar Tropa**
    -   Invoca aliado que causa dano por 5 turnos.
-   **Tudo ou Nada**
    -   Ataca três vezes, mas recebe parte do dano sem defesa.

### Summon específico (caso o jogador pegue a skill):

-   Tropa simplificada que causa dano automático por turno.

------------------------------------------------------------------------

## 3. Classe Mago

A classe **Mago** também herda Aventureiro, mas possui foco em magias.

### Características gerais:

-   Alta mana
-   Magias com efeitos especiais
-   Defesa baixa
-   Chance crítica: **10%**

### Habilidades:

-   **Raio Místico**
    -   Ignora 100% da defesa inimiga, mas tem dano reduzido.
-   **Maré de Fogo**
    -   Dano + queimadura por 2 turnos.
-   **Armadura Arcana**
    -   Aumenta a defesa em metade do ataque até o final do combate.
-   **Cortar**
    -   Dano por 5 turnos.
-   **Saber é Poder (passiva)**
    -   Aumenta dano de magias com metade do ataque.
-   **Meteorito**
    -   Dano massivo instantâneo com alto custo.
-   **Raio Congelante**
    -   Dano médio + reduz o próximo dano recebido em 50%.
-   **Invocar Ser**
    -   Invoca: Elefante, Tigre ou Vespa, cada um com efeitos únicos.
-   **Escudo Mágico**
    -   Ignora dano no turno, mas não pode atacar.
-   **Visão do Futuro (passiva)**
    -   20% de chance de esquivar ataques.

### Summon específico:

-   Elefante (vida extra), Tigre (dano por turno), Vespa (ataques
    múltiplos).

------------------------------------------------------------------------

## 4. Progressão de Nível

Sempre que um personagem sobe de nível:

-   +10% ataque
-   +10% vida máxima (e cura total)
-   +10% mana máxima (e recuperação total)
-   Habilidades mágicas também aumentam seu dano em 10%

A cada **5 níveis**, o jogador escolhe uma nova habilidade, respeitando
incompatibilidades (ex: Berserker × Fortificação).

------------------------------------------------------------------------

## 5. Dano Crítico

-   Guerreiro: 20% de chance\
-   Mago: 10% de chance

Crítico = dano × 2

Apenas habilidades **não especificadas como sem crítico** podem critar.

------------------------------------------------------------------------

Este documento explica totalmente como as três classes funcionam, suas
habilidades, estilos de combate e progressões.
