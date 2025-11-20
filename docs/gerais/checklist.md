## **SEMANA 1 — Fundamentos de POO**

- [x] Classes básicas criadas;
- [x] Construtores;
- [x] Menu inicial;
- [x] Fluxo principal funcionando;
- [x] Versão jogável simples;

## **SEMANA 2 — Regras, Coleções e Funções**

- [x] Uso de listas e dicionários (Invetário ainda não está totalmente integrado)
- [ ] Módulo random (Existe pacialmente nas missões, isso é sorteio de inimigos, itens e missões)
  - [ ] Combate completo com turnos detalhados
        Está **incompleto / sem detalhamento. Falta: Turnos (Detalha mais quem está recebendo o dando e quem está recebendo), implementa a recompensa, randomizar melhor o combate e itens recebidos.**
- [x] Inventário funcional (Escolhe itens do invetário);
  - [x] Sistema de cura/mana (através do inventário com itens de cura);
- [x] Validações no menu;

##### **Entregável:**

Versão aprimorada com múltiplos inimigos, missões e inventário funcional, incluindo
logs de turnos de batalha.

## **SEMANA 3 — Polimorfismo, Herança e Persistência**

- [x] Subclasses (Guerreiro e Mago);
- [x] Arqueiro / Chefão / Outros (Existe **parcialmente**)
- [x] Métodos sobrescritos avançados (Guerreiro e Mago possuem habilidades diferentes, mas ainda muito simples) (**Junto do Modulo de Random, vocês diversificam os ataques**).
- [x] Persistência JSON (100% Funcional, salvar e carregar).
- [x] Logger (ainda não existe; ou está funcional).
- [x] Polimorfismo básico (Parte do Guerreiro e mago, ataque).

##### **Entregável:**

Versão final do jogo com hierarquia OO, logs e persistência de dados.

## TIMES

### **O que falta do combate?**

**Requisito obrigatório.**

- [x] Existe combate básico.
- [x] Exibe turnos.
- [x] Exibe HP restante por turno.
- [x] Mostra dano aplicado.
- [x] Imprime resultado completo.
- [x] Dá loot completo.

---

### **O que falta Menu?**

- [x] Repositorio (**Não estamos usando "Repositorio"** , e sim apenas salvamento.py procedural.)
- [x] Logger. (**Não existe ainda.)**

---

### O que falta Personagem e Missão?

- [x] Criar personagem.
- [x] Escolher classe (Guerreiro e Mago).
- [x] Inventário funcional completo.
- [x] Missão básica (fluxo existe, mas ainda quebrado).
- [ ] XP, nível, evolução.
- [x] Recompensas (loot) completas.
