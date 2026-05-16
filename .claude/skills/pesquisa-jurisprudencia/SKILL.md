---
name: pesquisa-jurisprudencia
description: >
  Pesquisa jurisprudencial estruturada em bases brasileiras: STJ, STF, TJSP,
  TRTs e outros tribunais. Use quando usuario mencionar "jurisprudencia",
  "pesquisar decisao", "encontrar precedente", "STJ sobre", "TJ sobre",
  "pesquisa de jurisprudencia", "buscar acordao", "pesquisar tema juridico".
---

# Pesquisa Jurisprudencial — Brasil

## Principio Central

Pesquisar jurisprudencia requer metodo: tema claro, busca em multiplas
bases, filtro de relevancia e citacao responsavel. Nunca inventar precedentes;
sempre verificar existencia real.

## Preparacao da Pesquisa

### Antes de Pesquisar

1. Definir o **tema juridico** com precisao
2. Identificar o **tribunal relevante** (STJ para infracional federal, TJ para
   estadual, TRT para trabalhista)
3. Verificar se existe **sutileza especifica** (ex: "honorarios perito
   trabalhista" vs "honorarios perito civel")
4. Preparar **sinopse** do problema (2-3 linhas)

### Formula de Busca

Usar estrutura: `[TESE] site:[TRIBUNAL]`

| Tribunal | URL base | Filtros recomendados |
|----------|----------|---------------------|
| STJ | stj.jus.br/busca-unificada | REsp, RE, CC, AgInt |
| STF | stf.jus.br | RE, ADI, ADPF, MS |
| TJSP | tjsp.jus.br | Apelacao, Agravo |
| TJMG | tjmginternet.tjmg.jus.br | Civil, Criminal |
| TRT | trt.jus.br | Vara, Regiao |
| TRF | trf.jus.br | Regiao |

## Protocolo de Pesquisa

### Passo 1 — Pesquisa Macro

Busca inicial ampla para identificar principais correntes:

```
site:stj.jus.br [TEMA PRINCIPAL]
site:tjsp.jus.br [TEMA PRINCIPAL]
```

### Passo 2 — Pesquisa Refinada

Filtrar por tipo de inteiro, ano e relevancia:

```
site:stj.jus.br [TEMA] [DETALHE] "[TESE ESPECIFICA]"
```

### Passo 3 — Verificacao de Súmulas

Sempre verificar existencia de sumula vinculante ou sumula:

```
"sumula" [TRIBUNAL] "[TEMA]"
"sumula vinculante" [TEMA]
```

### Passo 4 — Captura de Dados

Para cada precedente encontrado, capturar:

```
TIPO: [REsp/RE/Apelacao/etc]
NUMERO: [numero]
TRIBUNAL: [nome completo]
RELATOR: [nome do ministro/desembargador]
DATA: [DD/MM/AAAA]
TESE: [enunciado da tese em 1-2 linhas]
EMENTA: [trecho relevante da ementa]
DISPOSITIVO: [conclusao resumida]
FONTE: [link completo]
```

### Passo 5 — Avaliacao de Relevancia

| Criterio | Pergunta |
|----------|----------|
| Autoridade | E do STJ/STF ou tribunal superior? |
| Atualidade | E pos-2015? Legislacao pode ter mudado |
| Aree | Abrange situacao similar a do cliente? |
| Reputacao | Relator tem jurisprudencia consolidada no tema? |

## Citacao Responsavel

### Formato de Citacao para Pecas

```
EMENTA: [trecho integral da ementa exatamente como no tribunal]
[Identificacao completa: Tribunal, numero, relator, data, DJe]
```

### Regras de Integridade

- **Nunca resumir** ementa de forma que altere o sentido
- **Nunca citar** precedent without verificar existencia real
- **Sempre informar** quando pesquisa nao encontrar resultado
- **Sempre distinguir** caso concreto do precedente

## Integracao com MCPs

- **websearch (mcp-fetch-server --duckduckgo):** pesquisa primaria em todas bases
- **wikipedia:** conceito juridico base antes de pesquisa em tribunal
- **context7:** busca contextualizada por tema juridico
- **fetch:** acessar base especifica do tribunal

## Casos de Uso Comum

| Situacao | Pesquisa recomendada |
|----------|----------------------|
| Honorarios advogado | STJ + "honorarios sucumbenciais" + ano > 2015 |
| Prisao domiciliar | STF + "prisao domiciliar" + "maiores 80" |
| Responsabilidade civil | TJSP + "responsabilidade civil" + "dano moral" |
| Horas extras | TRT + "horas extras" + "intervalo" |
| Contrato bancario | STJ + "contrato bancario" + "clausula abusiva" |

## Output Padrao

Apos pesquisa, apresentar:

```
[PESQUISA JURISPRUDENCIAL]
Tema: [tema]
Data: [DD/MM/AAAA]
Tribunais pesquisados: [lista]

[PRECEDENTES ENCONTRADOS]
1. [precedente 1 - formato completo]
2. [precedente 2 - formato completo]
[N se nao houver]

[SUMULAS IDENTIFICADAS]
- [sumula se houver]

[TESE PREPONDERANTE]
[sintese da corrente majoritaria em 2-3 linhas]

[ALINHAMENTO AO CASO]
[breve analise de como os precedentes se aplicam ao caso especifico]
```

