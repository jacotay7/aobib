---
title: "Efficient computation of minimum-variance wave-front reconstructors with sparse matrix techniques"
authors: ["Ellerbroek, B. L."]
year: 2002
venue: "JOSA A 19, 1803"
doi: "10.1364/JOSAA.19.001803"
url: "https://webarchive.gemini.edu/documentation/webdocs/preprints/gpre82.pdf"
alt_urls: []
access: author-copy
type: paper
subtopic: "Fast & iterative reconstructors"
also_relevant_to: ["05-wide-field-and-tomographic-ao"]
keywords: ["minimum variance", "sparse matrix", "fast reconstruction", "mcao", "multi-conjugate ao", "laser guide star", "computational complexity"]
---

# Efficient computation of minimum-variance wave-front reconstructors with sparse matrix techniques

**Ellerbroek (2002)** · *JOSA A 19, 1803* · [Free full text](https://webarchive.gemini.edu/documentation/webdocs/preprints/gpre82.pdf) · DOI: [10.1364/JOSAA.19.001803](https://doi.org/10.1364/JOSAA.19.001803)

## Summary

Computing conventional matrix-multiply reconstructors scales as O(n^3) in the number of actuators, and sparse-matrix methods known for least-squares reconstruction are not directly applicable to the minimum-variance reconstructors favoured for MCAO, because turbulence statistics are non-sparse and LGS tip-tilt uncertainty introduces global terms. The paper shows that sparse methods can still be used by adopting a sparse approximation of the turbulence statistics and by treating the non-sparse LGS position-uncertainty terms as low-rank updates handled with the matrix inversion lemma. Numerical examples indicate that the turbulence approximation has negligible effect on estimation accuracy, that the sparse minimum-variance reconstructor for a conventional NGS AO system can be computed in O(n^(3/2)) time (a few seconds for n = 3500), and that the computation is reduced by a factor of 8 for sample MCAO systems, with a projected factor of 30-40 for systems of about 10,000 actuators. The free link is the Gemini Observatory preprint (#82) of the journal paper.

## Keywords

`minimum variance` · `sparse matrix` · `fast reconstruction` · `mcao` · `multi-conjugate ao` · `laser guide star` · `computational complexity`
