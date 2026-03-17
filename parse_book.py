#!/usr/bin/env python3
"""
parse_book.py

Reads excitations_and_expressions_of_emergence.md and splits it into a
fully-organized folder/file structure under git_1.0.../book/.

Handles three equation formats found in the document:
  Format 1 (Ch 1, 6-7): unicode+\LaTeX+unicode on one line → extract LaTeX
  Format 2 (Ch 2-9):    [ ... LaTeX ... ] blocks            → $$ ... $$
  Format 3 (Ch 14-19):  multi-line unicode split             → keep compact line
"""

import re
import os
from pathlib import Path

SRC = Path("git_1.0_excitations_and_expressions_of_emergence/excitations_and_expressions_of_emergence.md")
BOOK = Path("git_1.0_excitations_and_expressions_of_emergence/book")

ZWSP = "\u200b"

# ── Book metadata ──────────────────────────────────────────────────────────────
PART_MAP = {
    1: ("I",   "Foundations of Emergence"),
    2: ("I",   "Foundations of Emergence"),
    3: ("I",   "Foundations of Emergence"),
    4: ("II",  "Persistence Mechanics"),
    5: ("II",  "Persistence Mechanics"),
    6: ("II",  "Persistence Mechanics"),
    7: ("III", "The CTS Survival Map and Excitation Library"),
    8: ("III", "The CTS Survival Map and Excitation Library"),
    9: ("III", "The CTS Survival Map and Excitation Library"),
    10: ("III","The CTS Survival Map and Excitation Library"),
    11: ("III","The CTS Survival Map and Excitation Library"),
    12: ("IV", "Matter, Shells, and Stability"),
    13: ("IV", "Matter, Shells, and Stability"),
    14: ("IV", "Matter, Shells, and Stability"),
    15: ("IV", "Matter, Shells, and Stability"),
    16: ("V",  "Implications for Physics"),
    17: ("V",  "Implications for Physics"),
    18: ("V",  "Implications for Physics"),
    19: ("V",  "Implications for Physics"),
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

# ── Slug helpers ───────────────────────────────────────────────────────────────
def slugify(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")[:60]

def chapter_dir(ch):
    return f"chapter_{ch:02d}_{slugify(CHAPTER_TITLES[ch])}"

def part_dir(ch):
    num, title = PART_MAP[ch]
    return f"part_{num.lower()}_{slugify(title)}"

# ── Equation cleaning ──────────────────────────────────────────────────────────

def clean_format2_blocks(lines):
    """Convert [ ... LaTeX ... ] blocks to $$ ... $$ display math."""
    result = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped == "[":
            # collect until matching lone ]
            inner = []
            i += 1
            depth = 1
            while i < len(lines):
                s = lines[i].strip()
                if s == "[":
                    depth += 1
                    inner.append(lines[i])
                elif s == "]":
                    depth -= 1
                    if depth == 0:
                        break
                    inner.append(lines[i])
                else:
                    inner.append(lines[i])
                i += 1
            body = "\n".join(l.rstrip() for l in inner).strip()
            if body:
                result.append("$$")
                for body_line in body.splitlines():
                    result.append(body_line)
                result.append("$$")
            # i now points at ], advance past it
        else:
            result.append(lines[i])
        i += 1
    return result


def strip_unicode_suffix(s):
    """
    Remove trailing unicode rendering from a Format-1 LaTeX string.
    The unicode suffix usually contains ZWSP (U+200B); when not, we detect
    the transition from LaTeX (ASCII) back to non-ASCII unicode.
    """
    # Method 1: ZWSP marker
    pos = s.find(ZWSP)
    if pos > 0:
        end = pos
        while end > 0 and s[end - 1] in " \t":
            end -= 1
        return s[:end].rstrip()

    # Method 2: find first non-ASCII char that occurs AFTER a LaTeX command
    # and is outside all braces (i.e. the unicode suffix starts here).
    brace_depth = 0
    for i, c in enumerate(s):
        if c == '{':
            brace_depth += 1
        elif c == '}':
            brace_depth -= 1
        elif brace_depth == 0 and ord(c) > 127:
            # non-ASCII outside braces after the LaTeX = suffix
            if i > 0:
                return s[:i].rstrip()
            break
    return s.rstrip()


def _looks_like_math_prefix(prefix):
    """
    Return True if prefix is a unicode math rendering (not English prose).
    Heuristics: no spaces, or contains math arrows/operators.
    """
    if not prefix:
        return True
    MATH_CHARS = "→←↔⇒⇐⟹⟺≥≤≠≈∞∈∉⊆⊂⊃∪∩∀∃∂∇∑∏∫±×÷·"
    if any(c in MATH_CHARS for c in prefix):
        return True
    if " " not in prefix.strip():
        # no spaces → probably a compact math expression like "S=RR˙tref"
        return True
    return False


def extract_latex_from_triple(line):
    """
    Format-1: A single line containing unicode + \\LaTeX + unicode.
    Returns cleaned line with LaTeX wrapped in $$ or $.
    """
    if "\\" not in line:
        return line
    m = re.search(r"\\[a-zA-Z{]", line)
    if not m:
        return line

    prefix = line[: m.start()].rstrip()
    latex_raw = line[m.start():]
    latex_clean = strip_unicode_suffix(latex_raw)

    # Decide display vs inline
    if _looks_like_math_prefix(prefix):
        # Full display equation — strip the unicode prefix, keep only LaTeX
        # But recover any simple ASCII operators before the backslash (e.g. "S=")
        ascii_prefix = re.sub(r"[^\x20-\x7e]", "", prefix).strip()
        full_latex = (ascii_prefix + latex_clean).strip() if ascii_prefix else latex_clean
        return f"$$\n{full_latex}\n$$"
    else:
        # Prose line with inline math at end
        return f"{prefix} ${latex_clean}$"


def _is_prose(line):
    """True if a line is clearly ordinary English prose."""
    s = line.strip()
    if not s or len(s) < 10:
        return False
    words = s.split()
    alpha_words = sum(1 for w in words if w.isalpha() and len(w) > 1)
    return alpha_words >= 3 and len(words) >= 4


def is_split_line(line):
    """True if a line looks like a Format-3 split fragment."""
    s = line.strip()
    if ZWSP in line:
        return True
    if not s:
        return False
    if _is_prose(line):
        return False
    # Short lines (≤8 chars) are almost always split fragments
    if len(s) <= 8:
        return True
    # Lines with substantial non-ASCII (subscript/superscript chars)
    if sum(ord(c) > 127 for c in s) / len(s) > 0.35:
        return True
    return False


def collapse_format3_splits(lines):
    """
    Format-3: a compact unicode equation line followed by individual
    letter/subscript/ZWSP lines repeating it.  Keep the compact line, skip splits.
    Strategy: if a line is followed by a ZWSP line in the next 20 lines,
    collapse all following split fragments.
    """
    # Pre-scan: find positions of ZWSP lines
    zwsp_positions = set(
        i for i, l in enumerate(lines) if ZWSP in l
    )

    result = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip lines inside $$ blocks
        if line.strip() == "$$":
            result.append(line)
            i += 1
            continue

        # Check if a ZWSP line follows within 20 lines (Format-3 indicator)
        near_zwsp = any(j in zwsp_positions for j in range(i + 1, min(i + 20, len(lines))))

        if near_zwsp and not _is_prose(line) and line.strip():
            # Emit the compact first line
            result.append(line)
            i += 1
            # Skip split fragments
            while i < len(lines) and is_split_line(lines[i]):
                i += 1
        else:
            result.append(line)
            i += 1
    return result


def clean_inline_latex(line):
    """
    Convert (\\LaTeX) inline patterns (from Format-2 inline usage) to $LaTeX$.
    e.g. (\Lambda_{lock}) → $\Lambda_{lock}$
    """
    return re.sub(r"\((\s*\\[^)]+)\)", lambda m: f"${m.group(1).strip()}$", line)


def process_lines(raw_lines):
    """Full equation-cleaning pipeline for a block of lines."""
    lines = list(raw_lines)

    # Pass 1: Format-2 block equations
    lines = clean_format2_blocks(lines)

    # Pass 2: Format-3 multiline unicode splits
    lines = collapse_format3_splits(lines)

    # Pass 3: Format-1 triple-format lines + inline (\\LaTeX) patterns
    # Skip lines already inside $$ ... $$ blocks (produced by Format-2 pass)
    result = []
    in_display_block = False
    for line in lines:
        if line.strip() == "$$":
            in_display_block = not in_display_block
            result.append(line)
            continue
        if not in_display_block:
            if re.search(r"\\[a-zA-Z{]", line) and ZWSP not in line:
                line = extract_latex_from_triple(line)
            line = clean_inline_latex(line)
        result.append(line)

    return result


# ── Parsing ────────────────────────────────────────────────────────────────────

CHAPTER_RE  = re.compile(r"^Chapter\s+(\d+)(?:\s*[—\-]+\s*(.+))?$")
SECTION_RE  = re.compile(r"^(\d+)\.(\d+)\s+(.+)$")
SUBSECT_RE  = re.compile(r"^(\d+)\.(\d+)\.(\d+)\s+(.+)$")
APPENDIX_RE = re.compile(r"^Appendix\s+([A-H])[.\s]+(.+)$")
CONCL_RE    = re.compile(r"^Conclusion\s*$")
PREFACE_RE  = re.compile(r"^Preface\s*$")

def is_toc_noise(line):
    """Skip navigation noise lines inserted by the exporter."""
    s = line.strip()
    return s in ("next", "Continuing strictly by the tracker.") or \
           re.match(r"^\(\d+\.\d+ of \d+\.\d+ — Chapter \d+ of \d+\)$", s) or \
           re.match(r"^Next Section$", s)


def parse(src_path):
    """
    Return list of section dicts:
      { type, chapter, section, subsection, title, letter, lines[] }
    """
    all_lines = src_path.read_text(encoding="utf-8").splitlines()

    sections = []

    # Find preface start (skip TOC)
    preface_idx = 0
    for idx, line in enumerate(all_lines):
        if PREFACE_RE.match(line.strip()) and idx > 50:
            preface_idx = idx
            break

    # ── helper ──
    def push(sec):
        if sec and sec["lines"]:
            sections.append(sec)

    current = {"type": "preface", "chapter": 0, "section": 0,
                "subsection": 0, "title": "Preface",
                "letter": "", "lines": []}

    i = preface_idx
    prev_was_chapter = False

    while i < len(all_lines):
        line = all_lines[i]
        raw  = line.strip()

        # skip noise
        if is_toc_noise(raw):
            i += 1
            continue

        # ── Appendix ──
        m = APPENDIX_RE.match(raw)
        if m:
            push(current)
            current = {"type": "appendix", "chapter": 0, "section": 0,
                       "subsection": 0, "title": m.group(2).strip(),
                       "letter": m.group(1), "lines": [f"# Appendix {m.group(1)}: {m.group(2).strip()}"]}
            i += 1
            prev_was_chapter = False
            continue

        # ── Conclusion ──
        if CONCL_RE.match(raw):
            push(current)
            current = {"type": "conclusion", "chapter": 0, "section": 0,
                       "subsection": 0, "title": "Conclusion",
                       "letter": "", "lines": ["# Conclusion"]}
            i += 1
            prev_was_chapter = False
            continue

        # ── Chapter header ──
        m = CHAPTER_RE.match(raw)
        if m:
            prev_was_chapter = True
            i += 1
            continue

        # ── Section header  (N.M Title) ──
        m = SECTION_RE.match(raw)
        if m:
            ch, sec, title = int(m.group(1)), int(m.group(2)), m.group(3).strip()
            # Ignore TOC lines (lines 1-192)
            if i < preface_idx:
                i += 1
                continue
            push(current)
            current = {"type": "section", "chapter": ch, "section": sec,
                       "subsection": 0, "title": title,
                       "letter": "",
                       "lines": [f"# {ch}.{sec} {title}"]}
            i += 1
            prev_was_chapter = False
            continue

        # ── Subsection header (N.M.K Title) ──
        m = SUBSECT_RE.match(raw)
        if m:
            ch, sec, sub, title = (int(m.group(1)), int(m.group(2)),
                                   int(m.group(3)), m.group(4).strip())
            if i < preface_idx:
                i += 1
                continue
            # subsections fold INTO the parent section file (as ## headers)
            if current and current["type"] == "section":
                current["lines"].append(f"\n## {ch}.{sec}.{sub} {title}\n")
            else:
                current["lines"].append(f"\n## {ch}.{sec}.{sub} {title}\n")
            i += 1
            prev_was_chapter = False
            continue

        # ── Regular content ──
        if current is not None:
            current["lines"].append(line)
        i += 1

    push(current)
    return sections


# ── Writing ────────────────────────────────────────────────────────────────────

def section_folder(sec):
    """Return relative path within book/ for a section dict."""
    t = sec["type"]
    if t == "preface":
        return Path("00_preface")
    if t == "conclusion":
        return Path("conclusion")
    if t == "appendix":
        return Path("appendices")
    if t == "section":
        ch  = sec["chapter"]
        s   = sec["section"]
        if ch not in PART_MAP:
            return Path("misc")
        return Path(part_dir(ch)) / chapter_dir(ch) / f"{ch}.{s}_{slugify(sec['title'])}"
    return Path("misc")


def write_section(sec, book_root):
    folder = book_root / section_folder(sec)
    folder.mkdir(parents=True, exist_ok=True)

    cleaned = process_lines(sec["lines"])
    content = "\n".join(cleaned)

    # Remove excessive blank lines (3+ → 2)
    content = re.sub(r"\n{3,}", "\n\n", content)

    if sec["type"] == "appendix":
        fname = f"appendix_{sec['letter'].lower()}.md"
        out = book_root / "appendices" / fname
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
    else:
        out = folder / "README.md"
        out.write_text(content, encoding="utf-8")

    return out


# ── MkDocs nav builder ─────────────────────────────────────────────────────────

def build_nav(sections):
    """Build the nav list for mkdocs.yml."""
    nav = ["- Home: index.md"]
    nav.append("- Preface: 00_preface/README.md")

    current_part = None
    current_ch   = None
    part_entries = {}   # part_dir -> list of chapter entries
    ch_entries   = {}   # (part_dir, ch_dir) -> list of section entries

    for sec in sections:
        if sec["type"] not in ("section",):
            continue
        ch = sec["chapter"]
        pd = part_dir(ch)
        cd = chapter_dir(ch)
        s  = sec["section"]
        path = f"{pd}/{cd}/{ch}.{s}_{slugify(sec['title'])}/README.md"
        entry = f"  - '{ch}.{s} {sec['title']}': {path}"
        key = (pd, cd)
        ch_entries.setdefault(key, []).append(entry)
        part_entries.setdefault(pd, set()).add(cd)

    # Emit parts in order
    seen_parts = []
    seen_chs   = []
    part_num, _ = PART_MAP[1]

    for ch in range(1, 20):
        pd = part_dir(ch)
        cd = chapter_dir(ch)
        p_num, p_title = PART_MAP[ch]

        if pd not in seen_parts:
            seen_parts.append(pd)
            nav.append(f"- 'Part {p_num}: {p_title}':")

        if (pd, cd) not in seen_chs:
            seen_chs.append((pd, cd))
            nav.append(f"  - 'Chapter {ch}: {CHAPTER_TITLES[ch]}':")

        key = (pd, cd)
        for entry in ch_entries.get(key, []):
            nav.append("  " + entry)

    nav.append("- Conclusion: conclusion/README.md")
    nav.append("- Appendices:")
    for letter, title in APPENDIX_TITLES.items():
        nav.append(f"  - 'Appendix {letter}: {title}': appendices/appendix_{letter.lower()}.md")

    return "\n".join(nav)


# ── Index file ─────────────────────────────────────────────────────────────────

INDEX_MD = """\
---
title: Astrosynthesis — Excitations and Expressions of Emergence
---

# Astrosynthesis
## Excitations and Expressions of Emergence

> *The enduring structures of the universe are not merely those that can appear,
> but those that can survive.*

---

This is the full text of **Astrosynthesis**, organized as a navigable book.
Each Part → Chapter → Section is its own folder; use the sidebar to navigate.

## Table of Contents

| Part | Chapters | Theme |
|------|----------|-------|
| I   | 1–3  | Foundations of Emergence |
| II  | 4–6  | Persistence Mechanics |
| III | 7–11 | CTS Survival Map and Excitation Library |
| IV  | 12–15| Matter, Shells, and Stability |
| V   | 16–19| Implications for Physics |

---

[Start reading → Preface](00_preface/README.md)
"""

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print(f"Reading {SRC} ...")
    sections = parse(SRC)
    print(f"  Found {len(sections)} sections")

    BOOK.mkdir(parents=True, exist_ok=True)

    written = []
    for sec in sections:
        out = write_section(sec, BOOK)
        print(f"  wrote {out.relative_to(BOOK.parent.parent)}")
        written.append(out)

    # index.md
    (BOOK / "index.md").write_text(INDEX_MD, encoding="utf-8")
    print(f"  wrote book/index.md")

    print(f"\nDone. {len(written)} files written to {BOOK}")


if __name__ == "__main__":
    main()
