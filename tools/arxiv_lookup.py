#!/usr/bin/env python3
"""Look up arXiv identifiers or search arXiv, printing title/authors/year/DOI/abstract.

Useful for verifying that an arXiv ID really is the paper you think it is
before adding an entry, and for reading the abstract when writing a summary.

Usage::

    python3 tools/arxiv_lookup.py 1001.2345 astro-ph/0601234
    python3 tools/arxiv_lookup.py --search 'ti:"pyramid wavefront sensor" AND au:Ragazzoni' [--max 10]
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import textwrap
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API = "https://export.arxiv.org/api/query?"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def query(params: dict) -> ET.Element:
    url = API + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return ET.fromstring(r.read())
        except Exception as exc:  # noqa: BLE001
            if attempt == 3:
                raise
            print(f"(retrying after error: {exc})", file=sys.stderr)
            time.sleep(3 * (attempt + 1))
    raise RuntimeError("unreachable")


def show(root: ET.Element, abstract: bool) -> None:
    entries = root.findall("a:entry", NS)
    if not entries:
        print("no results")
    for e in entries:
        aid = e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1]
        title = " ".join(e.findtext("a:title", "", NS).split())
        if title == "Error":
            print(f"ERROR: {' '.join(e.findtext('a:summary', '', NS).split())}")
            continue
        authors = [a.findtext("a:name", "", NS) for a in e.findall("a:author", NS)]
        year = e.findtext("a:published", "", NS)[:4]
        doi = e.findtext("arxiv:doi", "", NS)
        jref = e.findtext("arxiv:journal_ref", "", NS)
        print(f"arXiv:{aid}  ({year})")
        print(f"  title:   {title}")
        print(f"  authors: {', '.join(authors[:8])}{' et al.' if len(authors) > 8 else ''}")
        if jref:
            print(f"  journal: {' '.join(jref.split())}")
        if doi:
            print(f"  doi:     {doi}")
        if abstract:
            summ = " ".join(e.findtext("a:summary", "", NS).split())
            print(textwrap.indent(textwrap.fill(summ, 100), "  | "))
        print()


def show_abs_page(aid: str, abstract: bool) -> None:
    """Fallback: read citation_* meta tags from https://arxiv.org/abs/<id>."""
    req = urllib.request.Request(f"https://arxiv.org/abs/{aid}", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            page = r.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        print(f"arXiv:{aid}  ERROR fetching abs page: {exc}\n")
        return
    meta: dict[str, list[str]] = {}
    for name, content in re.findall(r'<meta name="citation_(\w+)" content="([^"]*)"', page):
        meta.setdefault(name, []).append(html.unescape(content))
    if "title" not in meta:
        print(f"arXiv:{aid}  no such paper\n")
        return
    authors = meta.get("author", [])
    print(f"arXiv:{aid}  ({meta.get('date', ['????'])[0][:4]})")
    print(f"  title:   {meta['title'][0]}")
    print(f"  authors: {'; '.join(authors[:8])}{' et al.' if len(authors) > 8 else ''}")
    if meta.get("doi"):
        print(f"  doi:     {meta['doi'][0]}")
    if abstract and meta.get("abstract"):
        print(textwrap.indent(textwrap.fill(" ".join(meta["abstract"][0].split()), 100), "  | "))
    print()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="arXiv identifiers")
    ap.add_argument("--search", help="arXiv API search_query string")
    ap.add_argument("--max", type=int, default=10)
    ap.add_argument("--no-abstract", action="store_true")
    args = ap.parse_args()
    if args.search:
        show(query({"search_query": args.search, "max_results": args.max}), not args.no_abstract)
    if args.ids:
        try:
            show(query({"id_list": ",".join(args.ids), "max_results": len(args.ids)}), not args.no_abstract)
        except Exception as exc:  # noqa: BLE001  (API rate-limited: read the abs pages instead)
            print(f"(arXiv API unavailable: {exc}; falling back to abs pages)", file=sys.stderr)
            for aid in args.ids:
                show_abs_page(aid, not args.no_abstract)
                time.sleep(1)
    if not (args.ids or args.search):
        ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
