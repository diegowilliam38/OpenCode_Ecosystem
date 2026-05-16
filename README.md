# 🧠 OpenCode Ecosystem

> Framework autônomo de IA assistida para desenvolvimento, pesquisa acadêmica e produção científica — construído sobre o [OpenCode CLI](https://opencode.ai).

[![Health Score](https://img.shields.io/badge/health-100%25-brightgreen)](.)
[![MCPs](https://img.shields.io/badge/MCPs-18-blue)](.)
[![Agents](https://img.shields.io/badge/agents-125+-purple)](.)
[![Skills](https://img.shields.io/badge/skills-74-orange)](.)
[![Evolution](https://img.shields.io/badge/evolution-8_rounds-green)](.)

---

## Visão Geral

Sistema modular que integra **18 MCPs**, **125+ agentes especializados**, **74 skills** e **2 plugins TypeScript** em uma arquitetura unificada com auto-gestão intra-sessão.

```
┌──────────────────────────────────────────────────┐
│              OpenCode Ecosystem v3.5              │
│                                                    │
│  MCPs (18) ◄──► Skills (74) ◄──► Agents (125+)   │
│       │            │                │              │
│       └────────────┼────────────────┘              │
│                    │                               │
│           ┌────────┴────────┐                      │
│           │  Health Engine  │                      │
│           │   (100% OK)    │                      │
│           └────────┬────────┘                      │
│                    │                               │
│  Plugins (12) ◄──► Commands (14) ◄──► LSP (1)    │
└──────────────────────────────────────────────────┘
```

## Módulos Principais

| Módulo | Descrição | Componentes |
|--------|-----------|-------------|
| **`agents/`** | Definições de agentes especializados | 57 agentes core (.md) |
| **`basis-research/`** | SEEKER — pipeline de pesquisa profunda | 10 agentes Python + árvore de argumentos |
| **`criador-artigo/`** | MASWOS — produção acadêmica Qualis A1 | 49 agentes + auto-scoring |
| **`nexus/`** | Orquestração multi-agente v6.2 | 52 scripts Python + 6 camadas |
| **`quantum/`** | QML Medical Imaging | VQC + Grad-CAM + ZNE |
| **`editais-br/`** | Busca de editais acadêmicos brasileiros | API + extractors + pipeline |
| **`plugins/`** | Sincronização e evolução | ecosystem-sync.ts + manus-evolve.ts |
| **`skills/`** | Habilidades do ecossistema | 12 categorias |
| **`evolution/`** | Ciclos evolutivos documentados | 8 rounds + skills auto-geradas |
| **`core/`** | Infraestrutura Python | SQLite WAL + Event Bus async |
| **`command/`** | Comandos slash | 14 comandos (/plan, /evolve, /auto, etc.) |

## Arquitetura de Plugins

### ecosystem-sync.ts (v3.5)
- Cross-validation automática em `session.created`
- Monitoramento de latência e erros por MCP
- Health scoring dinâmico com alertas (critical < 70, attention < 85)
- Observabilidade em JSONL

### manus-evolve.ts (v2.2)
- Pipeline PlanAct: PLAN → ACT → CORRECT → REFLECT → EXTRACT → EVOLVE → NEXUS
- Geração autônoma de skills em `session.idle`
- Nexus pipeline integrado: scan → heal → learn
- Auto-aprovação de ferramentas confiáveis

## MCPs Configurados (18)

| Categoria | MCPs |
|-----------|------|
| **Busca** | websearch (DuckDuckGo), gh_grep (GitHub), context7 (docs), scihub (papers) |
| **Navegador** | playwright, chrome-devtools |
| **Código** | eslint, diff, code-runner, python-interpreter |
| **Dados** | sqlite, fetch, pdf, time, pandoc |
| **Raciocínio** | sequential-thinking, memory, mem0 |
| **Infra** | filesystem, github |

## Pipeline Acadêmico

```
SEEKER (pesquisa) → Criador de Artigo (49 agentes, 8 fases)
  → Escrita Anti-IA (TSAC, 87 palavras proibidas)
  → Cross-validation (Pearson, 3 níveis)
  → Peer Review emulado (5 revisores)
  → Auto Score Qualis (10 critérios)
  → Manus Evolve (aprendizado por ciclo)
  → Qualis A1 95/100
```

## Requisitos

- **Node.js** v25+
- **Bun** 1.3+
- **Python** 3.11+
- **OpenCode CLI** 1.14+
- **Git**

## Instalação

```bash
git clone https://github.com/anvix9/opencode-ecosystem.git
cd opencode-ecosystem
npm install  # ou bun install
pip install -r basis-research/requirements.txt
```

## Uso

```bash
# Iniciar OpenCode com o ecossistema
opencode

# Comandos disponíveis
/plan        # Planejamento estruturado
/evolve      # Ciclo evolutivo
/auto        # Modo autônomo
/quantum     # Pipeline quântico
/artigo      # Produção acadêmica
/reversa     # Engenharia reversa
```

## Licença

MIT

---

*Desenvolvido com ❤️ usando OpenCode + big-pickle (OpenCode Zen)*
