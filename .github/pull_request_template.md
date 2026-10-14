<!-- See CONTRIBUTING.md for the curation rules. -->

- [ ] Each new entry links to a **legitimate free full text** (not ResearchGate/Academia.edu/shadow libraries)
- [ ] The summary is neutral and written from the paper or its abstract, not copied from the abstract
- [ ] Checked that the entry does not already exist (`grep -ril "<doi or arXiv id>" [0-9]*/`)
- [ ] Ran `python3 tools/build_index.py` and committed the regenerated indexes
- [ ] Ran `python3 tools/check_links.py <new files>`
