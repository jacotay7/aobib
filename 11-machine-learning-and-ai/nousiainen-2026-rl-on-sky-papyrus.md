---
title: "On-sky demonstration of reinforcement learning for adaptive optics control"
authors: ["Nousiainen, J.", "Chambouleyron, V.", "Neichel, B.", "Cetre, S.", "Sauvage, J.-F.", "Alagao, A.", "et al."]
year: 2026
venue: "A&A 711, A74"
doi: "10.1051/0004-6361/202659769"
arxiv: "2606.10771"
url: "https://arxiv.org/abs/2606.10771"
alt_urls: []
access: arXiv
type: paper
subtopic: "Reinforcement learning control"
also_relevant_to: ["04-control-and-reconstruction", "12-ao-systems-and-instruments"]
keywords: ["reinforcement learning", "po4ao", "on-sky demonstration", "papyrus", "vibration", "integrator", "turnkey control"]
---

# On-sky demonstration of reinforcement learning for adaptive optics control

**Nousiainen et al. (2026)** · *A&A 711, A74* · [Free full text](https://arxiv.org/abs/2606.10771) · DOI: [10.1051/0004-6361/202659769](https://doi.org/10.1051/0004-6361/202659769)

## Summary

Reports the first on-sky demonstration of a reinforcement-learning AO controller, PO4AO, deployed on the Papyrus AO system at the Coudé focus of the 1.52 m telescope at Observatoire de Haute-Provence. A Python implementation was interfaced with the existing DAO real-time controller through shared-memory buffers and compared with a standard integrator over several nights covering a range of flux levels and atmospheric conditions. PO4AO outperformed the integrator in all tested configurations, learned to compensate vibration patterns and was robust to measurement noise, operating with a single set of hyperparameters once tuned. These gains were obtained despite about 720 microseconds of extra latency, control jitter and occasional frame drops from the non-optimized implementation.

## Keywords

`reinforcement learning` · `po4ao` · `on-sky demonstration` · `papyrus` · `vibration` · `integrator` · `turnkey control`
