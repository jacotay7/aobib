# aobib: a curated registry of adaptive optics literature

A link-only, topic-organized index of noteworthy papers and learning resources in
**adaptive optics (AO)**: astronomical AO, plus AO for vision science, microscopy,
free-space optical communications and space imaging.

**Every entry links to a free, legitimate full text** (arXiv, open-access
publisher, ADS scan, institutional repository, author copy, or a copy on another academic site;
as a last resort, a full text checked by hand on ResearchGate). Important works
with no free copy are listed separately in [`PAYWALLED.md`](PAYWALLED.md).
No PDFs are stored here.

## How to use it

* **Browse by topic.** Each folder below has a `README.md` index grouped by sub-topic,
  with a short "Start here" list for newcomers.
* **Search by keyword.** [`KEYWORDS.md`](KEYWORDS.md) links to one page per letter listing every
  keyword and the entries tagged with it. Or search the repository directly:
  `grep -ril "pyramid" --include=*.md .`
* **Browse chronologically.** [`CATALOG.md`](CATALOG.md) lists every entry by year.
* **New to AO?** Start with [00 · Reviews, Textbooks & Training Resources](00-reviews-and-training/README.md).

Each entry file (`<topic>/<author>-<year>-<slug>.md`) holds YAML metadata (authors, venue,
DOI, arXiv ID, free link, keywords), a short neutral summary, and keywords. Papers relevant
to several topics live in one home folder and are cross-listed in the others' indexes.

## Topics

<!-- INDEX:START -->
| # | Topic | Entries | Cross-listed |
|---|---|---|---|
| 00 | [Reviews, Textbooks & Training Resources](00-reviews-and-training/README.md) | 46 | 49 |
| 01 | [Atmospheric Turbulence & Site Characterization](01-atmospheric-turbulence/README.md) | 69 | 35 |
| 02 | [Wavefront Sensing](02-wavefront-sensing/README.md) | 81 | 92 |
| 03 | [Deformable Mirrors & Wavefront Correctors](03-deformable-mirrors-and-correctors/README.md) | 57 | 24 |
| 04 | [Control, Reconstruction & Real-Time Computing](04-control-and-reconstruction/README.md) | 80 | 64 |
| 05 | [Wide-Field & Tomographic AO (MCAO, GLAO, LTAO, MOAO)](05-wide-field-and-tomographic-ao/README.md) | 63 | 105 |
| 06 | [Laser Guide Stars](06-laser-guide-stars/README.md) | 62 | 42 |
| 07 | [High-Contrast Imaging & Extreme AO](07-high-contrast-and-extreme-ao/README.md) | 80 | 104 |
| 08 | [Modeling, Error Budgets & Simulation](08-modeling-error-budgets-and-simulation/README.md) | 57 | 57 |
| 09 | [PSF Reconstruction, Characterization & Post-Processing](09-psf-reconstruction-and-post-processing/README.md) | 62 | 39 |
| 10 | [Calibration & System Identification](10-calibration-and-system-identification/README.md) | 58 | 36 |
| 11 | [Machine Learning & AI for AO](11-machine-learning-and-ai/README.md) | 47 | 16 |
| 12 | [AO Systems, Instruments & History](12-ao-systems-and-instruments/README.md) | 65 | 118 |
| 13 | [Solar Adaptive Optics](13-solar-ao/README.md) | 56 | 9 |
| 14 | [AO for Vision Science & Ophthalmology](14-vision-science-and-ophthalmology/README.md) | 53 | 11 |
| 15 | [AO for Microscopy & Biological Imaging](15-microscopy-and-biological-imaging/README.md) | 53 | 11 |
| 16 | [AO for Free-Space Optical Communications & Space Imaging](16-free-space-optical-communications-and-space/README.md) | 59 | 16 |
| 17 | [Segmented Apertures, Phasing & Petaling](17-segmented-apertures-and-phasing/README.md) | 48 | 15 |

**Total entries: 1096**
<!-- INDEX:END -->

## Maintenance

```bash
python3 tools/build_index.py              # validate all entries, regenerate every index
python3 tools/build_index.py --check      # validate only
python3 tools/check_links.py [topic ...]  # verify the full-text links still resolve
python3 tools/arxiv_lookup.py <arxiv-id>  # verify an arXiv ID / read its abstract
python3 tools/apply_keywords.py .         # rewrite keyword variants to the preferred form
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for curation rules and [`TEMPLATE.md`](TEMPLATE.md)
for the entry format.

## How this registry was made, and its limits

* **Curation date.** The initial registry was compiled in October 2026. Each entry reflects
  the state of the literature and of free access at that time.
* **AI-assisted.** The initial selection, summaries and keywords were drafted with the help of
  AI research agents (Anthropic's Claude). They worked from the papers' abstracts and full
  texts and checked metadata against arXiv, Crossref and the hosting sites. Every arXiv ID was
  machine-checked against arXiv's own record. The summaries have **not yet all been reviewed by
  a human expert**. Treat a summary as a pointer to the paper, not a substitute for it, and
  please [report errors](CONTRIBUTING.md).
* **Free access can change.** Links were checked when the entries were added. Publishers can
  withdraw free-to-read access, and repositories move. `tools/check_links.py` re-checks them.
* **Not exhaustive.** Selection favors foundational papers, widely used methods, first
  demonstrations, major facilities and reviews. Important work missing here is often
  paywalled; see [`PAYWALLED.md`](PAYWALLED.md). Suggestions are welcome.

## License

The text of this registry (summaries, indexes, READMEs) is licensed under
[Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). The scripts in
[`tools/`](tools/) are under the [MIT License](tools/LICENSE). Linked papers remain the
property of their authors and publishers. This repository only points to them.
