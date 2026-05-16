---
name: triagem-juridica
description: >
  Triagem jurídica de leads e consultas: classifica area do direito, avalia
  urgencia, identifica dados essenciais e encaminhamento correto. Use quando
  usuario mencionar "triar", "classificar consulta", "qualificar lead juridico",
  "primeiro atendimento", "encaminhamento", "triagem de demanda" ou similar.
---

# Triagem Jurídica — Classificacao e Encaminhamento de Demandas

## Principio Central

Todo contato juridico novo deve passar por triagem sistematica: identificar
area do direito, nivel de urgencia, dados essencias e melhor fluxo de
encaminhamento. Nunca diagnosticar resultado, apenas classificar e direcionar.

## Fluxo de Triagem

### ETAPA 1 — Identificacao da Area

Classificar em uma das areas principais:

| Codigo | Area | Exemplos de demanda |
|--------|------|---------------------|
| CIVEL | Civel Geral | Contratos, responsabilidade civil, usucapiao, cobrancas |
| TRAB | Trabalhista | CLT, verbas rescisorias, horas extras, assedio |
| CONS | Consumidor | Procon, CDC, produto defeituoso, servico mal prestado |
| FAM | Familia | Divorcio, guarda, pensao, inventario, interdiccao |
| PENAL | Penal | Crime, defesa, denuncia, habeas corpus |
| PREV | Previdencial | INSS, beneficio, aposentadoria, LOAS |
| TRIB | Tributario | IR, ICMS, ISS, divida ativa,_auto de infracao |
| IMOB | Imobiliario | contratos, locacao, usucapiao, evicao |
| EMP | Empresarial | sociedade, Recovery, falencia, MEI |
| OUT | Outro | Areas nao listadas |

### ETAPA 2 — Avaliacao de Urgencia

| Nivel | Condicoes | Prazo de encaminhamento |
|-------|-----------|-------------------------|
| URGENTE | Ameaca vida, violencia, detencao, prazo judicial iminente | Imediato |
| ALTO | Prazo processual < 5 dias, perda de direito iminente | 24-48h |
| MEDIO | Prazo processual 5-30 dias, dano economico significativo | 1 semana |
| BAIXO | Consulta geral, demanda nova sem prazo | 2 semanas |
| TRIAGEM | Dados insuficientes para classificar | Coletar mais info |

### ETAPA 3 — Dados Essenciais por Area

**CIVEL/TRAB/CONS:**
- Nome completo do cliente
- CPF / CNPJ
- Contato (telefone, email)
- Contra-parte / empresa
- Resumo da demanda (ate 5 linhas)
- Data ou prazo relevante (se houver)

**FAM:**
- Estado civil atual
- Presenca de filhos (idades)
- Patrimonio envolvido (imoveis, veiculos, contas)
- Violencia domestica (sim/nao) — se sim, URGENTE

**PENAL:**
- Tipo de feito (vitima, denuncia, defesa)
- Delegacia/numero do BO
- Prazo de flagrante ou prisao
- LOCALIZAR IMEDIATAMENTE ADVOGADO ESPECIALIZADO

**PREV:**
- Tipo de beneficio buscado
- contribuicao / carencia
- Deficiencia ou doenca (laudos)
- Ja pedir orientacao ao INSS

### ETAPA 4 — Frases de Classificacao

Apos classificar, usar sempre a frase:

```
Classificacao: [CODIGO] | Urgencia: [Nivel] | Encaminhamento: [Acao]
```

Exemplos:
- "Classificacao: TRAB | Urgencia: MEDIO | Encaminhamento: Agendar consulta"
- "Classificacao: CONS | Urgencia: BAIXO | Encaminhamento: Revisao contratual"
- "Classificacao: PENAL | Urgencia: URGENTE | Encaminhamento: LOCALIZAR ADVOGADO PENAL IMEDIATAMENTE"
- "Classificacao: FAM | Urgencia: ALTO | Encaminhamento: Medida protetiva em ate 48h"

### ETAPA 5 — Protocolo de Escalada

| Situacao | Acao |
|----------|------|
| Violence domestica | "Vou buscar advogado de Familia especializado em medida protetiva" |
| Prisao/flagrante | "Advogado Penal deve ser acionado imediatamente" |
| Prazo judicial < 48h | "Agendar consulta hoje mesmo ou buscar plantao OAB" |
| Menor de idade envolvido | "Advogado de Familia/Infancia acionado" |
| Dados insuficientes | Fazer perguntas de triagem antes de classificar |

## Regras de Compliance OAB

- Nao fazer promessa de resultado
- Nao dar opiniao juridica sem contrato firmado
- Nao cobrar consulta inicial sem combinado
- Sempre informar: "Isso e uma triagem inicial, nao constitui consulta juridica"

## Output Padrao

Apos triagem, apresentar:

```
[DADOS COLETADOS]
Nome: [nome]
CPF: [cpf]
Contato: [telefone] | [email]

[CLASSIFICACAO]
Area: [CODIGO] - [nome da area]
Urgencia: [Nivel]
Resumo: [ate 5 linhas]

[DADOS DA DEMANDA]
Tipo: [descricao]
Contra-parte: [nome/empresa]
Valor estimado (se aplicavel): [R$ X ou "a definir"]
Documentos mencionados: [lista breve]

[ENCAMINHAMENTO SUGERIDO]
Proxima acao: [agendar/encaminhar/pedir docs]
Prazo ideal: [DD/MM/AAAA]
Documentos necessarios: [lista]
```

## Integracao com MCPs

- Usar websearch para verificar urgencia de prazos (ex: "prazo contestacao [vara] [comarca]")
- Usar Wikipedia para identificar conceitos juridicos desconhecidos
- Usar fetch para consultar site do TJ para jurisprudencia rapida

## Casos Especiais

**Violencia domestica:** Classificar como FAM+URGENTE, jamais pedir mais informacoes
desnecessarias. Orientar: "Vou conecta-lo com advogado especializado agora."

**Detencao/Prisao:** Classificar como PENAL+URGENTE. Fornecer contato do
Plantao OAB local imediatamente.

**Menor de idade vitima:** Classificar como FAM+URGENTE+OUTRO. Contatar
Defensoria Publica se nao houver advogado disponivel.

