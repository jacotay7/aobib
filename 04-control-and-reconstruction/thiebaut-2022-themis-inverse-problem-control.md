---
title: "Closing the loop as an inverse problem: the real-time control of THEMIS adaptive optics"
authors: ["Thiébaut, É.", "Tallon, M.", "Tallon-Bosc, I.", "Gelly, B.", "Douet, R.", "Langlois, M.", "Moretto, G."]
year: 2022
venue: "Proc. SPIE 12185, 1218507"
doi: "10.1117/12.2630497"
arxiv: "2311.17779"
url: "https://arxiv.org/abs/2311.17779"
alt_urls: ["https://hal.science/hal-03877079"]
access: arXiv
type: paper
subtopic: "Control architectures (POLC, woofer-tweeter, cascade)"
also_relevant_to: ["13-solar-ao"]
keywords: ["inverse problems", "pseudo-open-loop control", "regularization", "noise covariance", "shack-hartmann", "themis", "solar adaptive optics", "real-time controller"]
---

# Closing the loop as an inverse problem: the real-time control of THEMIS adaptive optics

**Thiébaut et al. (2022)** · *Proc. SPIE 12185, 1218507* · [Free full text](https://arxiv.org/abs/2311.17779) · DOI: [10.1117/12.2630497](https://doi.org/10.1117/12.2630497)

## Summary

Describes the control strategy implemented for the adaptive optics of the THEMIS solar telescope, formulated as an inverse problem encompassing the whole system. The approach estimates Shack-Hartmann pixel variances, extracts wavefront slopes and their noise covariance in real time, and computes pseudo-open-loop data. Optimal commands are obtained by iteratively solving a regularized inverse problem with spatio-temporal constraints including Kolmogorov statistics. The dedicated real-time software runs on conventional CPUs with a latency below 300 microseconds from acquisition of the 400x400-pixel sensor image to sending the commands.

## Keywords

`inverse problems` · `pseudo-open-loop control` · `regularization` · `noise covariance` · `shack-hartmann` · `themis` · `solar adaptive optics` · `real-time controller`
