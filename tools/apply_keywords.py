#!/usr/bin/env python3
"""Apply the controlled keyword vocabulary (keyword_map.json) to every entry.

For each entry ``NN-topic/*.md`` (``README.md`` excluded) this rewrites

* the YAML front-matter ``keywords:`` list, and
* the line under ``## Keywords`` (`` `a` · `b` · ... ``),

replacing every variant keyword by its canonical form and dropping duplicates
created by the mapping (first occurrence wins, order preserved).  Nothing else
in the file is touched: only those two lines (or, for a block-style YAML list,
the list item lines) change, and line endings are preserved byte-for-byte.

Usage::

    python3 apply_keywords.py /path/to/aobib --dry-run          # summary only
    python3 apply_keywords.py /path/to/aobib --dry-run -v       # + per-file diff
    python3 apply_keywords.py /path/to/aobib                    # rewrite files
    python3 apply_keywords.py /path/to/aobib --map other.json

Afterwards run ``python3 tools/build_index.py`` to regenerate KEYWORDS.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

TOPIC_RE = re.compile(r"^\d\d-[a-z0-9-]+$")
SEP = " · "
BLOCK_ITEM_RE = re.compile(r"^(\s*-\s+)(.*?)(\s*)$")


def entries(root: Path) -> list[Path]:
    out = []
    for t in sorted(p for p in root.iterdir() if p.is_dir() and TOPIC_RE.match(p.name)):
        out += [f for f in sorted(t.glob("*.md")) if f.name != "README.md"]
    return out


def remap(kws: list[str], kmap: dict[str, str]) -> list[str]:
    seen, out = set(), []
    for k in kws:
        c = kmap.get(k, k)
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out


def eol_split(line: str) -> tuple[str, str]:
    """Split a line (as returned by splitlines(keepends=True)) into body and EOL."""
    body = line.rstrip("\r\n")
    return body, line[len(body):]


def scalar(s: str) -> str:
    v = yaml.safe_load(s)
    return "" if v is None else str(v)


class EntryError(Exception):
    pass


def process(text: str, kmap: dict[str, str]) -> tuple[str, list[str], list[str], list[str]]:
    """Return (new_text, old_yaml_keywords, new_yaml_keywords, warnings)."""
    warnings: list[str] = []
    lines = text.splitlines(keepends=True)
    if not lines or eol_split(lines[0])[0].strip() != "---":
        raise EntryError("no YAML front matter")
    end = next((i for i in range(1, len(lines)) if eol_split(lines[i])[0].strip() == "---"), None)
    if end is None:
        raise EntryError("unterminated front matter")

    # --- YAML keywords
    kidx = [i for i in range(1, end) if re.match(r"^keywords\s*:", lines[i])]
    if len(kidx) != 1:
        raise EntryError(f"expected one 'keywords:' line in front matter, found {len(kidx)}")
    ki = kidx[0]
    body, eol = eol_split(lines[ki])
    rest = body.split(":", 1)[1].strip()
    if rest:  # flow style: keywords: ["a", "b"]  or  [a, b]
        try:
            old = json.loads(rest)
        except json.JSONDecodeError:
            old = yaml.safe_load(rest)
        if not isinstance(old, list):
            raise EntryError("keywords is not a list")
        old = [str(k) for k in old]
        new = remap(old, kmap)
        if new != old:  # always emitted as a JSON flow list (valid YAML), as in TEMPLATE.md
            lines[ki] = "keywords: " + json.dumps(new, ensure_ascii=False) + eol
    else:  # block style: keywords:\n  - a\n  - b
        j = ki + 1
        items = []  # (line index, prefix, raw value, trailing ws, eol)
        while j < end:
            b, e = eol_split(lines[j])
            m = BLOCK_ITEM_RE.match(b)
            if not m:
                break
            items.append((j, m.group(1), m.group(2), m.group(3), e))
            j += 1
        old = [scalar(it[2]) for it in items]
        new = remap(old, kmap)
        if new != old:
            prefix, eol0 = items[0][1], items[0][4]
            raw0 = items[0][2]
            quote = raw0[0] if raw0[:1] in ("'", '"') else ""
            def fmt(k: str) -> str:
                if quote == '"':
                    return json.dumps(k, ensure_ascii=False)
                if quote == "'":
                    return "'" + k.replace("'", "''") + "'"
                return k if yaml.safe_load(k) == k else json.dumps(k, ensure_ascii=False)
            repl = [prefix + fmt(k) + eol0 for k in new]
            lines[items[0][0]: items[-1][0] + 1] = repl
            end += len(repl) - len(items)

    # --- "## Keywords" body line
    hidx = [i for i in range(end + 1, len(lines)) if eol_split(lines[i])[0].strip() == "## Keywords"]
    if len(hidx) != 1:
        warnings.append(f"expected one '## Keywords' heading, found {len(hidx)}; body not changed")
    else:
        j = hidx[0] + 1
        while j < len(lines) and not eol_split(lines[j])[0].strip():
            j += 1
        if j >= len(lines):
            warnings.append("no keyword line under '## Keywords'; body not changed")
        else:
            b, e = eol_split(lines[j])
            lead = b[: len(b) - len(b.lstrip())]
            parts = [p.strip() for p in b.strip().split("·")]
            if not all(len(p) >= 2 and p.startswith("`") and p.endswith("`") for p in parts):
                warnings.append(f"unrecognised keyword line {b.strip()[:60]!r}; body not changed")
            else:
                bkw = [p[1:-1] for p in parts]
                if bkw != old:
                    warnings.append("'## Keywords' line did not match YAML list; mapped it independently")
                nb = remap(bkw, kmap)
                if nb != bkw:
                    lines[j] = lead + SEP.join(f"`{k}`" for k in nb) + e
    return "".join(lines), old, new, warnings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repo", type=Path, help="path to the registry checkout")
    ap.add_argument("--map", type=Path, default=Path(__file__).with_name("keyword_map.json"))
    ap.add_argument("--dry-run", action="store_true", help="report what would change, write nothing")
    ap.add_argument("-v", "--verbose", action="store_true", help="list each changed file")
    args = ap.parse_args()

    kmap: dict[str, str] = json.loads(args.map.read_text(encoding="utf-8"))
    chains = {v: c for v, c in kmap.items() if c in kmap}
    if chains:
        print(f"error: map has chained entries: {chains}", file=sys.stderr)
        return 2

    root = args.repo.resolve()
    files = entries(root)
    before, after, merges = Counter(), Counter(), Counter()
    changed, removed_dupes, problems = [], 0, []
    for f in files:
        with open(f, encoding="utf-8", newline="") as fh:
            text = fh.read()
        try:
            new_text, old, new, warns = process(text, kmap)
        except EntryError as exc:
            problems.append(f"{f.relative_to(root)}: {exc} (skipped)")
            continue
        problems += [f"{f.relative_to(root)}: {w}" for w in warns]
        before.update(old)
        after.update(new)
        for k in old:
            if k in kmap:
                merges[(k, kmap[k])] += 1
        removed_dupes += len(old) - len(new)
        if new_text != text:
            changed.append(f)
            if args.verbose:
                print(f"{f.relative_to(root)}:\n    - {old}\n    + {new}")
            if not args.dry_run:
                with open(f, "w", encoding="utf-8", newline="") as fh:
                    fh.write(new_text)

    mode = "DRY RUN (nothing written)" if args.dry_run else "APPLIED"
    print(f"{mode}: {len(files)} entries scanned, {len(changed)} files "
          f"{'would change' if args.dry_run else 'changed'}")
    print(f"unique keywords: {len(before)} before -> {len(after)} after "
          f"({len(before) - len(after)} fewer)")
    print(f"keyword uses rewritten: {sum(merges.values())}; duplicates removed within entries: {removed_dupes}")
    print(f"map entries used: {len(merges)} of {len(kmap)}")
    singles_b = sum(1 for v in before.values() if v == 1)
    singles_a = sum(1 for v in after.values() if v == 1)
    print(f"keywords used once: {singles_b} before -> {singles_a} after")
    if problems:
        print(f"\n{len(problems)} warning(s):")
        for p in problems:
            print("  " + p)
    if not args.dry_run and changed:
        print("\nNow run: python3 tools/build_index.py   (regenerates KEYWORDS.md and indexes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
