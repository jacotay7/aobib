---
title: "Laboratory experiments of model-based reinforcement learning for adaptive optics control"
authors: ["Nousiainen, J.", "Engler, B.", "Kasper, M.", "Rajani, C.", "Helin, T.", "Héritier, C. T.", "Quanz, S. P.", "Glauser, A. M."]
year: 2024
venue: "JATIS 10, 019001"
doi: "10.1117/1.JATIS.10.1.019001"
arxiv: "2401.00242"
url: "https://arxiv.org/abs/2401.00242"
alt_urls: ["https://hal.science/hal-04650504"]
access: arXiv
type: paper
subtopic: "Reinforcement learning control"
also_relevant_to: ["04-control-and-reconstruction"]
keywords: ["reinforcement learning", "po4ao", "model-based reinforcement learning", "ghost", "eso", "real-time control", "pytorch", "latency"]
---

# Laboratory experiments of model-based reinforcement learning for adaptive optics control

**Nousiainen et al. (2024)** · *JATIS 10, 019001* · [Free full text](https://arxiv.org/abs/2401.00242) · DOI: [10.1117/1.JATIS.10.1.019001](https://doi.org/10.1117/1.JATIS.10.1.019001)

## Summary

Implements and adapts the PO4AO model-based reinforcement learning controller on the GPU-based High-order adaptive OpticS Testbench (GHOST) at ESO headquarters. The implementation allows training to run in parallel with inference, which the authors identify as necessary for on-sky operation, and the predictive and self-calibrating behaviour of the method is studied. The PyTorch implementation adds about 700 microseconds of latency on top of hardware, pipeline and Python-interface latency. The code is released as open source, and the paper documents RTC pipeline requirements, key hyperparameters and paths to lower latency.

## Keywords

`reinforcement learning` · `po4ao` · `model-based reinforcement learning` · `ghost` · `eso` · `real-time control` · `pytorch` · `latency`
