---
name: project-adopt
description: Onboarding para projetos existentes que recebem a estrutura Claude Code pela primeira vez. Descobre convenções do codebase antes de perguntar qualquer coisa.
disable-model-invocation: true
---

# Skill: project-adopt

**Quando executar:** Em projetos existentes que estão recebendo a estrutura Claude Code pela primeira vez. Invocada com `/project-adopt`.

**Diferença do `project-init`:**
- `project-init` → define convenções em projeto em branco
- `project-adopt` → descobre convenções que já existem no código — o codebase é a fonte de verdade

---

## Protocolo

### Fase 1 — Mapeamento (antes de perguntar qualquer coisa)

Use o agente `researcher` para explorar o projeto. Objetivo: chegar à entrevista já com respostas para as perguntas óbvias, confirmando com o usuário em vez de perguntando do zero.

**O que buscar:**

```
Stack real:
- package.json / pyproject.toml / go.mod / Cargo.toml / pom.xml
- arquivos de configuração: .eslintrc, prettier.config, tsconfig.json, ruff.toml
- Docker/infra: Dockerfile, docker-compose.yml, .env.example, railway.json, vercel.json

Convenções em uso:
- estrutura de diretórios (src/, app/, lib/, tests/, etc.)
- padrão de imports nos arquivos principais
- framework de testes e como os testes estão organizados
- configuração de linting e formatação

Estado atual:
- git log --oneline -20 (últimos commits — o que está sendo trabalhado)
- branches ativas (git branch -a)
- arquivos modificados recentemente

Documentação existente:
- README.md, docs/, CHANGELOG.md
- comentários de arquitetura nos arquivos principais
```

### Fase 2 — Entrevista de validação

Apresente o que encontrou e peça confirmação. Pergunte apenas o que não conseguiu inferir.

```
"Mapeei o projeto. Confirme ou corrija:

Stack detectada: [o que encontrou]
Convenções identificadas: [formatador, testes, estrutura]
Trabalho recente: [resumo dos últimos commits]

Algumas perguntas que preciso de você:

1. Qual será o slug do projeto? (ex: minha-api, archguard)
2. Existe alguma regra não-negociável que não está evidente no código?
   (ex: nunca alterar migrations existentes, PR obrigatório)
3. O projeto é solo, dupla ou time? Idioma de comunicação? (PT-BR / EN)
4. Integrações MCP necessárias? (GitHub, banco, Sentry, outros)
5. Há features em andamento que devo criar specs agora?"
```

### Fase 3 — Ações após validação

Execute em ordem:

1. **Preencha `.claude/memory/MEMORY.md`**
   - Use a stack e convenções *descobertas* do codebase (não as respondidas)
   - Inclua o que está sendo trabalhado atualmente como "Estado atual"
   - Salve `language: pt-br` ou `language: en` conforme indicado

2. **Atualize `CLAUDE.md`**
   - Substitua `[PROJECT_NAME]` pelo nome real
   - Adicione as regras não-negociáveis confirmadas pelo usuário

3. **Preencha `.claude/references.md`**
   - Adicione os links oficiais das libs identificadas no mapeamento

4. **Crie specs para trabalho em andamento**
   - Para cada branch ativa ou feature em progresso mencionada pelo usuário
   - Use a skill `/spec-create` com status `in-progress` e a seção "Como retomar" preenchida

5. **Crie `README_MCP.md`** se houver integrações MCP

6. **Registre no global-index**
   - Adicione o projeto em `claude-memories/global-index.md`

7. **Confirme ao usuário** o que foi configurado e pergunte se há ajustes

---

## O que NÃO fazer

- Não redefinir convenções que já existem no código — descubra e siga
- Não criar specs para todo o histórico do projeto — só para o que está ativo
- Não sobrescrever um `CLAUDE.md` existente sem mostrar o diff ao usuário primeiro

---

## Exemplo de MEMORY.md gerado por project-adopt

```markdown
---
project: archguard
repo: ecodelearn/archguard
stack: Bash + Gum TUI + AppArmor + Firejail + systemd
language: pt-br
---

# archguard — Memória do Projeto

## Contexto
Toolkit de hardening e auditoria de segurança para Linux.
28 scripts bash (~9.680 linhas). TUI interativa com Gum.

## Stack
Bash. Gum para TUI. AppArmor (perfis), Firejail (sandboxes).
Deploy: scripts locais. Distro-aware via distro.conf por módulo.

## Regras não-negociáveis
- Nunca commitar direto no main — branch + PR obrigatório
- Scripts com header descritivo + source distro.conf
- Alertas com severidade: CRITICO / ALTO / AVISO / INFO

## Estado atual
2026-03-04 — Módulo secure-boot concluído (PR #34).
Em andamento: revisão dos perfis AppArmor para Podman.

## Integrações ativas
- GitHub MCP (PRs e issues)
```
