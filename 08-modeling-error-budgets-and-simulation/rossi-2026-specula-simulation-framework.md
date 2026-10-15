---
title: "Introducing a new generation adaptive optics simulation framework: from PASSATA to SPECULA"
authors: ["Rossi, F.", "Puglisi, A.", "Agapito, G."]
year: 2026
venue: "JATIS 12, 019001"
doi: "10.1117/1.JATIS.12.1.019001"
arxiv: "2602.06688"
url: "https://arxiv.org/abs/2602.06688"
alt_urls: ["https://github.com/ArcetriAdaptiveOptics/SPECULA", "https://specula.readthedocs.io/"]
access: arXiv
type: software
subtopic: "End-to-end simulation codes"
also_relevant_to: []
keywords: ["specula", "passata", "end-to-end simulation", "python", "gpu", "hpc", "hardware-in-the-loop", "simulation code"]
---

# Introducing a new generation adaptive optics simulation framework: from PASSATA to SPECULA

**Rossi et al. (2026)** · *JATIS 12, 019001* · [Free full text](https://arxiv.org/abs/2602.06688) · DOI: [10.1117/1.JATIS.12.1.019001](https://doi.org/10.1117/1.JATIS.12.1.019001)

## Summary

SPECULA is a Python AO simulation framework developed at Arcetri as the successor of PASSATA. Physical entities are modeled as processing objects that exchange data objects, and a simulation is defined by a description file rather than a script. The same code runs on CPU and GPU, using CuPy and CUDA streams for efficiency, and can distribute computation over multiple nodes, as tested on the Leonardo supercomputer. It can also run hybrid simulations that interface simulated and real hardware components, demonstrated in the Arcetri AO laboratory.

## Keywords

`specula` · `passata` · `end-to-end simulation` · `python` · `gpu` · `hpc` · `hardware-in-the-loop` · `simulation code`
