---
title: "An augmented wavelet reconstructor for atmospheric tomography"
authors: ["Ramlau, R.", "Stadler, B."]
year: 2020
venue: "Electronic Transactions on Numerical Analysis 54, 256 (2021)"
doi: "10.1553/etna_vol54s256"
arxiv: "2011.06842"
url: "https://arxiv.org/abs/2011.06842"
alt_urls: []
access: arXiv
type: paper
subtopic: "Fast & iterative reconstructors"
also_relevant_to: ["05-wide-field-and-tomographic-ao"]
keywords: ["wavelet reconstructor", "fewha", "tomography", "conjugate gradient", "krylov subspace recycling", "extremely large telescope", "fast reconstruction"]
---

# An augmented wavelet reconstructor for atmospheric tomography

**Ramlau & Stadler (2020)** · *Electronic Transactions on Numerical Analysis 54, 256 (2021)* · [Free full text](https://arxiv.org/abs/2011.06842) · DOI: [10.1553/etna_vol54s256](https://doi.org/10.1553/etna_vol54s256)

## Summary

Addresses the computational cost of atmospheric tomography for ELT adaptive optics, where matrix-vector multiplication becomes expensive. The Finite Element Wavelet Hybrid Algorithm (FEWHA) uses a matrix-free representation of the forward operator and a preconditioned conjugate gradient solver, reducing floating-point operations and memory. The paper proposes an augmented FEWHA that uses Krylov subspace recycling to reduce the number of PCG iterations by 50%. A parallel implementation of augmented FEWHA is shown to meet the real-time requirements of the ELT.

## Keywords

`wavelet reconstructor` · `fewha` · `tomography` · `conjugate gradient` · `krylov subspace recycling` · `extremely large telescope` · `fast reconstruction`
