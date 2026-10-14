# 09 · PSF Reconstruction, Characterization & Post-Processing

An adaptive-optics image is the true scene convolved with a point spread function (PSF) that has a
diffraction-limited core, a turbulent halo, and a shape that changes with time, wavelength and
position in the field (anisoplanatism). Most quantitative science with AO, including crowded-field
photometry, micro-arcsecond astrometry, galaxy morphology and deconvolution of resolved objects,
depends on how well this PSF is known. Approaches fall into a few families: *PSF reconstruction*
(PSF-R) from AO control-loop telemetry, which goes back to Véran et al. (1997); *parametric or
Fourier-based PSF models* fitted to the data or driven by a few atmospheric parameters;
*empirical extraction* of the PSF from stars in the science frame (StarFinder, DAOPHOT-like tools);
and *blind or myopic deconvolution*, which estimates the PSF and the object together.

This folder collects the key papers on these methods and on their use for AO astrometry and
photometry. It covers telemetry-based PSF-R for single-conjugate, tomographic, ground-layer and
pyramid-based systems (Keck, CANARY, MUSE, SPHERE, LBT/SOUL, MICADO), models of the off-axis and
anisoplanatic PSF, parametric models such as PSFAO, deconvolution methods, the error budgets of
AO astrometry (Galactic Center, GeMS, ELT instruments), MCAO crowded-field photometry, and Strehl
ratio statistics. Fourier-domain performance models and PSF-prediction tools such as TIPTOP are in
[08](../08-modeling-error-budgets-and-simulation/README.md) and are cross-listed here. Several
classic papers, among them Véran et al. 1997, MISTRAL (Mugnier et al. 2004) and Flicker & Rigaut
2005, have no free full text and are listed in `PAYWALLED.md`.

## Subtopics

- **Reviews and overviews**: surveys of PSF determination methods and of AO astrometry/photometry
- **PSF reconstruction from AO telemetry**: U_ij and covariance-based PSF-R, Keck/Gemini, CANARY MOAO, MUSE GLAO, SPHERE, pyramid-based SOUL, MCAO and off-axis PSF-R for the ELT/MICADO, PRIME (telemetry and focal-plane data combined)
- **Anisoplanatic and off-axis PSF modeling**: analytic anisoplanatism models, semi-empirical off-axis PSFs, LGS off-axis PSFs, AIROPA, AnisoCADO
- **Parametric PSF models and PSF estimation from images**: PSFAO model, joint atmosphere/instrument estimation, PSF from crowded-field power spectra
- **Deconvolution and image restoration**: marginal blind/myopic deconvolution, MCMC uncertainty, space-variant deblurring, asteroid PSF estimation
- **Precision astrometry with AO**: error budgets, distortion calibration, Galactic Center reference frames, GeMS/MCAO astrometry, ELT predictions
- **Crowded-field photometry and PSF fitting**: StarFinder, local PSF fitting under anisoplanatism, MCAO photometry strategies
- **Strehl ratio and PSF metrics**: statistics and temporal variability of the Strehl ratio

## Start here

- [Beltramo-Martin et al. (2020), Review of PSF reconstruction methods and application to post-processing](beltramo-martin-2020-review-psf-reconstruction.md): classified overview of PSF determination techniques and their use in post-processing
- [Gendron et al. (2006), New algorithms for AO PSF reconstruction](gendron-2006-new-psf-reconstruction-algorithms.md): the classical telemetry-based PSF-R formalism and faster variants
- [Beltramo-Martin et al. (2019), PRIME](beltramo-martin-2019-prime-psf-reconstruction.md): combining telemetry with the science image, validated on Keck/NIRC2
- [Fétick et al. (2019), Physics-based model of the AO-corrected PSF](fetick-2019-psfao-physics-based-psf-model.md): parametric PSFAO model for PSF fitting
- [Britton (2006), The anisoplanatic PSF in AO](britton-2006-anisoplanatic-psf.md): predicting off-axis PSFs from the guide star and a turbulence profile
- [Fritz et al. (2010), What is limiting near-infrared astrometry in the Galactic Centre?](fritz-2010-limiting-nir-astrometry-galactic-center.md): AO astrometric error budget
- [Diolaiti et al. (2000), StarFinder](diolaiti-2000-starfinder.md): PSF extraction and fitting in crowded AO fields
- [Fétick et al. (2020), Blind deconvolution with AO: the parametric marginal approach](fetick-2020-marginal-blind-deconvolution.md): PSF estimation and deconvolution from the science image

## Related topics

- [08 · Modeling, Error Budgets & Simulation](../08-modeling-error-budgets-and-simulation/README.md): Fourier PSF models, TIPTOP, PSF prediction
- [05 · Wide-Field & Tomographic AO](../05-wide-field-and-tomographic-ao/README.md): MCAO/GLAO/MOAO systems whose PSFs are modeled here
- [01 · Atmospheric Turbulence](../01-atmospheric-turbulence/README.md): isoplanatism and Cn2 profiles that drive PSF variation
- [10 · Calibration & System Identification](../10-calibration-and-system-identification/README.md): NCPA and turbulence identification from telemetry
- [07 · High-Contrast & Extreme AO](../07-high-contrast-and-extreme-ao/README.md): high-Strehl PSF structure and HCI post-processing
- [11 · Machine Learning & AI](../11-machine-learning-and-ai/README.md): learned PSF estimation and deconvolution
- [13 · Solar AO](../13-solar-ao/README.md): image restoration for solar AO
- [12 · AO Systems & Instruments](../12-ao-systems-and-instruments/README.md): instruments (Keck, MICADO, SPHERE, MUSE) whose data are analysed here

<!-- INDEX:START -->
_62 entries. Generated by `tools/build_index.py`; do not edit by hand._

### Anisoplanatic and off-axis PSF modeling

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2000 | [Characterization of adaptive optics point spread function for anisoplanatic imaging. Application to stellar field deconvolution](fusco-2000-anisoplanatic-psf-stellar-field-deconvolution.md) | Fusco et al. | [full text](https://aas.aanda.org/articles/aas/full/2000/04/ds1812/ds1812.html) |
| 2002 | [Characterizing the Adaptive Optics Off-Axis Point-Spread Function. I. A Semi-Empirical Method for Use in Natural Guide Star Observations](steinbring-2002-off-axis-psf-natural-guide-star.md) | Steinbring et al. | [full text](https://arxiv.org/abs/astro-ph/0207261) |
| 2005 | [Accounting for the anisoplanatic point spread function in deep wide-field adaptive optics images](cresci-2005-anisoplanatic-psf-deep-fields.md) | Cresci et al. | [full text](https://arxiv.org/abs/astro-ph/0504467) |
| 2005 | [Characterizing the Adaptive Optics Off-Axis Point-Spread Function. II. Methods for Use in Laser Guide Star Observations](steinbring-2005-off-axis-psf-lgs-methods.md) | Steinbring et al. | [full text](https://arxiv.org/abs/astro-ph/0505208) |
| 2006 | [The Anisoplanatic Point-Spread Function in Adaptive Optics](britton-2006-anisoplanatic-psf.md) | Britton | [full text](https://arxiv.org/abs/astro-ph/0603170) |
| 2015 | [Anisoplanatism effect on the E-ELT SCAO point spread function. A preserved coherent core across the field](clenet-2015-elt-scao-anisoplanatism-psf.md) | Clénet et al. | [full text](https://hal.science/hal-02423539) |
| 2016 | [The AIROPA software package: milestones for testing general relativity in the strong gravity regime with AO](witzel-2016-airopa-software-package.md) | Witzel et al. | [full text](https://authors.library.caltech.edu/records/2y3jk-6z077) |
| 2018 | [Off-axis point spread function characterization in laser guide star adaptive optics systems](beltramo-martin-2018-off-axis-psf-lgs.md) | Beltramo-Martin et al. | [full text](https://arxiv.org/abs/1804.05198) |
| 2019 | [Asymmetries in adaptive optics point spread functions](madurowicz-2019-asymmetries-ao-psf.md) | Madurowicz et al. | [full text](https://arxiv.org/abs/1909.12981) |
| 2020 | [AnisoCADO: a python package for analytically generating adaptive optics point spread functions for the Extremely Large Telescope](leschinski-2020-anisocado.md) *(software)* | Leschinski & Gendron | [full text](https://arxiv.org/abs/2006.14572) |
| 2022 | [AIROPA II: Modeling Instrumental Aberrations for Off-Axis Point Spread Functions in Adaptive Optics](ciurlo-2022-airopa-ii-instrumental-aberrations.md) | Ciurlo et al. | [full text](https://arxiv.org/abs/2210.10940) |
| 2022 | [AIROPA III: Testing Simulated and On-Sky Data](turri-2022-airopa-iii-simulated-on-sky.md) | Turri et al. | [full text](https://arxiv.org/abs/2207.00548) |
| 2023 | [AIROPA IV: Validating point spread function reconstruction on various science cases](terry-2023-airopa-iv-psf-validation.md) | Terry et al. | [full text](https://arxiv.org/abs/2209.05489) |

### Crowded-field photometry and PSF fitting

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2000 | [Analysis of isoplanatic high resolution stellar fields by the StarFinder code](diolaiti-2000-starfinder.md) | Diolaiti et al. | [full text](https://arxiv.org/abs/astro-ph/0009177) |
| 2010 | [Accurate photometry with adaptive optics in the presence of anisoplanatic effects with a sparsely sampled PSF](schoedel-2010-photometry-anisoplanatic-sparse-psf.md) | Schödel | [full text](https://arxiv.org/abs/0912.1219) |
| 2013 | [Holographic imaging of crowded fields: high angular resolution imaging with excellent quality at very low cost](schodel-2013-holographic-imaging-crowded-fields.md) | Schödel et al. | [full text](https://arxiv.org/abs/1110.2261) |
| 2015 | [Toward Precision Photometry for the ELT Era: The Double Subgiant Branch of NGC 1851 Observed with the Gemini/GeMS MCAO System](turri-2015-gems-ngc1851-photometry.md) | Turri et al. | [full text](https://arxiv.org/abs/1509.01764) |
| 2017 | [Optimal Stellar Photometry for Multi-conjugate Adaptive Optics Systems Using Science-based Metrics](turri-2017-mcao-optimal-stellar-photometry.md) | Turri et al. | [full text](https://arxiv.org/abs/1611.00422) |

### Deconvolution and image restoration

| Year | Entry | Authors | Link |
|---|---|---|---|
| 1998 | [Myopic deconvolution of adaptive optics images by use of object and point-spread function power spectra](conan-1998-myopic-deconvolution-power-spectra.md) | Conan et al. | [full text](https://www.researchgate.net/publication/5565962_Myopic_deconvolution_of_adaptive_optics_images_by_use_of_object_and_point-spread_function_power_spectra) |
| 2004 | [MISTRAL: a myopic edge-preserving image restoration method, with application to astronomical adaptive-optics-corrected long-exposure images](mugnier-2004-mistral-myopic-deconvolution.md) | Mugnier et al. | [full text](https://www.researchgate.net/publication/8220499_Mistral_a_myopic_edge-preserving_image_restoration_method_with_application_to_astronomical_adaptive-optics-corrected_long-exposure_images) |
| 2006 | [Deconvolution of multiple images with high dynamic range and an application to LBT LINC-NIRVANA](anconelli-2006-multiple-image-deconvolution-lbt.md) | Anconelli et al. | [full text](https://www.aanda.org/articles/aa/pdf/2006/46/aa5836-06.pdf) |
| 2007 | [AIDA: an adaptive image deconvolution algorithm with application to multi-frame and three-dimensional data](hom-2007-aida-adaptive-deconvolution.md) | Hom et al. | [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3166524/) |
| 2015 | [A method for space-variant deblurring with application to adaptive optics imaging in astronomy](la-camera-2015-space-variant-deblurring.md) | La Camera et al. | [full text](https://arxiv.org/abs/1505.01684) |
| 2020 | [Blind deconvolution in astronomy with adaptive optics: the parametric marginal approach](fetick-2020-marginal-blind-deconvolution.md) | Fétick et al. | [full text](https://arxiv.org/abs/2006.11160) |
| 2023 | [Improved prior for adaptive optics point spread function estimation from science images: Application for deconvolution](lau-2023-improved-prior-psf-estimation.md) | Lau et al. | [full text](https://arxiv.org/abs/2303.09422) |
| 2023 | [Marginalized myopic deconvolution of adaptive optics corrected images using MCMC methods](yan-2023-marginalized-myopic-deconvolution-mcmc.md) | Yan et al. | [full text](https://hal.science/hal-04051187) |
| 2024 | [Blind and robust reconstruction of adaptive optics point spread functions for asteroid deconvolution and moon detection](berdeu-2024-blind-psf-asteroid-deconvolution.md) | Berdeu et al. | [full text](https://arxiv.org/abs/2410.08585) |

### Parametric PSF models and PSF estimation from images

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2006 | [Constraining the Adaptive Optics Point-Spread Function in Crowded Fields: Measuring Photometric Aperture Corrections](sheehy-2006-psf-crowded-fields-aperture-corrections.md) | Sheehy et al. | [full text](https://arxiv.org/abs/astro-ph/0604551) |
| 2019 | [Physics-based model of the adaptive-optics-corrected point spread function. Applications to the SPHERE/ZIMPOL and MUSE instruments](fetick-2019-psfao-physics-based-psf-model.md) | Fétick et al. | [full text](https://arxiv.org/abs/1908.02200) |
| 2020 | [Joint estimation of atmospheric and instrumental defects using a parsimonious point spread function model. On-sky validation using state of the art worldwide adaptive-optics assisted instruments](beltramo-martin-2020-joint-estimation-parsimonious-psf.md) | Beltramo-Martin et al. | [full text](https://arxiv.org/abs/2009.00994) |

### Precision astrometry with AO

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2009 | [Precision Astrometry with Adaptive Optics](cameron-2009-precision-astrometry-ao.md) | Cameron et al. | [full text](https://arxiv.org/abs/0805.2153) |
| 2010 | [What is limiting near-infrared astrometry in the Galactic Centre?](fritz-2010-limiting-nir-astrometry-galactic-center.md) | Fritz et al. | [full text](https://arxiv.org/abs/0909.2592) |
| 2010 | [High-precision astrometry with MICADO at the European Extremely Large Telescope](trippe-2010-micado-astrometry.md) | Trippe et al. | [full text](https://arxiv.org/abs/0910.5114) |
| 2010 | [Improving Galactic Center Astrometry by Reducing the Effects of Geometric Distortion](yelda-2010-galactic-center-astrometry-distortion.md) | Yelda et al. | [full text](https://arxiv.org/abs/1010.0064) |
| 2014 | [Astrometric performance of the Gemini multiconjugate adaptive optics system in crowded fields](neichel-2014-gems-astrometric-performance.md) | Neichel et al. | [full text](https://arxiv.org/abs/1409.0719) |
| 2016 | [Astrometry with MCAO: HST-GeMS proper motions in the globular cluster NGC 6681](massari-2016-gems-hst-proper-motions.md) | Massari et al. | [full text](https://arxiv.org/abs/1609.05923) |
| 2018 | [Optimal correction of distortion for high-angular-resolution images. Application to GeMS data](bernard-2018-distortion-correction-gems.md) | Bernard et al. | [full text](https://arxiv.org/abs/1709.08567) |
| 2019 | [The Galactic Center: Improved Relative Astrometry for Velocities, Accelerations, and Orbits near the Supermassive Black Hole](jia-2019-galactic-center-relative-astrometry.md) | Jia et al. | [full text](https://arxiv.org/abs/1902.02491) |
| 2021 | [Towards realistic modelling of the astrometric capabilities of MCAO systems: detecting an intermediate mass black hole with MAVIS](monty-2021-mavis-mcao-astrometry.md) | Monty et al. | [full text](https://arxiv.org/abs/2107.13199) |
| 2022 | [Optimal Differential Astrometry for Multiconjugate Adaptive Optics. I. Astrometric Distortion Mapping using On-sky GeMS Observations of NGC 6723](taheri-2022-mcao-differential-astrometry-distortion.md) | Taheri et al. | [full text](https://arxiv.org/abs/2203.12547) |
| 2023 | [Smartphone screens as astrometric calibrators](walk-2023-smartphone-astrometric-calibrators.md) | Walk et al. | [full text](https://arxiv.org/abs/2303.04961) |

### PSF reconstruction from AO telemetry

| Year | Entry | Authors | Link |
|---|---|---|---|
| 1997 | [Estimation of the adaptive optics long-exposure point-spread function using control loop data](veran-1997-psf-estimation-control-loop-data.md) | Véran et al. | [full text](https://www.researchgate.net/publication/260961563_Estimation_of_the_adaptive_optics_long-exposure_point-spread_function_using_control_loop_data) |
| 2006 | [New algorithms for adaptive optics point-spread function reconstruction](gendron-2006-new-psf-reconstruction-algorithms.md) | Gendron et al. | [full text](https://arxiv.org/abs/astro-ph/0606681) |
| 2010 | [Adaptive optics point spread function reconstruction: lessons learned from on-sky experiment on Altair/Gemini and pathway for future systems](jolissaint-2010-altair-psf-reconstruction.md) | Jolissaint et al. | [full text](https://arxiv.org/abs/1007.2458) |
| 2011 | [First Successful Adaptive Optics PSF Reconstruction at W. M. Keck Observatory](jolissaint-2012-keck-psf-reconstruction.md) | Jolissaint et al. | [full text](https://arxiv.org/abs/1202.3486) |
| 2016 | [PSF reconstruction validated using on-sky CANARY data in MOAO mode](martin-2016-canary-moao-psf-reconstruction.md) | Martin et al. | [full text](https://arxiv.org/abs/1610.02176) |
| 2016 | [Point spread function determination for Keck adaptive optics](ragland-2016-keck-psf-determination.md) | Ragland et al. | [full text](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9909/99091P/Point-spread-function-determination-for-Keck-adaptive-optics/10.1117/12.2231814.pdf) |
| 2019 | [PRIME: PSF Reconstruction and Identification for Multiple-source characterization Enhancement - application to Keck/NIRC2 imager](beltramo-martin-2019-prime-psf-reconstruction.md) | Beltramo-Martin et al. | [full text](https://arxiv.org/abs/1903.02772) |
| 2020 | [Pushing point-spread function reconstruction to the next level: application to SPHERE/ZIMPOL](beltramo-martin-2020-psf-reconstruction-sphere-zimpol.md) | Beltramo-Martin et al. | [full text](https://arxiv.org/abs/2001.10267) |
| 2020 | [Reconstruction of the ground-layer adaptive-optics point spread function for MUSE Wide Field Mode observations](fusco-2020-muse-wfm-glao-psf-reconstruction.md) | Fusco et al. | [full text](https://arxiv.org/abs/2003.04028) |
| 2021 | [Point-spread function reconstruction of adaptive-optics imaging: meeting the astrometric requirements for time-delay cosmography](chen-2021-psf-reconstruction-time-delay-cosmography.md) | Chen et al. | [full text](https://arxiv.org/abs/2106.11060) |
| 2022 | [BRUTE, PSF Reconstruction for the SOUL pyramid-based Single Conjugate Adaptive Optics facility of the LBT](arcidiacono-2022-brute-soul-psf-reconstruction.md) | Arcidiacono et al. | [full text](https://arxiv.org/abs/2209.03278) |
| 2022 | [Point spread function reconstruction for SOUL+LUCI LBT data](simioni-2022-psf-reconstruction-soul-luci.md) | Simioni et al. | [full text](https://arxiv.org/abs/2209.01563) |
| 2022 | [Direction dependent point spread function reconstruction for multi-conjugate adaptive optics on giant segmented mirror telescopes](wagner-2022-mcao-direction-dependent-psf-reconstruction.md) | Wagner et al. | [full text](https://arxiv.org/abs/2012.11429) |
| 2023 | [Off-axis point spread function reconstruction for single conjugate adaptive optics](wagner-2023-off-axis-scao-psf-reconstruction.md) | Wagner et al. | [full text](https://arxiv.org/abs/2303.07905) |
| 2025 | [Validating the On-axis Point Spread Function Reconstruction for Keck Adaptive Optics](sabhlok-2025-keck-on-axis-psf-reconstruction.md) | Sabhlok et al. | [full text](https://iopscience.iop.org/article/10.1088/1538-3873/ae02c4) |
| 2026 | [The MICADO first light imager for the ELT: the PSF Reconstruction Software](grazian-2026-micado-psf-reconstruction-software.md) | Grazian et al. | [full text](https://arxiv.org/abs/2609.11593) |

### Reviews and overviews

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2010 | [Recent Results and Perspectives for Precision Astrometry and Photometry with Adaptive Optics](lu-2010-precision-astrometry-photometry-ao.md) *(review)* | Lu et al. | [full text](https://arxiv.org/abs/1008.1293) |
| 2020 | [Review of PSF reconstruction methods and application to post-processing](beltramo-martin-2020-review-psf-reconstruction.md) *(review)* | Beltramo-Martin et al. | [full text](https://hal.science/hal-03240495) |

### Strehl ratio and PSF metrics

| Year | Entry | Authors | Link |
|---|---|---|---|
| 2004 | [Is that really your Strehl ratio?](roberts-2004-is-that-really-your-strehl-ratio.md) | Roberts et al. | [full text](https://www.researchgate.net/publication/253843024_Is_that_really_your_Strehl_ratio) |
| 2007 | [The Strehl Ratio in Adaptive Optics Images: Statistics and Estimation](soummer-2007-strehl-ratio-statistics.md) | Soummer & Ferrari | [full text](https://arxiv.org/abs/0706.1718) |
| 2008 | [Temporal variability and statistics of the Strehl ratio in adaptive-optics images](gladysz-2008-strehl-ratio-temporal-variability.md) | Gladysz et al. | [full text](https://arxiv.org/abs/0801.4889) |

### Cross-listed from other topics

| Year | Entry | Authors | Home topic |
|---|---|---|---|
| 1967 | [Photometric error analysis. VI. Confirmation of Reiger's theory of scintillation](../01-atmospheric-turbulence/young-1967-scintillation-photometric-error.md) | Young | [01-atmospheric-turbulence](../01-atmospheric-turbulence/README.md) |
| 1994 | [Wavefront sensing and image restoration from focused and defocused solar images](../13-solar-ao/lofdahl-1994-phase-diversity-solar-images.md) | Löfdahl & Scharmer | [13-solar-ao](../13-solar-ao/README.md) |
| 2002 | [Multi-frame blind deconvolution with linear equality constraints](../13-solar-ao/lofdahl-2002-mfbd-linear-equality-constraints.md) | Löfdahl | [13-solar-ao](../13-solar-ao/README.md) |
| 2003 | [Tilt anisoplanatism in laser-guide-star-based multiconjugate adaptive optics](../05-wide-field-and-tomographic-ao/flicker-2003-tilt-anisoplanatism-lgs-mcao.md) | Flicker et al. | [05-wide-field-and-tomographic-ao](../05-wide-field-and-tomographic-ao/README.md) |
| 2003 | [The Structure of High Strehl Ratio Point-Spread Functions](../07-high-contrast-and-extreme-ao/perrin-2003-high-strehl-psf-structure.md) | Perrin et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2004 | [Performance of the Keck Observatory adaptive-optics system](../08-modeling-error-budgets-and-simulation/vandam-2004-keck-ao-performance-error-budget.md) | van Dam et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2005 | [An Analysis of Fundamental Waffle Mode in Early AEOS Adaptive Optics Images](../04-control-and-reconstruction/makidon-2005-waffle-mode-aeos.md) | Makidon et al. | [04-control-and-reconstruction](../04-control-and-reconstruction/README.md) |
| 2005 | [Solar image restoration by use of multi-frame blind de-convolution with multiple objects and phase diversity](../13-solar-ao/vannoort-2005-momfbd-solar-image-restoration.md) | van Noort et al. | [13-solar-ao](../13-solar-ao/README.md) |
| 2006 | [Angular Differential Imaging: A Powerful High-Contrast Imaging Technique](../07-high-contrast-and-extreme-ao/marois-2006-angular-differential-imaging.md) | Marois et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2006 | [Phase diversity: a technique for wave-front sensing and for diffraction-limited imaging](../02-wavefront-sensing/mugnier-2006-phase-diversity-review.md) | Mugnier et al. | [02-wavefront-sensing](../02-wavefront-sensing/README.md) |
| 2006 | [Speckle reconstruction of photometric data observed with adaptive optics](../13-solar-ao/puschmann-2006-speckle-reconstruction-ao-photometry.md) | Puschmann & Sailer | [13-solar-ao](../13-solar-ao/README.md) |
| 2007 | [A New Algorithm for Point-Spread Function Subtraction in High-Contrast Imaging: A Demonstration with Angular Differential Imaging](../07-high-contrast-and-extreme-ao/lafreniere-2007-loci.md) | Lafrenière et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2008 | [Speckle interferometry with adaptive optics corrected solar data](../13-solar-ao/woger-2008-speckle-interferometry-ao-solar.md) | Wöger et al. | [13-solar-ao](../13-solar-ao/README.md) |
| 2010 | [Synthetic Modeling of Astronomical Closed Loop Adaptive Optics](../08-modeling-error-budgets-and-simulation/jolissaint-2010-synthetic-modeling-closed-loop-ao.md) | Jolissaint | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2010 | [High-order aberration compensation with Multi-frame Blind Deconvolution and Phase Diversity image restoration techniques](../13-solar-ao/scharmer-2010-high-order-aberration-compensation-mfbd.md) | Scharmer et al. | [13-solar-ao](../13-solar-ao/README.md) |
| 2012 | [PynPoint: an image processing package for finding exoplanets](../07-high-contrast-and-extreme-ao/amara-2012-pynpoint.md) | Amara & Quanz | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2012 | [Detection and Characterization of Exoplanets and Disks Using Projections on Karhunen-Loève Eigenimages](../07-high-contrast-and-extreme-ao/soummer-2012-klip.md) | Soummer et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2014 | [Speckle image reconstruction of the adaptive optics solar images](../13-solar-ao/zhong-2014-speckle-reconstruction-ao-solar-images.md) | Zhong et al. | [13-solar-ao](../13-solar-ao/README.md) |
| 2017 | [VIP: Vortex Image Processing Package for High-contrast Direct Imaging](../07-high-contrast-and-extreme-ao/gomezgonzalez-2017-vip.md) | Gomez Gonzalez et al. | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2018 | [Real-time multiframe blind deconvolution of solar images](../13-solar-ao/asensioramos-2018-real-time-mfbd-deep-learning.md) | Asensio Ramos et al. | [13-solar-ao](../13-solar-ao/README.md) |
| 2018 | [Focal-plane Cn2(h) profiling based on single-conjugate adaptive optics compensated images](../10-calibration-and-system-identification/beltramo-martin-2018-focal-plane-cn2-profiling.md) | Beltramo-Martin et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2018 | [Budget d'erreur en optique adaptative : Simulation numérique haute performance et modélisation dans la perspective des ELT](../08-modeling-error-budgets-and-simulation/ferreira-2018-error-budget-gpu-simulation-thesis.md) | Ferreira | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2018 | [Numerical estimation of wavefront error breakdown in adaptive optics](../08-modeling-error-budgets-and-simulation/ferreira-2018-wavefront-error-breakdown.md) | Ferreira et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2018 | [Determination of the optical turbulence parameters from the adaptive optics telemetry: critical analysis and on-sky validation](../10-calibration-and-system-identification/jolissaint-2018-dm-telemetry-seeing-keck.md) | Jolissaint et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2020 | [TIPTOP: a new tool to efficiently predict your favorite AO PSF](../08-modeling-error-budgets-and-simulation/neichel-2021-tiptop-ao-psf-prediction.md) | Neichel et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2020 | [LEO satellite imaging with adaptive optics and marginalized blind deconvolution](../16-free-space-optical-communications-and-space/petit-2020-leo-satellite-imaging-ao-blind-deconvolution.md) | Petit et al. | [16-free-space-optical-communications-and-space](../16-free-space-optical-communications-and-space/README.md) |
| 2020 | [Wide field-of-view, high-resolution Solar observation in combination with ground layer adaptive optics and speckle imaging](../13-solar-ao/zhong-2020-glao-speckle-imaging-nvst.md) | Zhong et al. | [13-solar-ao](../13-solar-ao/README.md) |
| 2021 | [Learning to do multiframe wavefront sensing unsupervised: Applications to blind deconvolution](../11-machine-learning-and-ai/asensioramos-2021-unsupervised-multiframe-wfs.md) | Asensio Ramos & Olspert | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2022 | [Multi-frame blind deconvolution and phase diversity with statistical inclusion of uncorrected high-order modes](../13-solar-ao/lofdahl-2022-mfbd-statistical-diversity.md) | Löfdahl & Hillberg | [13-solar-ao](../13-solar-ao/README.md) |
| 2022 | [Performance characterization and near-realtime monitoring of MUSE adaptive optics modes at Paranal](../08-modeling-error-budgets-and-simulation/wevers-2022-muse-ao-performance-monitoring.md) | Wevers et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2023 | [An Introduction to High Contrast Differential Imaging of Exoplanets and Disks](../07-high-contrast-and-extreme-ao/follette-2023-intro-high-contrast-differential-imaging.md) | Follette | [07-high-contrast-and-extreme-ao](../07-high-contrast-and-extreme-ao/README.md) |
| 2023 | [Prediction of AO corrected PSF for SPHERE / AOF NFM](../08-modeling-error-budgets-and-simulation/kuznetsov-2023-psf-prediction-sphere-aof.md) | Kuznetsov et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2023 | [Image-to-image translation for wavefront and point spread function estimation](../11-machine-learning-and-ai/smith-2023-image-translation-wavefront-psf.md) | Smith et al. | [11-machine-learning-and-ai](../11-machine-learning-and-ai/README.md) |
| 2024 | [Integral field spectroscopy supports atmospheric optics to reveal the finite outer scale of the turbulence](../01-atmospheric-turbulence/garcialorenzo-2024-ifs-outer-scale.md) | García-Lorenzo et al. | [01-atmospheric-turbulence](../01-atmospheric-turbulence/README.md) |
| 2024 | [Adaptive Optics Telemetry Standard: Design and specification of a novel data exchange format](../10-calibration-and-system-identification/gomes-2024-adaptive-optics-telemetry-standard.md) | Gomes et al. | [10-calibration-and-system-identification](../10-calibration-and-system-identification/README.md) |
| 2025 | [torchmfbd: a flexible multi-object multi-frame blind deconvolution code](../13-solar-ao/asensioramos-2025-torchmfbd.md) | Asensio Ramos et al. | [13-solar-ao](../13-solar-ao/README.md) |
| 2026 | [Joint optical-digital design strategy for adaptive optics systems: application to wavelength selection for satellite imaging](../16-free-space-optical-communications-and-space/cheyssial-2026-joint-optical-digital-design-satellite-imaging.md) | Cheyssial et al. | [16-free-space-optical-communications-and-space](../16-free-space-optical-communications-and-space/README.md) |
| 2026 | [Characterization of the MUSE NFM PSF as a function of atmospheric conditions: TipTop calibration](../08-modeling-error-budgets-and-simulation/congiu-2026-muse-nfm-psf-tiptop-etc.md) | Congiu et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |
| 2026 | [Data-calibrated point spread function prediction: General description of the method and demonstration on MUSE-NFM](../08-modeling-error-budgets-and-simulation/kuznetsov-2026-data-calibrated-psf-prediction.md) | Kuznetsov et al. | [08-modeling-error-budgets-and-simulation](../08-modeling-error-budgets-and-simulation/README.md) |

<!-- INDEX:END -->
