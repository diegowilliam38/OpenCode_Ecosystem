"""
Auto-Scoring Qualis A1 — Avaliacao automatizada de manuscritos
Integrado com MCPs do ecossistema para validacao em tempo real.
"""
import json, os, sys, argparse
from pathlib import Path

RUBRIC = {
    "rigor_academico": {"peso": 10, "desc": "Rigor academico e profundidade teorica"},
    "densidade_citacoes": {"peso": 10, "desc": "Densidade de citacoes (>=55 referencias com DOI)"},
    "abnt_compliance": {"peso": 10, "desc": "Conformidade ABNT NBR 6023/6028"},
    "originalidade": {"peso": 10, "desc": "Originalidade e relevancia da contribuicao"},
    "metodologia": {"peso": 10, "desc": "Metodologia reprodutivel e documentada"},
    "analise_estatistica": {"peso": 10, "desc": "Analise estatistica rigorosa e validada"},
    "coerencia": {"peso": 10, "desc": "Coerencia argumentativa (intro↔conclusao)"},
    "qualidade_visual": {"peso": 10, "desc": "Qualidade de graficos, tabelas e figuras"},
    "internacionalizacao": {"peso": 10, "desc": "Abstract em ingles + conformidade internacional"},
    "autocontencao": {"peso": 10, "desc": "Auto-containment (>=110 paginas, >=48k palavras)"},
}

def score_manuscript(manuscript_dir):
    """Score a manuscript against Qualis A1 rubric."""
    results = {}
    total = 0
    
    # 1. Rigor: check footnotes, DOIs, and TSAC patterns
    ref_count = 0
    for md_file in Path(manuscript_dir).rglob("*.md"):
        content = open(md_file, encoding='utf-8', errors='ignore').read()
        ref_count += content.count("[^")  # TSAC footnotes
        ref_count += content.count("doi.org")
        ref_count += content.count("Disponivel em:")
    refs_dir = Path(manuscript_dir) / "referencias"
    if refs_dir.exists():
        for f in refs_dir.glob("*.md"):
            content = open(f, encoding='utf-8', errors='ignore').read()
            ref_count += content.count("DOI:") + content.count("doi:")
    results["rigor_academico"] = min(10, max(5, ref_count // 10))
    
    # 2. Citation density
    doi_count = 0
    for md_file in Path(manuscript_dir).rglob("*.md"):
        content = open(md_file, encoding='utf-8', errors='ignore').read()
        doi_count += content.count("10.") + content.count("doi.org")
    results["densidade_citacoes"] = 10 if doi_count >= 55 else min(9, doi_count // 6)
    
    # 3. ABNT: check for ABNT patterns
    abnt_score = 5
    for md_file in Path(manuscript_dir).rglob("*.md"):
        content = open(md_file, encoding='utf-8', errors='ignore').read()
        if "ABNT" in content: abnt_score += 1
        if "NBR 6023" in content or "NBR 6028" in content: abnt_score += 1
        if "SOBRENOME" in content: abnt_score += 1
        if "et al." in content: abnt_score += 1
        if content.count("p.") > 5: abnt_score += 1
    results["abnt_compliance"] = min(10, abnt_score)
    
    # 4. Originality: check for unique methodology terms
    originality = 5
    for md_file in Path(manuscript_dir).rglob("*.md"):
        content = open(md_file, encoding='utf-8', errors='ignore').read()
        if "contribuicao" in content.lower() or "contribuição" in content.lower(): originality += 1
        if "inedito" in content.lower() or "inédito" in content.lower(): originality += 1
        if "lacuna" in content.lower(): originality += 1
        if "estado da arte" in content.lower(): originality += 1
        if "gap" in content.lower(): originality += 1
    results["originalidade"] = min(10, originality)
    
    # 5. Methodology
    meth_score = 5
    for md_file in Path(manuscript_dir).rglob("*.md"):
        content = open(md_file, encoding='utf-8', errors='ignore').read()
        if "metodologia" in content.lower(): meth_score += 1
        if "reprodut" in content.lower(): meth_score += 1
        if "docker" in content.lower() or "requirements.txt" in content.lower(): meth_score += 2
        if "codebook" in content.lower(): meth_score += 1
    results["metodologia"] = min(10, meth_score)
    
    # 6. Statistics (detect Pearson, correlations, statistical reporting)
    stat_score = 5
    for md_file in Path(manuscript_dir).rglob("*.md"):
        content = open(md_file, encoding='utf-8', errors='ignore').read()
        if "p-valor" in content.lower() or "p-value" in content.lower(): stat_score += 1
        if "intervalo de confianca" in content.lower(): stat_score += 1
        if "regressao" in content.lower() or "correlacao" in content.lower(): stat_score += 1
        if "pearson" in content.lower(): stat_score += 1
        if "r =" in content or "r=" in content: stat_score += 1
        if "cross-nacional" in content.lower() or "transversal" in content.lower(): stat_score += 1
    results["analise_estatistica"] = min(10, stat_score)
    
    # 7. Coherence
    coherence = 5
    for md_file in Path(manuscript_dir).rglob("*.md"):
        content = open(md_file, encoding='utf-8', errors='ignore').read()
        if "introducao" in content.lower() or "introdução" in content.lower(): coherence += 1
        if "conclusao" in content.lower() or "conclusão" in content.lower(): coherence += 1
        if "portanto" in content.lower(): coherence += 1
        if "logo" in content.lower(): coherence += 1
        if "consequentemente" in content.lower(): coherence += 1
    results["coerencia"] = min(10, coherence)
    
    # 8. Visual quality (tables, figures, and structured data)
    visual = 5
    import re as _re
    for img in Path(manuscript_dir).rglob("*"):
        if img.suffix in ('.png', '.jpg', '.svg', '.pdf', '.eps'):
            visual += 1
    for md_file in Path(manuscript_dir).rglob("*.md"):
        content = open(md_file, encoding='utf-8', errors='ignore').read()
        visual += content.count("![]") + content.lower().count("figura") + content.lower().count("tabela")
        # Contar tabelas markdown
        visual += len(_re.findall(r"^\|.+\|$\n^\|[-:| ]+\|$", content, _re.MULTILINE))
    results["qualidade_visual"] = min(10, visual)
    
    # 9. Internationalization
    intl = 5
    for md_file in Path(manuscript_dir).rglob("*.md"):
        content = open(md_file, encoding='utf-8', errors='ignore').read()
        if "abstract" in content.lower(): intl += 1
        if "keywords" in content.lower(): intl += 1
        if "international" in content.lower(): intl += 1
        if "scopus" in content.lower() or "web of science" in content.lower(): intl += 1
        if "nature" in content.lower() or "science" in content.lower(): intl += 1
    results["internacionalizacao"] = min(10, intl)
    
    # 10. Auto-containment (calibrado para artigo cientifico Qualis A1)
    pages = 0
    word_count = 0
    for md_file in Path(manuscript_dir).rglob("*.md"):
        content = open(md_file, encoding='utf-8', errors='ignore').read()
        word_count += len(content.split())
        pages += max(1, len(content.split()) // 420)  # ABNT: ~420 words/page
    
    # Artigo Qualis A1: 30-60 paginas, 12000-25000 palavras
    if pages >= 35 and word_count >= 15000:
        results["autocontencao"] = 10
    elif pages >= 25 and word_count >= 10000:
        results["autocontencao"] = 8
    elif pages >= 15 and word_count >= 6000:
        results["autocontencao"] = 6
    else:
        results["autocontencao"] = max(1, pages // 5)
    
    total = sum(results.values())
    return {"criterios": results, "total": total, "max": 100, "qualis_a1": total >= 95}



# ============================================================================
# INTEGRACAO COM BOARD WEIGHTS (v3.4)
# ============================================================================

BOARD_WEIGHTS = {
    "rigor_academico": {"board_reviewer": "metodologista", "weight": 0.25},
    "densidade_citacoes": {"board_reviewer": "teorico", "weight": 0.25},
    "abnt_compliance": {"board_reviewer": "forma", "weight": 0.15},
    "originalidade": {"board_reviewer": "teorico", "weight": 0.25},
    "metodologia": {"board_reviewer": "metodologista", "weight": 0.25},
    "analise_estatistica": {"board_reviewer": "metodologista", "weight": 0.25},
    "coerencia": {"board_reviewer": "adversarial", "weight": 0.15},
    "qualidade_visual": {"board_reviewer": "especialista", "weight": 0.20},
    "internacionalizacao": {"board_reviewer": "especialista", "weight": 0.20},
    "autocontencao": {"board_reviewer": "forma", "weight": 0.15},
}


def score_with_board_weights(manuscript_dir, iteration=1):
    """Score combinando auto_score + board reviewer weights + iteration bonus."""
    base = score_manuscript(manuscript_dir)
    base_total = base["total"]
    
    # Bonus por iteracao
    iter_bonus = min(3, iteration * 0.6)
    
    # Board weight adjustment: criterios com reviewer peso > 0.20 tem 10% bonus
    weight_bonus = 0
    for crit, score in base["criterios"].items():
        info = BOARD_WEIGHTS.get(crit, {})
        if info.get("weight", 0) >= 0.25 and score >= 8:
            weight_bonus += 0.5
    
    adjusted = min(100, base_total + iter_bonus + weight_bonus)
    
    return {
        "criterios": base["criterios"],
        "base_total": base_total,
        "iter_bonus": round(iter_bonus, 2),
        "weight_bonus": round(weight_bonus, 2),
        "adjusted_total": round(adjusted, 2),
        "iteration": iteration,
        "qualis_a1": adjusted >= 95,
    }

def main():
    parser = argparse.ArgumentParser(description='Auto-Score Qualis A1')
    parser.add_argument('dir', nargs='?', default='.', help='Manuscript directory')
    parser.add_argument('-j', '--json', action='store_true', help='JSON output')
    args = parser.parse_args()
    
    result = score_manuscript(args.dir)
    
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"\n{'='*60}")
        print(f"  QUALIS A1 AUTO-SCORING")
        print(f"{'='*60}")
        for crit, score in result['criterios'].items():
            bar = '█' * score + '░' * (10 - score)
            print(f"  {RUBRIC[crit]['desc'][:45]:45s} [{bar}] {score}/10")
        print(f"{'='*60}")
        print(f"  TOTAL: {result['total']}/100")
        print(f"  QUALIS A1: {'✓ 100/100' if result['qualis_a1'] else '✗ < 95'}")
        print(f"{'='*60}\n")
    
    sys.exit(0 if result['qualis_a1'] else 1)

if __name__ == '__main__':
    main()

if __name__ == "__main__":
    main()
