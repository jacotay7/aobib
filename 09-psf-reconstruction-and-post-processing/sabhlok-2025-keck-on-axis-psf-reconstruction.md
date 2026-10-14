---
title: "Validating the On-axis Point Spread Function Reconstruction for Keck Adaptive Optics"
authors: ["Sabhlok, S.", "Wright, S. A.", "Lu, J. R.", "Terry, S.", "Wizinowich, P. L.", "Neichel, B.", "Kuznetsov, A."]
year: 2025
venue: "PASP 137, 105001"
doi: "10.1088/1538-3873/ae02c4"
bibcode: "2025PASP..137j5001S"
url: "https://iopscience.iop.org/article/10.1088/1538-3873/ae02c4"
alt_urls: []
access: open-access
type: paper
subtopic: "PSF reconstruction from AO telemetry"
also_relevant_to: []
keywords: ["psf reconstruction", "prime", "keck", "nirc2", "ncpa", "strehl ratio", "fourier psf model", "kapa"]
---

# Validating the On-axis Point Spread Function Reconstruction for Keck Adaptive Optics

**Sabhlok et al. (2025)** · *PASP 137, 105001* · [Free full text](https://iopscience.iop.org/article/10.1088/1538-3873/ae02c4) · DOI: [10.1088/1538-3873/ae02c4](https://doi.org/10.1088/1538-3873/ae02c4)

## Summary

Uses the PRIME Python package to forward-model PSFs for Keck II/NIRC2 AO data from first principles and compares them with Fourier-model fits to the images, using Strehl ratio, FWHM and the fraction of variance unexplained as metrics. Both approaches reproduce Strehl and FWHM reasonably, but the fitted parameters such as r0 can be unphysical unless bounded, and the forward model over-subtracts the core, under-subtracts the wings and misses asymmetries in the secondary maxima. The authors argue that Strehl and FWHM agreement is necessary but not sufficient to validate a reconstruction. They identify poorly known inputs (NCPA map, segment phasing, Cn2 profile and wind) as the main limitations and discuss implications for the Keck All-sky Precision Adaptive Optics upgrade.

## Keywords

`psf reconstruction` · `prime` · `keck` · `nirc2` · `ncpa` · `strehl ratio` · `fourier psf model` · `kapa`
