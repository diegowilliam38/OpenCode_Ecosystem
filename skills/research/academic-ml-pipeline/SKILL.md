---
name: academic-ml-pipeline
description: "Pipeline ML completo para análise acadêmica: correlação bootstrap, classificação ARM, detecção de anomalias, clusterização, feature importance e integração com artigo científico"
user-invocable: true
license: MIT
compatibility: OpenCode, Claude Code
metadata:
  author: OpenCode Ecosystem v4.1
  version: "1.1.0"
  ecossistema: opencode
  categoria: pesquisa-academica
  round: 11
  learning-session: "artigo-ARM-IAG-262-observacoes"
  v3-features: "knowledge_complexity, export_sophistication, product_density"
  v3-date: "2026-05-14"
allowed-tools: Read Edit Write Bash Python Code-Runner
---

# Academic ML Pipeline v1.1

Pipeline de Machine Learning para análise acadêmica, validado em sessão real com dataset de 262 observações × 14 features (11 originais + 3 de complexidade econômica) sobre Armadilha da Renda Média (ARM) e Inteligência Artificial Generativa (IAG).

## Visão Geral

Pipeline integrado que conecta análise quantitativa → geração de figuras → inserção em artigo acadêmico → exportação ABNT multi-formato.

## Workflow Completo (7 Etapas)

### Etapa 1: Configuração Reprodutível
- Seed global fixa (42)
- Hash do script registrado em metadados
- Diretório de outputs versionado
- Imports: pandas, numpy, scikit-learn, scipy, matplotlib, seaborn, plotly, json

### Etapa 2: Pré-processamento e Integridade
- Imputação por mediana (preserva distribuição)
- Flag de imputação para cada feature (diagnóstico)
- Classificação ARM relativa: bottom 20% crescimento entre países de renda média (PIBpc $1.136–$13.845)
- Z-score para detecção de outliers univariados
- Merged dataset com flags de proveniência

### Etapa 3: Análise Exploratória e Correlação
- Matriz de correlação de Pearson com heatmap (RdBu_r, -1 a +1)
- Matriz triangular superior (evita duplicação)
- Bootstrap de correlações (1000 iterações) para intervalos de confiança
- Correlações parciais com controle de PIB per capita
- Exportação para tabelas LaTeX/CSV

### Etapa 4: Classificação Supervisionada
- Target: ARM relativa (0/1)
- Modelos: Regressão Logística (baseline) + Random Forest
- Validação: Stratified K-Fold (k=5), 3 repeats
- Métricas: acurácia, F1, ROC-AUC, precisão, recall (com desvio padrão)
- Feature importance: importance_inherent (RF) + permutation importance (3 repeats)
- Threshold de 0.5 para classificação binária

### Etapa 5: Detecção de Anomalias e Clusterização
- **Anomalias**: Isolation Forest (contamination=auto, random_state=42)
  - Top 20 anomalias com scores
  - Visualização: scatter plot PIBpc × AI Readiness
- **Clusters**: K-Means (k=4, KMeans++ initialization)
  - Perfis: GDP per capita médio, AI readiness médio, contagem ARM
  - Visualização: scatter plot com centroides

### Etapa 6: Features de Complexidade Econômica (v3)
- **knowledge_complexity (KCI proxy)**: PC1 de 6 features de inovação (P&D, patentes, alta tecnologia, internet, ensino superior, prontidão IA). Explica 41.5% da variância. Carga mais alta: tertiary_enrollment (0.50), rd_spending (0.48), internet_users (0.47).
- **export_sophistication (EXPY proxy)**: PIB per capita ponderado por intensidade tecnológica das exportações (high_tech_exp, patent_apps, rd_spending). Pesos: 0.4/0.35/0.25 conforme Hausmann et al. (2007).
- **product_density (Densidade Produtiva)**: Similaridade cosseno do perfil multivariado (11 features) do país com a fronteira tecnológica (top 10% PIB per capita). Normalizado [0,1].

### Etapa 7: Integração com Artigo Científico
- Geração de 7 figuras sequenciais (PNG 300dpi):
  - Fig 1: Feature Importance (RF + Permutation)
  - Fig 2: Classificação (Logística vs RF)
  - Fig 3: Clusters de Desenvolvimento
  - Fig 4: Anomalias (Isolation Forest)
  - Fig 5: Matriz de Correlação
  - Fig 6: Fluxograma Metodológico
  - Fig 7: Mapa-múndi ARM+IAG (Plotly choropleth + scattergeo)
- Nomenclatura padronizada: fig{1-7}_{nome}.png
- Alt text descritivo para cada figura
- Paths relativos no artigo markdown
- Validação: 7/7 paths no disco, zero erros de encoding

## Recursos da Skill

| Recurso | Localização | Descrição |
|---------|-------------|-----------|
| Script gerador de figuras | `scripts/gerar_figuras.py` | Gera 7 figuras do pipeline ML |
| Referência de features | `references/feature_catalog.md` | Catálogo das 11 features |
| Template de resultados | `references/results_template.json` | Schema JSON de resultados ML |
| Log de métricas | `references/metrics_log.md` | Registro de métricas da sessão real |

## Métricas da Sessão de Validação

| Métrica | v2 (11 features) | v3 (14 features) |
|---------|:----------------:|:----------------:|
| Dataset | 262 obs × 11 feats | 262 obs × 14 feats |
| ARM strict | 3 países | 3 países |
| ARM relativa | 29 países | 29 países |
| LogReg ROC-AUC | 0.707 ± 0.085 | **0.722 ± 0.057** (+1.5%) |
| LogReg Accuracy | 0.649 ± 0.041 | 0.641 ± 0.043 (-0.8%) |
| RF ROC-AUC | 0.791 ± 0.072 | 0.773 ± 0.053 (-1.8%) |
| RF Accuracy | 87.4% | 87.4% (=) |
| Linear Reg R2 | -0.193 | **-0.174** (+1.9%) |
| Anomalias | 27 | 27 |
| Clusters (k=4) | 126/54/81/1 | 125/84/52/1 |

### Feature Importance — 3 Novas Features de Complexidade (v3)

| Feature | RF Importance | Rank (14 feats) | Permutation Importance |
|---------|:------------:|:---------------:|:---------------------:|
| product_density | **12.86%** | **#2** (atrás apenas de GDP pc) | 0.80% |
| knowledge_complexity | **8.88%** | **#3** | 3.23% |
| export_sophistication | **5.26%** | **#10** | 1.62% |

### Ganho Preditivo Líquido (v3 vs v2)

| Modelo | Acurácia | AUC | R2 |
|--------|:-------:|:---:|:--:|
| Logistic Regression | -0.0075 | **+0.0151** | — |
| Random Forest | -0.0001 | -0.0182 | — |
| Linear Regression | — | — | **+0.0191** |
| Ridge (alpha=1) | — | — | **+0.0175** |
| Random Forest Reg | — | — | -0.0316 |

**Interpretação**: As 3 medidas de complexidade econômica agregam valor preditivo para modelos lineares/paramétricos (LogReg AUC +1.5%, R2 +1.9%), mas são parcialmente redundantes para Random Forest, que já captura interações não-lineares entre as 11 features originais. A **product_density** emerge como a 2ª feature mais importante (12.9%), superando P&D, internet e educação — confirmando a tese de Hidalgo et al. (2007) de que a densidade no espaço de produtos é preditora central do desenvolvimento econômico.

## Referências

- Script de pipeline v2: `03_ml_pipeline_v2.py` (11 features)
- Script de pipeline v3: `03_ml_pipeline_v3.py` (14 features, 3 novas de complexidade)
- Script de figuras: `gerar_figuras.py` (reproduzível com seed 42)
- Dataset: WDI + Oxford Insights AIPI + FMI/WEO
- Hausmann, R., Hidalgo, C. A., et al. (2014). *The Atlas of Economic Complexity*. MIT Press.
- Hausmann, R., Hwang, J., & Rodrik, D. (2007). What you export matters. *Journal of Economic Growth*, 12(1), 1-25.
- Hidalgo, C. A., Klinger, B., Barabási, A. L., & Hausmann, R. (2007). The product space conditions the development of nations. *Science*, 317(5837), 482-487.
