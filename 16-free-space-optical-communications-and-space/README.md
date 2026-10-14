# 16 · AO for Free-Space Optical Communications & Space Imaging

Adaptive optics is increasingly used outside astronomy to correct turbulence on optical links between the ground and space, and along horizontal paths. In a space-to-ground downlink, AO at the optical ground station corrects the received wavefront so that it can be coupled efficiently into a single-mode fiber for coherent or high-rate receivers. In a ground-to-space uplink, the transmitted beam is pre-compensated. Because the satellite moves, the uplink has to be aimed ahead of the downlink, and the resulting point-ahead anisoplanatism limits how much a downlink-derived correction helps. Proposed remedies include laser guide stars, estimators that use downlink amplitude and phase, and tomography. Low-elevation and horizontal links add strong scintillation and branch points, which break conventional wavefront sensing. The same tools apply to free-space quantum key distribution, to optical frequency transfer between atomic clocks, and to ground-based imaging and laser ranging of satellites and space debris for space situational awareness.

This folder collects reviews, channel and performance models, ground-station AO systems, uplink pre-compensation methods and experiments, and work on wavefront sensing in strong scintillation. It also covers AO for quantum links, AO for frequency-transfer links, and AO for imaging and ranging of objects in orbit. Directed-energy and weapons-oriented work is out of scope. General turbulence theory and Cn2 profiling are in [01](../01-atmospheric-turbulence/README.md), and laser guide star physics is in [06](../06-laser-guide-stars/README.md).

## Subtopics

- **Reviews & overviews**: surveys of space and free-space optical communication and turbulence mitigation
- **Turbulence effects & link channel modelling**: transmittance and fading statistics, statistics of single-mode-fiber coupling after AO, fast link simulators
- **AO for space-to-ground downlinks & optical ground stations**: OPALS, LCRD, ONERA FEELINGS, coherent receivers, control for LEO tracking
- **Uplink pre-compensation & point-ahead anisoplanatism**: GEO feeder links, point-ahead phase estimation, LGS-assisted uplinks, field and on-sky demonstrations
- **Strong scintillation & horizontal links**: plenoptic, phase-diversity and phase-retrieval sensing, mode-based coupling, control under scintillation
- **Quantum communication with AO**: satellite and terrestrial QKD with AO-assisted fiber coupling and daytime operation
- **Optical frequency transfer & scientific links**: clock-comparison links through turbulence
- **Deep-space optical communications**: JPL OCTL, AO for daytime deep-space reception, the DSOC ground receivers at Palomar and Table Mountain
- **Satellite imaging & space situational awareness**: AO imaging and laser ranging of satellites and debris, joint design of AO and deconvolution

## Start here

- [Kaushal & Kaddoum (2017): Optical communication in space, challenges and mitigation techniques](kaushal-2017-optical-communication-in-space.md): broad survey of the channel and of mitigation techniques
- [Martínez Rey (2023): Review of AO pre-compensation for ground-to-space links](martinezrey-2023-uplink-precompensation-review.md): history, challenges and outlook of uplink AO
- [Wright et al. (2015): AO correction into single-mode fiber for the OPALS LEO downlink](wright-2015-ao-smf-opals-leo-downlink.md): AO-corrected, fiber-coupled LEO downlink demonstrated on the ISS OPALS link
- [Canuet et al. (2018): Statistics of single-mode-fiber coupling with partial AO](canuet-2018-smf-coupling-statistics-ao.md): analytical model of fading after AO on downlinks
- [Osborn et al. (2021): AO pre-compensated laser uplink to LEO and GEO](osborn-2021-ao-precompensated-uplink-leo-geo.md): parameter study of uplink AO modes, including LGS
- [Conan et al. (2019): AO for GEO feeder links](conan-2019-ao-geo-feeder-links-reciprocity.md): reciprocity-based error budgets and the FEEDELIO experiment
- [Kudielka et al. (2023): First GEO feeder-link demonstration with AO pre-compensation](kudielka-2023-first-geo-feeder-link-ao-precompensation.md): on-sky uplink pre-compensation to Alphasat
- [Marulanda Acosta et al. (2024): Satellite-to-ground QKD with AO](marulandaacosta-2024-satellite-qkd-adaptive-optics.md): how AO affects secret key rates
- [Bennet et al. (2015): AO for satellite imaging and space debris ranging](bennet-2015-ao-satellite-imaging-debris-ranging.md): AO for space situational awareness at Mount Stromlo

## Related topics

- [01 · Atmospheric turbulence](../01-atmospheric-turbulence/README.md): scintillation, Cn2 profiles, isoplanatism
- [02 · Wavefront sensing](../02-wavefront-sensing/README.md)
- [04 · Control and reconstruction](../04-control-and-reconstruction/README.md): LQG and predictive control
- [06 · Laser guide stars](../06-laser-guide-stars/README.md)
- [08 · Modeling, error budgets and simulation](../08-modeling-error-budgets-and-simulation/README.md)
- [09 · PSF reconstruction and post-processing](../09-psf-reconstruction-and-post-processing/README.md): deconvolution for satellite imaging
- [12 · AO systems and instruments](../12-ao-systems-and-instruments/README.md)

<!-- INDEX:START -->
_59 entries. Generated by `tools/build_index.py`; do not edit by hand._

### AO for space-to-ground downlinks & optical ground stations

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2015 | [Adaptive optics correction into single mode fiber for a low Earth orbiting space to ground optical communication link using the OPALS downlink](wright-2015-ao-smf-opals-leo-downlink.md) | Wright et al. | [full text](https://doi.org/10.1364/OE.23.033705) |
| 2018 | [First results from the adaptive optics system from LCRD's Optical Ground Station One](roberts-2018-lcrd-ogs1-ao-first-results.md) *(proceedings)* | Roberts et al. | [full text](https://amostech.com/TechnicalPapers/2018/Adaptive-Optics_Imaging/Roberts.pdf) |
| 2020 | [Space-Ground Coherent Optical Links: Ground Receiver Performance With Adaptive Optics and Digital Phase-Locked Loop](paillier-2020-coherent-receiver-ao-dpll.md) | Paillier et al. | [full text](https://arxiv.org/abs/1911.11851) |
| 2020 | [Zonal-based high-performance control in adaptive optics systems with application to astronomy and satellite tracking](prengere-2020-zonal-lqg-satellite-tracking.md) | Prengère et al. | [full text](https://hal.science/hal-03169469) |
| 2021 | [Adaptive optics upgrades for laser communications to the ESA optical ground station](fischer-2021-esa-ogs-ao-upgrades.md) | Fischer et al. | [full text](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/11852/2599370/Adaptive-optics-upgrades-for-laser-communications-to-the-ESA-optical/10.1117/12.2599370.full) |
| 2022 | [FEELINGS: the Onera's optical ground station for Geo Feeder links demonstration](petit-2022-feelings-onera-optical-ground-station.md) *(proceedings)* | Petit et al. | [full text](https://hal.science/hal-03828251) |
| 2022 | [Demonstration of 100 Gbps coherent free-space optical communications at LEO tracking rates](walsh-2022-100gbps-coherent-fso-leo-tracking.md) | Walsh et al. | [full text](https://www.nature.com/articles/s41598-022-22027-0) |
| 2023 | [Performance of the adaptive optics system for Laser Communications Relay Demonstration’s Ground Station 1](roberts-2023-lcrd-ogs1-ao-performance.md) | Roberts et al. | [full text](https://dataverse.jpl.nasa.gov/dataset.xhtml?persistentId=doi:10.48577/jpl.TY3IBB) |
| 2023 | [Adaptive Optics for LEO-to-Ground Optical Communication: Modeling, Optimization, and Experiment](rodriguezrobles-2023-ao-leo-ground-thesis.md) *(thesis)* | Rodríguez Robles | [full text](https://theses.hal.science/tel-04746416) |
| 2025 | [Commissioning of the TeraNet Optical Ground Station Network](schediwy-2025-teranet-ogs-network.md) | Schediwy et al. | [full text](https://arxiv.org/abs/2510.25090) |
| 2025 | [LEO-to-ground low elevation optical communication: optimization of an adaptive optics design robust to scintillation](vene-2025-leo-low-elevation-ao-scintillation.md) *(proceedings)* | Vène et al. | [full text](https://arxiv.org/abs/2607.22069) |

### Deep-space optical communications

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2003 | [The JPL Optical Communications Telescope Laboratory Test Bed for the Future Optical Deep Space Network](wilson-2003-octl-test-bed-optical-deep-space-network.md) *(report)* | Wilson et al. | [full text](https://ipnpr.jpl.nasa.gov/progress_report/42-153/153G.pdf) |
| 2004 | [Adaptive Optics Communications Performance Analysis](srinivasan-2004-ao-communications-performance-analysis.md) *(report)* | Srinivasan et al. | [full text](https://ipnpr.jpl.nasa.gov/progress_report/42-158/158B.pdf) |
| 2005 | [Performance of the Optical Communication Adaptive Optics Testbed](troy-2005-optical-communication-ao-testbed.md) *(report)* | Troy et al. | [full text](https://ipnpr.jpl.nasa.gov/progress_report/42-161/161A.pdf) |
| 2019 | [Daytime adaptive optics for deep space optical communication](roberts-2019-daytime-ao-deep-space-optical-comm.md) *(proceedings)* | Roberts et al. | [full text](https://dataverse.jpl.nasa.gov/api/access/datafile/63980) |
| 2025 | [Ground laser receivers for the Deep Space Optical Communications demonstration: performance and lessons learned from first year of operations](alerstam-2025-dsoc-ground-laser-receivers.md) *(proceedings)* | Alerstam et al. | [full text](https://dataverse.jpl.nasa.gov/dataset.xhtml?persistentId=doi:10.48577/jpl.ORZETR) |

### Optical frequency transfer & scientific links

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2021 | [Point-to-point stabilized optical frequency transfer with active optics](dixmatthews-2021-optical-frequency-transfer-active-optics.md) | Dix-Matthews et al. | [full text](https://arxiv.org/abs/2007.04985) |
| 2022 | [Ultrastable Free-Space Laser Links for a Global Network of Optical Atomic Clocks](gozzard-2022-ultrastable-free-space-laser-links-clocks.md) | Gozzard et al. | [full text](https://arxiv.org/abs/2103.12909) |

### Quantum communication with AO

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2020 | [Adaptive optics benefit for quantum key distribution uplink from ground to a satellite](pugh-2020-ao-benefit-qkd-uplink.md) | Pugh et al. | [full text](https://arxiv.org/abs/1906.04193) |
| 2021 | [Adaptive-optics-enabled quantum communication: A technique for daytime space-to-Earth links](gruneisen-2021-ao-enabled-daytime-quantum-communication.md) | Gruneisen et al. | [full text](https://arxiv.org/abs/2006.07745) |
| 2023 | [Fast Adaptive Optics for High-Dimensional Quantum Communications in Turbulent Channels](scarfe-2023-fast-ao-high-dimensional-qkd.md) | Scarfe et al. | [full text](https://arxiv.org/abs/2311.13041) |
| 2024 | [Building Europe's first space-based Quantum Key Distribution system - The German Aerospace Center's role in the EAGLE-1 mission](calistrorivera-2024-eagle1-dlr-qkd-ogs.md) *(proceedings)* | Calistro-Rivera et al. | [full text](https://arxiv.org/abs/2412.03222) |
| 2024 | [Increasing the secret key rate of satellite-to-ground entanglement-based QKD assisted by adaptive optics](marulandaacosta-2024-entanglement-qkd-ao.md) | Marulanda Acosta et al. | [full text](https://arxiv.org/abs/2411.09564) |
| 2024 | [Analysis of satellite-to-ground quantum key distribution with adaptive optics](marulandaacosta-2024-satellite-qkd-adaptive-optics.md) | Marulanda Acosta et al. | [full text](https://arxiv.org/abs/2111.06747) |
| 2026 | [Intermodal quantum key distribution over an 18 km free-space channel with adaptive optics and room-temperature detectors](rossi-2026-intermodal-qkd-18km-ao.md) | Rossi et al. | [full text](https://arxiv.org/abs/2602.16680) |

### Reviews & overviews

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2014 | [Survey on free space optical communication: a communication theory perspective](khalighi-2014-fso-communication-survey.md) | Khalighi & Uysal | [full text](https://ieeexplore.ieee.org/ielx7/9739/6963743/06844864.pdf) |
| 2017 | [Optical Communication in Space: Challenges and Mitigation Techniques](kaushal-2017-optical-communication-in-space.md) *(review)* | Kaushal & Kaddoum | [full text](https://arxiv.org/abs/1705.10630) |
| 2020 | [Space Optical Links for Communication Networks](carrascocasado-2020-free-space-optical-links-space.md) *(book-chapter)* | Carrasco-Casado & Mata-Calvo | [full text](https://arxiv.org/abs/2012.13166) |
| 2023 | [Atmospheric Pre-Compensation of Ground-to-Space Communications with Adaptive Optics: Past, Present and Future - A Field Review](martinezrey-2023-uplink-precompensation-review.md) *(review)* | Martínez Rey | [full text](https://www.mdpi.com/2304-6732/10/7/858) |

### Satellite imaging & space situational awareness

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2002 | [Characterization of the AEOS Adaptive Optics System](roberts-2002-aeos-ao-characterization.md) | Roberts & Neyman | [full text](https://iopscience.iop.org/article/10.1086/343221/pdf) |
| 2015 | [Adaptive optics for satellite imaging and space debris ranging](bennet-2015-ao-satellite-imaging-debris-ranging.md) *(proceedings)* | Bennet et al. | [full text](https://amostech.com/TechnicalPapers/2015/Adaptive_Optics_Imaging/Bennet.pdf) |
| 2015 | [Resolved observations of geostationary satellites from the 6.5 m MMT](hart-2015-geo-satellites-mmt-ao.md) *(proceedings)* | Hart et al. | [full text](https://amostech.com/TechnicalPapers/2015/Adaptive_Optics_Imaging/Hart.pdf) |
| 2018 | [Extending Daytime Adaptive Optics to Faint Objects](hart-2018-daytime-ao-faint-objects.md) *(proceedings)* | Hart | [full text](https://amostech.com/TechnicalPapers/2018/Adaptive-Optics_Imaging/Hart.pdf) |
| 2020 | [LEO satellite imaging with adaptive optics and marginalized blind deconvolution](petit-2020-leo-satellite-imaging-ao-blind-deconvolution.md) *(proceedings)* | Petit et al. | [full text](https://hal.science/hal-03051923) |
| 2026 | [Joint optical-digital design strategy for adaptive optics systems: application to wavelength selection for satellite imaging](cheyssial-2026-joint-optical-digital-design-satellite-imaging.md) | Cheyssial et al. | [full text](https://doi.org/10.1364/OE.581902) |

### Strong scintillation & horizontal links

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2023 | [Tbit/s line-rate satellite feeder links enabled by coherent modulation and full-adaptive optics](horst-2023-tbit-feeder-link-full-ao.md) | Horst et al. | [full text](https://www.nature.com/articles/s41377-023-01201-7) |
| 2024 | [Single-Shot Phase Diversity Wavefront Sensing in Deep Turbulence via Metasurface Optics](jimenez-2024-metasurface-phase-diversity-deep-turbulence.md) | Jimenez et al. | [full text](https://arxiv.org/abs/2410.18789) |
| 2025 | [High-Performance Adaptive Optics Control in Strong Turbulence Scenarios for Free Space Optical Communications](torres-2025-ao-control-strong-turbulence-fso-thesis.md) *(thesis)* | Torres | [full text](https://theses.hal.science/tel-05634004) |
| 2025 | [A Framework for Iterative Phase Retrieval Technique Integration into Atmospheric Adaptive Optics—Part II: High Resolution Wavefront Control in Strong Scintillations](vorontsov-2025-iterative-phase-retrieval-strong-scintillation.md) | Vorontsov & Polnau | [full text](https://doi.org/10.3390/photonics12030185) |

### Turbulence effects & link channel modelling

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2016 | [Atmospheric Quantum Channels with Weak and Strong Turbulence](vasylyev-2016-atmospheric-quantum-channels-turbulence.md) | Vasylyev et al. | [full text](https://arxiv.org/abs/1604.01373) |
| 2018 | [Statistical properties of single-mode fiber coupling of satellite-to-ground laser links partially corrected by adaptive optics](canuet-2018-smf-coupling-statistics-ao.md) | Canuet et al. | [full text](https://hal.science/hal-01904583) |
| 2018 | [Performance analysis of an adaptive optics system for free-space optics communication through atmospheric turbulence](wang-2018-ao-performance-fso-communication.md) | Wang et al. | [full text](https://doi.org/10.1038/s41598-018-19559-9) |
| 2019 | [Satellite-based links for Quantum Key Distribution: beam effects and weather dependence](liorni-2019-satellite-qkd-beam-effects-weather.md) | Liorni et al. | [full text](https://arxiv.org/abs/1906.08115) |
| 2019 | [Performance analysis of 349-element adaptive optics unit for a coherent free space optical communication system](yang-2019-349-element-ao-coherent-fso.md) | Yang et al. | [full text](https://www.nature.com/articles/s41598-019-48338-3) |
| 2022 | [FAST: Fourier domain adaptive optics simulation tool for bidirectional ground-space optical links through atmospheric turbulence](farley-2022-fast-fourier-ao-simulation-links.md) | Farley et al. | [full text](https://doi.org/10.1364/OE.458659) |
| 2022 | [Application of AdamSPGD algorithm to sensor-less adaptive optics in coherent free-space optical communication system](zhang-2022-adamspgd-sensorless-ao-coherent-fso.md) | Zhang et al. | [full text](https://doi.org/10.1364/OE.451350) |
| 2023 | [Assessment of adaptive optics-corrected optical links statistics from integrated turbulence parameters through a Gaussian process metamodel](klotz-2023-ao-link-statistics-gaussian-process.md) | Klotz et al. | [full text](https://doi.org/10.1002/sat.1497) |

### Uplink pre-compensation & point-ahead anisoplanatism

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2019 | [Validation of pre-compensation under point-ahead-angle in a 1 km free-space propagation experiment](brady-2019-precompensation-point-ahead-1km.md) | Brady et al. | [full text](https://doi.org/10.1364/OE.27.017840) |
| 2019 | [Adaptive Optics for GEO-Feeder Links: from Performance Analysis via Reciprocity Based Models to Experimental Demonstration](conan-2019-ao-geo-feeder-links-reciprocity.md) *(proceedings)* | Conan et al. | [full text](https://hal.science/hal-03206080) |
| 2020 | [Uplink wavefront corrector system: from paper to reality](martinezrey-2020-uplink-wavefront-corrector-system.md) | Martínez Rey et al. | [full text](https://doi.org/10.1364/OE.28.005886) |
| 2021 | [Adaptive Optics pre-compensated laser uplink to LEO and GEO](osborn-2021-ao-precompensated-uplink-leo-geo.md) | Osborn et al. | [full text](https://doi.org/10.1364/OE.413013) |
| 2022 | [Feasibility demonstration of AO pre-compensation for GEO feeder links in a relevant environment](montmerlebonnefois-2022-ao-precompensation-geo-feeder-demo.md) | Montmerle Bonnefois et al. | [full text](https://doi.org/10.1364/OE.470705) |
| 2023 | [Successful first optical feeder link demonstration between a ground station and a GEO satellite applying adaptive optics pre-compensation ("Alpha-Up")](kudielka-2023-first-geo-feeder-link-ao-precompensation.md) *(proceedings)* | Kudielka et al. | [full text](https://hal.science/hal-04605018) |
| 2023 | [Optimization of High Data Rate Ground to Satellite Links Pre-compensated by Adaptive Optics](lognone-2023-ground-geo-precompensation-thesis.md) *(thesis)* | Lognoné | [full text](https://theses.hal.science/tel-04465340) |
| 2023 | [Phase estimation at the point-ahead angle for AO pre-compensated ground to GEO satellite telecoms](lognone-2023-phase-estimation-point-ahead-geo.md) | Lognoné et al. | [full text](https://doi.org/10.1364/OE.476328) |
| 2024 | [Pre-distortion adaptive optics for optical feeder links: simulations and performance analyses](hristovski-2024-predistortion-ao-feeder-links.md) | Hristovski et al. | [full text](https://doi.org/10.1364/OE.521494) |
| 2024 | [Tip tilt and focus estimation based on LGS and downlink joint measurements for ground to GEO satellite optical communication link](lognone-2024-tip-tilt-focus-lgs-downlink-geo.md) | Lognoné et al. | [full text](https://doi.org/10.1364/OE.538333) |
| 2024 | [GEOStar: demonstration of laser guide star adaptive optics for free space optical communications](reeves-2024-geostar-lgs-ao-fso.md) *(proceedings)* | Reeves et al. | [full text](https://elib.dlr.de/220215/1/128771S-1.pdf) |
| 2025 | [Uplink Pre-Compensation for Ground-to-Space Optical Communications Using Downlink Tomographic Reconstruction](frost-2025-uplink-precompensation-downlink-tomography.md) | Frost et al. | [full text](https://arxiv.org/abs/2509.08866) |

### Cross-listed from other topics

| Year | Entry | Authors | Home topic |
|---|---|---|---|
| 1971 | [The Effects of the Turbulent Atmosphere on Wave Propagation](../01-atmospheric-turbulence/tatarskii-1971-turbulent-atmosphere-wave-propagation.md) | Tatarskii | [01-atmospheric-turbulence](../01-atmospheric-turbulence/README.md) |
| 1998 | [Stochastic parallel-gradient-descent technique for high-resolution wave-front phase-distortion correction](../15-microscopy-and-biological-imaging/vorontsov-1998-stochastic-parallel-gradient-descent.md) | Vorontsov & Sivokon | [15-microscopy-and-biological-imaging](../15-microscopy-and-biological-imaging/README.md) |
| 2014 | [Adaptive optics in the formation of optical beams and images](../00-reviews-and-training/lukin-2014-adaptive-optics-formation-beams-images.md) | Lukin | [00-reviews-and-training](../00-reviews-and-training/README.md) |
| 2015 | [From Dye Laser Factory to Portable Semiconductor Laser: Four Generations of Sodium Guide Star Lasers for Adaptive Optics in Astronomy and Space Situational Awareness](../06-laser-guide-stars/dorgeville-2015-four-generations-sodium-lasers.md) | d'Orgeville & Fetzer | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2018 | [Turbulence correction with artificial neural networks](../11-machine-learning-and-ai/lohani-2018-turbulence-correction-ann.md) | Lohani & Glasser | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2020 | [Simulating Anisoplanatic Turbulence by Sampling Inter-modal and Spatially Correlated Zernike Coefficients](../01-atmospheric-turbulence/chimitt-2020-anisoplanatic-zernike-sampling.md) | Chimitt & Chan | [01-atmospheric-turbulence](../01-atmospheric-turbulence/README.md) |
| 2021 | [Feature issue introduction: applications of adaptive optics](../00-reviews-and-training/christou-2021-feature-issue-applications-adaptive-optics.md) | Christou et al. | [00-reviews-and-training](../00-reviews-and-training/README.md) |
| 2023 | [Demonstrating 24-hour continuous vertical monitoring of atmospheric optical turbulence](../01-atmospheric-turbulence/griffiths-2023-24h-shimm-continuous-monitoring.md) | Griffiths et al. | [01-atmospheric-turbulence](../01-atmospheric-turbulence/README.md) |
| 2023 | [Availability assessment of AO corrected optical links by machine learning](../11-machine-learning-and-ai/klotz-2023-thesis-ml-optical-link-availability.md) | Klotz | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2023 | [Marginalized myopic deconvolution of adaptive optics corrected images using MCMC methods](../09-psf-reconstruction-and-post-processing/yan-2023-marginalized-myopic-deconvolution-mcmc.md) | Yan et al. | [09-psf-reconstruction-and-post-processing](../09-psf-reconstruction-and-post-processing/README.md) |
| 2024 | [Phasing segmented telescopes via deep learning methods: application to a deployable CubeSat](../17-segmented-apertures-and-phasing/dumont-2024-deep-learning-phasing-cubesat.md) | Dumont et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2025 | [Accurate Zernike-corrected phase screens for arbitrary power spectra](../01-atmospheric-turbulence/bachmann-2025-zernike-corrected-phase-screens.md) | Bachmann et al. | [01-atmospheric-turbulence](../01-atmospheric-turbulence/README.md) |
| 2025 | [Optical turbulence forecast for ground-based astronomy and free-space optical communication](../01-atmospheric-turbulence/masciadri-2025-turbulence-forecast-astronomy-fso.md) | Masciadri et al. | [01-atmospheric-turbulence](../01-atmospheric-turbulence/README.md) |
| 2026 | [Tip-tilt retrieval using trilateration of a sodium laser guide star](../06-laser-guide-stars/barrett-2026-lgs-tip-tilt-trilateration.md) | Barrett et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2026 | [Short-Term Turbulence Prediction for Seeing Using Machine Learning](../11-machine-learning-and-ai/medlej-2026-short-term-seeing-prediction-ml.md) | Medlej et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2026 | [Performance comparison of the nonlinear curvature and Shack-Hartmann wavefront sensors in strong turbulence](../02-wavefront-sensing/potier-2026-nlcwfs-vs-shack-hartmann-strong-turbulence.md) | Potier et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |

<!-- INDEX:END -->
