---
name: followup-advocacia
description: >
  Rotina de follow-up para escritorio de advocacia: lembretes de prazos,
  cadencia de contatos, pipeline de demandas e produtividade.
  Use quando usuario mencionar "follow-up", "lembrete", "prazo", "pipeline",
  "produtividade escritorio", "cadencia", "relatorio semanal", "rotina OAB".
---

# Follow-up Advocacia — Produtividade e Gestao de Demandas

## Principio Central

Todo advogado precisa de sistema simples para nunca perder prazo,
manter contato com cliente e acompanhar pipeline de demandas.
Este follow-up opera em 3 camadas: diaria, semanal e mensal.

## Camada Diaria (Ritual Matinal)

### Revisao Matinal (5 minutos)

A cada novo dia, verificar:

1. **Audiencias Hoje:** Listar audiencias do dia com hora, vara, cliente
2. **Prazos Hoje:** Prazos que vencem hoje (diligencias, contestacoes, recursos)
3. **Pendencias Urgentes:** Tarefas pendentes ha mais de 3 dias
4. **Clientes Sem Contato:** Clientes sem interacao ha mais de 15 dias

### Cadencia de Contato

| Tipo de cliente | Frequencia de contato |
|-----------------|------------------------|
| Processo ativo (tramitando) | A cada 7-10 dias |
| Aguardando decisão | A cada 15 dias |
| Cliente novo (primeiros 30 dias) | A cada 5 dias |
| Cliente dormente (>60 sem processo) | Mensal |
| Cliente inativo (>1 ano) | Trimestral |

### Template de Contato

```
Ola [Nome], tudo bem?

Venho acompanha-lo sobre o processo [numero].
Status atual: [ultimo andamento].
Proximo passo: [data/acao esperada].

Precisa de algo? Estou a disposicao.
```

## Camada Semanal (Revisao de Sexta)

### Checklist Semanal

1. **Novos andamentos:** Verificar sistemas dos tribunais
2. **Clientes sem retorno:** Contatar quem nao respondeu na semana
3. **Prazo da semana que vem:** Antecipar tarefas
4. **Novos leads:** Avaliar status do funil deCaptação
5. **Honorarios:** Verificar inadimplencia

### Relatorio Semanal

```
SEMANA [DD a DD/MM/AAAA]
==========

AUDiencias: [N]
Prazos cumpridos: [N]
Novos processos: [N]
Clientes contatados: [N]
Honorarios recebidos: R$ [valor]
Clientes inadimplentes: [N]

OBSERVACOES:
- [items relevantes]

PROXIMA SEMANA:
- [N] prazos a vencer
- [N] audiencias agendadas
```

## Camada Mensal (Gestao Estrategica)

### Gestao de Pipeline

Categorizar todas demandas em pipeline:

| Estadio | Descricao | Status |
|---------|-----------|--------|
| CAPTACAO | Novo lead, em qualificacao | Frio→Quente |
| PROPOSTA | Proposta enviada, aguardando resposta | 7-15 dias |
| CONTRATADO | Contrato firmado, aguardando inicio | 30 dias |
| ATIVO | Processo em tramitacao | A cada 7 dias |
| DECISAO | Aguardando sentenca/acordao | 15 dias |
| ENCERRADO | Processo finalizado | Arquivo |
| INADIMPLENTE | Cliente sem pagamento | Bloquear |
| PERDIDO | Nao fechou ou desistiu | Anotar motivo |

### Metricas de Escritorio

| Metrica | Meta Mensal | Como melhorar |
|---------|------------|---------------|
| Fechamento | >30% propostas | follow-up 7 dias |
| Retencao | >85% clientes ativos | contato mensal |
| Inadimplencia | <10% receita | cobranca 15 dias |
| Prazo perdidos | 0 | alertas 5 dias antes |

## Integracao com MCPs

- **time (mcp-time):** Agendar lembretes de prazos
- **sqlite (mcp-server-sqlite):** Armazenar log de contatos
- **websearch:** Verificar prazos em tribunais
- **fetch:** Acessar sistemas de tribunais

## Sistema de Alertas

| Tipo | Trigger | Acao |
|------|---------|------|
| URGENTE | Prazo < 48h | Contato imediato |
| ALTO | Prazo < 5 dias | Alerta hoje |
| MEDIO | Prazo < 15 dias | Agendar revisao |
| BAIXO | Prazo > 15 dias | Revisao semanal |

## Regras de Compliance

- Nunca contatar cliente em excesso (max 1x por semana)
- Registrar TODOS os contatos em sistema
- Nunca fazer promessa de resultado
- Manter linguagem profissional em todos contatos

## Automacao Sugerida

Quando integrado ao Chat Juridico ou CRM:

```
[TRIGGER] Prazo definido no sistema
  → [ACAO] Enviar lembretes automaticos em D-5, D-2, D-1
  → [ACAO] Notificar advogado no WhatsApp
  → [ACAO] Adicionar tarefa na agenda
```

## Output Padrao — Resumo de Producao

```
RESUMO DE PRODUCAO — [MES/ANO]
==============================

DEMANDAS ATIVAS: [N]
- Trabalhista: [N]
- Civil: [N]
- Consumidor: [N]
- Familia: [N]
- Outros: [N]

PRAZOS VENCIDOS: [N]
PRAZOS CUMPRIDOS: [N]
AUDIENCIAS REALIZADAS: [N]

NOVOS CLIENTES: [N]
CLIENTES PERDIDOS: [N]
RECEITA HONORARIOS: R$ [valor]
INADIMPLENCIA: [N] clientes (R$ [valor])

TOP ACCOES REALIZADAS:
1. [acao mais frequente]
2. [segunda mais frequente]
3. [terceira]

PARA O PROXIMO MES:
- [prioridade 1]
- [prioridade 2]
- [prioridade 3]
```

