---
title: "Real-time implementation of an LQG tip-tilt controller for regular science observation on GeMS"
authors: ["Sivo, G.", "Juvénal, R.", "Kulcsár, C.", "Garrel, V.", "Gigoux, P.", "Raynaud, H.-F.", "et al."]
year: 2016
venue: "Proc. SPIE 9909, 99094Y"
doi: "10.1117/12.2233191"
url: "https://hal.science/hal-01722330"
alt_urls: []
access: repository
type: paper
subtopic: "Vibration & windshake rejection"
also_relevant_to: ["05-wide-field-and-tomographic-ao"]
keywords: ["lqg control", "tip-tilt control", "vibration", "autoregressive model", "gems", "gemini", "real-time controller"]
---

# Real-time implementation of an LQG tip-tilt controller for regular science observation on GeMS

**Sivo et al. (2016)** · *Proc. SPIE 9909, 99094Y* · [Free full text](https://hal.science/hal-01722330) · DOI: [10.1117/12.2233191](https://doi.org/10.1117/12.2233191)

## Summary

Explores the performance limitation of integrator tip-tilt control in GeMS, the Gemini South MCAO system, which cannot mitigate vibrations at arbitrary frequencies. A tip-tilt LQG controller is implemented with two classes of perturbation models: a sum of second-order autoregressive models identified from an estimated power spectral density (as used on CANARY and SPHERE), and cascaded ARMA models of order 2 identified by prediction error minimization. The models produce tip or tilt state-space models up to order 20 and 30 respectively. The parallelized real-time implementation and expected performance are discussed ahead of on-sky tests.

## Keywords

`lqg control` · `tip-tilt control` · `vibration` · `autoregressive model` · `gems` · `gemini` · `real-time controller`
