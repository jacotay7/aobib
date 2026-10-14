---
title: "Adaptive optics control with multi-agent model-free reinforcement learning"
authors: ["Pou, B.", "Ferreira, F.", "Quiñones, E.", "Gratadour, D.", "Martin, M."]
year: 2022
venue: "Optics Express 30, 2991"
doi: "10.1364/OE.444099"
url: "https://opg.optica.org/oe/fulltext.cfm?uri=oe-30-2-2991"
alt_urls: ["https://hal.sorbonne-universite.fr/hal-03549248"]
access: open-access
type: paper
subtopic: "Reinforcement learning control"
also_relevant_to: ["04-control-and-reconstruction"]
keywords: ["reinforcement learning", "multi-agent", "model-free", "autoencoder", "shack-hartmann", "lqg control", "error budget"]
---

# Adaptive optics control with multi-agent model-free reinforcement learning

**Pou et al. (2022)** · *Optics Express 30, 2991* · [Free full text](https://opg.optica.org/oe/fulltext.cfm?uri=oe-30-2-2991) · DOI: [10.1364/OE.444099](https://doi.org/10.1364/OE.444099)

## Summary

Formulates closed-loop AO control as a multi-agent reinforcement learning problem in which the controller learns a non-linear policy without prior information on atmospheric dynamics. To address the challenges of applying RL to AO, model-free multi-agent RL is combined with an autoencoder neural network that mitigates noise, and existing error-budget analysis is extended to include an RL controller. For an 8 m telescope with a 40x40 Shack-Hartmann system, the controller significantly improves on the integrator and performs comparably to an LQG controller with perfect knowledge of the atmosphere. The error-budget analysis indicates that the RL controller partially compensates bandwidth error and helps mitigate aliasing propagation.

## Keywords

`reinforcement learning` · `multi-agent` · `model-free` · `autoencoder` · `shack-hartmann` · `lqg control` · `error budget`
