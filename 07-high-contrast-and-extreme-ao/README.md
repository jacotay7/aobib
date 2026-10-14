# 07 · High-Contrast Imaging & Extreme AO

High-contrast imaging aims to detect and characterize faint companions (exoplanets, brown dwarfs) and circumstellar disks a few tenths of an arcsecond from stars that are 1e4 to 1e10 times brighter. On the ground this requires extreme adaptive optics (ExAO): systems with thousands of actuators, kHz loop rates and very low residual wavefront error, feeding a coronagraph. In practice the achievable contrast is set less by the coronagraph than by residual starlight speckles. These come from AO temporal and aliasing errors (the wind-driven halo), from non-common path aberrations (NCPA) between the wavefront sensor and the science camera, from telescope effects such as the low-wind / island effect, and from slow instrumental drifts. They are fought with focal-plane wavefront sensing and dark-hole control, with dedicated low-order and Zernike-type NCPA sensors, and with differential observing and post-processing strategies.

This folder collects the foundational analyses of ExAO contrast limits and speckle statistics. It also covers the reference papers for current ExAO instruments (GPI, SPHERE/SAXO and SAXO+, SCExAO, MagAO-X, PALM-3000, KPIC, ELT/PCS), focal-plane wavefront sensing and control (speckle nulling, EFC/pair-wise probing, self-coherent camera, Fast & Furious, linear dark field control, iEFC), and NCPA and low-order sensing (ZELDA, COFFEE, LLOWFS, QACITS). Further sections cover the low-wind effect and wind-driven halo, post-processing and detection statistics (ADI, SDI, LOCI, KLIP, RDI, PACO, PynPoint, VIP), and wavefront control for space coronagraphs and their testbeds (dark-hole algorithms, Roman CGI, HiCAT, HWO). Coronagraph mask design and exoplanet science results are covered only where they bear directly on the AO and wavefront-control problem.

## Subtopics

- **Reviews & tutorials**: broad reviews of high-contrast imaging and the 2018 Optimal Optical Coronagraph workshop reviews
- **ExAO fundamentals & contrast limits**: analytic limits of AO-fed coronagraphy, error budgets, coronagraph–AO interplay
- **ExAO systems & instruments**: GPI/GPI 2.0, SPHERE/SAXO/SAXO+, SCExAO, MagAO-X, PALM-3000, KPIC, ELT/PCS
- **Speckle physics & statistics**: speckle noise, pinned speckles, speckle intensity statistics and lifetimes
- **Focal-plane wavefront sensing & dark-hole control**: speckle nulling, EFC and pair-wise probing, self-coherent camera, Fast & Furious, LDFC, iEFC, on-sky dark holes
- **NCPA & low-order wavefront sensing**: ZELDA, COFFEE, LLOWFS, QACITS, NCPA stability, NCPA behind pyramid second stages
- **Low-wind effect & wind-driven halo**: island/low-wind effect diagnosis and correction, wind-driven halo origin and impact
- **Post-processing & detection statistics**: ADI, SDI, LOCI, KLIP and forward modeling, RDI, PACO, software packages, small-sample statistics, data challenges
- **Space coronagraph wavefront control & testbeds**: dark-hole concept, stroke minimization, dark-hole maintenance, Roman CGI, HiCAT, HWO laboratory status

## Start here

- [Follette (2023): An Introduction to High Contrast Differential Imaging of Exoplanets and Disks](follette-2023-intro-high-contrast-differential-imaging.md): tutorial on terminology, observing and data reduction
- [Guyon (2005): Limits of Adaptive Optics for High-Contrast Imaging](guyon-2005-limits-ao-high-contrast.md): the fundamental ExAO contrast error terms
- [Soummer et al. (2007): Speckle Noise and Dynamic Range in Coronagraphic Images](soummer-2007-speckle-noise-coronagraphic-images.md): statistical model of the speckles that limit contrast
- [Beuzit et al. (2019): SPHERE](beuzit-2019-sphere-exoplanet-imager.md) and [Macintosh et al. (2014): GPI first light](macintosh-2014-gpi-first-light.md): the two reference second-generation ExAO instruments
- [Jovanovic et al. (2018): Review II, common-path wavefront sensing/control and coherent differential imaging](jovanovic-2018-review-hci-wavefront-control-cdi.md): overview of focal-plane techniques
- [Groff et al. (2016): Methods and limitations of focal plane sensing, estimation, and control](groff-2016-focal-plane-sensing-estimation-control.md): dark-hole estimation and control explained
- [Marois et al. (2006): Angular Differential Imaging](marois-2006-angular-differential-imaging.md): the observing strategy behind most ground-based post-processing

## Related topics

- [00 · Reviews & Training](../00-reviews-and-training/README.md)
- [02 · Wavefront Sensing](../02-wavefront-sensing/README.md): pyramid, Zernike and focal-plane sensors used in ExAO
- [03 · Deformable Mirrors & Correctors](../03-deformable-mirrors-and-correctors/README.md): high-actuator-count and MEMS DMs
- [04 · Control & Reconstruction](../04-control-and-reconstruction/README.md): predictive control, vibration mitigation, fast reconstructors
- [08 · Modeling, Error Budgets & Simulation](../08-modeling-error-budgets-and-simulation/README.md): HCIPy, PROPER, POPPY, contrast error budgets
- [09 · PSF Reconstruction & Post-processing](../09-psf-reconstruction-and-post-processing/README.md)
- [10 · Calibration & System Identification](../10-calibration-and-system-identification/README.md): NCPA calibration outside high contrast
- [11 · Machine Learning & AI](../11-machine-learning-and-ai/README.md): learned focal-plane sensing and control for ExAO
- [12 · AO Systems & Instruments](../12-ao-systems-and-instruments/README.md)
- [17 · Segmented Apertures & Phasing](../17-segmented-apertures-and-phasing/README.md): island effect and segmented-aperture coronagraphy

<!-- INDEX:START -->
_80 entries. Generated by `tools/build_index.py`; do not edit by hand._

### ExAO fundamentals & contrast limits

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2001 | [Ground-based Coronagraphy with High-Order Adaptive Optics](sivaramakrishnan-2001-ground-coronagraphy-high-order-ao.md) | Sivaramakrishnan et al. | [full text](https://arxiv.org/abs/astro-ph/0103012) |
| 2004 | [Spatially filtered wave-front sensor for high-order adaptive optics](poyneer-2004-spatially-filtered-wavefront-sensor.md) | Poyneer & Macintosh | [full text](https://exaoc.ucolick.org/documents/Papers/XAOPI%20papers/poyneer_sfwfs.pdf) |
| 2005 | [Limits of Adaptive Optics for High-Contrast Imaging](guyon-2005-limits-ao-high-contrast.md) | Guyon | [full text](https://arxiv.org/abs/astro-ph/0505086) |
| 2006 | [Fundamental limitations on Earth-like planet detection with extremely large telescopes](cavarroc-2006-limitations-earth-like-planets-elt.md) | Cavarroc et al. | [full text](https://arxiv.org/abs/astro-ph/0509713) |
| 2006 | [High-order adaptive optics requirements for direct detection of extrasolar planets: Application to the SPHERE instrument](fusco-2006-high-order-ao-requirements-sphere.md) | Fusco et al. | [full text](https://opg.optica.org/oe/fulltext.cfm?uri=oe-14-17-7515) |
| 2006 | [Theoretical Limits on Extrasolar Terrestrial Planet Detection with Coronagraphs](guyon-2006-theoretical-limits-coronagraphs.md) | Guyon et al. | [full text](https://arxiv.org/abs/astro-ph/0608506) |
| 2018 | [Ground-based adaptive optics coronagraphic performance under closed-loop predictive control](males-2018-predictive-control-coronagraph-contrast.md) | Males & Guyon | [full text](https://arxiv.org/abs/1712.07189) |

### ExAO systems & instruments

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2008 | [The Gemini Planet Imager: from science to design to construction](macintosh-2008-gpi-science-to-construction.md) | Macintosh et al. | [full text](https://www.osti.gov/servlets/purl/945746) |
| 2013 | [PALM-3000: Exoplanet Adaptive Optics for the 5 m Hale Telescope](dekany-2013-palm-3000.md) | Dekany et al. | [full text](https://arxiv.org/abs/1309.1216) |
| 2014 | [First light of the Gemini Planet Imager](macintosh-2014-gpi-first-light.md) | Macintosh et al. | [full text](https://arxiv.org/abs/1403.7520) |
| 2015 | [The Subaru Coronagraphic Extreme Adaptive Optics System: Enabling High-Contrast Imaging on Solar-System Scales](jovanovic-2015-scexao.md) | Jovanovic et al. | [full text](https://arxiv.org/abs/1507.00017) |
| 2016 | [Status and performance of the Gemini Planet Imager adaptive optics system](bailey-2016-gpi-ao-status-performance.md) | Bailey et al. | [full text](https://arxiv.org/abs/1609.08689) |
| 2016 | [Performance of the Gemini Planet Imager's adaptive optics system](poyneer-2016-gpi-ao-performance.md) | Poyneer et al. | [full text](https://www.osti.gov/biblio/1240924) |
| 2016 | [SAXO: the extreme adaptive optics system of SPHERE (I) system overview and global laboratory performance](sauvage-2016-saxo-system-overview.md) | Sauvage et al. | [full text](https://authors.library.caltech.edu/records/4fxff-axc63) |
| 2018 | [Upgrading the Gemini Planet Imager: GPI 2.0](chilcote-2018-gpi-2-upgrade.md) | Chilcote et al. | [full text](https://arxiv.org/abs/1807.07145) |
| 2018 | [MagAO-X: project status and first laboratory results](males-2018-magao-x-status.md) | Males et al. | [full text](https://arxiv.org/abs/1807.04315) |
| 2019 | [SPHERE: the exoplanet imager for the Very Large Telescope](beuzit-2019-sphere-exoplanet-imager.md) | Beuzit et al. | [full text](https://arxiv.org/abs/1902.04080) |
| 2020 | [SPHERE+: Imaging young Jupiters down to the snowline](boccaletti-2020-sphere-plus.md) *(report)* | Boccaletti et al. | [full text](https://arxiv.org/abs/2003.05714) |
| 2021 | [PCS - A Roadmap for Exoearth Imaging with the ELT](kasper-2021-pcs-roadmap-elt.md) | Kasper et al. | [full text](https://arxiv.org/abs/2103.11196) |
| 2024 | [Numerical simulations for the SAXO+ upgrade: Performance analysis of the adaptive optics system](goulas-2024-saxo-plus-simulations.md) | Goulas et al. | [full text](https://arxiv.org/abs/2406.17644) |
| 2025 | [Technical description and performance of the phase II version of the Keck Planet Imager and Characterizer](jovanovic-2025-kpic-phase-ii.md) | Jovanovic et al. | [full text](https://arxiv.org/abs/2502.01863) |

### Focal-plane wavefront sensing & dark-hole control

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2006 | [High-Contrast Imaging from Space: Speckle Nulling in a Low-Aberration Regime](borde-2006-speckle-nulling-low-aberration.md) | Bordé & Traub | [full text](https://arxiv.org/abs/astro-ph/0510597) |
| 2010 | [Self-coherent camera as a focal plane wavefront sensor: simulations](galicher-2010-self-coherent-camera-simulations.md) | Galicher et al. | [full text](https://arxiv.org/abs/0911.2465) |
| 2013 | [Focal Plane Wavefront Sensing using Residual Adaptive Optics Speckles](codona-2013-focal-plane-wfs-residual-ao-speckles.md) | Codona & Kenworthy | [full text](https://arxiv.org/abs/1303.0527) |
| 2013 | [Estimation and correction of wavefront aberrations using the self-coherent camera: laboratory results](mazoyer-2013-scc-laboratory.md) | Mazoyer et al. | [full text](https://arxiv.org/abs/1306.5561) |
| 2014 | [On-Sky Speckle Nulling Demonstration at Small Angular Separation with SCExAO](martinache-2014-on-sky-speckle-nulling-scexao.md) | Martinache et al. | [full text](https://arxiv.org/abs/1405.0824) |
| 2016 | [Methods and limitations of focal plane sensing, estimation, and control in high-contrast imaging](groff-2016-focal-plane-sensing-estimation-control.md) *(review)* | Groff et al. | [full text](https://doi.org/10.1117/1.JATIS.2.1.011009) |
| 2017 | [Spatial linear dark field control: stabilizing deep contrast for exoplanet imaging using bright speckles](miller-2017-spatial-linear-dark-field-control.md) | Miller et al. | [full text](https://arxiv.org/abs/1703.04259) |
| 2019 | [Minimization of non-common path aberrations at the Palomar telescope using a self-coherent camera](galicher-2019-scc-palomar-ncpa.md) | Galicher et al. | [full text](https://arxiv.org/abs/1909.09130) |
| 2020 | [Comparing focal plane wavefront control techniques: Numerical simulations and laboratory experiments](potier-2020-comparing-focal-plane-wavefront-control.md) | Potier et al. | [full text](https://arxiv.org/abs/2003.04336) |
| 2021 | [First on-sky demonstration of spatial Linear Dark Field Control with the vector-Apodizing Phase Plate at Subaru/SCExAO](bos-2021-ldfc-on-sky-scexao.md) | Bos et al. | [full text](https://arxiv.org/abs/2106.06286) |
| 2022 | [Increasing the raw contrast of VLT/SPHERE with the dark-hole technique. II. On-sky wavefront correction and coherent differential imaging](potier-2022-sphere-dark-hole-on-sky.md) | Potier et al. | [full text](https://arxiv.org/abs/2208.11244) |
| 2023 | [On-sky speckle nulling through a single-mode fiber with the Keck Planet Imager and Characterizer](xin-2023-kpic-speckle-nulling-fiber.md) | Xin et al. | [full text](https://arxiv.org/abs/2307.11893) |
| 2026 | [On-sky dark hole diggin' with implicit Electric Field Conjugation on MagAO-X](haffert-2026-iefc-on-sky-magao-x.md) | Haffert et al. | [full text](https://arxiv.org/abs/2607.08146) |

### Low-wind effect & wind-driven halo

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2018 | [Origin of the asymmetry of the wind driven halo observed in high-contrast images](cantalloube-2018-wind-driven-halo-asymmetry.md) | Cantalloube et al. | [full text](https://arxiv.org/abs/1810.13171) |
| 2018 | [Low wind effect on VLT/SPHERE: impact, mitigation strategy, and results](milli-2018-low-wind-effect-sphere.md) | Milli et al. | [full text](https://arxiv.org/abs/1806.05370) |
| 2018 | [Calibration of the island effect: Experimental validation of closed-loop focal plane wavefront control on Subaru/SCExAO](ndiaye-2018-island-effect-calibration-scexao.md) | N'Diaye et al. | [full text](https://arxiv.org/abs/1712.03963) |
| 2019 | [Overview of focal plane wavefront sensors to correct for the Low Wind Effect on SUBARU/SCExAO](vievard-2019-focal-plane-wfs-low-wind-effect.md) *(proceedings)* | Vievard et al. | [full text](https://arxiv.org/abs/1912.10179) |
| 2020 | [On-sky verification of Fast and Furious focal-plane wavefront sensing: Moving forward toward controlling the island effect at Subaru/SCExAO](bos-2020-fast-and-furious-scexao-island-effect.md) | Bos et al. | [full text](https://arxiv.org/abs/2005.12097) |
| 2020 | [Wind-driven halo in high-contrast images. I. Analysis of the focal-plane images of SPHERE](cantalloube-2020-wind-driven-halo-sphere.md) | Cantalloube et al. | [full text](https://arxiv.org/abs/2003.05794) |

### NCPA & low-order wavefront sensing

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2013 | [Calibration of quasi-static aberrations in exoplanet direct-imaging instruments with a Zernike phase-mask sensor](ndiaye-2013-zelda-zernike-ncpa.md) | N'Diaye et al. | [full text](https://arxiv.org/abs/1305.5143) |
| 2013 | [High-order myopic coronagraphic phase diversity (COFFEE) for wave-front control in high-contrast imaging systems](paul-2013-coffee-high-order.md) | Paul et al. | [full text](https://arxiv.org/abs/1310.5459) |
| 2014 | [Lyot-based Low Order Wavefront Sensor for Phase-mask Coronagraphs: Principle, Simulations and Laboratory Experiments](singh-2014-lyot-low-order-wfs.md) | Singh et al. | [full text](https://arxiv.org/abs/1404.7201) |
| 2015 | [Post-coronagraphic tip-tilt sensing for vortex phase masks: The QACITS technique](huby-2015-qacits-tip-tilt-vortex.md) | Huby et al. | [full text](https://arxiv.org/abs/1509.06158) |
| 2019 | [Calibration of quasi-static aberrations in exoplanet direct-imaging instruments with a Zernike phase-mask sensor. III. On-sky validation in VLT/SPHERE](vigan-2019-zelda-on-sky-sphere.md) | Vigan et al. | [full text](https://arxiv.org/abs/1907.11241) |
| 2022 | [Calibration of quasi-static aberrations in exoplanet direct-imaging instruments with a Zernike phase-mask sensor. IV. Temporal stability of non-common path aberrations in VLT/SPHERE](vigan-2022-zelda-ncpa-temporal-stability.md) | Vigan et al. | [full text](https://arxiv.org/abs/2202.10470) |
| 2026 | [Non-common path aberration compensation and a dark hole loop with a pyramid adaptive optics system: Application to SAXO+](goulas-2026-saxo-plus-ncpa-dark-hole-pyramid.md) | Goulas et al. | [full text](https://arxiv.org/abs/2603.08508) |

### Post-processing & detection statistics

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2000 | [Efficient Speckle Noise Attenuation in Faint Companion Imaging](marois-2000-speckle-attenuation-sdi.md) | Marois et al. | [full text](https://iopscience.iop.org/article/10.1086/316492) |
| 2002 | [Imaging Spectroscopy for Extrasolar Planet Detection](sparks-2002-spectral-deconvolution.md) | Sparks & Ford | [full text](https://arxiv.org/abs/astro-ph/0209078) |
| 2006 | [Angular Differential Imaging: A Powerful High-Contrast Imaging Technique](marois-2006-angular-differential-imaging.md) | Marois et al. | [full text](https://arxiv.org/abs/astro-ph/0512335) |
| 2007 | [A New Algorithm for Point-Spread Function Subtraction in High-Contrast Imaging: A Demonstration with Angular Differential Imaging](lafreniere-2007-loci.md) | Lafrenière et al. | [full text](https://arxiv.org/abs/astro-ph/0702697) |
| 2012 | [PynPoint: an image processing package for finding exoplanets](amara-2012-pynpoint.md) | Amara & Quanz | [full text](https://arxiv.org/abs/1207.6637) |
| 2012 | [Detection and Characterization of Exoplanets and Disks Using Projections on Karhunen-Loève Eigenimages](soummer-2012-klip.md) | Soummer et al. | [full text](https://arxiv.org/abs/1207.4197) |
| 2014 | [Fundamental Limitations of High Contrast Imaging Set by Small Sample Statistics](mawet-2014-small-sample-statistics.md) | Mawet et al. | [full text](https://arxiv.org/abs/1407.2247) |
| 2016 | [Detection and Characterization of Exoplanets using Projections on Karhunen-Loève Eigenimages: Forward Modeling](pueyo-2016-klip-forward-modeling.md) | Pueyo | [full text](https://arxiv.org/abs/1604.06097) |
| 2017 | [VIP: Vortex Image Processing Package for High-contrast Direct Imaging](gomezgonzalez-2017-vip.md) | Gomez Gonzalez et al. | [full text](https://arxiv.org/abs/1705.06184) |
| 2018 | [Exoplanet detection in angular differential imaging by statistical learning of the nonstationary patch covariances](flasseur-2018-paco.md) | Flasseur et al. | [full text](https://www.aanda.org/articles/aa/full_html/2018/10/aa32745-18/aa32745-18.html) |
| 2019 | [Reference Star Differential Imaging of Close-in Companions and Circumstellar Disks with the NIRC2 Vortex Coronagraph at the W. M. Keck Observatory](ruane-2019-reference-star-differential-imaging-nirc2.md) | Ruane et al. | [full text](https://arxiv.org/abs/1901.04090) |
| 2020 | [Exoplanet imaging data challenge: benchmarking the various image processing methods for exoplanet detection](cantalloube-2020-exoplanet-imaging-data-challenge.md) | Cantalloube et al. | [full text](https://arxiv.org/abs/2101.05080) |

### Reviews & tutorials

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2009 | [High-Contrast Observations in Optical and Infrared Astronomy](oppenheimer-2009-high-contrast-observations.md) *(review)* | Oppenheimer & Hinkley | [full text](https://arxiv.org/abs/0903.4466) |
| 2012 | [Review of small-angle coronagraphic techniques in the wake of ground-based second-generation adaptive optics systems](mawet-2012-review-small-angle-coronagraphy.md) *(review)* | Mawet et al. | [full text](https://arxiv.org/abs/1207.5481) |
| 2016 | [Imaging Extrasolar Giant Planets](bowler-2016-imaging-extrasolar-giant-planets.md) *(review)* | Bowler | [full text](https://arxiv.org/abs/1605.02731) |
| 2018 | [Extreme Adaptive Optics](guyon-2018-extreme-adaptive-optics-review.md) *(review)* | Guyon | [full text](https://www.annualreviews.org/doi/pdf/10.1146/annurev-astro-081817-052000) |
| 2018 | [Review of high-contrast imaging systems for current and future ground-based and space-based telescopes II. Common path wavefront sensing/control and coherent differential imaging](jovanovic-2018-review-hci-wavefront-control-cdi.md) *(review)* | Jovanovic et al. | [full text](https://arxiv.org/abs/1807.07043) |
| 2018 | [Review of high-contrast imaging systems for current and future ground- and space-based telescopes I. Coronagraph design methods and optical performance metrics](ruane-2018-review-hci-systems-coronagraph-design.md) *(review)* | Ruane et al. | [full text](https://arxiv.org/abs/1807.07042) |
| 2023 | [Direct Imaging and Spectroscopy of Extrasolar Planets](currie-2023-direct-imaging-spectroscopy-review.md) *(review)* | Currie et al. | [full text](https://arxiv.org/abs/2205.05696) |
| 2023 | [An Introduction to High Contrast Differential Imaging of Exoplanets and Disks](follette-2023-intro-high-contrast-differential-imaging.md) *(tutorial)* | Follette | [full text](https://arxiv.org/abs/2308.01354) |

### Space coronagraph wavefront control & testbeds

| Year | Entry | Authors | Link |
|---|---|---|---|
| 1995 | [High-Dynamic-Range Imaging Using a Deformable Mirror for Space Coronography](malbet-1995-dark-hole-deformable-mirror.md) | Malbet et al. | [full text](https://arxiv.org/abs/astro-ph/9502042) |
| 2009 | [Optimal dark hole generation via two deformable mirrors with stroke minimization](pueyo-2009-two-dm-stroke-minimization.md) | Pueyo et al. | [full text](https://arxiv.org/abs/1111.5111) |
| 2019 | [Dark Hole Maintenance and A Posteriori Intensity Estimation in the Presence of Speckle Drift in a High-contrast Space Coronagraph](pogorelyuk-2019-dark-hole-maintenance-speckle-drift.md) | Pogorelyuk & Kasdin | [full text](https://arxiv.org/abs/1902.01880) |
| 2022 | [High-contrast imager for complex aperture telescopes (HiCAT): 8. Dark zone demonstration with simultaneous closed-loop low-order wavefront sensing and control](soummer-2022-hicat-dark-zone-low-order-wfsc.md) | Soummer et al. | [full text](https://arxiv.org/abs/2409.13026) |
| 2024 | [Current laboratory performance of starlight suppression systems, and potential pathways to desired Habitable Worlds Observatory exoplanet science capabilities](mennesson-2024-lab-starlight-suppression-hwo.md) | Mennesson et al. | [full text](https://arxiv.org/abs/2404.18036) |
| 2025 | [High-order wavefront sensing and control for the Roman Coronagraph Instrument (CGI): architecture and measured performance](cady-2025-roman-cgi-howfsc.md) | Cady et al. | [full text](https://arxiv.org/abs/2507.23738) |

### Speckle physics & statistics

| Year | Entry | Authors | Link |
|---|---|---|---|
| 1999 | [Speckle Noise and the Detection of Faint Companions](racine-1999-speckle-noise-faint-companions.md) | Racine et al. | [full text](https://iopscience.iop.org/article/10.1086/316367) |
| 2003 | [The Structure of High Strehl Ratio Point-Spread Functions](perrin-2003-high-strehl-psf-structure.md) | Perrin et al. | [full text](https://arxiv.org/abs/astro-ph/0306468) |
| 2005 | [Speckle lifetimes in high-contrast adaptive optics](macintosh-2005-speckle-lifetimes-high-contrast.md) | Macintosh et al. | [full text](https://www.osti.gov/servlets/purl/875947) |
| 2006 | [Speckle Statistics in Adaptively Corrected Images](fitzgerald-2006-speckle-statistics-ao-images.md) | Fitzgerald & Graham | [full text](https://arxiv.org/abs/astro-ph/0510503) |
| 2007 | [Temporal Evolution of Coronagraphic Dynamic Range and Constraints on Companions to Vega](hinkley-2007-temporal-evolution-coronagraphic-dynamic-range.md) | Hinkley et al. | [full text](https://arxiv.org/abs/astro-ph/0609337) |
| 2007 | [Speckle Noise and Dynamic Range in Coronagraphic Images](soummer-2007-speckle-noise-coronagraphic-images.md) | Soummer et al. | [full text](https://arxiv.org/abs/0706.1739) |
| 2013 | [Speckle temporal stability in XAO coronagraphic images. II. Refine model for quasi-static speckle temporal evolution for VLT/SPHERE](martinez-2013-speckle-temporal-stability-sphere.md) | Martinez et al. | [full text](https://arxiv.org/abs/1302.7211) |

### Cross-listed from other topics

| Year | Entry | Authors | Home topic |
|---|---|---|---|
| 2002 | [Fast wave-front reconstruction in large adaptive optics systems with use of the Fourier transform](../04-control-and-reconstruction/poyneer-2002-fourier-transform-wavefront-reconstruction.md) | Poyneer et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2003 | [Analytical study of diffraction effects in extremely large segmented telescopes](../17-segmented-apertures-and-phasing/yaitskova-2003-diffraction-effects-segmented-elts.md) | Yaitskova et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2005 | [Optimal modal Fourier-transform wavefront control](../04-control-and-reconstruction/poyneer-2005-optimal-modal-fourier-control.md) | Poyneer & Véran | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2005 | [Lyot Coronagraphy on Giant Segmented-Mirror Telescopes](../17-segmented-apertures-and-phasing/sivaramakrishnan-2005-lyot-coronagraphy-segmented-telescopes.md) | Sivaramakrishnan & Yaitskova | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2005 | [Adaptive optics for high-contrast imaging: pyramid sensor versus spatially filtered Shack-Hartmann sensor](../02-wavefront-sensing/verinaud-2005-pyramid-vs-spatially-filtered-shack-hartmann.md) | Vérinaud et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2006 | [Demonstrating sub-nm closed loop MEMS flattening](../03-deformable-mirrors-and-correctors/evans-2006-sub-nm-mems-flattening.md) | Evans et al. | [03-deformable-mirrors-and-correctors](../03-deformable-mirrors-and-correctors/README.md) |
| 2007 | [PROPER: an optical propagation library](../08-modeling-error-budgets-and-simulation/krist-2007-proper-optical-propagation-library.md) | Krist | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2007 | [Calibration and precompensation of noncommon path aberrations for extreme adaptive optics](../10-calibration-and-system-identification/sauvage-2007-ncpa-calibration-precompensation.md) | Sauvage et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2007 | [The Strehl Ratio in Adaptive Optics Images: Statistics and Estimation](../09-psf-reconstruction-and-post-processing/soummer-2007-strehl-ratio-statistics.md) | Soummer & Ferrari | [09-psf-reconstruction-and-post-processing](../09-psf-reconstruction-and-post-processing/README.md) |
| 2008 | [On-line long-exposure phase diversity: a powerful tool for sensing quasi-static aberrations of extreme adaptive optics imaging systems](../10-calibration-and-system-identification/mugnier-2008-long-exposure-phase-diversity.md) | Mugnier et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2008 | [First laboratory validation of vibration filtering with LQG control law for Adaptive Optics](../04-control-and-reconstruction/petit-2008-lqg-vibration-filtering-laboratory.md) | Petit et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2009 | [Stroke saturation on a MEMS deformable mirror for woofer-tweeter adaptive optics](../03-deformable-mirrors-and-correctors/morzinski-2009-mems-stroke-saturation-woofer-tweeter.md) | Morzinski et al. | [03-deformable-mirrors-and-correctors](../03-deformable-mirrors-and-correctors/README.md) |
| 2010 | [High sensitivity wavefront sensing with a nonlinear curvature wavefront sensor](../02-wavefront-sensing/guyon-2010-nonlinear-curvature-wfs.md) | Guyon | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2010 | [Kalman filtering to suppress spurious signals in adaptive optics control](../04-control-and-reconstruction/poyneer-2010-kalman-filtering-spurious-signals.md) | Poyneer & Véran | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2011 | [Astronomical Optics (University of Arizona course lectures)](../00-reviews-and-training/guyon-2011-astronomical-optics-course.md) | Guyon et al. | [00-reviews-and-training](../00-reviews-and-training/README.md) |
| 2012 | [Image quality and high contrast improvements on VLT/NACO](../12-ao-systems-and-instruments/girard-2012-naco-image-quality-high-contrast.md) | Girard et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2012 | [POPPY: Physical Optics Propagation in Python](../08-modeling-error-budgets-and-simulation/perrin-2012-poppy-physical-optics-propagation.md) | Perrin et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2013 | [The asymmetric pupil Fourier wavefront sensor](../02-wavefront-sensing/martinache-2013-asymmetric-pupil-fourier-wfs.md) | Martinache | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2014 | [Anti-aliasing Wiener filtering for wave-front reconstruction in the spatial-frequency domain for high-order astronomical adaptive-optics systems](../04-control-and-reconstruction/correia-2014-anti-aliasing-wiener-reconstruction.md) | Correia & Teixeira | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2014 | [On-sky vibration environment for the Gemini Planet Imager and mitigation effort](../04-control-and-reconstruction/hartung-2014-gpi-vibration-mitigation.md) | Hartung et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2014 | [Fast & Furious focal-plane wavefront sensing](../02-wavefront-sensing/korkiakoski-2014-fast-and-furious-focal-plane.md) | Korkiakoski et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2014 | [Deformable mirror interferometric analysis for the direct imagery of exoplanets](../03-deformable-mirrors-and-correctors/mazoyer-2014-dm-interferometric-analysis.md) | Mazoyer et al. | [03-deformable-mirrors-and-correctors](../03-deformable-mirrors-and-correctors/README.md) |
| 2014 | [SPHERE eXtreme AO control scheme: final performance assessment and on sky validation of the first auto-tuned LQG based operational system](../04-control-and-reconstruction/petit-2014-sphere-saxo-lqg-tip-tilt.md) | Petit et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2015 | [Optimized calibration strategy for high order adaptive optics systems in closed-loop: the slope-oriented Hadamard actuation](../10-calibration-and-system-identification/meimon-2015-slope-oriented-hadamard.md) | Meimon et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2016 | [General formalism for Fourier-based wave front sensing](../02-wavefront-sensing/fauvarque-2016-general-formalism-fourier-wfs.md) | Fauvarque et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2016 | [Adaptive optics in high-contrast imaging](../00-reviews-and-training/milli-2016-adaptive-optics-high-contrast-imaging.md) | Milli et al. | [00-reviews-and-training](../00-reviews-and-training/README.md) |
| 2016 | [Tackling down the low wind effect on SPHERE instrument](../17-segmented-apertures-and-phasing/sauvage-2016-low-wind-effect-sphere.md) | Sauvage et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2017 | [Iterative wave-front reconstruction in the Fourier domain](../04-control-and-reconstruction/bond-2017-iterative-fourier-domain-reconstruction.md) | Bond et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2017 | [Modeling astronomical adaptive optics performance with temporally filtered Wiener reconstruction of slope data](../08-modeling-error-budgets-and-simulation/correia-2017-temporally-filtered-wiener-error-budget.md) | Correia et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2017 | [Adaptive Optics Predictive Control with Empirical Orthogonal Functions (EOFs)](../04-control-and-reconstruction/guyon-2017-eof-predictive-control.md) | Guyon & Males | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2017 | [Fine cophasing of segmented aperture telescopes with ZELDA, a Zernike wavefront sensor in the diffraction-limited regime](../17-segmented-apertures-and-phasing/janin-potiron-2017-zelda-fine-cophasing.md) | Janin-Potiron et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2017 | [Quantifying telescope phase discontinuities external to adaptive optics systems by use of phase diversity and focal plane sharpening](../10-calibration-and-system-identification/lamb-2017-phase-discontinuities-phase-diversity.md) | Lamb et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2017 | [The coronagraphic Modal Wavefront Sensor: a hybrid focal-plane sensor for the high-contrast imaging of circumstellar environments](../02-wavefront-sensing/wilby-2017-coronagraphic-modal-wfs.md) | Wilby et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2018 | [Status of MagAO and review of astronomical science with visible light adaptive optics](../12-ao-systems-and-instruments/close-2018-magao-visible-ao-science-review.md) | Close et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2018 | [The Compute and Control for Adaptive Optics (cacao) real-time control software package](../04-control-and-reconstruction/guyon-2018-cacao-real-time-control-software.md) | Guyon et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2018 | [Single conjugate adaptive optics for the ELT instrument METIS](../12-ao-systems-and-instruments/hippler-2018-scao-elt-metis.md) | Hippler et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2018 | [Pair-based Analytical model for Segmented Telescopes Imaging from Space for sensitivity analysis](../17-segmented-apertures-and-phasing/leboulleux-2018-pastis-segmented-telescope-model.md) | Leboulleux et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2018 | [Characterizing vibrations at the Subaru Telescope for the Subaru coronagraphic extreme adaptive optics instrument](../10-calibration-and-system-identification/lozi-2018-subaru-telescope-vibrations.md) | Lozi et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2018 | [HCIPy tutorial notebooks (adaptive optics, wavefront sensing and coronagraphy)](../00-reviews-and-training/por-2018-hcipy-tutorial-notebooks.md) | Por et al. | [00-reviews-and-training](../00-reviews-and-training/README.md) |
| 2018 | [High Contrast Imaging for Python (HCIPy): an open-source adaptive optics and coronagraph simulator](../08-modeling-error-budgets-and-simulation/por-2018-hcipy-high-contrast-simulator.md) | Por et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2019 | [Simultaneous phase and amplitude aberration sensing with a liquid-crystal vector-Zernike phase mask](../02-wavefront-sensing/doelman-2019-vector-zernike-wfs.md) | Doelman et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2019 | [Demonstrating predictive wavefront control with the Keck II near-infrared pyramid wavefront sensor](../04-control-and-reconstruction/jensenclem-2019-keck-pyramid-predictive-control.md) | Jensen-Clem et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2019 | [Asymmetries in adaptive optics point spread functions](../09-psf-reconstruction-and-post-processing/madurowicz-2019-asymmetries-ao-psf.md) | Madurowicz et al. | [09-psf-reconstruction-and-post-processing](../09-psf-reconstruction-and-post-processing/README.md) |
| 2020 | [Deep residual learning for low-order wavefront sensing in high-contrast imaging systems](../11-machine-learning-and-ai/allan-2020-deep-residual-low-order-wfs.md) | Allan et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2020 | [Joint estimation of atmospheric and instrumental defects using a parsimonious point spread function model. On-sky validation using state of the art worldwide adaptive-optics assisted instruments](../09-psf-reconstruction-and-post-processing/beltramo-martin-2020-joint-estimation-parsimonious-psf.md) | Beltramo-Martin et al. | [09-psf-reconstruction-and-post-processing](../09-psf-reconstruction-and-post-processing/README.md) |
| 2020 | [Pushing point-spread function reconstruction to the next level: application to SPHERE/ZIMPOL](../09-psf-reconstruction-and-post-processing/beltramo-martin-2020-psf-reconstruction-sphere-zimpol.md) | Beltramo-Martin et al. | [09-psf-reconstruction-and-post-processing](../09-psf-reconstruction-and-post-processing/README.md) |
| 2020 | [Adaptive optics with an infrared pyramid wavefront sensor at Keck](../02-wavefront-sensing/bond-2020-keck-infrared-pyramid.md) | Bond et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2020 | [Performance limits of adaptive-optics/high-contrast imagers with pyramid wave-front sensors](../02-wavefront-sensing/correia-2020-pyramid-performance-limits-high-contrast.md) | Correia et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2020 | [The adaptive optics simulation analysis tool(kit) (AOSAT)](../08-modeling-error-budgets-and-simulation/feldt-2020-aosat-simulation-analysis-toolkit.md) | Feldt et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2020 | [Microelectromechanical deformable mirror development for high-contrast imaging, part 2: the impact of quantization errors on coronagraph image contrast](../03-deformable-mirrors-and-correctors/ruane-2020-mems-dm-quantization-contrast.md) | Ruane et al. | [03-deformable-mirrors-and-correctors](../03-deformable-mirrors-and-correctors/README.md) |
| 2020 | [Effects of mirror seeing on high-contrast adaptive optics instruments](../01-atmospheric-turbulence/tallis-2020-mirror-seeing-high-contrast.md) | Tallis et al. | [01-atmospheric-turbulence](../01-atmospheric-turbulence/README.md) |
| 2020 | [Robustness of prediction for extreme adaptive optics systems under various observing conditions: An analysis using VLT/SPHERE adaptive optics data](../04-control-and-reconstruction/vankooten-2020-sphere-prediction-robustness.md) | van Kooten et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2021 | [Variation on a Zernike wavefront sensor theme: optimal use of photons](../02-wavefront-sensing/chambouleyron-2021-z2wfs-zernike-variation.md) | Chambouleyron et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2021 | [Data-driven subspace predictive control of adaptive optics for high-contrast imaging](../04-control-and-reconstruction/haffert-2021-subspace-predictive-control.md) | Haffert et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2021 | [Analytical tolerancing of segmented telescope co-phasing for exo-Earth high-contrast imaging](../17-segmented-apertures-and-phasing/laginja-2021-segment-tolerancing-high-contrast.md) | Laginja et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2021 | [Self-optimizing adaptive optics control with reinforcement learning for high-contrast imaging](../11-machine-learning-and-ai/landman-2021-rl-self-optimizing-ao-control.md) | Landman et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2021 | [Focal plane wavefront sensing using machine learning: performance of convolutional neural networks compared to fundamental limits](../11-machine-learning-and-ai/orban-de-xivry-2021-cnn-focal-plane-wfs.md) | Orban de Xivry et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2021 | [Three-sided pyramid wavefront sensor, part 1: simulations and analysis for astronomical adaptive optics](../02-wavefront-sensing/schatz-2021-three-sided-pyramid-simulations.md) | Schatz et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2021 | [Characterizing deformable mirrors for the MagAO-X instrument](../03-deformable-mirrors-and-correctors/van-gorkom-2021-magao-x-dm-characterization.md) | Van Gorkom et al. | [03-deformable-mirrors-and-correctors](../03-deformable-mirrors-and-correctors/README.md) |
| 2022 | [Cascade adaptive optics: contrast performance analysis of a two-stage controller by numerical simulations](../04-control-and-reconstruction/cerpa-urra-2022-cascade-ao-two-stage-controller.md) | Cerpa-Urra et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2022 | [Controlling petals using fringes: discontinuous wavefront sensing through sparse aperture interferometry at Subaru/SCExAO](../17-segmented-apertures-and-phasing/deo-2022-petal-control-sparse-aperture-interferometry.md) | Deo et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2022 | [The GPU-based High-order adaptive OpticS Testbench](../04-control-and-reconstruction/engler-2022-ghost-gpu-xao-testbench.md) | Engler et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2022 | [Reference optical turbulence and wind profiles for single conjugate and extreme adaptive optics](../01-atmospheric-turbulence/farley-2022-reference-profiles-scao-xao.md) | Farley | [01-atmospheric-turbulence](../01-atmospheric-turbulence/README.md) |
| 2022 | [Battle of the Predictive Wavefront Controls: Comparing Data and Model-Driven Predictive Control for High Contrast Imaging](../04-control-and-reconstruction/fowler-2022-predictive-control-comparison.md) | Fowler et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2022 | [Redundant apodization for direct imaging of exoplanets 2: Application to island effects](../17-segmented-apertures-and-phasing/leboulleux-2022-redundant-apodization-island-effects.md) | Leboulleux et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2022 | [Toward on-sky adaptive optics control using reinforcement learning. Model-based policy optimization for adaptive optics](../11-machine-learning-and-ai/nousiainen-2022-po4ao-towards-on-sky-rl.md) | Nousiainen et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2022 | [Low-wind-effect impact on Shack-Hartmann-based adaptive optics. Partial control solution in the context of SPHERE and GRAVITY+](../17-segmented-apertures-and-phasing/pourre-2022-low-wind-effect-shack-hartmann.md) | Pourré et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2022 | [A deep learning approach for focal-plane wavefront sensing using vortex phase diversity](../11-machine-learning-and-ai/quesnel-2022-deep-learning-vortex-fpwfs.md) | Quesnel et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2022 | [Optique adaptative : correction des effets de la turbulence atmosphérique sur les images astronomiques (Adaptive optics: correcting atmospheric turbulence effects on astronomical images)](../00-reviews-and-training/rousset-2022-optique-adaptative-turbulence-images-astronomiques.md) | Rousset & Fusco | [00-reviews-and-training](../00-reviews-and-training/README.md) |
| 2022 | [On-sky validation of image-based adaptive optics wavefront sensor referencing](../10-calibration-and-system-identification/skaf-2022-drwho-image-based-wfs-referencing.md) | Skaf et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2022 | [Predictive wavefront control on Keck II adaptive optics bench: on-sky coronagraphic results](../04-control-and-reconstruction/vankooten-2022-keck-predictive-control-on-sky.md) | van Kooten et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2023 | [Analytical modelling of adaptive optics systems: Role of the influence function](../08-modeling-error-budgets-and-simulation/berdeu-2023-influence-function-fitting-error-model.md) | Berdeu et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2023 | [GPI 2.0: performance evaluation of the wavefront sensor's EMCCD](../02-wavefront-sensing/doo-2023-gpi2-pyramid-emccd.md) | Do Ó et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2023 | [Simulating METIS' SCAO System](../08-modeling-error-budgets-and-simulation/feldt-2023-simulating-metis-scao.md) | Feldt et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2023 | [Tempestas ex machina: A review of machine learning methods for wavefront control](../11-machine-learning-and-ai/fowler-2023-ml-wavefront-control-review.md) | Fowler & Landman | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2023 | [Closed-Loop Until Further Notice: Comparing Predictive Control Methods in Closed-Loop](../04-control-and-reconstruction/fowler-2023-closed-loop-eof-prediction.md) | Fowler et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2023 | [Real-time experimental demonstrations of a photonic lantern wavefront sensor](../02-wavefront-sensing/lin-2023-photonic-lantern-wfs-real-time-demo.md) | Lin et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2023 | [Random Vibration Testing of Microelectromechanical Deformable Mirrors for Space-based High-Contrast Imaging](../03-deformable-mirrors-and-correctors/potier-2023-mems-dm-random-vibration.md) | Potier et al. | [03-deformable-mirrors-and-correctors](../03-deformable-mirrors-and-correctors/README.md) |
| 2023 | [Nonlinear wave front reconstruction from a pyramid sensor using neural networks](../11-machine-learning-and-ai/wong-2023-nn-pyramid-reconstruction-scexao.md) | Wong et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2024 | [Blind and robust reconstruction of adaptive optics point spread functions for asteroid deconvolution and moon detection](../09-psf-reconstruction-and-post-processing/berdeu-2024-blind-psf-asteroid-deconvolution.md) | Berdeu et al. | [09-psf-reconstruction-and-post-processing](../09-psf-reconstruction-and-post-processing/README.md) |
| 2024 | [Spectral interferometric wavefront sensing: a solution for petalometry at Subaru/SCExAO](../17-segmented-apertures-and-phasing/deo-2024-spectral-interferometric-petalometry.md) | Deo et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2024 | [Upgrading SPHERE with the second stage AO system SAXO+: frequency-based data-driven controller for adaptive optics](../04-control-and-reconstruction/dinis-2024-saxo-plus-frequency-data-driven-controller.md) | Dinis et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2024 | [Estimating Atmospheric Wind Speeds From Gemini Planet Imager AO Telemetry](../10-calibration-and-system-identification/du-2024-gpi-wind-speed-telemetry.md) | Du et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2024 | [High strehl and high contrast for the ELT instrument METIS - Final design, implementation, and predicted performance of the single-conjugate adaptive optics system](../12-ao-systems-and-instruments/feldt-2024-metis-scao-final-design.md) | Feldt et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2024 | [Making the unmodulated pyramid wavefront sensor smart. Closed-loop demonstration of neural network wavefront reconstruction with MagAO-X](../11-machine-learning-and-ai/landman-2024-smart-unmodulated-pwfs-lab.md) | Landman et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2024 | [AO3k at Subaru: First on-sky results of the facility extreme-AO](../12-ao-systems-and-instruments/lozi-2024-ao3k-subaru-first-on-sky.md) | Lozi et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2024 | [On-sky, real-time optical gain calibration on MagAO-X using incoherent speckles](../02-wavefront-sensing/mcewen-2024-magaox-optical-gain-speckles.md) | McEwen et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2024 | [Cascade adaptive optics with a second stage based on a Zernike wavefront sensor for exoplanet observations](../02-wavefront-sensing/ndiaye-2024-cascade-ao-zernike-second-stage.md) | N'Diaye et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2024 | [Keck Primary Mirror Closed-loop Segment Control Using a Vector-Zernike Wavefront Sensor](../17-segmented-apertures-and-phasing/salama-2024-keck-vector-zernike-segment-control.md) | Salama et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2024 | [RISTRETTO: a comparative performance analysis of the unmodulated pyramid wavefront sensor and the Zernike wavefront sensor](../02-wavefront-sensing/shinde-2024-ristretto-unmodulated-pyramid-vs-zernike.md) | Shinde et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2024 | [The Bi-O-edge wavefront sensor: how Foucault-knife-edge variants can boost extreme adaptive optics](../02-wavefront-sensing/verinaud-2024-bi-o-edge-wfs.md) | Vérinaud et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2025 | [Reinforcement learning for wavefront command in exoplanet imaging (Apprentissage par renforcement pour la correction de surface d'onde en imagerie d'exoplanetes)](../11-machine-learning-and-ai/gutierrez-2025-thesis-rl-wavefront-exoplanet.md) | Gutierrez | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2025 | [Making the unmodulated pyramid wavefront sensor smart II. First on-sky demonstration of extreme adaptive optics with deep learning](../11-machine-learning-and-ai/landman-2025-smart-pwfs-on-sky-magao-x.md) | Landman et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2025 | [Supervised and reinforcement learning for extreme adaptive optics with application to exoplanet imaging](../11-machine-learning-and-ai/pou-2025-thesis-supervised-rl-xao.md) | Pou Mulet | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2025 | [Keck Observatory as an HWO Testbed: validating wavefront sensing and control schemes on a large segmented aperture in parallel with high-contrast science](../17-segmented-apertures-and-phasing/salama-2025-keck-hwo-segmented-testbed.md) | Salama et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2025 | [On-sky demonstration of second-stage wavefront control with a photonic lantern](../02-wavefront-sensing/sengupta-2025-photonic-lantern-on-sky-second-stage.md) | Sengupta et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2026 | [Ground control to major time-lag: on-sky results of data-driven predictive wavefront control at Keck Observatory](../04-control-and-reconstruction/fowler-2026-keck-eof-on-sky.md) | Fowler et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2026 | [First Light for the GRAVITY+ Adaptive Optics: Extreme Adaptive Optics for the Very Large Telescope Interferometer](../12-ao-systems-and-instruments/gravity-collaboration-2026-first-light-gravity-plus-ao.md) | GRAVITY+ Collaboration et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2026 | [On-sky demonstration of self-learning predictive control with MagAO-X](../04-control-and-reconstruction/haffert-2026-self-learning-predictive-control-magaox.md) | Haffert et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2026 | [Sensor fusion on MagAO-X: real time vibration control using accelerometers](../10-calibration-and-system-identification/johnson-2026-magaox-accelerometer-vibrations.md) | Johnson et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2026 | [Polychromatic pyramid wavefront sensor with MKID technology for high contrast imaging](../02-wavefront-sensing/magniez-2026-polychromatic-pyramid-mkid.md) | Magniez et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2026 | [On-sky demonstration of a vector Zernike wavefront sensor in a cascaded adaptive optics system](../02-wavefront-sensing/motte-2026-vector-zernike-on-sky-cascade.md) | Motte et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2026 | [Control algorithms for dual-wavefront sensor single-conjugate adaptive optics](../04-control-and-reconstruction/sengupta-2026-dual-wfs-control-algorithms.md) | Sengupta et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2026 | [SAXO+, the second-stage adaptive optics for SPHERE: a review of six selected control algorithms and the results achieved to date](../04-control-and-reconstruction/tallon-2026-saxo-plus-control-algorithms-review.md) | Tallon et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |

<!-- INDEX:END -->
