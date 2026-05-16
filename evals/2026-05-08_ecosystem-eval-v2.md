---
eval_date: 2026-05-08
ecosystem_version: 3.5
total_skills: 9
total_py_scripts: 4
total_plugins: 2
total_ciclos: 7
overall_health: 100
---

# Ecosystem Evaluation v2 - 2026-05-08

## Summary

| Metric | Result | Peso | Score |
|--------|--------|------|-------|
| py_compile | 4/4 OK | 2.0 | 100 |
| SKILL.md < 2.5KB | 9/9 OK | 2.0 | 100 |
| Frontmatter YAML | 9/9 OK | 1.5 | 100 |
| CJK zero leak | 50 files clean | 1.5 | 100 |
| Plugins (sync+evolve) | 2/2 present | 1.0 | 100 |
| Eval file present | 1 eval | 1.0 | 100 |
| Scoring 100/100 | pesquisa/doutorado/mestrado/startup | 1.5 | 100 |
| AGENTS.md evolution | 7 ciclos registrados | 1.0 | 100 |
| Orquestração ativa | ecosystem-sync + manus-evolve | 1.0 | 100 |
| Editais curados | 52 (16 FAPs estaduais) | 0.5 | 100 |

**Overall: 100/100**

## Component Details

### editais-br v7.3
- CACHE_VERSION = 'v7.1' (cache versionado)
- 52 editais curados (28 base + 16 FAPs estaduais + 4 exterior + 4 setoriais)
- 25 sub-dimensoes de classificacao
- Scoring query-aware 0-100 (query 30 + tipo 30 + perfil 20 + mecanismo 10 + completude 12 - penalidades 35)
- Word-boundary regex (_M helper) elimina falsos positivos de substring
- Perfil default inteligente por tipo

### Skills (9/9)
- docling-pdf-extraction: 2486B
- frontend-philosophy: 642B
- editais-br: 2480B
- code-philosophy: 622B
- code-review: 1260B
- plan-review: 1252B
- reasoning-orchestrator: 1979B
- token-efficiency: 1052B
- plan-protocol: 1497B

### Plugins (2)
- ecosystem-sync.ts (19KB) - Sincronizador multi-MCP
- manus-evolve.ts (15KB) - Motor evolutivo autonomo

## Scoring Distribution

| Categoria | Top Score | Matches 100 | Spread |
|-----------|-----------|-------------|--------|
| pesquisa | 100 | 4/4 | 0 pts |
| doutorado | 100 | 9/10 | 62 pts |
| mestrado | 100 | 8/10 | 82 pts |
| startup | 100 | 1/7 | 82 pts |
| cultura | 70 | 0/2 | 32 pts |
