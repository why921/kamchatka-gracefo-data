# Kamchatka GRACE/GRACE-FO Data and Analysis

Research data, processing scripts, and reproducibility materials for evaluating
gravity-field changes associated with the 2025 Kamchatka earthquake sequence.
The project combines GRACE/GRACE-FO Level-2 spherical harmonics and Mascon
products with ShakeMap constraints, environmental corrections, and
product-specific spatial operators.

> [!IMPORTANT]
> The current earthquake-attribution verdict is **`NOT_CONFIRMED`**. Materials
> in this repository document an active scientific investigation and should not
> be interpreted as a confirmed satellite detection of the earthquake signal.

## Repository Scope

This repository is intended to share:

- analysis and visualization scripts;
- lightweight data inventories, download manifests, and provenance records;
- selected redistributable derived data products;
- figures, manuscript materials, and audit reports needed to evaluate the
  processing chain.

Large upstream datasets and local computational artifacts are excluded from
Git by default. Their source documentation and retrieval instructions are kept
with the project wherever possible.

## Current Scientific Status (2026-07-22)

The project attribution verdict is `NOT_CONFIRMED`. The original 1.5-degree
STEP08 global P0 was found to contain near-field aliasing and an inconsistent
seawater-interface treatment; it is retained for audit only. STEP08-R repairs
the template with a global coarse far field, a tapered 0.5-degree near-field
correction, and a 5-km depth-continued GEBCO interface. The repaired template
correlates 0.982 with the independent high-resolution regional reference. Its
August 2025 three-center scales are 0.888–0.957 and it explains 21.8%–32.3% of
spatial energy on the fixed 2% support. The authoritative products are under
`outputs/STEP08_global_unfiltered_P0/08_repaired_nested_global_P0/`. All eight
STEP08 computational-completeness gates pass; this validates execution and
reporting, not earthquake detection or attribution.

STEP09-E subsequently projected global GLDAS, ERA5-Land, ERA5 surface pressure,
and CMEMS bottom pressure through the repaired STEP08-R operator and rebuilt
the three-center 2002-04--2026-04 timeline. The August 2025
environment-corrected STEP08-R scales are 1.249--1.614. STEP10-M replaces the
Mascon source-minus-control main estimator with native-support spatial matched
filtering of the full positive/negative STEP08-R template. August amplitudes
are 0.521 (JPL), 0.904 (CSR), and 0.254 (GSFC), explaining 9.4--13.0% of
covariance-weighted spatial energy. Native-Mascon and spherical-harmonic
eight-month medians are directionally compatible but not significantly
correlated (Pearson r=0.569; Spearman rho=0.452). The stronger earlier
source-minus-control correlation is retained only as a regional sensitivity.
These results are now interpreted in a no-reference-product framework. The
USGS-driven STEP08-R field is a coseismic spatial prior, not gravity truth;
Level-2 and Mascon products are parallel processing expressions of the same
satellite observations. Their signals must be compared only after the same
physical hypothesis has been passed through each product's own spatial
operator and actual monthly sampling window. August 2025 is the first complete
post-event month, but it averages the permanent coseismic step, early
postseismic evolution, and residual environmental variability. STEP11-T/D now
uses each center's exact solution bounds to integrate step, logarithmic
afterslip, exponential-relaxation, and combined hypotheses. The six-product
parallel matrix is computationally complete: the three Level-2 branches prefer
step plus logarithmic afterslip, JPL/CSR Mascon prefer step plus exponential
relaxation, and GSFC Mascon prefers a step. This product dependence prevents a
unique mechanism interpretation. The project verdict remains `NOT_CONFIRMED`
pending STEP09-N full correlated-noise injection/recovery.

Current authoritative downstream outputs:

- `outputs/STEP09_postseismic_spatiotemporal_environment/`
- `outputs/STEP10_SH_MASCON_crossvalidation/`
- `outputs/STEP10_native_mascon_P0_matched_filter/`
- `outputs/STEP11_temporal_parallel_detection/`
- `outputs/STEP11C_full_environment_spatial_correction/`

STEP11-C provides the audited product-specific spatial environmental correction.
It uses the STEP06-v2/STEP08-R Level-2 chain, native-support Mascon operators,
an ensemble of GLDAS and ERA5-Land (with individual-model sensitivities), exact
JPL GAD removal, and CMEMS sensitivity for CSR/GSFC. Full ERA5 surface pressure
is not subtracted because AOD1B has already been applied. Corrected August 2025
scales are 1.406--1.476 for Level-2, 0.130 for JPL Mascon, 1.015 for CSR
Mascon, and 0.347 for GSFC Mascon. JPL spans -0.033--0.293 across the two
hydrology models and is not robust; the project remains `NOT_CONFIRMED`.

## Repository Layout

- `data/`: source-data documentation, manifests, checksums, and selected
  shareable products. Most downloaded scientific data are ignored by default.
- `scripts/`: Python download, processing, validation, and plotting workflows.
- `figures/`: selected figures intended for review or publication.
- `outputs/`: generated analysis products retained locally unless explicitly
  selected for release.
- `GRL/`: manuscript, supporting-information, tables, and publication figures.
- `external/`: external model or software integrations and their metadata.

Local caches, temporary builds, private toolchains, and generated scratch
outputs are excluded through `.gitignore`.

## Data Availability

The repository does not automatically redistribute all upstream GRACE/GRACE-FO,
ShakeMap, hydrology, atmospheric, or ocean products. These datasets may be
large and remain subject to their providers' access conditions and licenses.

The `data/` directory is configured to track lightweight documentation and
machine-readable manifests (`.md`, `.txt`, `.json`, and `.jsonl`) while
ignoring bulk data by default. Before publishing a binary dataset, verify its
license, provenance, checksum, and file size. Large files should be released
through an appropriate data archive or Git LFS rather than ordinary Git
history.

## Quick Start

Clone the repository and run workflows from its root directory:

```bash
git clone https://github.com/why921/kamchatka-gracefo-data.git
cd kamchatka-gracefo-data
```

The Python environment is not yet pinned in a project-level dependency file.
Before running the complete workflow, review the imports and configuration near
the top of the relevant script. For download workflows, use a dry run first
whenever the script provides one.

## Useful Entrypoints

- Plot ShakeMap grids:

```bash
python3 scripts/plot_shakemap_hdf.py
```

- Plot ocean-focused GRACE source/control regions:

```bash
python3 scripts/plot_grace_ocean_regions.py
```

- Plot real JPL mascon footprints intersecting the rupture core:

```bash
python3 scripts/plot_real_mascon_overlay.py
```

- Plot a GRACE monthly difference with the rupture core:

```bash
python3 scripts/plot_grace_month_diff_with_rupture.py 2025-08 2025-07
```

- Download PO.DAAC GRACE/GRACE-FO Level-2 GSM monthly spherical harmonic files:

```bash
python3 scripts/download_grace_gsm_l2.py
```

Default mission, centers, date range, output directory, product type, and
optional Earthdata credentials are configured near the top of
`scripts/download_grace_gsm_l2.py`. The downloader queries CMR for the six
PO.DAAC collections and keeps only `GSM-*` files by default. Use `--dry-run`
first to list matching files without downloading.

## Reproducibility and Scientific Use

The detailed status above distinguishes computational completeness from
scientific confirmation. Users should preserve product provenance, monthly
sampling bounds, environmental-correction choices, and spatial-operator
definitions when reproducing or comparing results.

## Citation

Formal citation metadata and a DOI have not yet been assigned. Until a release
is archived, cite this GitHub repository together with the original providers
of every upstream dataset used in an analysis.

## License

A project-wide license has not yet been assigned. Third-party datasets and
external software retain their original terms. Add a top-level license before
the first public release so that reuse conditions for original code and
derived products are explicit.
