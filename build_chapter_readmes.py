#!/usr/bin/env python3
"""
build_chapter_readmes.py
Creates Part README.md files, Chapter README.md files, and mkdocs.yml nav.
"""
import os
from pathlib import Path

BOOK = Path("git_1.0_excitations_and_expressions_of_emergence/book")

PART_MAP = {
    1: ("I",   "Foundations of Emergence",                   [1, 2, 3]),
    4: ("II",  "Persistence Mechanics",                      [4, 5, 6]),
    7: ("III", "The CTS Survival Map and Excitation Library", [7, 8, 9, 10, 11]),
    12: ("IV", "Matter, Shells, and Stability",              [12, 13, 14, 15]),
    16: ("V",  "Implications for Physics",                   [16, 17, 18, 19]),
}

CHAPTER_TITLES = {
    1:  "The Problem of Emergence",
    2:  "The Collapse Tension Substrate",
    3:  "Dimensional Emergence as Constraint Acquisition",
    4:  "Retention, Loss, and the Selection Number",
    5:  "Eligibility, Drift, and Stability Gates",
    6:  "Topology and Objecthood",
    7:  "The CTS Energy Functional",
    8:  "The CTS Excitation Ledger",
    9:  "Derived Quantities for the Ledger",
    10: "The Threshold Phase Chart",
    11: "The Named CTS Survival Map",
    12: "From Expressions to Durable Structures",
    13: "Shells as Persistence Solutions",
    14: "Stability Bands and Survival Landscapes",
    15: "Composite Structures and Braided Persistence",
    16: "Emergent Geometry",
    17: "Emergent Time and Entropy",
    18: "Light, Propagation, and the Cheapest Expressions",
    19: "Comparison with Existing Theories",
}

CHAPTER_SUMMARIES = {
    1:  "Establishes the central problem: why does structure *persist*? Derives the selection number $S = R/(\\dot{R}\\,t_{ref})$ and the persistence condition $S \\geq 1$.",
    2:  "Introduces the Collapse Tension Substrate (CTS) — a pre-geometric scalar field whose internal competition between collapse and tension determines which structures can survive.",
    3:  "Derives the dimensional ladder of emergence: from 0D scalar variation through 1D gradient bias, 2D circulation, to 3D curvature closure and boundary formation.",
    4:  "Formalises the three foundational quantities: retained structure $R$, loss rate $\\dot{R}$, and the persistence horizon $t_{ref}$. Derives the selection number rigorously.",
    5:  "Introduces eligibility $\\chi$, drift stability $D$, and the corrected persistence condition $\\chi D S \\geq 1$. Analyses failure modes.",
    6:  "Shows how closure, chirality, and composite order constitute topological protection. Derives the topology factor $T_{obj}$ and the objecthood threshold.",
    7:  "Constructs the CTS energy functional $E[\\Phi, \\mathbf{A}]$ from first principles. Analyses vacuum structure, bifurcation, and correlation length.",
    8:  "Catalogs all excitation classes: wave modes, phase-locked modes, vortices, rings, chiral primitives, shells, and braids.",
    9:  "Derives the full excitation ledger quantities: $E_{form}$, $E_{lock}$, $E_{total}$, the lock ratio $\\Lambda_{lock}$, and the abundance law.",
    10: "Introduces the threshold phase chart with axes $\\Lambda_{lock}$ and $\\mathcal{R}_{eff}$. Defines the survival curve $y = 1/x$.",
    11: "Names and interprets all regions of the CTS survival map as an atlas of emergence.",
    12: "Distinguishes excitations that remain background modes from those that become durable structures. Analyses closure vs. shell-lock.",
    13: "Treats shells as multi-fan lock events. Derives curvature-as-closure-memory and nested shell architectures.",
    14: "Reads the Semi-Empirical Mass Formula as a CTS survival equation. Interprets the valley of stability and drip lines as persistence landscapes.",
    15: "Analyses pair and triple-braid composite structures. Derives composite thresholds and conditions for favoured composite survival.",
    16: "Proposes that geometry emerges from stabilised relational separation. Explores how closure and curvature give rise to proto-geometry.",
    17: "Derives time as ordered loss, entropy as coherence degradation, and the second law in CTS language.",
    18: "Shows wave modes are the least burdened expressions. Formalises why propagation must precede closure.",
    19: "Compares CTS against thermodynamics, Landau–Ginzburg models, decoherence, nuclear stability, and complex systems theory.",
}

CHAPTER_TO_PART = {}
for start, (num, title, chs) in PART_MAP.items():
    for ch in chs:
        CHAPTER_TO_PART[ch] = (num, title)

APPENDIX_TITLES = {
    "A": "Derivation of the Selection Number",
    "B": "Derivation of the Corrected Threshold",
    "C": "Derivation of the CTS Energy Functional",
    "D": "Vortex, Ring, Shell, and Braid Energy Estimates",
    "E": "The CTS Excitation Ledger",
    "F": "Threshold Phase Chart and Survival Map",
    "G": "Notation, Symbols, and Conventions",
    "H": "Glossary of CTS Terms",
}

def slugify(s):
    import re
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")[:60]

def part_dir(num):
    titles = {
        "I":   "foundations_of_emergence",
        "II":  "persistence_mechanics",
        "III": "the_cts_survival_map_and_excitation_library",
        "IV":  "matter_shells_and_stability",
        "V":   "implications_for_physics",
    }
    return f"part_{num.lower()}_{titles[num]}"

def chapter_dir(ch):
    return f"chapter_{ch:02d}_{slugify(CHAPTER_TITLES[ch])}"

# ── Write Part READMEs ─────────────────────────────────────────────────────────
for start, (num, title, chs) in PART_MAP.items():
    pd = BOOK / part_dir(num)
    pd.mkdir(parents=True, exist_ok=True)
    ch_list = "\n".join(
        f"- [Chapter {ch}: {CHAPTER_TITLES[ch]}]({chapter_dir(ch)}/README.md)"
        for ch in chs
    )
    content = f"""\
# Part {num}: {title}

{ch_list}
"""
    (pd / "README.md").write_text(content, encoding="utf-8")
    print(f"wrote {pd.relative_to(BOOK.parent.parent)}/README.md")

# ── Write Chapter READMEs ─────────────────────────────────────────────────────
for ch in range(1, 20):
    p_num, p_title = CHAPTER_TO_PART[ch]
    pd = BOOK / part_dir(p_num) / chapter_dir(ch)
    pd.mkdir(parents=True, exist_ok=True)

    # List sections that exist
    sections = sorted(pd.glob("*.*/README.md"))
    sec_links = ""
    for s in sections:
        sec_name = s.parent.name  # e.g. "1.1_why_origin_stories..."
        parts = sec_name.split("_", 1)
        num_str = parts[0]
        label = parts[1].replace("_", " ").title() if len(parts) > 1 else sec_name
        sec_links += f"- [{num_str.upper()} {label}]({sec_name}/README.md)\n"

    summary = CHAPTER_SUMMARIES.get(ch, "")
    content = f"""\
# Chapter {ch}: {CHAPTER_TITLES[ch]}

> {summary}

## Sections

{sec_links}
"""
    (pd / "README.md").write_text(content, encoding="utf-8")
    print(f"wrote {pd.relative_to(BOOK.parent.parent)}/README.md")

# ── Appendices placeholder if missing ─────────────────────────────────────────
app_dir = BOOK / "appendices"
app_dir.mkdir(parents=True, exist_ok=True)
for letter, title in APPENDIX_TITLES.items():
    p = app_dir / f"appendix_{letter.lower()}.md"
    if not p.exists():
        p.write_text(f"# Appendix {letter}: {title}\n\n*Content to be added.*\n", encoding="utf-8")

# ── Build MkDocs nav ─────────────────────────────────────────────────────────
nav_lines = [
    "nav:",
    "  - Home: index.md",
    "  - Preface: 00_preface/README.md",
]

for start, (num, title, chs) in PART_MAP.items():
    nav_lines.append(f"  - 'Part {num}: {title}':")
    nav_lines.append(f"    - Overview: {part_dir(num)}/README.md")
    for ch in chs:
        nav_lines.append(f"    - 'Ch {ch}: {CHAPTER_TITLES[ch]}':")
        nav_lines.append(f"      - Overview: {part_dir(num)}/{chapter_dir(ch)}/README.md")
        # Find sections
        ch_path = BOOK / part_dir(num) / chapter_dir(ch)
        for sec_dir in sorted(ch_path.iterdir()):
            if sec_dir.is_dir() and (sec_dir / "README.md").exists():
                sec_name = sec_dir.name
                parts = sec_name.split("_", 1)
                label = parts[1].replace("_", " ").title() if len(parts) > 1 else sec_name
                rel = f"{part_dir(num)}/{chapter_dir(ch)}/{sec_name}/README.md"
                nav_lines.append(f"      - '{parts[0]} {label}': {rel}")

nav_lines.append("  - Conclusion: conclusion/README.md")
nav_lines.append("  - Appendices:")
for letter, title in APPENDIX_TITLES.items():
    nav_lines.append(f"    - 'Appendix {letter}: {title}': appendices/appendix_{letter.lower()}.md")

print("\n".join(nav_lines[:10]), "...")
nav_text = "\n".join(nav_lines)

# Write nav to a file for inclusion in mkdocs.yml
(BOOK / "_nav.yml").write_text(nav_text, encoding="utf-8")
print(f"\nNav written ({len(nav_lines)} entries)")
