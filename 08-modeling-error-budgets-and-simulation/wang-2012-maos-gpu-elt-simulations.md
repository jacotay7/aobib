---
title: "Computer simulations and real-time control of ELT AO systems using graphical processing units"
authors: ["Wang, L.", "Ellerbroek, B."]
year: 2012
venue: "Proc. SPIE 8447, 844723"
doi: "10.1117/12.926500"
url: "https://authors.library.caltech.edu/records/cfxdp-cd340"
alt_urls: ["https://github.com/lianqiw/maos", "https://lianqiw.github.io/maos/"]
access: repository
type: software
subtopic: "End-to-end simulation codes"
also_relevant_to: ["04-control-and-reconstruction"]
keywords: ["maos", "end-to-end simulation", "gpu", "tmt", "nfiraos", "mcao", "minimum variance", "simulation code"]
---

# Computer simulations and real-time control of ELT AO systems using graphical processing units

**Wang & Ellerbroek (2012)** · *Proc. SPIE 8447, 844723* · [Free full text](https://authors.library.caltech.edu/records/cfxdp-cd340) · DOI: [10.1117/12.926500](https://doi.org/10.1117/12.926500)

## Summary

The paper describes MAOS, the C-based multi-threaded adaptive optics simulator used for TMT AO studies, and its port of time-critical parts to GPUs with CUDA. A roughly tenfold speed-up per GTX 580 GPU relative to a quad-core CPU is reported, with one time step of a full end-to-end NFIRAOS MCAO simulation taking about 0.1 s on a desktop with two GPUs. The authors also show that the TMT minimum variance reconstructor can be assembled in matrix-vector-multiply form in 8 s on 8 GPUs and benchmark GPU MVM latency for real-time control. MAOS is open source (GitHub) and supports SCAO, MCAO, LTAO, MOAO and GLAO configurations.

## Keywords

`maos` · `end-to-end simulation` · `gpu` · `tmt` · `nfiraos` · `mcao` · `minimum variance` · `simulation code`
