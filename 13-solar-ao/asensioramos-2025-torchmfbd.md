---
title: "torchmfbd: a flexible multi-object multi-frame blind deconvolution code"
authors: ["Asensio Ramos, A.", "Díaz Baso, C.", "Kuckein, C.", "Esteban Pozuelo, S.", "Löfdahl, M. G."]
year: 2025
venue: "A&A 703, A269"
doi: "10.1051/0004-6361/202555530"
arxiv: "2505.10639"
url: "https://arxiv.org/abs/2505.10639"
alt_urls: []
access: arXiv
type: software
subtopic: "Image restoration with solar AO (speckle, MFBD, MOMFBD)"
also_relevant_to: ["09-psf-reconstruction-and-post-processing"]
keywords: ["momfbd", "multi-frame blind deconvolution", "image restoration", "gpu", "pytorch", "field-dependent psf", "software"]
---

# torchmfbd: a flexible multi-object multi-frame blind deconvolution code

**Asensio Ramos et al. (2025)** · *A&A 703, A269* · [Free full text](https://arxiv.org/abs/2505.10639) · DOI: [10.1051/0004-6361/202555530](https://doi.org/10.1051/0004-6361/202555530)

## Summary

Presents torchmfbd, an open-source multi-object multi-frame blind deconvolution code built on PyTorch for GPU-accelerated restoration of solar observations. It implements MOMFBD as a maximum a-posteriori estimation, handles spatially variant PSFs by dividing large fields into patches, and supports both wavefront-based and data-driven PSF parameterisations, including an experimental approach based on non-negative matrix factorisation. Smoothness and sparsity regularisation, apodisation and destretching are included. The code is demonstrated on real solar observations.

## Keywords

`momfbd` · `multi-frame blind deconvolution` · `image restoration` · `gpu` · `pytorch` · `field-dependent psf` · `software`
