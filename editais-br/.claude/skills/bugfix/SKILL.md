---
name: bugfix
description: Protocolo sistemático de triage de bugs. Use ao receber report ou comportamento inesperado. Segue a sequência reproduzir→localizar→reduzir→corrigir→guardar→verificar.
disable-model-invocation: true
argument-hint: "[descrição do bug]"
---

# Skill: bugfix

**Quando usar:** Ao receber um report de bug ou comportamento inesperado. Substitui improvisação por um processo sistemático que evita corrigir sintoma em vez de causa raiz.

---

## Triage — execute nesta ordem, sem pular etapas

### 1. Reproduzir
Confirme que consegue reproduzir o bug de forma confiável antes de tocar em qualquer código.
- Qual é o input ou sequência de ações que dispara o problema?
- O bug é determinístico ou intermitente?
- Se intermitente: qual é a taxa de ocorrência?

### 2. Localizar
Identifique a camada onde a falha ocorre:
- UI / frontend?
- Lógica de negócio / API?
- Banco de dados / query?
- Integração externa / rede?
- Build / tooling / ambiente?

### 3. Reduzir
Isole o caso mínimo que ainda reproduz o problema.
- Qual é o menor input que falha?
- Qual é o menor trecho de código envolvido?
- O problema existe em ambiente limpo (sem dados de estado anteriores)?

### 4. Corrigir
Corrija a **causa raiz**, não o sintoma.
- Se a correção precisar de mais de 20 linhas, questione se está atacando a causa certa
- Não faça refatorações adjacentes junto com o fix — escopo separado, commit separado
- Se descobrir outros bugs no caminho: registre como issue/TODO, não corrija agora

### 5. Guardar (regression coverage)
Adicione o menor teste que teria falhado antes do fix e passa agora.
- Testes unitários para lógica pura
- Testes de integração para boundary (DB, rede, I/O)
- O teste deve estar no mesmo commit do fix

### 6. Verificar
Confirme end-to-end para o report original:
- O comportamento esperado está correto?
- Os testes existentes continuam passando?
- O fix não introduz regressão?

---

## Stop-the-line

Se em qualquer etapa acontecer algo inesperado:
1. **Pare** — não continue adicionando código
2. **Preserve** — salve logs, stack trace, estado atual
3. **Re-planeje** — volte ao passo 1 com a nova informação

---

## Template de documentação do fix

Preencha ao concluir — registre na spec ou diretamente em `lessons.md`:

```
**Bug:** [descrição em 1 frase]
**Repro:** [passos mínimos para reproduzir]
**Esperado vs real:** [comportamento esperado] / [comportamento observado]
**Causa raiz:** [o que de fato estava errado]
**Fix:** [o que foi alterado — arquivo:linha]
**Cobertura de regressão:** [nome do teste adicionado]
**Verificação:** [comando rodado + resultado]
**Risco/rollback:** [baixo|médio|alto — como reverter se necessário]
```

---

## Após o fix

- Se o bug revelou uma lacuna de conhecimento: adicione entrada em `lessons.md`
- Se o fix exigiu uma decisão arquitetural: registre em `decisions.md`
- Se o padrão de fix for reutilizável em outros projetos: use a skill `/publish-pattern`
