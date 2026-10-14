#!/usr/bin/env python3
"""Validate paper entries and regenerate the index files of the registry.

Each topic lives in a top-level folder named ``NN-topic-name``.  Every ``*.md``
file in a topic folder other than ``README.md`` is a paper entry with YAML
front matter (see ``TEMPLATE.md``).  This script

* validates every entry's front matter,
* rewrites the block between ``<!-- INDEX:START -->`` and ``<!-- INDEX:END -->``
  in each topic ``README.md`` and in the root ``README.md``,
* regenerates ``KEYWORDS.md`` (keyword -> entries) and ``CATALOG.md``
  (every entry, by year).

Usage::

    python3 tools/build_index.py            # validate + rebuild everything
    python3 tools/build_index.py --check    # validate only, write nothing
    python3 tools/build_index.py --topic 02-wavefront-sensing   # rebuild one topic README
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TOPIC_RE = re.compile(r"^\d\d-[a-z0-9-]+$")
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"

REQUIRED = ["title", "authors", "year", "url", "access", "type", "subtopic", "keywords"]
# Controlled vocabulary: variant keyword -> preferred keyword (see CONTRIBUTING.md).
_KWMAP = Path(__file__).with_name("keyword_map.json")
KEYWORD_MAP: dict[str, str] = json.loads(_KWMAP.read_text(encoding="utf-8")) if _KWMAP.exists() else {}
ACCESS = {"arXiv", "open-access", "ADS-scan", "author-copy", "repository", "free-to-read", "hosted-copy", "researchgate"}
TYPES = {
    "paper", "review", "tutorial", "book", "book-chapter", "thesis", "lecture-notes",
    "course", "software", "dataset", "report", "website", "proceedings",
}


def topics() -> list[Path]:
    return sorted(p for p in ROOT.iterdir() if p.is_dir() and TOPIC_RE.match(p.name))


def load_entry(path: Path) -> tuple[dict | None, list[str]]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, ["missing YAML front matter"]
    try:
        _, fm, _ = text.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    except Exception as exc:  # noqa: BLE001
        return None, [f"unparseable front matter: {exc}"]
    errs = [f"missing field '{k}'" for k in REQUIRED if not meta.get(k)]
    if meta.get("access") and meta["access"] not in ACCESS:
        errs.append(f"access '{meta['access']}' not in {sorted(ACCESS)}")
    if meta.get("type") and meta["type"] not in TYPES:
        errs.append(f"type '{meta['type']}' not in {sorted(TYPES)}")
    if not isinstance(meta.get("authors", []), list):
        errs.append("authors must be a list")
    if not isinstance(meta.get("keywords", []), list):
        errs.append("keywords must be a list")
    else:
        for k in meta.get("keywords") or []:
            pref = KEYWORD_MAP.get(str(k).strip().lower())
            if pref:
                errs.append(f"keyword '{k}' should be '{pref}' (tools/keyword_map.json; "
                            "python3 tools/apply_keywords.py . fixes it)")
    for t in meta.get("also_relevant_to") or []:
        if not (ROOT / t).is_dir():
            errs.append(f"also_relevant_to '{t}' is not a topic folder")
    meta["_path"] = path
    meta["_topic"] = path.parent.name
    return meta, errs


def collect() -> tuple[dict[str, list[dict]], list[str]]:
    by_topic: dict[str, list[dict]] = {}
    problems: list[str] = []
    for t in topics():
        entries = []
        for f in sorted(t.glob("*.md")):
            if f.name == "README.md":
                continue
            meta, errs = load_entry(f)
            problems += [f"{f.relative_to(ROOT)}: {e}" for e in errs]
            if meta:
                entries.append(meta)
        by_topic[t.name] = entries
    # duplicate detection across the whole registry
    seen: dict[str, Path] = {}
    for entries in by_topic.values():
        for m in entries:
            for key in ("doi", "arxiv", "url"):
                v = str(m.get(key) or "").strip().lower().rstrip("/")
                if not v:
                    continue
                k = f"{key}:{v}"
                if k in seen:
                    problems.append(
                        f"duplicate {key} {v}: {m['_path'].relative_to(ROOT)} and "
                        f"{seen[k].relative_to(ROOT)}"
                    )
                else:
                    seen[k] = m["_path"]
    return by_topic, problems


def authors_short(m: dict) -> str:
    a = [str(x) for x in m.get("authors") or []]
    if not a:
        return ""
    first = a[0].split(",")[0].strip()
    if len(a) == 1:
        return first
    if len(a) == 2:
        return f"{first} & {a[1].split(',')[0].strip()}"
    return f"{first} et al."


def esc(s: str) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def title_of(topic: str) -> str:
    readme = ROOT / topic / "README.md"
    if readme.exists():
        for line in readme.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return topic


def row(m: dict, rel_from: Path) -> str:
    link = m["_path"].relative_to(rel_from).as_posix()
    tag = "" if m.get("type") in (None, "paper") else f" *({m['type']})*"
    return (
        f"| {m.get('year', '')} | [{esc(m['title'])}]({link}){tag} | {esc(authors_short(m))} | "
        f"[full text]({m['url']}) |"
    )


def sort_key(m: dict):
    return (int(m.get("year") or 0), authors_short(m).lower())


def topic_index(topic: str, entries: list[dict], cross: list[dict]) -> str:
    out = [f"_{len(entries)} entries. Generated by `tools/build_index.py`; do not edit by hand._", ""]
    groups: dict[str, list[dict]] = defaultdict(list)
    for m in entries:
        groups[m["subtopic"]].append(m)
    for sub in sorted(groups, key=str.lower):
        out += [f"### {sub}", "", "| Year | Entry | Authors | Link |", "|---|---|---|---|"]
        out += [row(m, ROOT / topic) for m in sorted(groups[sub], key=sort_key)]
        out.append("")
    if cross:
        out += ["### Cross-listed from other topics", "", "| Year | Entry | Authors | Home topic |",
                "|---|---|---|---|"]
        for m in sorted(cross, key=sort_key):
            link = Path("..", m["_topic"], m["_path"].name).as_posix()
            out.append(f"| {m.get('year', '')} | [{esc(m['title'])}]({link}) | "
                       f"{esc(authors_short(m))} | [{m['_topic']}](../{m['_topic']}/README.md) |")
        out.append("")
    return "\n".join(out)


def splice(path: Path, block: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if START in text and END in text:
        pre, rest = text.split(START, 1)
        _, post = rest.split(END, 1)
        text = f"{pre}{START}\n{block}\n{END}{post}"
    else:
        text = f"{text.rstrip()}\n\n{START}\n{block}\n{END}\n"
    path.write_text(text, encoding="utf-8")


def build(by_topic: dict[str, list[dict]], only: str | None) -> None:
    cross: dict[str, list[dict]] = defaultdict(list)
    for entries in by_topic.values():
        for m in entries:
            for t in m.get("also_relevant_to") or []:
                if t != m["_topic"]:
                    cross[t].append(m)
    for t, entries in by_topic.items():
        if only and t != only:
            continue
        splice(ROOT / t / "README.md", topic_index(t, entries, cross.get(t, [])))
    if only:
        return

    all_entries = [m for es in by_topic.values() for m in es]

    # root README topic table
    lines = ["| # | Topic | Entries | Cross-listed |", "|---|---|---|---|"]
    for t, es in by_topic.items():
        name = title_of(t).split("·", 1)[-1].strip()
        lines.append(f"| {t[:2]} | [{name}]({t}/README.md) | {len(es)} | {len(cross.get(t, []))} |")
    lines += ["", f"**Total entries: {len(all_entries)}**"]
    splice(ROOT / "README.md", "\n".join(lines))

    # KEYWORDS.md (index) + keywords/<letter>.md (one page per initial, to keep pages small)
    kw: dict[str, list[dict]] = defaultdict(list)
    for m in all_entries:
        for k in m.get("keywords") or []:
            kw[str(k).strip().lower()].append(m)
    kdir = ROOT / "keywords"
    kdir.mkdir(exist_ok=True)
    for old in kdir.glob("*.md"):
        old.unlink()
    by_letter: dict[str, list[str]] = defaultdict(list)
    for k in sorted(kw):
        if k:
            c = k[0].upper()
            by_letter[c if c.isalpha() else "0-9"].append(k)
    letters = sorted(by_letter, key=lambda c: (c != "0-9", c))
    out = ["# Keyword index", "",
           "Every keyword used in the registry, with the entries tagged with it, split into one page per "
           "initial letter. Generated by `tools/build_index.py`; do not edit by hand. On a letter page, use "
           "your browser's find (Ctrl-F) to jump to a keyword.", "",
           f"{len(kw)} keywords in total.", "", "| Letter | Keywords |", "|---|---|"]
    out += [f"| [{c}](keywords/{c.lower()}.md) | {len(by_letter[c])} |" for c in letters]
    (ROOT / "KEYWORDS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    for c in letters:
        page = [f"# Keywords: {c}", "", "[All letters](../KEYWORDS.md) · " +
                " · ".join(f"[{x}]({x.lower()}.md)" for x in letters), ""]
        for k in by_letter[c]:
            items = ", ".join(
                f"[{esc(authors_short(m))} {m.get('year', '')}](../{m['_topic']}/{m['_path'].name})"
                for m in sorted(kw[k], key=sort_key)
            )
            page.append(f"- **{k}** ({len(kw[k])}): {items}")
        (kdir / f"{c.lower()}.md").write_text("\n".join(page) + "\n", encoding="utf-8")

    # CATALOG.md
    out = ["# Full catalog", "",
           "All entries in chronological order. Generated by `tools/build_index.py`; do not edit by hand.",
           "", "| Year | Entry | Authors | Topic | Link |", "|---|---|---|---|---|"]
    for m in sorted(all_entries, key=sort_key):
        out.append(
            f"| {m.get('year', '')} | [{esc(m['title'])}]({m['_topic']}/{m['_path'].name}) | "
            f"{esc(authors_short(m))} | [{m['_topic'][:2]}]({m['_topic']}/README.md) | "
            f"[full text]({m['url']}) |"
        )
    (ROOT / "CATALOG.md").write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate only; write nothing")
    ap.add_argument("--topic", help="only rebuild this topic's README")
    args = ap.parse_args()

    by_topic, problems = collect()
    if args.topic:
        problems = [p for p in problems if p.startswith(args.topic)]
    for p in problems:
        print(f"WARNING: {p}", file=sys.stderr)
    n = sum(len(v) for v in by_topic.values())
    print(f"{n} entries in {len(by_topic)} topics; {len(problems)} problem(s).")
    if not args.check:
        build(by_topic, args.topic)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
