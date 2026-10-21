# 02 · Wavefront Sensing

The wavefront sensor (WFS) turns phase errors into intensity signals on a detector. Its sensitivity, linearity, dynamic range and aliasing behaviour, together with its detector, set much of an AO system's performance, especially on faint guide stars and in extreme AO. Astronomical AO has relied on three main sensor families. The Shack-Hartmann measures local slopes from spot positions behind a lenslet array. The curvature sensor measures intensity differences between defocused pupil images. The pyramid sensor is a modulated focal-plane knife-edge test that is now the baseline for most ELT single-conjugate and extreme AO systems. The pyramid is one member of the wider class of Fourier-filtering sensors, which also includes the Zernike phase-contrast sensor and optical-differentiation sensors. A unified formalism now describes their sensitivity, linearity and noise propagation, and much recent work deals with their non-linear behaviour (optical gains), with reconstruction beyond the linear regime, and with new mask designs. In parallel, focal-plane methods (phase diversity, LIFT, Fast & Furious, asymmetric-pupil and photonic-lantern sensors) sense aberrations directly in the science image.

This folder covers sensor principles, theory and fundamental limits; centroiding and noise for the Shack-Hartmann; pyramid modulation, optical gains, non-modulated operation, reconstruction and hardware variants; Zernike, vector-Zernike and optical-differentiation sensors; linear and non-linear curvature sensing; focal-plane, holographic and photonic sensors; and low-noise WFS detectors (EMCCD/OCAM, sCMOS, SAPHIRA/C-RED One, MKIDs). LGS-specific sensing (spot elongation, Ingot) lives in 06. Coronagraphic dark-hole and NCPA sensors (ZELDA, COFFEE, LLOWFS) live in 07. Machine-learning reconstructors live in 11. All of these are cross-listed here where relevant.

## Subtopics

- **Overviews and sensor comparisons**: Shack-Hartmann vs pyramid vs curvature, noise and aliasing comparisons
- **Shack-Hartmann sensors and centroiding**: centroid algorithms, correlation, matched filter, peak-locking bias, tutorials
- **Fourier-filtering WFS formalism and sensitivity**: unified FFWFS theory, convolutional/kernel models, noise propagation, fundamental sensitivity limits, optimised masks
- **Pyramid WFS: principles and modelling**: original sensitivity arguments, linearity, mathematical forward models
- **Pyramid WFS: optical gains, non-linearity and reconstruction**: optical-gain estimation and compensation, non-modulated operation, non-linear and super-resolved reconstruction, reconstructor review
- **Pyramid WFS: variants and implementations**: three-sided, roof-prism, bright pyramid, Bi-O-edge, SLM-programmable masks, infrared and ELT implementations
- **Zernike, optical-differentiation and other Fourier-filtering sensors**: Zernike and vector-Zernike sensors, second-stage cascade AO, generalised optical differentiation
- **Curvature sensors**: curvature noise propagation, non-linear curvature WFS (nlCWFS), curvature sensing for active optics
- **Focal-plane, holographic and photonic sensors**: phase diversity, LIFT, Fast & Furious, asymmetric pupil Fourier WFS, holographic modal WFS, photonic lanterns
- **Wavefront sensor detectors**: EMCCD/OCAM, photon counting, sCMOS noise, SAPHIRA and C-RED One e-APD arrays, MKIDs

## Start here

- [Ragazzoni & Farinato (1999): Sensitivity of a pyramidic wave front sensor in closed loop AO](ragazzoni-1999-pyramid-sensitivity-closed-loop.md): the origin of the pyramid's sensitivity advantage
- [Thomas et al. (2006): Comparison of centroid computation algorithms in a Shack-Hartmann sensor](thomas-2006-centroid-algorithms-shack-hartmann.md): reference study of SH centroiding versus flux and read noise
- [Guyon (2005): Limits of adaptive optics for high-contrast imaging](../07-high-contrast-and-extreme-ao/guyon-2005-limits-ao-high-contrast.md) (in 07): compares WFS sensitivity across spatial frequencies
- [Fauvarque et al. (2016): General formalism for Fourier-based wave front sensing](fauvarque-2016-general-formalism-fourier-wfs.md): unified view of pyramid and Zernike sensors
- [Chambouleyron et al. (2023): Modeling noise propagation in Fourier-filtering wavefront sensing](chambouleyron-2023-noise-propagation-ffwfs.md): fundamental sensitivity limits and a pyramid vs Zernike comparison
- [Deo et al. (2019): Modal compensation of pyramid wavefront sensor optical gain](deo-2019-pyramid-optical-gain-modal-compensation.md): the optical-gain problem and a practical solution
- [Guyon (2010): Nonlinear curvature wavefront sensor](guyon-2010-nonlinear-curvature-wfs.md): curvature sensing pushed toward the sensitivity limit
- [Mugnier et al. (2006): Phase diversity review](mugnier-2006-phase-diversity-review.md): focal-plane wavefront sensing by phase diversity

## Related topics

- [00 · Reviews & Training](../00-reviews-and-training/README.md): broad AO reviews and courses that introduce wavefront sensors
- [04 · Control & Reconstruction](../04-control-and-reconstruction/README.md): reconstructors (including pyramid-specific and Fourier methods) and modal gain optimisation
- [06 · Laser Guide Stars](../06-laser-guide-stars/README.md): spot elongation, LGS Shack-Hartmann design, Ingot WFS
- [07 · High-Contrast & Extreme AO](../07-high-contrast-and-extreme-ao/README.md): ZELDA, COFFEE, LLOWFS and focal-plane dark-hole sensing
- [08 · Modeling, Error Budgets & Simulation](../08-modeling-error-budgets-and-simulation/README.md): analytic and end-to-end models of WFS behaviour
- [10 · Calibration & System Identification](../10-calibration-and-system-identification/README.md): interaction matrices, NCPA, misregistration
- [11 · Machine Learning & AI](../11-machine-learning-and-ai/README.md): neural-network reconstructors for pyramid and focal-plane sensors
- [13 · Solar AO](../13-solar-ao/README.md): correlating Shack-Hartmann sensors on extended scenes
- [17 · Segmented Apertures & Phasing](../17-segmented-apertures-and-phasing/README.md): pyramid and Zernike sensing of petal/segment piston

<!-- INDEX:START -->
_81 entries. Generated by `tools/build_index.py`; do not edit by hand._

### Curvature sensors

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2002 | [Extended analysis of curvature sensing](vandam-2002-extended-analysis-curvature-sensing.md) | van Dam & Lane | [full text](https://www.researchgate.net/publication/11281097_Extended_analysis_of_curvature_sensing) |
| 2010 | [High sensitivity wavefront sensing with a nonlinear curvature wavefront sensor](guyon-2010-nonlinear-curvature-wfs.md) | Guyon | [full text](https://arxiv.org/abs/0911.1310) |
| 2010 | [Curvature sensors: noise and its propagation](kellerer-2010-curvature-sensor-noise-propagation.md) | Kellerer | [full text](https://arxiv.org/abs/1006.2413) |
| 2012 | [The AOLI low-order non-linear curvature wavefront sensor: a method for high sensitivity wavefront reconstruction](crass-2012-aoli-nonlinear-curvature-wfs.md) *(proceedings)* | Crass et al. | [full text](https://arxiv.org/abs/1207.0991) |
| 2015 | [Curvature wavefront sensing for the Large Synoptic Survey Telescope](xin-2015-curvature-wavefront-sensing-lsst.md) | Xin et al. | [full text](https://arxiv.org/abs/1506.04839) |
| 2022 | [Spatial frequency response and sensitivity of the non-linear curvature wavefront sensor](letchev-2022-nlcwfs-spatial-frequency-response.md) *(proceedings)* | Letchev et al. | [full text](https://arxiv.org/abs/2209.00071) |
| 2023 | [Development of a non-linear curvature wavefront sensor for the Subaru Telescope's AO3k system](ahn-2023-nlcwfs-subaru-ao3k.md) *(proceedings)* | Ahn et al. | [full text](https://hal.science/hal-04429016) |

### Focal-plane, holographic and photonic sensors

| Year | Entry | Authors | Link |
|---|---|---|---|
| 1982 | [Phase retrieval algorithms: a comparison](fienup-1982-phase-retrieval-algorithms-comparison.md) | Fienup | [full text](https://www.researchgate.net/publication/43160608_Phase_retrieval_algorithms_a_comparison) |
| 1992 | [Joint estimation of object and aberrations by using phase diversity](paxman-1992-joint-estimation-phase-diversity.md) | Paxman et al. | [full text](https://www.researchgate.net/publication/247175436_Joint_estimation_of_object_and_aberrations_by_using_phase_diversity) |
| 2006 | [Phase diversity: a technique for wave-front sensing and for diffraction-limited imaging](mugnier-2006-phase-diversity-review.md) *(review)* | Mugnier et al. | [full text](https://hal.science/hal-00408562) |
| 2010 | [LIFT: a focal-plane wavefront sensor for real-time low-order sensing on faint sources](meimon-2010-lift-focal-plane-low-order-sensor.md) | Meimon et al. | [full text](https://www.researchgate.net/publication/46288944_LIFT_a_focal-plane_wavefront_sensor_for_real-time_low-order_sensing_on_faint_sources) |
| 2013 | [The asymmetric pupil Fourier wavefront sensor](martinache-2013-asymmetric-pupil-fourier-wfs.md) | Martinache | [full text](https://arxiv.org/abs/1303.6678) |
| 2013 | [Experimental validation of LIFT for estimation of low-order modes in low-flux wavefront sensing](plantet-2013-lift-experimental-validation.md) | Plantet et al. | [full text](https://doi.org/10.1364/OE.21.016337) |
| 2014 | [Fast & Furious focal-plane wavefront sensing](korkiakoski-2014-fast-and-furious-focal-plane.md) | Korkiakoski et al. | [full text](https://arxiv.org/abs/1406.1006) |
| 2017 | [The coronagraphic Modal Wavefront Sensor: a hybrid focal-plane sensor for the high-contrast imaging of circumstellar environments](wilby-2017-coronagraphic-modal-wfs.md) | Wilby et al. | [full text](https://arxiv.org/abs/1610.04235) |
| 2018 | [Demonstration of a photonic lantern low order wavefront sensor using an adaptive optics testbed](corrigan-2018-photonic-lantern-tip-tilt-sensor.md) *(proceedings)* | Corrigan et al. | [full text](https://arxiv.org/abs/1809.08131) |
| 2020 | [An all-photonic focal-plane wavefront sensor](norris-2020-photonic-lantern-focal-plane-wfs.md) | Norris et al. | [full text](https://doi.org/10.1038/s41467-020-19117-w) |
| 2022 | [Focal-plane wavefront sensing with photonic lanterns: theoretical framework](lin-2022-photonic-lantern-wfs-theory.md) | Lin et al. | [full text](https://arxiv.org/abs/2208.10563) |
| 2023 | [Real-time experimental demonstrations of a photonic lantern wavefront sensor](lin-2023-photonic-lantern-wfs-real-time-demo.md) | Lin et al. | [full text](https://arxiv.org/abs/2312.13381) |
| 2024 | [Striving towards robust phase diversity on-sky: implementing LIFT for VLT/MUSE-NFM](kuznetsov-2024-lift-muse-nfm-on-sky.md) | Kuznetsov et al. | [full text](https://arxiv.org/abs/2406.08529) |
| 2025 | [On-sky demonstration of second-stage wavefront control with a photonic lantern](sengupta-2025-photonic-lantern-on-sky-second-stage.md) | Sengupta et al. | [full text](https://arxiv.org/abs/2511.20560) |

### Fourier-filtering WFS formalism and sensitivity

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2016 | [General formalism for Fourier-based wave front sensing](fauvarque-2016-general-formalism-fourier-wfs.md) | Fauvarque et al. | [full text](https://arxiv.org/abs/1611.02969) |
| 2017 | [General formalism for Fourier-based wave front sensing: application to the pyramid wave front sensors](fauvarque-2017-fourier-wfs-pyramid-class.md) | Fauvarque et al. | [full text](https://arxiv.org/abs/1607.03269) |
| 2019 | [Kernel formalism applied to Fourier-based wave-front sensing in presence of residual phases](fauvarque-2019-kernel-formalism-fourier-wfs.md) | Fauvarque et al. | [full text](https://arxiv.org/abs/1902.05440) |
| 2020 | [Performance limits of adaptive-optics/high-contrast imagers with pyramid wavefront sensors](correia-2020-pyramid-performance-limits-high-contrast.md) | Correia et al. | [full text](https://arxiv.org/abs/2003.06011) |
| 2022 | [Joint optimization of wavefront sensing and reconstruction with automatic differentiation](landman-2022-autodiff-optimized-wfs.md) *(proceedings)* | Landman et al. | [full text](https://arxiv.org/abs/2209.05904) |
| 2023 | [Modeling noise propagation in Fourier-filtering wavefront sensing, fundamental limits, and quantitative comparison](chambouleyron-2023-noise-propagation-ffwfs.md) | Chambouleyron et al. | [full text](https://arxiv.org/abs/2212.13577) |

### Overviews and sensor comparisons

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2005 | [Adaptive optics for high-contrast imaging: pyramid sensor versus spatially filtered Shack-Hartmann sensor](verinaud-2005-pyramid-vs-spatially-filtered-shack-hartmann.md) | Vérinaud et al. | [full text](https://articles.adsabs.harvard.edu/pdf/2005MNRAS.357L..26V) |
| 2006 | [Wavefront sensing: from historical roots to the state-of-the-art](campbell-2006-wavefront-sensing-historical-roots.md) *(review)* | Campbell & Greenaway | [full text](https://waf.eps.hw.ac.uk/downloads/papers/Wavefront%20Sensing%20-%20ITHD3%20-%20Distributable%20version.pdf) |
| 2011 | [Error propagation: a comparison of Shack-Hartmann and curvature sensors](kellerer-2011-error-propagation-shack-hartmann-curvature.md) | Kellerer & Kellerer | [full text](https://arxiv.org/abs/1102.4378) |
| 2024 | [Performance comparison of the Shack-Hartmann and pyramid wavefront sensors with a laser guide star for 40 m telescopes](oyarzun-2024-shack-hartmann-vs-pyramid-lgs.md) | Oyarzún et al. | [full text](https://arxiv.org/abs/2410.04863) |
| 2024 | [RISTRETTO: a comparative performance analysis of the unmodulated pyramid wavefront sensor and the Zernike wavefront sensor](shinde-2024-ristretto-unmodulated-pyramid-vs-zernike.md) *(proceedings)* | Shinde et al. | [full text](https://arxiv.org/abs/2409.04255) |
| 2026 | [Performance comparison of the nonlinear curvature and Shack-Hartmann wavefront sensors in strong turbulence](potier-2026-nlcwfs-vs-shack-hartmann-strong-turbulence.md) | Potier et al. | [full text](https://arxiv.org/abs/2609.10536) |

### Pyramid WFS: optical gains, non-linearity and reconstruction

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2018 | [Efficient, nonlinear phase estimation with the nonmodulated pyramid wavefront sensor](frazin-2018-nonlinear-estimation-non-modulated-pyramid.md) | Frazin | [full text](https://arxiv.org/abs/1804.01011) |
| 2018 | [Nonlinear wavefront reconstruction methods for pyramid sensors using Landweber and Landweber-Kaczmarz iterations](hutterer-2018-landweber-pyramid-reconstruction.md) | Hutterer & Ramlau | [full text](https://arxiv.org/abs/1808.07673) |
| 2019 | [A telescope-ready approach for modal compensation of pyramid wavefront sensor optical gain](deo-2019-pyramid-optical-gain-modal-compensation.md) | Deo et al. | [full text](https://www.aanda.org/articles/aa/pdf/2019/09/aa35847-19.pdf) |
| 2020 | [Pyramid wavefront sensor optical gains compensation using a convolutional model](chambouleyron-2020-pyramid-optical-gains-convolutional.md) | Chambouleyron et al. | [full text](https://arxiv.org/abs/2006.08294) |
| 2020 | [Review on methods for wavefront reconstruction from pyramid wavefront sensor data](shatokhina-2020-review-pyramid-reconstruction.md) *(review)* | Shatokhina et al. | [full text](https://doi.org/10.1117/1.JATIS.6.1.010901) |
| 2021 | [Focal-plane-assisted pyramid wavefront sensor: enabling frame-by-frame optical gain tracking](chambouleyron-2021-focal-plane-assisted-pyramid.md) | Chambouleyron et al. | [full text](https://arxiv.org/abs/2103.02297) |
| 2023 | [Non-modulated pyramid wavefront sensor: use in sensing and correcting atmospheric turbulence](agapito-2023-non-modulated-pyramid-calibration.md) | Agapito et al. | [full text](https://arxiv.org/abs/2308.01066) |
| 2024 | [Using the Gerchberg-Saxton algorithm to reconstruct nonmodulated pyramid wavefront sensor measurements](chambouleyron-2024-gerchberg-saxton-non-modulated-pyramid.md) | Chambouleyron et al. | [full text](https://arxiv.org/abs/2309.14283) |
| 2024 | [On-sky, real-time optical gain calibration on MagAO-X using incoherent speckles](mcewen-2024-magaox-optical-gain-speckles.md) *(proceedings)* | McEwen et al. | [full text](https://arxiv.org/abs/2407.13022) |
| 2025 | [Super-resolution wavefront reconstruction in adaptive-optics with pyramid sensors](correia-2025-super-resolution-pyramid.md) | Correia et al. | [full text](https://arxiv.org/abs/2512.17469) |
| 2025 | [Generalized non-linear reconstructor for all Fourier-type wavefront sensors](laidlaw-2025-nonlinear-reconstructor-fourier-wfs.md) | Laidlaw | [full text](https://arxiv.org/abs/2505.03477) |
| 2025 | [Optical gains measurement with a gain scheduling camera: on-sky demonstration with PAPYRUS and perspectives](striffling-2025-gain-scheduling-camera-papyrus.md) | Striffling et al. | [full text](https://arxiv.org/abs/2511.15471) |

### Pyramid WFS: principles and modelling

| Year | Entry | Authors | Link |
|---|---|---|---|
| 1999 | [Sensitivity of a pyramidic wave front sensor in closed loop adaptive optics](ragazzoni-1999-pyramid-sensitivity-closed-loop.md) | Ragazzoni & Farinato | [full text](https://articles.adsabs.harvard.edu/pdf/1999A%26A...350L..23R) |
| 2001 | [Pyramid wavefront sensor behavior in partial correction adaptive optic systems](esposito-2001-pyramid-partial-correction.md) | Esposito & Riccardi | [full text](https://www.aanda.org/articles/aa/pdf/2001/14/aacl202.pdf) |
| 2006 | [Linearity of the pyramid wavefront sensor](burvall-2006-linearity-pyramid-wfs.md) | Burvall et al. | [full text](https://doi.org/10.1364/OE.14.011925) |
| 2019 | [Real-time adaptive optics with pyramid wavefront sensors: part I. A theoretical analysis of the pyramid sensor model](hutterer-2019-pyramid-sensor-model-analysis.md) | Hutterer et al. | [full text](https://arxiv.org/abs/1810.00682) |

### Pyramid WFS: variants and implementations

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2002 | [A pyramid wavefront sensor with no dynamic modulation](ragazzoni-2002-pyramid-no-dynamic-modulation.md) | Ragazzoni et al. | [full text](http://www.eso.org/~evernet/optcommunication.pdf) |
| 2019 | [Adaptive optics with programmable Fourier-based wavefront sensors: a spatial light modulator approach to the LAM/ONERA on-sky pyramid sensor testbed](janinpotiron-2019-loops-slm-fourier-wfs.md) | Janin-Potiron et al. | [full text](https://arxiv.org/abs/1903.06599) |
| 2019 | [Visible and near-infrared laboratory demonstration of a simplified pyramid wavefront sensor](lozi-2019-roof-prism-pyramid.md) | Lozi et al. | [full text](https://arxiv.org/abs/1901.11165) |
| 2020 | [Adaptive optics with an infrared pyramid wavefront sensor at Keck](bond-2020-keck-infrared-pyramid.md) | Bond et al. | [full text](https://doi.org/10.1117/1.JATIS.6.3.039003) |
| 2020 | [Fast modulation and dithering for the NFIRAOS pyramid wavefront sensor](chapin-2020-nfiraos-pyramid-modulation.md) *(proceedings)* | Chapin et al. | [full text](https://arxiv.org/abs/2108.06429) |
| 2021 | [The bright pyramid wavefront sensor](gerard-2021-bright-pyramid-wfs.md) *(proceedings)* | Gerard et al. | [full text](https://arxiv.org/abs/2107.13105) |
| 2021 | [Three-sided pyramid wavefront sensor, part 1: simulations and analysis for astronomical adaptive optics](schatz-2021-three-sided-pyramid-simulations.md) | Schatz et al. | [full text](https://hal.science/hal-03512484) |
| 2022 | [Three-sided pyramid wavefront sensor, part II: preliminary demonstration on the new comprehensive adaptive optics and coronagraph test instrument testbed](schatz-2022-three-sided-pyramid-cacti.md) | Schatz et al. | [full text](https://arxiv.org/abs/2210.03823) |
| 2024 | [The Bi-O edge wavefront sensor: how Foucault-knife-edge variants can boost extreme adaptive optics](verinaud-2024-bi-o-edge-wfs.md) | Vérinaud et al. | [full text](https://arxiv.org/abs/2309.07485) |

### Shack-Hartmann sensors and centroiding

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2006 | [Comparison of centroid computation algorithms in a Shack-Hartmann sensor](thomas-2006-centroid-algorithms-shack-hartmann.md) | Thomas et al. | [full text](https://articles.adsabs.harvard.edu/pdf/2006MNRAS.371..323T) |
| 2007 | [Iteratively weighted centroiding for Shack-Hartmann wave-front sensors](baker-2007-iteratively-weighted-centroiding.md) | Baker & Moallem | [full text](https://doi.org/10.1364/OE.15.005147) |
| 2009 | [Performance of centroiding algorithms at low light level conditions in adaptive optics](vyas-2009-centroiding-low-light.md) *(proceedings)* | Vyas et al. | [full text](https://arxiv.org/abs/1001.1503) |
| 2010 | [Estimation of centroid positions with a matched-filter algorithm: relevance for aberrometry of the eye](leroux-2010-matched-filter-centroiding.md) | Leroux & Dainty | [full text](https://doi.org/10.1364/OE.18.001197) |
| 2014 | [Real-time correlation reference update for astronomical adaptive optics](basden-2014-correlation-reference-update.md) | Basden et al. | [full text](https://arxiv.org/abs/1401.2635) |
| 2018 | [Peak-locking centroid bias in Shack-Hartmann wavefront sensing](anugu-2018-peak-locking-centroid-bias.md) | Anugu et al. | [full text](https://arxiv.org/abs/1801.06836) |
| 2025 | [La mesure de surface d'onde par Shack-Hartmann (Shack-Hartmann wavefront measurement)](michau-2025-shack-hartmann-tutorial-photoniques.md) *(tutorial)* | Michau & Fusco | [full text](https://hal.science/hal-05210245) |

### Wavefront sensor detectors

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2003 | [Photon counting strategies with low-light-level CCDs](basden-2003-photon-counting-l3ccd.md) | Basden et al. | [full text](https://arxiv.org/abs/astro-ph/0307305) |
| 2011 | [OCam with CCD220, the fastest and most sensitive camera to date for AO wavefront sensing](feautrier-2011-ocam-ccd220-wfs-camera.md) | Feautrier et al. | [full text](https://iopscience.iop.org/article/10.1086/658879/pdf) |
| 2015 | [Analysis of electron multiplying charge coupled device and scientific CMOS readout noise models for Shack-Hartmann wavefront sensor accuracy](basden-2015-emccd-scmos-readout-noise-shack-hartmann.md) | Basden | [full text](https://arxiv.org/abs/1506.07929) |
| 2018 | [EMCCD for pyramid wavefront sensor: laboratory characterization](agapito-2018-ocam2k-emccd-pyramid-soul.md) *(proceedings)* | Agapito et al. | [full text](https://arxiv.org/abs/2012.14634) |
| 2018 | [Overview of the SAPHIRA detector for adaptive optics applications](goebel-2018-saphira-detector-ao.md) | Goebel et al. | [full text](https://arxiv.org/abs/1805.08419) |
| 2022 | [Last performances improvement of the C-RED One camera using the 320x256 e-APD infrared Saphira detector](feautrier-2022-c-red-one-saphira-camera.md) *(proceedings)* | Feautrier & Gach | [full text](https://arxiv.org/abs/2208.00377) |
| 2023 | [GPI 2.0: performance evaluation of the wavefront sensor's EMCCD](doo-2023-gpi2-pyramid-emccd.md) *(proceedings)* | Do Ó et al. | [full text](https://arxiv.org/abs/2310.06276) |
| 2024 | [Characterizing the performance of two C-RED ONE cameras for implementation in RISTRETTO and SAXO+ projects](shinde-2024-c-red-one-characterization.md) *(proceedings)* | Shinde et al. | [full text](https://arxiv.org/abs/2409.04247) |
| 2026 | [Polychromatic pyramid wavefront sensor with MKID technology for high contrast imaging](magniez-2026-polychromatic-pyramid-mkid.md) | Magniez et al. | [full text](https://arxiv.org/abs/2601.08398) |

### Zernike, optical-differentiation and other Fourier-filtering sensors

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2016 | [Generalised optical differentiation wavefront sensor: a sensitive high dynamic range wavefront sensor](haffert-2016-generalised-optical-differentiation-wfs.md) | Haffert | [full text](https://doi.org/10.1364/OE.24.018986) |
| 2017 | [A holographic diffuser generalised optical differentiation wavefront sensor](marafatto-2017-holographic-diffuser-godwfs.md) *(proceedings)* | Marafatto et al. | [full text](https://arxiv.org/abs/1808.02261) |
| 2019 | [Simultaneous phase and amplitude aberration sensing with a liquid-crystal vector-Zernike phase mask](doelman-2019-vector-zernike-wfs.md) | Doelman et al. | [full text](https://arxiv.org/abs/1811.08805) |
| 2020 | [Using the generalised-optical differentiation wavefront sensor for laser guide star wavefront sensing](haffert-2020-godwfs-laser-guide-star.md) *(proceedings)* | Haffert et al. | [full text](https://arxiv.org/abs/2012.02336) |
| 2021 | [Variation on a Zernike wavefront sensor theme: optimal use of photons](chambouleyron-2021-z2wfs-zernike-variation.md) | Chambouleyron et al. | [full text](https://arxiv.org/abs/2105.07690) |
| 2024 | [Cascade adaptive optics with a second stage based on a Zernike wavefront sensor for exoplanet observations: Experimental validation on the ESO/GHOST testbed](ndiaye-2024-cascade-ao-zernike-second-stage.md) | N'Diaye et al. | [full text](https://arxiv.org/abs/2411.11946) |
| 2026 | [On-sky demonstration of a vector Zernike wavefront sensor in a cascaded adaptive optics system](motte-2026-vector-zernike-on-sky-cascade.md) | Motte et al. | [full text](https://arxiv.org/abs/2608.30666) |

### Cross-listed from other topics

| Year | Entry | Authors | Home topic |
|---|---|---|---|
| 1991 | [A simple low-order adaptive optics system for near-infrared applications](../12-ao-systems-and-instruments/roddier-1991-low-order-adaptive-optics-system.md) | Roddier et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 1994 | [Wavefront sensing and image restoration from focused and defocused solar images](../13-solar-ao/lofdahl-1994-phase-diversity-solar-images.md) | Löfdahl & Scharmer | [13-solar-ao](../13-solar-ao/README.md) |
| 1997 | [Aberrations and retinal image quality of the normal human eye](../14-vision-science-and-ophthalmology/liang-1997-aberrations-retinal-image-quality.md) | Liang & Williams | [14-vision-science-and-ophthalmology](../14-vision-science-and-ophthalmology/README.md) |
| 2002 | [Laser beacon wave-front sensing without focal anisoplanatism](../06-laser-guide-stars/buscher-2002-laser-beacon-without-focal-anisoplanatism.md) | Buscher et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2002 | [SLODAR: measuring optical turbulence altitude with a Shack-Hartmann wavefront sensor](../01-atmospheric-turbulence/wilson-2002-slodar-shack-hartmann.md) | Wilson | [01-atmospheric-turbulence](../01-atmospheric-turbulence/README.md) |
| 2003 | [Calibration of NAOS and CONICA static aberrations. Application of the phase diversity technique](../10-calibration-and-system-identification/blanc-2003-naos-conica-phase-diversity.md) | Blanc et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2003 | [Suppressing anomalous localized waffle behavior in least-squares wavefront reconstructors](../04-control-and-reconstruction/gavel-2003-waffle-least-squares-reconstructors.md) | Gavel | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2003 | [Calibration of NAOS and CONICA static aberrations. Experimental results](../10-calibration-and-system-identification/hartung-2003-naos-conica-static-aberrations.md) | Hartung et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2004 | [Spatially filtered wave-front sensor for high-order adaptive optics](../07-high-contrast-and-extreme-ao/poyneer-2004-spatially-filtered-wavefront-sensor.md) | Poyneer & Macintosh | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2005 | [Modelling astronomical adaptive optics - I. The software package CAOS](../08-modeling-error-budgets-and-simulation/carbillet-2005-caos-software-package.md) | Carbillet et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2005 | [Pyramid sensor for segmented mirror alignment](../17-segmented-apertures-and-phasing/esposito-2005-pyramid-sensor-segment-alignment.md) | Esposito et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2005 | [Limits of Adaptive Optics for High-Contrast Imaging](../07-high-contrast-and-extreme-ao/guyon-2005-limits-ao-high-contrast.md) | Guyon | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2005 | [Extended object wavefront sensing based on the correlation spectrum phase](../13-solar-ao/knutsson-2005-correlation-spectrum-phase-wfs.md) | Knutsson et al. | [13-solar-ao](../13-solar-ao/README.md) |
| 2006 | [Laboratory testing the layer oriented wavefront sensor for the multiconjugate adaptive optics demonstrator](../05-wide-field-and-tomographic-ao/arcidiacono-2006-mad-layer-oriented-wfs.md) | Arcidiacono et al. | [05-wide-field-and-tomographic-ao](../05-wide-field-and-tomographic-ao/README.md) |
| 2006 | [Wave front sensor-less adaptive optics: a model-based approach using sphere packings](../15-microscopy-and-biological-imaging/booth-2006-sensorless-ao-sphere-packings.md) | Booth | [15-microscopy-and-biological-imaging](../15-microscopy-and-biological-imaging/README.md) |
| 2006 | [Shack-Hartmann wavefront sensing with elongated sodium laser beacons: centroiding versus matched filtering](../06-laser-guide-stars/gilles-2006-elongated-lgs-matched-filtering.md) | Gilles & Ellerbroek | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2006 | [Wavefront reconstruction with artificial neural networks](../11-machine-learning-and-ai/guo-2006-wavefront-reconstruction-ann.md) | Guo et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2006 | [Adaptive wavefront correction in two-photon microscopy using coherence-gated wavefront sensing](../15-microscopy-and-biological-imaging/rueckel-2006-coherence-gated-wavefront-sensing.md) | Rueckel et al. | [15-microscopy-and-biological-imaging](../15-microscopy-and-biological-imaging/README.md) |
| 2007 | [Calibration and precompensation of noncommon path aberrations for extreme adaptive optics](../10-calibration-and-system-identification/sauvage-2007-ncpa-calibration-precompensation.md) | Sauvage et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2008 | [On-Line Long-Exposure Phase Diversity: a Powerful Tool for Sensing Quasi-Static Aberrations of Extreme Adaptive Optics Imaging Systems](../10-calibration-and-system-identification/mugnier-2008-long-exposure-phase-diversity.md) | Mugnier et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2008 | [PYRAMIR: Calibration and Operation of a Pyramid Near-Infrared Wavefront Sensor](../10-calibration-and-system-identification/peter-2008-pyramir-calibration.md) | Peter et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2008 | [The Pyramid Phasing Sensor (PYPS)](../17-segmented-apertures-and-phasing/pinna-2008-pyramid-phasing-sensor-pyps.md) | Pinna et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2008 | [Study of optimal wavefront sensing with elongated laser guide stars](../06-laser-guide-stars/thomas-2008-elongated-lgs-wavefront-sensing.md) | Thomas et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2010 | [Lessons learned with the Active Phasing Experiment: comparison of four optical phasing sensors on a segmented Very Large Telescope](../17-segmented-apertures-and-phasing/gonte-2010-ape-four-phasing-sensors.md) | Gonté & Surdej | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2010 | [Evaluation of image-shift measurement algorithms for solar Shack-Hartmann wavefront sensors](../13-solar-ao/lofdahl-2010-image-shift-algorithms-solar-shwfs.md) | Löfdahl | [13-solar-ao](../13-solar-ao/README.md) |
| 2010 | [Fourier transform-wavefront reconstruction for the pyramid wavefront sensor](../04-control-and-reconstruction/quiros-pacheco-2010-fourier-reconstruction-pyramid.md) | Quirós-Pacheco et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2011 | [Large Binocular Telescope Adaptive Optics System: New achievements and perspectives in adaptive optics](../12-ao-systems-and-instruments/esposito-2011-lbt-ao-new-achievements.md) | Esposito et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2011 | [Phase sensor for solar adaptive-optics](../13-solar-ao/kellerer-2011-phase-sensor-solar-ao.md) | Kellerer | [13-solar-ao](../13-solar-ao/README.md) |
| 2012 | [GRAVITY Coudé Infrared Adaptive Optics (CIAO) system for the VLT Interferometer](../12-ao-systems-and-instruments/kendrew-2012-gravity-ciao.md) | Kendrew et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2012 | [Topics in Adaptive Optics](../00-reviews-and-training/tyson-2012-topics-in-adaptive-optics.md) | Tyson | [00-reviews-and-training](../00-reviews-and-training/README.md) |
| 2013 | [Calibration of quasi-static aberrations in exoplanet direct-imaging instruments with a Zernike phase-mask sensor](../07-high-contrast-and-extreme-ao/ndiaye-2013-zelda-zernike-ncpa.md) | N'Diaye et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2013 | [High-order myopic coronagraphic phase diversity (COFFEE) for wave-front control in high-contrast imaging systems](../07-high-contrast-and-extreme-ao/paul-2013-coffee-high-order.md) | Paul et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2014 | [Lyot-based Low Order Wavefront Sensor for Phase-mask Coronagraphs: Principle, Simulations and Laboratory Experiments](../07-high-contrast-and-extreme-ao/singh-2014-lyot-low-order-wfs.md) | Singh et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2015 | [Conjugate adaptive optics in widefield microscopy with an extended-source wavefront sensor](../15-microscopy-and-biological-imaging/li-2015-conjugate-ao-widefield-extended-source.md) | Li et al. | [15-microscopy-and-biological-imaging](../15-microscopy-and-biological-imaging/README.md) |
| 2015 | [Improved shift estimates on extended Shack-Hartmann wavefront sensor images](../13-solar-ao/townson-2015-improved-shift-estimates-extended-shwfs.md) | Townson et al. | [13-solar-ao](../13-solar-ao/README.md) |
| 2016 | [Sparse aperture differential piston measurements using the pyramid wave-front sensor](../17-segmented-apertures-and-phasing/arcidiacono-2016-pyramid-sparse-aperture-piston.md) | Arcidiacono et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2016 | [The adaptive optics modes for HARMONI: from Classical to Laser Assisted Tomographic AO](../05-wide-field-and-tomographic-ao/neichel-2016-harmoni-ao-modes.md) | Neichel et al. | [05-wide-field-and-tomographic-ao](../05-wide-field-and-tomographic-ao/README.md) |
| 2016 | [First light on an adaptive optics system using a non-modulation pyramid wavefront sensor for a 1.8 m telescope](../12-ao-systems-and-instruments/wang-2016-lijiang-nonmodulated-pyramid-first-light.md) | Wang et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2017 | [On-sky demonstration of matched filters for wavefront measurements using ELT-scale elongated laser guide stars](../06-laser-guide-stars/basden-2017-matched-filter-elongated-lgs-on-sky.md) | Basden et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2017 | [Fine cophasing of segmented aperture telescopes with ZELDA, a Zernike wavefront sensor in the diffraction-limited regime](../17-segmented-apertures-and-phasing/janin-potiron-2017-zelda-fine-cophasing.md) | Janin-Potiron et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2018 | [Advanced wavefront reconstruction methods for segmented Extremely Large Telescope pupils using pyramid sensors](../17-segmented-apertures-and-phasing/hutterer-2018-segmented-pupil-pyramid-reconstruction.md) | Hutterer et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2018 | [A new calibration strategy for adaptive telescopes with pyramid WFS](../10-calibration-and-system-identification/heritier-2018-pseudo-synthetic-calibration-lbt.md) | Héritier et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2018 | [Sensing and control of segmented mirrors with a pyramid wavefront sensor in the presence of spiders](../17-segmented-apertures-and-phasing/schwartz-2018-pyramid-segmented-mirror-spiders.md) | Schwartz et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2018 | [Generating Artificial Reference Images for Open Loop Correlation Wavefront Sensors](../13-solar-ao/townson-2018-artificial-reference-images-correlation-wfs.md) | Townson et al. | [13-solar-ao](../13-solar-ao/README.md) |
| 2019 | [Single conjugate adaptive optics for the ELT instrument METIS](../12-ao-systems-and-instruments/hippler-2019-scao-elt-metis.md) | Hippler et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2019 | [Learning-based Shack-Hartmann wavefront sensor for high-order aberration detection](../11-machine-learning-and-ai/hu-2019-learning-based-shack-hartmann.md) | Hu et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2019 | [Adaptive optics light-sheet microscopy based on direct wavefront sensing without any guide star](../15-microscopy-and-biological-imaging/hubert-2019-ao-light-sheet-extended-source-wfs.md) | Hubert et al. | [15-microscopy-and-biological-imaging](../15-microscopy-and-biological-imaging/README.md) |
| 2019 | [Real-time adaptive optics with pyramid wavefront sensors: part II. Accurate wavefront reconstruction using iterative methods](../04-control-and-reconstruction/hutterer-2019-pyramid-iterative-reconstruction.md) | Hutterer et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2019 | [Innovative Calibration Strategies for Large Adaptive Telescopes with Pyramid Wave-Front Sensors](../10-calibration-and-system-identification/heritier-2019-calibration-strategies-thesis.md) | Héritier | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2019 | [Deep learning wavefront sensing](../11-machine-learning-and-ai/nishizaki-2019-deep-learning-wavefront-sensing.md) | Nishizaki et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2019 | [Analysis the MICADO-MAORY SCAO performance](../08-modeling-error-budgets-and-simulation/vidal-2019-micado-maory-scao-performance.md) | Vidal et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2019 | [Calibration of quasi-static aberrations in exoplanet direct-imaging instruments with a Zernike phase-mask sensor. III. On-sky validation in VLT/SPHERE](../07-high-contrast-and-extreme-ao/vigan-2019-zelda-on-sky-sphere.md) | Vigan et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2020 | [Image-based wavefront sensing for astronomy using neural networks](../11-machine-learning-and-ai/andersen-2020-image-based-wfs-neural-networks.md) | Andersen et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2020 | [On-sky correction of non-common path aberration with the pyramid wavefront sensor](../10-calibration-and-system-identification/esposito-2020-ncpa-pyramid-on-sky-lbt.md) | Esposito et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2020 | [Infrared wavefront sensing for adaptive optics assisted galactic center observations with the VLT interferometer and GRAVITY: operation and results](../12-ao-systems-and-instruments/hippler-2020-infrared-wavefront-sensing-gravity.md) | Hippler et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2020 | [Nonlinear wavefront reconstruction with convolutional neural networks for Fourier-based wavefront sensors](../11-machine-learning-and-ai/landman-2020-cnn-nonlinear-fourier-wfs.md) | Landman & Haffert | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2020 | [Comparing focal plane wavefront control techniques: Numerical simulations and laboratory experiments](../07-high-contrast-and-extreme-ao/potier-2020-comparing-focal-plane-wavefront-control.md) | Potier et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2021 | [ELT-scale elongated LGS wavefront sensing: on-sky results](../06-laser-guide-stars/bardou-2021-elt-elongated-lgs-on-sky.md) | Bardou et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2021 | [A correlation-locking adaptive filtering technique for minimum variance integral control in adaptive optics](../04-control-and-reconstruction/deo-2021-close-modal-gain-adaptive-filtering.md) | Deo et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2021 | [Deep learning wavefront sensing method for Shack-Hartmann sensors with sparse sub-apertures](../11-machine-learning-and-ai/he-2021-deep-learning-sparse-shack-hartmann.md) | He et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2021 | [Current status of PAPYRUS: the pyramid based adaptive optics system at LAM/OHP](../12-ao-systems-and-instruments/muslimov-2021-papyrus-pyramid-ao-ohp.md) | Muslimov et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2021 | [Focal plane wavefront sensing using machine learning: performance of convolutional neural networks compared to fundamental limits](../11-machine-learning-and-ai/orban-de-xivry-2021-cnn-focal-plane-wfs.md) | Orban de Xivry et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2022 | [Confusion in differential piston measurement with the pyramid wavefront sensor](../17-segmented-apertures-and-phasing/bertrou-cantou-2022-pyramid-differential-piston-confusion.md) | Bertrou-Cantou et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2022 | [Phasing the Giant Magellan Telescope with the holographic dispersed fringe sensor](../17-segmented-apertures-and-phasing/haffert-2022-holographic-dispersed-fringe-sensor.md) | Haffert et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2022 | [Performance of a complementary metal-oxide-semiconductor sensor for laser guide star wavefront sensing](../06-laser-guide-stars/ke-2022-cmos-sensor-lgs-wavefront-sensing.md) | Ke et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2022 | [Adapting the pyramid wavefront sensor for pupil fragmentation of the ELT class telescopes](../17-segmented-apertures-and-phasing/levraud-2022-pyramid-pupil-fragmentation.md) | Levraud et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2022 | [Super-resolution wavefront reconstruction](../04-control-and-reconstruction/oberti-2022-super-resolution-wavefront-reconstruction.md) | Oberti et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2022 | [Model-free reinforcement learning with a non-linear reconstructor for closed-loop adaptive optics control with a pyramid wavefront sensor](../11-machine-learning-and-ai/pou-2022-rl-nonlinear-reconstructor-pyramid.md) | Pou et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2022 | [On-sky Reconstruction of Keck Primary Mirror Piston Offsets Using a Zernike Wavefront Sensor](../17-segmented-apertures-and-phasing/van-kooten-2022-keck-zernike-segment-piston.md) | van Kooten et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2023 | [Mitigating the nonlinearities in a pyramid wavefront sensor](../11-machine-learning-and-ai/archinuk-2023-pyramid-nonlinearities-ml.md) | Archinuk et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2023 | [Including the pyramid optical gains into analytical models](../08-modeling-error-budgets-and-simulation/fetick-2023-pyramid-optical-gains-analytical-models.md) | Fétick et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2023 | [SOUL at LBT: commissioning results, science and future](../12-ao-systems-and-instruments/pinna-2023-soul-lbt-commissioning.md) | Pinna et al. | [12-ao-systems-and-instruments](../12-ao-systems-and-instruments/README.md) |
| 2023 | [Nonlinear Wave Front Reconstruction from a Pyramid Sensor using Neural Networks](../11-machine-learning-and-ai/wong-2023-nn-pyramid-reconstruction-scexao.md) | Wong et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2024 | [Deep optics preconditioner for modulation-free pyramid wavefront sensing](../11-machine-learning-and-ai/guzman-2024-deep-optics-preconditioner-pwfs.md) | Guzmán et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2024 | [Making the unmodulated Pyramid wavefront sensor smart. Closed-loop demonstration of neural network wavefront reconstruction with MagAO-X](../11-machine-learning-and-ai/landman-2024-smart-unmodulated-pwfs-lab.md) | Landman et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2024 | [A strategy for sensing the petal mode in the presence of AO residual turbulence with the pyramid wavefront sensor](../17-segmented-apertures-and-phasing/levraud-2024-petal-mode-sensing-pyramid.md) | Levraud et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2024 | [Metasurface-based toroidal lenslet array design for addressing laser guide star elongation](../06-laser-guide-stars/munro-2024-metasurface-toroidal-lenslet-lgs.md) | Munro et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2024 | [Expected performance of the Pyramid wavefront sensor with a laser guide star for 40 m class telescopes](../06-laser-guide-stars/oyarzun-2024-pyramid-wfs-lgs-40m.md) | Oyarzún et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2024 | [Integrating supervised and reinforcement learning for predictive control with an unmodulated pyramid wavefront sensor for adaptive optics](../11-machine-learning-and-ai/pou-2024-supervised-rl-unmodulated-pwfs.md) | Pou et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2024 | [Ingot-like class of wavefront sensors for laser guide stars](../06-laser-guide-stars/ragazzoni-2024-ingot-wavefront-sensor.md) | Ragazzoni et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2024 | [Keck Primary Mirror Closed-loop Segment Control Using a Vector-Zernike Wavefront Sensor](../17-segmented-apertures-and-phasing/salama-2024-keck-vector-zernike-segment-control.md) | Salama et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2024 | [Transformer neural networks for closed-loop adaptive optics using nonmodulated pyramid wavefront sensors](../11-machine-learning-and-ai/weinberger-2024-transformer-nonmodulated-pwfs.md) | Weinberger et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2025 | [Event-based detectors for laser guide star tip-tilt sensing](../06-laser-guide-stars/cockram-2025-event-based-lgs-tip-tilt.md) | Cockram & Martinez Rey | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2025 | [Making the unmodulated pyramid wavefront sensor smart II. First on-sky demonstration of extreme adaptive optics with deep learning](../11-machine-learning-and-ai/landman-2025-smart-pwfs-on-sky-magao-x.md) | Landman et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2025 | [Single-Shot Phase Diversity Wavefront Sensing in Deep Turbulence via Metasurface Optics](../16-free-space-optical-communications-and-space/martinjimenez-2025-metasurface-phase-diversity-deep-turbulence.md) | Martin Jimenez et al. | [16-free-space-optical-communications-and-space](../16-free-space-optical-communications-and-space/README.md) |
| 2025 | [A Framework for Iterative Phase Retrieval Technique Integration into Atmospheric Adaptive Optics—Part II: High Resolution Wavefront Control in Strong Scintillations](../16-free-space-optical-communications-and-space/vorontsov-2025-iterative-phase-retrieval-strong-scintillation.md) | Vorontsov & Polnau | [16-free-space-optical-communications-and-space](../16-free-space-optical-communications-and-space/README.md) |
| 2025 | [LEO-to-ground low elevation optical communication: optimization of an adaptive optics design robust to scintillation](../16-free-space-optical-communications-and-space/vene-2025-leo-low-elevation-ao-scintillation.md) | Vène et al. | [16-free-space-optical-communications-and-space](../16-free-space-optical-communications-and-space/README.md) |
| 2026 | [Modelling Fourier filtering wavefront sensors for PSD-based methods: the AOPERA tool](../08-modeling-error-budgets-and-simulation/fetick-2026-aopera-fourier-filtering-wfs-psd.md) | Fétick et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2026 | [Non-common path aberration compensation and a dark hole loop with a pyramid adaptive optics system: Application to SAXO+](../07-high-contrast-and-extreme-ao/goulas-2026-saxo-plus-ncpa-dark-hole-pyramid.md) | Goulas et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2026 | [The first on-sky demonstration of intensity-based angular phase estimation](../16-free-space-optical-communications-and-space/lognone-2026-on-sky-intensity-angular-phase-estimation.md) | Lognoné et al. | [16-free-space-optical-communications-and-space](../16-free-space-optical-communications-and-space/README.md) |
| 2026 | [Sensing ELT petal modes with a discrete beam combiner: an end-to-end theoretical model](../17-segmented-apertures-and-phasing/madhav-2026-discrete-beam-combiner-petal-sensing.md) | Madhav et al. | [17-segmented-apertures-and-phasing](../17-segmented-apertures-and-phasing/README.md) |
| 2026 | [Impact of microlenses shape on the performance of laser guide star wavefront sensors for ELT-class telescopes](../06-laser-guide-stars/rouquette-2026-microlens-shape-lgs-wfs.md) | Rouquette et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |
| 2026 | [Slow focus sensor for the Keck I laser guide star adaptive optics system using focal plane wavefront sensing](../06-laser-guide-stars/salgueiro-2026-keck-slow-focus-focal-plane.md) | Salgueiro et al. | [06-laser-guide-stars](../06-laser-guide-stars/README.md) |

<!-- INDEX:END -->
