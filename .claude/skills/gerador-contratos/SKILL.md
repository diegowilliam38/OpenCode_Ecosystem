---
name: gerador-contratos
description: >
  Gerador de contratos juridicos em HTML otimizado para PDF, com identidade
  visual profissional. Contratos sociais, procuraes, acordos, termos,
  compromissos. Use quando usuario mencionar "gerar contrato", "redigir
  acordo", "contrato social", "procurao", "termo de", "documento juridico
  em PDF", "HTML de contrato".
---

# Gerador de Contratos Juridicos HTML

Gera arquivos `.html` otimizados para exportacao em PDF via browser
(Ctrl+P → Salvar como PDF → Margens: Padrao → Graficos de fundo: ativado).

## Tipos de Contrato Suportados

| Tipo | Descricao |
|------|-----------|
| CONTRATO-SOCIAL | Sociedade limitada, Ltda, SL |
| PROCURACAO | Geral, especial, substabelecimento |
| ACORDO | Extrajudicial, judicial, termos |
| TERMO | Responsabilidade, confidencialidade, quitacao |
| COMPROMISSO | Compra e venda, locacao, honra |
| MINUTA-CONSULTIVO | Documento em formato de contrato para revisao |

## Fluxo de Geracao

1. Identificar **tipo de contrato** e **partes** envolvidas
2. Verificar se escritorio ja configurado (dados de cabealho)
3. Se nao configurado, rodar wizard de configuracao
4. Coletar dados especificos do contrato
5. Gerar HTML completo
6. Salvar em `[tipo]_[partes]_data.html`
7. Presentar com `present_files`

## Preenchimento de Dados

### Dados Fixos (via configuracao do escritorio)

| Campo | Descricao |
|-------|-----------|
| {{NOME_ADVOGADO}} | Nome completo do advogado |
| {{OAB}} | Numero da OAB |
| {{RAZAO_SOCIAL}} | Razao social do escritorio |
| {{SIGLA}} | Sigla do logo (2 letras) |
| {{NOME_ESCRITORIO_CURTO}} | Nome curto para logo |
| {{ENDERECO_COMPLETO}} | Endereco formatado |
| {{CIDADE_UF}} | Cidade-UF |
| {{EMAIL}} | Email de contato |

### Dados Variaveis (por contrato)

| Campo | Descricao |
|-------|-----------|
| {{TIPO_CONTRATO}} | Nome do tipo de contrato |
| {{PARTE_A}} | Nome/qualificacao da parte A |
| {{PARTE_B}} | Nome/qualificacao da parte B |
| {{OBJETO}} | Objeto do contrato |
| {{VALOR}} | Valor (numero + extenso) |
| {{DATA_INICIO}} | Data de inicio |
| {{DATA_FIM}} | Data de termino |
| {{DATA_ASSINATURA}} | Data da assinatura |

## Estrutura HTML

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --ink:#1A1714;--gold:#B08A4E;--glt:#CFA96A;--muted:#6B5E4E;
  --rule:#DDD6C8;--cream-t:rgba(176,138,78,.05);
  --font-titulo:'Space Grotesk',sans-serif;--font-corpo:'DM Sans',sans-serif;
  --fs:15px;--line-height:1.65;--recuo:2cm;
  --faixa-width:6px;--margin-left:32mm;--margin-right:20mm;
}
html,body{margin:0;padding:0;background:white;-webkit-print-color-adjust:exact;print-color-adjust:exact}
@page{size:A4 portrait;margin-top:25mm;margin-bottom:22mm;margin-left:0;margin-right:0}
.doc{font-family:var(--font-corpo);font-size:var(--fs);color:var(--ink);background:white;width:210mm;margin:0 auto;padding-top:25mm;padding-bottom:0;padding-right:var(--margin-right);padding-left:var(--margin-left);border-left:var(--faixa-width) solid var(--gold);-webkit-print-color-adjust:exact;print-color-adjust:exact}
@media print{.doc{padding-top:0;margin:0}}
.hdr{display:flex;align-items:flex-end;justify-content:space-between;padding-bottom:12px;border-bottom:2px solid var(--gold);margin-bottom:26px;gap:20px;page-break-after:avoid;break-after:avoid}
.hdr-right{text-align:right}
.hdr-right .escritorio-nome{font-family:var(--font-titulo);font-size:8.5px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--muted);margin-bottom:5px}
.hdr-right .contato{font-size:9px;color:var(--ink);line-height:1.7}
.hdr-right .contato .sep{color:var(--gold);margin:0 4px}
.hdr-right .contato .email{color:var(--muted);font-size:8.5px}
.contrato-titulo{font-family:var(--font-titulo);font-size:18px;font-weight:700;color:var(--ink);text-align:center;text-transform:uppercase;letter-spacing:3px;margin:24px 0;page-break-after:avoid;break-after:avoid}
.par{font-size:var(--fs);color:var(--ink);line-height:var(--line-height);text-align:justify;text-indent:var(--recuo);margin-bottom:20px;orphans:3;widows:3;page-break-inside:avoid;break-inside:avoid}
.clausula-titulo{font-family:var(--font-titulo);font-size:var(--fs);font-weight:700;text-transform:uppercase;color:var(--ink);line-height:1.5;margin:20px 0 8px var(--recuo);page-break-after:avoid;break-after:avoid;page-break-inside:avoid;break-inside:avoid}
.fechamento{margin-top:40px;page-break-inside:avoid;break-inside:avoid}
.local-data{font-size:var(--fs);color:var(--ink);text-align:left;margin-bottom:40px}
.assinatura{font-family:var(--font-titulo);font-size:var(--fs);font-weight:500;color:var(--ink);text-align:center;line-height:1.7;page-break-inside:avoid;break-inside:avoid}
.assinatura .oab{font-size:13px;font-weight:400;color:var(--muted)}
.doc-footer{margin-top:32px;padding-top:12px;border-top:1px solid var(--rule);display:flex;justify-content:space-between;align-items:center;font-family:var(--font-titulo);font-size:8px;color:var(--muted);letter-spacing:1px;page-break-inside:avoid;break-inside:avoid}
.doc-footer .pgn{color:var(--gold);font-weight:600;font-size:9px}
</style>

<body>
<div class="doc">
  <div class="hdr">[Logo SVG][Dados escritorio]</div>
  <div class="contrato-titulo">{{TIPO_CONTRATO}}</div>
  <p class="par">[Preambulo identificando as partes]</p>
  <div class="clausula-titulo">CLÁUSULA PRIMEIRA — DO OBJETO</div>
  <p class="par">[Descricao do objeto]</p>
  <div class="clausula-titulo">CLÁUSULA SEGUNDA — DAS OBRIGAÇÕES</div>
  <p class="par">[Obrigacoes das partes]</p>
  <div class="fechamento">
    <p class="par">E por estarem de pleno acordo, as partes assinam o presente instrumento em 02 (duas) vias de igual teor.</p>
    <div class="local-data">{{CIDADE_UF}}, DD de mes de AAAA.</div>
    <div style="display:flex;justify-content:space-between;margin-top:40px;">
      <div class="assinatura" style="width:45%;">
        {{PARTE_A}}<br><span class="oab">ASSINATURA</span>
      </div>
      <div class="assinatura" style="width:45%;">
        {{PARTE_B}}<br><span class="oab">ASSINATURA</span>
      </div>
    </div>
  </div>
  <div class="doc-footer"><span>Documento Confidencial</span><span class="pgn">N / N</span></div>
</div>
</body>
```

## Regras de Exportacao

```
Ctrl+P → Salvar como PDF
Margens: Padrao
Graficos de fundo: ATIVADO ← obrigatorio
Escala: 100%
```

## Checklist de Verificacao

- [ ] Partes identificadas com nome/qualificacao/CNPJ/CPF
- [ ] Objeto descrito com precisao
- [ ] Prazo ou duracao definido
- [ ] Clausula de rescisao presente
- [ ] Clausula de foro competente incluida
- [ ] Assinatura com espaco para 2 vias

