---
title: "Focal plane wavefront sensing using machine learning: performance of convolutional neural networks compared to fundamental limits"
authors: ["Orban de Xivry, G.", "Quesnel, M.", "Vanberg, P.-O.", "Absil, O.", "Louppe, G."]
year: 2021
venue: "MNRAS 505, 5702"
doi: "10.1093/mnras/stab1634"
arxiv: "2106.04456"
url: "https://arxiv.org/abs/2106.04456"
alt_urls: []
access: arXiv
type: paper
subtopic: "Image-based & focal-plane wavefront sensing"
also_relevant_to: ["07-high-contrast-and-extreme-ao", "02-wavefront-sensing"]
keywords: ["focal-plane wavefront sensing", "convolutional neural network", "cnn", "ncpa", "phase retrieval", "resnet", "u-net", "photon noise"]
---

# Focal plane wavefront sensing using machine learning: performance of convolutional neural networks compared to fundamental limits

**Orban de Xivry et al. (2021)** · *MNRAS 505, 5702* · [Free full text](https://arxiv.org/abs/2106.04456) · DOI: [10.1093/mnras/stab1634](https://doi.org/10.1093/mnras/stab1634)

## Summary

Uses deep convolutional neural networks to measure non-common path aberrations from focal-plane images, using phase diversity to lift the sign ambiguity. Two architectures are considered: ResNet-50 to estimate Zernike coefficients and U-Net to estimate the phase directly, trained on labelled simulated datasets at various flux levels and for 20 or 100 Zernike modes. In these idealized simulations the networks reach the photon-noise limit over a wide range of conditions, e.g. residual wavefront error below lambda/1500 rms for 2e6 photons when estimating 20 modes in one iteration. The models are robust to varying signal-to-noise ratio, higher-order aberrations and aberration amplitude, and perform similarly to or better than iterative phase retrieval.

## Keywords

`focal-plane wavefront sensing` · `convolutional neural network` · `cnn` · `ncpa` · `phase retrieval` · `resnet` · `u-net` · `photon noise`
