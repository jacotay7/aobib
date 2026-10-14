---
title: "Adapting optimal LQG methods to ELT-sized AO systems"
authors: ["Correia, C.", "Conan, J.-M.", "Kulcsár, C.", "Raynaud, H.-F.", "Petit, C."]
year: 2010
venue: "Proc. AO4ELT1 (Paris, 2009), 07003"
doi: "10.1051/ao4elt/201007003"
url: "https://ao4elt.edpsciences.org/articles/ao4elt/pdf/2010/01/ao4elt_07003.pdf"
alt_urls: []
access: open-access
type: paper
subtopic: "LQG, Kalman & minimum-variance control"
also_relevant_to: []
keywords: ["lqg control", "kalman filter", "minimum variance", "riccati equation", "conjugate gradient", "fourier domain preconditioning", "sparse methods", "elt", "computational complexity"]
---

# Adapting optimal LQG methods to ELT-sized AO systems

**Correia et al. (2010)** · *Proc. AO4ELT1 (Paris, 2009), 07003* · [Free full text](https://ao4elt.edpsciences.org/articles/ao4elt/pdf/2010/01/ao4elt_07003.pdf) · DOI: [10.1051/ao4elt/201007003](https://doi.org/10.1051/ao4elt/201007003)

## Summary

Addresses the computational cost of minimum-variance Linear-Quadratic-Gaussian (LQG) control for extremely large telescope AO, whose standard real-time implementation scales as O(n^2) in the number of degrees of freedom. The authors move from modal to zonal descriptions of the phase, measurements and DM influence functions to obtain sparse operators, and use a doubling algorithm on a reduced system to speed up the off-line solution of the estimation Riccati equation. In real time, the product with the Kalman gain is computed with Fourier-domain preconditioned conjugate gradients (FD-PCG), using a sparse spectral approximation of the estimation error covariance so that the Riccati solution itself is not needed, reducing the cost to O(n log n). Monte Carlo simulations of an 8 m single-conjugate system with 20 Shack-Hartmann subapertures across give long-exposure Strehl ratios of about 81% for the modal, zonal, sparse and FD-PCG variants alike. Extension to wide-field AO is noted as ongoing work.

## Keywords

`lqg control` · `kalman filter` · `minimum variance` · `riccati equation` · `conjugate gradient` · `fourier domain preconditioning` · `sparse methods` · `elt` · `computational complexity`
