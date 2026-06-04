# Roadmap — OpenCode Ecosystem v5.0.0

> Atualizado: 04/06/2026 — derivado do parecer tecnico SWE-EVAL v1.0

---

## Prioridades de Evolucao

### P0 — Critico (Producao Auditavel)

| ID | Componente | Status | Esforco |
|----|-----------|:------:|:-------:|
| L2 | Supply Chain Security (SHA256 + Ed25519) | 100% | Medio |
| L6 | Permission Tiers + Audit Log (4 niveis) | 100% | Baixo |
| — | Integracao L2+L6 ao ciclo de carga de skills | A fazer | Medio |
| — | Chaves de assinatura para todas as 150 skills | A fazer | Alto |

### P1 — Alto (Qualidade Continua)

| ID | Componente | Status | Esforco |
|----|-----------|:------:|:-------:|
| L3 | SpecDriftDetector (AST diff) | 100% | Alto |
| L4 | Context Grounding / API Hallucination | 100% | Alto |
| — | CI/CD gate com SpecDriftDetector | A fazer | Medio |
| — | Integracao L4 ao Cora-Debate V6 | A fazer | Medio |

### P2 — Medio (Ecossistema)

| ID | Componente | Status | Esforco |
|----|-----------|:------:|:-------:|
| L1 | SWE Process Benchmarks | 100% | Alto |
| L5 | ArtifactSyncEngine | 100% | Medio |
| L7 | Registry v2.0 | 100% | Medio |
| — | Expandir SWE para 20 tarefas × 4 niveis | A fazer | Alto |
| — | Migrar 150 skills do registry v1 para v2 | A fazer | Alto |

### P3 — Baixo (Pesquisa)

| ID | Componente | Status | Esforco |
|----|-----------|:------:|:-------:|
| L8 | EvalLab (t-test + Cohen's d) | 100% | Alto |
| L9 | CrossPlatformValidator | 100% | Baixo |
| — | Experimento A/B real: SDD vs Vibe Coding | A fazer | Alto |
| — | Validacao real cross-platform de 50 skills | A fazer | Medio |

---

## Marcos de Entrega

| Marco | Data Prevista | Componentes |
|-------|:------------:|-------------|
| M1 — Security Baseline | Jun/2026 | L2 + L6 integrados ao ciclo de carga |
| M2 — Quality Gate | Jul/2026 | L3 + L4 como gates de CI/CD obrigatorios |
| M3 — Registry Migration | Ago/2026 | 150 skills migradas para Registry v2.0 |
| M4 — Experimentacao | Set/2026 | Experimento A/B real publicado |

---

## Metricas de Sucesso

| Metrica | Atual | Meta |
|---------|:-----:|:----:|
| Cobertura TDD SWE-EVAL | 34/34 (100%) | Manter |
| Skills com assinatura | 0/150 (0%) | 150/150 (100%) |
| Cobertura Registry v2.0 | 0/150 (0%) | 150/150 (100%) |
| Drift Score medio | N/A | ≤ 5 |
| Grounding Score medio | N/A | ≥ 80/100 |
| Permission violations/mes | N/A | 0 nao autorizadas |
| Experimentos EvalLab | 0 | ≥ 3 |
| Skills cross-platform validadas | 0 | ≥ 50 |

---

*Roadmap alinhado com o parecer tecnico dos manuscritos fundacionais.*
*Prioridades: seguranca (P0) > qualidade continua (P1) > ecossistema (P2) > pesquisa (P3).*
