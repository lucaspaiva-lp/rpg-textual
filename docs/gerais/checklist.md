## **SEMANA 1 — Fundamentos de POO**

- [X] Classes básicas criadas;
- [X] Construtores;
- [X] Menu inicial;
- [X] Fluxo principal funcionando;
- [X] Versão jogável simples;

## **SEMANA 2 — Regras, Coleções e Funções**

- [X] Uso de listas e dicionários (Invetário ainda não está totalmente integrado)
- [ ] Módulo random (Existe pacialmente nas missões, isso é sorteio de inimigos, itens e missões)
  - [ ] Combate completo com turnos detalhados
    Está **incompleto / sem detalhamento. Falta: Turnos (Detalha mais quem está recebendo o dando e quem está recebendo), implementa a recompensa, randomizar melhor o combate e itens recebidos.**
- [X] Inventário funcional (Escolhe itens do invetário);
  - [X] Sistema de cura/mana (através do inventário com itens de cura);
- [X] Validações no menu;

##### **Entregável:**

Versão aprimorada com múltiplos inimigos, missões e inventário funcional, incluindo
logs de turnos de batalha.

## **SEMANA 3 — Polimorfismo, Herança e Persistência**

- [X] Subclasses (Guerreiro e Mago);
- [X] Arqueiro / Chefão / Outros (Existe **parcialmente**)
- [ ] Métodos sobrescritos avançados (Guerreiro e Mago possuem habilidades diferentes, mas ainda muito simples) (**Junto do Modulo de Random, vocês diversificam os ataques**).
- [X] Persistência JSON (100% Funcional, salvar e carregar).
- [X] Logger (ainda não existe; ou está funcional).
- [X] Polimorfismo básico (Parte do Guerreiro e mago, ataque).

##### **Entregável:**

Versão final do jogo com hierarquia OO, logs e persistência de dados.

## TIMES

### **O que falta do combate?**

**Requisito obrigatório.**

- [X] Existe combate básico.
- [X] Exibe turnos.
- [X] Exibe HP restante por turno.
- [X] Mostra dano aplicado.
- [X] Imprime resultado completo.
- [ ] Dá loot completo.

---

### **O que falta Menu?**

- [X] Repositorio (**Não estamos usando "Repositorio"** , e sim apenas salvamento.py procedural.)
- [X] Logger. (**Não existe ainda.)**

---

### O que falta Personagem e Missão?

- [X] Criar personagem.
- [X] Escolher classe (Guerreiro e Mago).
- [X] Inventário funcional completo.
- [X] Missão básica (fluxo existe, mas ainda quebrado).
- [ ] XP, nível, evolução.
- [ ] Recompensas (loot) completas.
