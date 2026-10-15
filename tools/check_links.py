#!/usr/bin/env python3
"""Check that the full-text links of registry entries still resolve.

Usage::

    python3 tools/check_links.py                 # every entry
    python3 tools/check_links.py 02-wavefront-sensing [more topics or files...]

Prints one line per non-OK link.  Some publishers reject scripted requests
(HTTP 403) even though the page opens fine in a browser; those are reported as
"BLOCKED?" rather than failures so they can be checked by hand.  Servers with a
broken TLS certificate chain that still serve the page are reported as "SSL-CERT".
HAL pages sit behind a bot check that stalls scripted requests, so HAL links are
checked through the HAL search API instead: the record must exist and carry a
full-text file ("HAL-NOFILE" otherwise).
ResearchGate links are not requested at all (the site forbids scripted access);
they are listed as "MANUAL" so they can be rechecked in a browser.
"""

from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.parse
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (X11; Linux x86_64) aobib-linkcheck"
HAL_API = "https://api.archives-ouvertes.fr/search/?"
HAL_HOST = re.compile(r"^https?://([a-z0-9-]+\.)*(hal\.science|ccsd\.cnrs\.fr|hal\.[a-z0-9.-]+)/", re.I)
HAL_ID = re.compile(r"/([a-z][a-z0-9]*-\d{6,})(?:v\d+)?(?:/|$)")
HAL_COLLECTION = re.compile(r"^https?://[^/]+/([A-Z][A-Z0-9_-]+)/?$")


def urls_of(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    try:
        meta = yaml.safe_load(text.split("---", 2)[1]) or {}
    except Exception:  # noqa: BLE001
        return []
    return [u for u in [meta.get("url"), *(meta.get("alt_urls") or [])] if u]


def hal_status(url: str) -> str | None:
    """Status of a HAL record or collection via the HAL API; None if not a HAL link or the API fails."""
    if not HAL_HOST.match(url):
        return None
    if m := HAL_ID.search(url):
        query = {"q": f"halId_s:{m.group(1)}", "fl": "halId_s,fileMain_s"}
    elif m := HAL_COLLECTION.match(url):
        query = {"q": f"collCode_s:{m.group(1)}", "rows": 0}
    else:
        return None
    req = urllib.request.Request(HAL_API + urllib.parse.urlencode(query), headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            resp = json.load(r)["response"]
    except Exception:  # noqa: BLE001
        return None
    if not resp.get("numFound"):
        return "HAL-NOTFOUND"
    if "halId_s" in query["q"] and not resp["docs"][0].get("fileMain_s"):
        return "HAL-NOFILE"
    return "200"


def status(url: str) -> str:
    if hal := hal_status(url):
        return hal
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return str(r.status)
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405, 404, 400, 418, 501):
                return str(e.code)
            last = str(e.code)
        except urllib.error.URLError as e:
            if isinstance(e.reason, ssl.SSLError):
                # broken certificate chain on the server; browsers often cope -> retry unverified
                try:
                    with urllib.request.urlopen(req, timeout=30, context=ssl._create_unverified_context()) as r:
                        return f"SSL-{r.status}"
                except Exception:  # noqa: BLE001
                    pass
            last = type(e.reason).__name__
            if method == "GET":
                return last
        except Exception as e:  # noqa: BLE001
            last = type(e).__name__
            if method == "GET":
                return last
    return last


def main() -> int:
    targets = [ROOT / a for a in sys.argv[1:]] or [p for p in ROOT.iterdir() if p.is_dir()]
    files: list[Path] = []
    for t in targets:
        if t.is_file():
            files.append(t)
        elif t.is_dir() and t.name[:2].isdigit():
            files += [f for f in sorted(t.glob("*.md")) if f.name != "README.md"]
    jobs = [(f, u) for f in files for u in urls_of(f)]
    manual = [(f, u) for f, u in jobs if "researchgate.net" in u]
    jobs = [j for j in jobs if j not in manual]
    for f, u in manual:
        print(f"MANUAL - {f.relative_to(ROOT)} {u}")
    bad = 0
    with ThreadPoolExecutor(max_workers=12) as ex:
        for (f, u), s in zip(jobs, ex.map(lambda j: status(j[1]), jobs)):
            if s.startswith("2"):
                continue
            if s.startswith("SSL-2"):
                label = "SSL-CERT"  # page served, but the server's TLS chain is incomplete
            else:
                label = "BLOCKED?" if s in ("403", "418", "429") else "FAIL"
            bad += label == "FAIL"
            print(f"{label} {s} {f.relative_to(ROOT)} {u}")
    print(f"checked {len(jobs)} links in {len(files)} entries; {bad} failure(s); {len(manual)} left for manual check")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
