---
title: "Transformer neural networks for closed-loop adaptive optics using nonmodulated pyramid wavefront sensors"
authors: ["Weinberger, C.", "Tapia, J.", "Neichel, B.", "Vera, E."]
year: 2024
venue: "A&A 687, A202"
doi: "10.1051/0004-6361/202349118"
arxiv: "2405.05472"
url: "https://arxiv.org/abs/2405.05472"
alt_urls: []
access: arXiv
type: paper
subtopic: "Nonlinear pyramid & Fourier-filtering WFS reconstruction"
also_relevant_to: ["02-wavefront-sensing"]
keywords: ["pyramid wavefront sensor", "pwfs", "unmodulated", "transformer", "convolutional neural network", "nonlinear reconstruction", "closed-loop control"]
---

# Transformer neural networks for closed-loop adaptive optics using nonmodulated pyramid wavefront sensors

**Weinberger et al. (2024)** · *A&A 687, A202* · [Free full text](https://arxiv.org/abs/2405.05472) · DOI: [10.1051/0004-6361/202349118](https://doi.org/10.1051/0004-6361/202349118)

## Summary

Trains and compares deep neural networks as non-linear estimators for the non-modulated pyramid wavefront sensor, from classical and recent convolutional networks to a Global Context Vision Transformer (GCViT). A training strategy is introduced that accounts for the change in residual statistics between open and closed loop and adds noise for robustness. In simulation the transformer is the most accurate in open loop and in closed loop avoids estimation issues at the pupil borders; at strong turbulence it closes the loop comparably to a pyramid with 12 lambda/D modulation, and at higher noise only the transformer closes the loop. On an optical bench, the GCViT closed a real AO loop with Strehl ratios between 0.28 and 0.77 for r0 from 6 to 20 cm.

## Keywords

`pyramid wavefront sensor` · `pwfs` · `unmodulated` · `transformer` · `convolutional neural network` · `nonlinear reconstruction` · `closed-loop control`
