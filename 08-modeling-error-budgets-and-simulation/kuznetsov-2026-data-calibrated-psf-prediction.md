---
title: "Data-calibrated point spread function prediction: General description of the method and demonstration on MUSE-NFM"
authors: ["Kuznetsov, A.", "Neichel, B.", "Oberti, S.", "Fusco, T."]
year: 2026
venue: "A&A 708, A311"
doi: "10.1051/0004-6361/202557297"
arxiv: "2603.23339"
url: "https://arxiv.org/abs/2603.23339"
alt_urls: []
access: arXiv
type: paper
subtopic: "Model validation & PSF prediction"
also_relevant_to: ["09-psf-reconstruction-and-post-processing", "11-machine-learning-and-ai"]
keywords: ["psf prediction", "model validation", "tiptop", "muse", "neural network", "ltao", "fourier model"]
---

# Data-calibrated point spread function prediction: General description of the method and demonstration on MUSE-NFM

**Kuznetsov et al. (2026)** · *A&A 708, A311* · [Free full text](https://arxiv.org/abs/2603.23339) · DOI: [10.1051/0004-6361/202557297](https://doi.org/10.1051/0004-6361/202557297)

## Summary

The paper presents a framework for fast, data-calibrated modeling of AO-corrected PSFs that captures their spatial and spectral variability without full AO telemetry. A Fourier-based PSF model inspired by TIPTOP takes a compact set of physical parameters retrievable from the ESO archive, and a lightweight neural network, trained end to end with the PSF model on on-sky data, corrects these inputs for miscalibrations. On MUSE-NFM standard stars the median errors are 13.5% in Strehl ratio and 10.9% in core FWHM. In crowded MUSE-NFM fields of omega Centauri, off-axis wavelength-dependent PSFs are predicted with Strehl errors below 5% and FWHM errors of 4.6%.

## Keywords

`psf prediction` · `model validation` · `tiptop` · `muse` · `neural network` · `ltao` · `fourier model`
