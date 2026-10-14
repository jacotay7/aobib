---
title: "Image-based wavefront sensing for astronomy using neural networks"
authors: ["Andersen, T.", "Owner-Petersen, M.", "Enmark, A."]
year: 2020
venue: "JATIS 6, 034002"
doi: "10.1117/1.JATIS.6.3.034002"
url: "https://doi.org/10.1117/1.JATIS.6.3.034002"
alt_urls: []
access: open-access
type: paper
subtopic: "Image-based & focal-plane wavefront sensing"
also_relevant_to: ["02-wavefront-sensing"]
keywords: ["convolutional neural network", "cnn", "focal-plane wavefront sensing", "phase diversity", "resnet", "zernike", "closed-loop control"]
---

# Image-based wavefront sensing for astronomy using neural networks

**Andersen et al. (2020)** · *JATIS 6, 034002* · [Free full text](https://doi.org/10.1117/1.JATIS.6.3.034002) · DOI: [10.1117/1.JATIS.6.3.034002](https://doi.org/10.1117/1.JATIS.6.3.034002)

## Summary

Studies wavefront sensing with convolutional neural networks using a pair of in-focus and out-of-focus point spread functions, motivated by real-time image sharpening in astronomical telescopes. A large simulated dataset including noise, guide-star magnitude, wide-band blurring and detector bit depth was used to train several networks to estimate Zernike approximations of the incoming wavefront. The authors find that a ResNet performs well, reaching about 130 nm rms wavefront error for r0 = 0.3 m and guide-star magnitudes 4 to 8 with an inference time of 8 ms, and that it can be used in closed loop. Adding a Kalman filter or recurrent network was found not to improve performance.

## Keywords

`convolutional neural network` · `cnn` · `focal-plane wavefront sensing` · `phase diversity` · `resnet` · `zernike` · `closed-loop control`
