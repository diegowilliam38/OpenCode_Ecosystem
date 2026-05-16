---
name: project-init
description: Onboarding da primeira sessão para projetos novos. Execute automaticamente quando MEMORY.md não tiver contexto. Entrevista o desenvolvedor e configura todos os arquivos de memória.
disable-model-invocation: true
---

# Skill: project-init

**Quando executar:** Automaticamente quando `.claude/memory/MEMORY.md` não tiver contexto preenchido. Pode ser invocada manualmente com `/project-init`.

**Objetivo:** Entrevistar o desenvolvedor, configurar o projeto e popular todos os arquivos de memória para que qualquer sessão futura comece com contexto completo — sem re-explicar nada.

---

## Protocolo de entrevista

Conduza as perguntas em sequência, uma por vez. Aguarde cada resposta antes de continuar.

### 0 — Preferência de idioma ← COMECE AQUI

Faça esta pergunta nas duas línguas simultaneamente, exatamente uma vez:

---
"What language do you prefer to work in?
Qual idioma você prefere para trabalhar?

**1** — English
**2** — Português"

---

A partir daqui, use APENAS o idioma escolhido para todas as perguntas, respostas e conteúdo dos arquivos gerados.

Salve a escolha como `language: en` ou `language: pt-br` no front matter do MEMORY.md.

---

### 1 — Identificação e slug

"Qual será o **slug** deste projeto? (identificador único, curto, sem espaços — ex: `minha-api`, `ecommerce-v2`)"

"E o nome completo e objetivo principal em 1-2 frases?"

"Qual é o repositório GitHub do novo projeto? (ex: `username/minha-api`) — deixe em branco se ainda não criou"

### 2 — Stack tecnológica

"Qual é a stack? (linguagem, frameworks principais, banco de dados, infraestrutura/cloud)"

### 3 — Regras não-negociáveis

"Existe alguma regra que NUNCA deve ser quebrada neste projeto?
(ex: sempre PNPM, nunca alterar migrations existentes, PR obrigatório para main)"

### 4 — Equipe

"O projeto é solo, dupla ou time? Quantas pessoas?"

### 5 — Integrações MCP

"Quais integrações externas são necessárias?
(GitHub, banco de dados, Sentry, outros — ou nenhuma por enquanto)"

### 6 — Documentação das libs

"Quais são as principais libs, frameworks e ferramentas deste projeto que têm documentação oficial?
(ex: Fastify, Prisma, React, Docker — vou adicionar os links em `.claude/references.md` para consulta rápida)"

### 7 — Estado inicial

"O projeto já tem código ou está começando do zero? Se já existe, descreva brevemente o estado atual."

---

## Ações após a entrevista

Execute em ordem:

1. **Preencha `.claude/memory/MEMORY.md`**
   - Insira slug, repo, stack e **language** no front matter YAML
   - Preencha todas as seções com as respostas coletadas
   - Escreva o conteúdo no idioma escolhido

2. **Atualize `CLAUDE.md`**
   - Substitua `[PROJECT_NAME]` pelo nome real do projeto
   - Adicione as regras não-negociáveis na seção de princípios

3. **Preencha a seção "Deste Projeto" em `.claude/references.md`**
   - Para cada lib/framework mencionado na pergunta 6, adicione uma linha na tabela
   - Use a URL da documentação oficial

4. **Crie `README_MCP.md`** na raiz (se houver integrações)
   - Liste as integrações mencionadas
   - Inclua o comando `claude mcp add` para cada uma
   - Escreva no idioma escolhido

5. **Registre no global-index**
   - Acesse `claude-memories/global-index.md`
   - Adicione o projeto na tabela de registro: slug | repo | domínio | status "ativo"
   - Crie a entrada na árvore de conhecimento

6. **Finalize o git** (OBRIGATÓRIO — não pule este passo)

   Execute via Bash:
   ```bash
   git remote get-url origin
   ```
   Mostre o remote atual ao usuário. Se ainda apontar para o template (`template-claude-code`), siga:

   **Se o usuário forneceu o repo GitHub:**
   ```bash
   git remote set-url origin git@github.com:<usuario>/<repo>.git
   ```
   Depois, stage e commit de tudo que foi configurado:
   ```bash
   git add CLAUDE.md .claude/memory/MEMORY.md .claude/references.md .claude/specs/INDEX.md
   git commit -m "feat: initialize project from template"
   ```
   Pergunte: "Deseja que eu faça push para `origin main` agora?"
   - Se sim: `git push -u origin main`
   - Se não: informe o comando para o usuário rodar quando quiser

   **Se o usuário NÃO forneceu o repo GitHub:**
   Faça apenas o commit local com os arquivos configurados:
   ```bash
   git add CLAUDE.md .claude/memory/MEMORY.md .claude/references.md .claude/specs/INDEX.md
   git commit -m "feat: initialize project from template"
   ```
   Mostre instruções claras para o usuário:
   ```
   Quando criar o repositório no GitHub, rode:
     git remote set-url origin git@github.com:<seu-usuario>/<seu-repo>.git
     git push -u origin main
   ```

7. **Confirme ao usuário** o que foi configurado e pergunte se há ajustes

8. **Instrua sobre o próximo passo obrigatório**

   Ao final, sempre exiba esta mensagem:

   ---
   **Próximo passo:** crie a primeira spec do projeto com `/spec-create`, depois rode `/project-seal` para commitar e publicar tudo no repositório.
   ---

---

## Exemplo de MEMORY.md gerado corretamente

```markdown
---
project: minha-api
repo: ecodelearn/minha-api
stack: Node.js + Fastify + PostgreSQL + Redis
language: pt-br
---

# minha-api — Memória do Projeto

## Contexto
API REST para gestão de pedidos B2B. Processamento de ~50k req/dia.

## Stack
Node.js + Fastify + PostgreSQL + Redis. Deploy na Railway. PNPM obrigatório.

## Regras não-negociáveis
- Nunca alterar migrations existentes — sempre criar nova migration
- Branch obrigatória para main — PR com review
- Testes com Vitest, coverage mínimo 80%

## Estado atual
2026-03-04 — Projeto iniciado. Estrutura base configurada.

## Integrações ativas
- GitHub MCP (gh pr, issues)
- PostgreSQL MCP (queries de dados)
```
