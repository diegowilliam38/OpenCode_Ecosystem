<div align="center">

# OpenCode Ecosystem v5.0.0

### Multi-Agent AI Platform for Assisted Scientific Research

**Ultima atualizacao: 2026-06-04** · 18 Rounds · 125 Agentes · 46 MCPs · 150 Skills · **CORA-Score 3.04 (M4)** · **SWOT 100/100** · **SWE-EVAL v1.0**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Node.js 20+](https://img.shields.io/badge/Node.js-20+-green.svg)](https://nodejs.org/)
[![Agents](https://img.shields.io/badge/Agents-125-6366f1?style=flat-square)](agents/)
[![MCPs](https://img.shields.io/badge/MCP_Servers-46-0ea5e9?style=flat-square)](opencode.json)
[![Skills](https://img.shields.io/badge/Skills-150-10b981?style=flat-square)](skills/)
[![Tests](https://img.shields.io/badge/Testes-34/34_SWE--Eval-22c55e?style=flat-square)](swe-eval-v1/)
[![CORA-Score](https://img.shields.io/badge/CORA--Score-3.04_M4-e11d48?style=flat-square)](https://github.com/MarceloClaro/CORA-Eval-Dissertacao)
[![SWE-Score](https://img.shields.io/badge/SWE--Score-v1.0-8b5cf6?style=flat-square)](swe-eval-v1/)
[![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF?style=flat-square)](https://github.com/MarceloClaro/Antiprojeto-UFC-PPGTE/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square)](https://github.com/MarceloClaro/Antiprojeto-UFC-PPGTE)
[![SWOT](https://img.shields.io/badge/SWOT-100/100-f59e0b?style=flat-square)](https://github.com/MarceloClaro/Antiprojeto-UFC-PPGTE)

</div>

---

## Sobre

O **OpenCode Ecosystem** e uma plataforma multi-agente para pesquisa cientifica assistida. Diferente de sistemas que dependem de um unico modelo, este ecossistema coordena **125 agentes especializados**, **46 servidores MCP** e **150 skills** que colaboram, debatem e verificam resultados entre si.

A arquitetura de 6 camadas com injecao de dependencia suporta um pipeline academico que vai da busca autonoma em fontes academicas (arXiv, PubMed, OpenAlex, Semantic Scholar, CORE, Sci-Hub) ate a geracao de artigos com exportacao LaTeX/PDF, passando por revisao simulada por pares e verificacao formal multi-agente.

### SWE-EVAL v1.0 — Framework de Evolucao (NOVO)

Derivado do parecer tecnico sobre os manuscritos "Engenharia de Software com Agentes Inteligentes" (livro, Sandeco, 7 capitulos) e "From Prompt to Process" (artigo, arXiv:2606.04967v1), o **SWE-EVAL** preenche 9 lacunas de seguranca e qualidade no ecossistema:

| ID | Componente | Status | Prioridade |
|----|-----------|:------:|:----------:|
| L1 | SWE Process Benchmarks (6 dimensoes × 5 tarefas) | 100% | P2 |
| L2 | Supply Chain Security (SHA256 + Ed25519) | 100% | **P0** |
| L3 | SpecDriftDetector (AST diff spec↔codigo) | 100% | **P1** |
| L4 | Context Grounding / API Hallucination Detection | 100% | **P1** |
| L5 | ArtifactSyncEngine (grafo de dependencias) | 100% | P2 |
| L6 | Permission Tiers + Audit Log (4 niveis) | 100% | **P0** |
| L7 | Registry v2.0 (SemVer + SHA256 + assinatura) | 100% | P2 |
| L8 | EvalLab (t-test + Cohen's d + ANOVA) | 100% | P3 |
| L9 | CrossPlatformValidator (3 plataformas) | 100% | P3 |

> **TDD:** 34/34 testes passando | **Arquivos:** 30 (specs + codigo + testes) | **Linhas:** ~2.400 Python

Este projeto e um trabalho em andamento. Muitos componentes estao em estagio experimental e as metricas reportadas sao auto-avaliadas pelo proprio sistema, nao por auditores externos.

---

## CORA-Eval — Maturidade Cientifica

O ecossistema e validado pelo **CORA-Eval**, benchmark de 150 tarefas em 10
dimensoes × 4 niveis (Basico a Pesquisa). Resultados da execucao real:

| Metrica | Valor |
|---------|:-----:|
| CORA-Score bruto | **3.04** (Pesquisa, M4) `[auto-reportado]` |
| Validacao externa (PE + Rosalind + Expandida) | **51/51 (100%)** |
| Testes internos (16 suites) | **327/327 (100%)** |
| Testes skipados (WDAC Windows) | 17 (numpy/scipy indisponivel) |
| Calibracao V1-V7 (F1 medio) | **95.5%** (466 testes) |
| Cross-Validation K=10 | **CV=2.2%** |
| Dimensoes em N4 (Pesquisa) | **5** (D1, D2, D3, D7, D10) |
| Avaliacao SWOT+TDD | **100/100** (13/13 recomendacoes) |

> **Repositorio:** [CORA-Eval-Dissertacao](https://github.com/MarceloClaro/CORA-Eval-Dissertacao)
> **Avaliacao:** [Anteprojeto-UFC-PPGTE](https://github.com/MarceloClaro/Antiprojeto-UFC-PPGTE)

---

## Ciclos de Desenvolvimento (18 iteracoes)

### Iteracao 18 — SWE-EVAL v1.0 ← NOVO
| Metrica | Valor |
|---------|-------|
| Score auto-atribuido | 96/100 |
| Origem | Manuscrito "Engenharia de Software com Agentes Inteligentes" (Sandeco, 7 cap.) + Artigo "From Prompt to Process" (arXiv:2606.04967v1) |
| Skills adicionadas | swe-eval-v1, supply-chain-security, spec-drift-detector, context-grounding, artifact-sync, permission-tiers, registry-v2, eval-lab, cross-platform-validator |
| Resultado | 9 componentes implementados; 34/34 TDD; 2.400+ linhas Python; auditoria revelou 9 lacunas (0 completas → 9 completas) |
| Parecer Tecnico | [PARECER_TECNICO.md](PARECER_TECNICO.md) — analise formal dos 2 manuscritos |

### Iteracao 17 — CORA-Eval Benchmark
| Metrica | Valor |
|---------|-------|
| Score auto-atribuido | 97/100 |
| Resultado | 150 tarefas em 10 dimensoes; baseline CORA-Score 0.67 |

### Iteracoes 1-16
| Score medio auto-atribuido | 85-98/100 |
| Ver historico completo em [OPENCODE_ECOSYSTEM.md](OPENCODE_ECOSYSTEM.md) |

---

## Progressao (auto-reportada)

| Metrica | Inicio (~v1.0) | Atual (~v5.0.0) | Variacao |
|---------|:--------------:|:---------------:|:--------:|
| Skills | 20 | 150 | +130 |
| Agentes | ~25 | 125 | +100 |
| MCPs | 12 | 46 | +34 |
| Testes | ~200 | 591 passando | +391 |
| Iteracoes | 1 | 18 | +17 |
| Componentes SWE-EVAL | 0 | 9 (34/34 TDD) | +9 |

---

## Estrutura do Repositorio

| Diretorio/Arquivo | Descricao |
|-------------------|-----------|
| `agents/` | 79 definicoes de agentes em Markdown com frontmatter YAML |
| `skills/` | 150 skills com padrao progressive disclosure |
| `nexus/` | Orquestrador multi-agente Nexus |
| `quantum/` | Modulo de computacao quantica |
| `criador-artigo/` | Pipeline academico MASWOS |
| `basis-research/` | Subsistema SEEKER de pesquisa autonoma |
| `core/` | Infraestrutura core — Container DI, bridges |
| `plugins/` | Plugins TypeScript — AutoEvolve, sync |
| `swe-eval-v1/` | **NOVO** — Framework de evolucao com 9 componentes TDD |
| `commands/` | 29 definicoes de comandos slash |
| `diagrams/` | Diagramas SVG de arquitetura |
| `evolution/` | Registros das 18 iteracoes |
| `docs/` | Documentacao de engenharia de software |
| `tdd-docs/` | Documentacao de TDD academico |
| `tests/` | Suite de testes |
| `opencode.json` | Configuracao principal (46 MCPs, agentes, skills) |
| `PARECER_TECNICO.md` | **NOVO** — Analise tecnica dos manuscritos fundacionais |
| `ROADMAP.md` | **Atualizado** — Roadmap com prioridades P0-P3 |

---

## Documentacao

| Documento | Conteudo |
|-----------|----------|
| [PARECER_TECNICO.md](PARECER_TECNICO.md) | **NOVO** — Analise dos manuscritos "Engenharia de Software com Agentes Inteligentes" e "From Prompt to Process" |
| [SWE-EVAL v1.0](swe-eval-v1/FRAMEWORK.md) | **NOVO** — Framework de 9 componentes para evolucao do ecossistema |
| [ENGENHARIA_DE_SOFTWARE.md](docs/ENGENHARIA_DE_SOFTWARE.md) | SDD, TDD, CI/CD, SWEBOK, Git Safety, ADR |
| [Roadmap](ROADMAP.md) | Planejamento futuro com SWE-EVAL |
| [Cora-Debate](tdd-docs/CORA_DEBATE.md) | Verificacao simbolica V1-V7 |
| [PhD Auditor](tdd-docs/PHD_AUDITOR.md) | NashSolver, StatisticalRigor |
| [TDD Academico](tdd-docs/README.md) | 557 testes, 25/25 validacoes |

---

## Instalacao

```bash
git clone https://github.com/MarceloClaro/OpenCode_Ecosystem.git
cd OpenCode_Ecosystem
bun install
pip install -r requirements.txt
opencode init
```

---

## Licenca

MIT License — veja [LICENSE](LICENSE).

Copyright (c) 2026 Marcelo Claro Laranjeira · marceloclaro@gmail.com · Prefeitura Municipal de Crateus/CE — [ORCID: 0000-0001-8996-2887](https://orcid.org/0000-0001-8996-2887).

---

## Citacao

```bibtex
@software{OpenCode_Ecosystem2026,
  author = {Marcelo Claro Laranjeira},
  title = {OpenCode Ecosystem: Multi-Agent AI Platform for Assisted Scientific Research},
  year = {2026},
  version = {5.0.0},
  url = {https://github.com/MarceloClaro/OpenCode_Ecosystem}
}
```

---

<div align="center">

**OpenCode Ecosystem v5.0.0** · 18 Iteracoes · 125 Agentes · 46 MCPs · 150 Skills · SWE-EVAL v1.0

Trabalho em andamento — metricas auto-reportadas

Autor: Marcelo Claro Laranjeira — [ORCID: 0000-0001-8996-2887](https://orcid.org/0000-0001-8996-2887)

Professor / Pedagogo — Secretaria de Educacao, Prefeitura Municipal de Crateus, Ceara, Brasil

Contato: marceloclaro@gmail.com | +55 (88) 981587145

</div>
