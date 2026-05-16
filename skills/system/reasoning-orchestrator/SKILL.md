---
name: reasoning-orchestrator
description: "Orquestracao Meta-Granular Nexus (v6.0) dos 58 tipos de raciocinio para selecao de framework logico, nivel de profundidade (L1-L4) e matriz de intersecao antes de analises"
user-invocable: true
license: MIT
compatibility: OpenCode, Claude Code, Cursor, Gemini CLI
metadata:
  author: OpenCode Ecosystem
  version: "6.0.0"
  openclaw:
            emoji: "🧠"
    homepage: https://github.com/anomalyco/opencode
allowed-tools: Read Edit Write Glob Grep Bash Task SequentialThinking
---

# Reasoning Orchestrator Nexus v6.0

Nucleo de inteligencia analitica integrando 58 modelos mentais em arquitetura de 4 niveis de profundidade (L1-L4).

## Protocolo Nexus: Checkpoint Meta-Granular

**OBRIGATORIO**: Antes de iniciar qualquer tarefa analitica, realize o Checkpoint Nexus:

1. **Definicao de Profundidade**: Escolha o nivel (L1 a L4) em `references/depth_levels.md`
2. **Selecao de Tipos**: Identifique os raciocinios em `references/reasoning_types.md`
3. **Matriz de Intersecao**: Verifique combinacoes em `references/intersection_matrix.md`
4. **Sincronizacao**: Aplique barreiras logicas para validar a saida

## Exemplo de Checkpoint Nexus (Nivel L3)

> **Checkpoint Nexus**:
> - **Nivel**: L3 (Critico/Academico)
> - **Raciocinios**: Bayesiano (Atualizacao de pesos), Sistemico (Arquitetura RAG), Falsificacionista (Teste de estresse)
> - **Intersecao**: IA & LLMs
> - **Barreira**: Aplicar Falsificacionista na conclusao para garantir robustez

## Quick Reference Files

| File | Content |
|------|---------|
| `references/reasoning_types.md` | Catalogo de 58 tipos com indicadores de profundidade |
| `references/depth_levels.md` | Definicao dos niveis L1-L4 |
| `references/intersection_matrix.md` | Matriz de combinacoes e barreiras de sincronizacao |
| `references/api_reference.md` | Documentacao de referencia da API |
| `scripts/example.py` | Script helper example |
| `templates/example_template.txt` | Template example |
