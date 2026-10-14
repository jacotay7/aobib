---
title: "Forecasting wavefront corrections in an adaptive optics system"
authors: ["Hafeez, R.", "Archinuk, F.", "Fabbro, S.", "Teimoorinia, H.", "Véran, J.-P."]
year: 2022
venue: "JATIS 8, 029003"
doi: "10.1117/1.JATIS.8.2.029003"
arxiv: "2112.01437"
url: "https://arxiv.org/abs/2112.01437"
alt_urls: []
access: arXiv
type: paper
subtopic: "Learned predictive control"
also_relevant_to: ["04-control-and-reconstruction"]
keywords: ["predictive control", "telemetry", "altair", "gemini", "lstm", "autoregressive model", "tip-tilt"]
---

# Forecasting wavefront corrections in an adaptive optics system

**Hafeez et al. (2022)** · *JATIS 8, 029003* · [Free full text](https://arxiv.org/abs/2112.01437) · DOI: [10.1117/1.JATIS.8.2.029003](https://doi.org/10.1117/1.JATIS.8.2.029003)

## Summary

Uses telemetry from the Gemini North ALTAIR AO system to assess how well tip-tilt and high-order correction commands can be forecast to reduce lag error. A linear auto-regressive 'forecasting filter' with few coefficients (about 30 for tip-tilt and 5 for high-order modes), complementing the integral controller, reduces rms wavefront error by factors of about 5 for tip-tilt and 2 for high-order modes, and can be updated with less than 10 s of telemetry. Non-linear models (LSTM and dilated convolutional networks) were also evaluated and gave no perceptible improvement over the linear predictions, even at large lags. The authors conclude that non-linear wavefront distortions for ALTAIR may not be forecastable with the current setup.

## Keywords

`predictive control` · `telemetry` · `altair` · `gemini` · `lstm` · `autoregressive model` · `tip-tilt`
