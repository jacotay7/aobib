# Contributing / curation rules

The easiest way to help is to open an issue: **Suggest a paper** or **Report an error**
(wrong metadata, inaccurate summary, dead or non-free link). Pull requests are welcome too;
CI validates every entry and checks that the generated indexes are up to date.

## What goes in

An entry is anything that helps someone get to the adaptive-optics literature
on their topic quickly: research papers, reviews, free books and book
chapters, lecture notes, courses, theses, software documentation, datasets.

### Selection criteria

The registry is curated, not exhaustive. An entry should meet at least one of these:

1. **Foundational:** introduced a concept, quantity or method that later work builds on
   (e.g. the Fried parameter, the pyramid sensor, LQG control for AO).
2. **Widely used method or tool:** a reconstructor, calibration technique, simulation code or
   data-analysis method in routine use, or the standard reference for one.
3. **First demonstration:** the first on-sky, in-lab or in-vivo demonstration of a technique.
4. **Major facility or system:** the design or performance reference for a significant AO system
   or instrument, at any observatory or in any field (astronomy, vision, microscopy, communications).
5. **Review, tutorial or teaching resource:** gives an efficient way into a sub-field.
6. **Influential recent work** (roughly the last five years): new methods that are being picked up
   by other groups, even if not yet widely cited.

Citation count is a useful signal but not a requirement. Prefer the journal version or the most
complete paper when the same work appears in several places. When several papers cover the same
work, keep the one a newcomer should read first and mention the others in its summary. Aim for
breadth across groups and countries: important work from smaller programs belongs here too.

**Hard rule: free full text only.** Every entry must link to a full text that
anyone can read without paying or logging in. Acceptable sources:

| `access` value | Meaning |
|---|---|
| `arXiv` | arXiv (or another preprint server) copy of the paper |
| `open-access` | Gold/green OA at the publisher (Optics Express, Light: Sci. & Appl., AO4ELT proceedings, A&A Open Access, ...) |
| `free-to-read` | Publisher makes it free to read although not formally OA (e.g. older ApJ/AJ/PASP/A&A, ESO Messenger) |
| `ADS-scan` | Full scanned article hosted by NASA ADS |
| `author-copy` | PDF posted by an author on their own or their institution's web page |
| `repository` | Institutional/national repository (HAL, eScholarship, NASA NTRS, DTIC, university thesis archive, Zenodo) |
| `hosted-copy` | Full text posted on an academic or institutional site by someone other than the authors, e.g. a university course page, a project wiki or a lab reading list. Prefer any source above when one exists. |
| `researchgate` | Full text on ResearchGate, preferably uploaded by an author. Use only when no source above exists, and only after a person has checked in a browser that the full text (not a preview) is readable. ResearchGate blocks scripts, so these links cannot be re-verified automatically. |

Not acceptable: shadow libraries (Sci-Hub, LibGen and similar), document-sharing sites such as Scribd, and
Academia.edu (login walls). ResearchGate is allowed only as a last
resort, under the `researchgate` rule above. Paywalled works that deserve to be here go in
[`PAYWALLED.md`](PAYWALLED.md) instead.

We only link; never commit PDFs or full text to this repository.

## How to add an entry

1. Pick the single best **home topic** folder. If it is also useful elsewhere,
   list the other folders in `also_relevant_to` and it will be cross-listed
   in their indexes automatically. Do not create duplicate files.
2. Copy [`TEMPLATE.md`](TEMPLATE.md) to `<topic>/<firstauthor>-<year>-<short-slug>.md`.
3. Fill in the front matter. Verify arXiv IDs with
   `python3 tools/arxiv_lookup.py <id>` and the link with
   `python3 tools/check_links.py <topic>/<file>.md`.
4. Write a neutral 3–6 sentence summary from the abstract or paper itself,
   plus keywords (lowercase; reuse existing keywords from
   [`KEYWORDS.md`](KEYWORDS.md) where possible).
5. Run `python3 tools/build_index.py` to validate and regenerate all indexes.

## Keyword conventions

* lowercase, spelled out, singular: `deformable mirror`, not `DMs`
* include the common acronym as its own keyword when people search by it:
  `pyramid wavefront sensor` **and** `pwfs`; `multi-conjugate ao` **and** `mcao`
* name instruments/telescopes/codes when relevant: `gpi`, `sphere`, `keck`, `elt`, `compass`
* 5–12 keywords per entry
* use the preferred form of a term: [`tools/keyword_map.json`](tools/keyword_map.json) lists known variants
  and the keyword to use instead (e.g. `lqg` → `lqg control`, `coronagraphy` → `coronagraph`). The validator
  rejects listed variants; `python3 tools/apply_keywords.py .` rewrites them. Add new variants to the map
  when you spot them.
