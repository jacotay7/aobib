---
title: "Prediction of AO corrected PSF for SPHERE / AOF NFM"
authors: ["Kuznetsov, A.", "Neichel, B.", "Oberti, S.", "Fusco, T."]
year: 2023
venue: "Proc. AO4ELT7 (Avignon, 2023)"
doi: "10.13009/AO4ELT7-2023-106"
url: "https://hal.science/hal-04402888"
alt_urls: []
access: repository
type: paper
subtopic: "Model validation & PSF prediction"
also_relevant_to: ["09-psf-reconstruction-and-post-processing", "11-machine-learning-and-ai"]
keywords: ["psf prediction", "model validation", "tiptop", "sphere", "telemetry", "neural network", "on-sky performance"]
---

# Prediction of AO corrected PSF for SPHERE / AOF NFM

**Kuznetsov et al. (2023)** · *Proc. AO4ELT7 (Avignon, 2023)* · [Free full text](https://hal.science/hal-04402888) · DOI: [10.13009/AO4ELT7-2023-106](https://doi.org/10.13009/AO4ELT7-2023-106)

## Summary

The authors use the TIPTOP analytical PSF model, driven by reduced telemetry, to predict on-axis PSFs of the SPHERE instrument and test the predictions against on-sky data. They find that the uncalibrated physics-based model gives errors of 34.6% on on-sky data (14.8% on synthetic data), showing that calibration of analytical models is needed. The model is therefore coupled to a feed-forward neural network that corrects its inputs, with two training strategies presented. The calibrated model reaches a prediction error of 13.6% on real on-sky data and 1.7% on simulated data.

## Keywords

`psf prediction` · `model validation` · `tiptop` · `sphere` · `telemetry` · `neural network` · `on-sky performance`
