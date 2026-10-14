---
title: "Fast minimum variance wavefront reconstruction for extremely large telescopes"
authors: ["Thiébaut, É.", "Tallon, M."]
year: 2010
venue: "JOSA A 27, 1046"
doi: "10.1364/JOSAA.27.001046"
arxiv: "1003.0274"
url: "https://arxiv.org/abs/1003.0274"
alt_urls: []
access: arXiv
type: paper
subtopic: "Fast & iterative reconstructors"
also_relevant_to: []
keywords: ["frim", "fractal iterative method", "minimum variance", "conjugate gradient", "preconditioning", "kolmogorov prior", "extremely large telescope", "sparse"]
---

# Fast minimum variance wavefront reconstruction for extremely large telescopes

**Thiébaut & Tallon (2010)** · *JOSA A 27, 1046* · [Free full text](https://arxiv.org/abs/1003.0274) · DOI: [10.1364/JOSAA.27.001046](https://doi.org/10.1364/JOSAA.27.001046)

## Summary

Introduces FRiM (FRactal Iterative Method), a minimum-variance wavefront reconstructor designed for extremely large telescope adaptive optics. The regularized problem enforcing Kolmogorov prior statistics is solved with conjugate gradients, exploiting the sparsity of the wavefront-sensor model and avoiding storage and inversion of large matrices. A fractal approximation of the Karhunen-Loeve basis allows the prior to be applied in O(N) operations, and an O(N) preconditioner yields the solution in 5-10 iterations independently of N. For a 128x128 Shack-Hartmann sensor, FRiM is reported to be more than 100 times faster than vector-matrix multiplication.

## Keywords

`frim` · `fractal iterative method` · `minimum variance` · `conjugate gradient` · `preconditioning` · `kolmogorov prior` · `extremely large telescope` · `sparse`
