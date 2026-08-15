# Kamchatka GRACE-FO gravity anomaly

This repository contains the **minimal public reproducibility package** for:

> *GRACE-FO Reveals a Persistent Gravity-Field Anomaly Following the 2025
> Mw 8.8 Kamchatka Earthquake*

It is intentionally limited to the final gravity fields, final figures, and a
compact statement of the core analysis principles. Raw provider data, local
caches, intermediate experiments, submission files, and internal project
reports are not redistributed here.

## What is included

- `data/monthly_gravity_fields.npz`: final radial-gravity fields for CSR, GFZ,
  JPL, and their center median from August 2025 through April 2026.
- `data/finite_fault_gravity_fields.npz`: the USGS and GNSS finite-fault
  gravity predictions after the common satellite-gravity spatial operator.
- `figures/main/`: final manuscript Figures 1--3.
- `figures/supporting/`: Supporting Information Figures S1--S2.
- `code/core_analysis.py`: a compact implementation of the central equations
  and statistical principles.

See `DATA_MANIFEST.csv` for file sizes and SHA-256 checksums.

## Scientific scope

The released material supports the manuscript's three core tests:

1. finite-fault prediction at GRACE-FO spatial resolution;
2. persistence and environmental sensitivity of the template-aligned anomaly;
3. spatial localization and detection/robustness diagnostics.

The processing centers share the same satellite tracking record and are not
treated as statistically independent observations. July 2025 is omitted from
the post-event analysis because it mixes pre- and post-origin days; the nine
complete post-event months run from August 2025 through April 2026.

## Data not redistributed

The package does not contain raw GRACE/GRACE-FO, AOD1B, GLDAS, ERA5-Land,
CMEMS, ECCO, GEBCO, or third-party finite-fault archives. These products can be
large, may require user registration, and remain subject to provider terms.
Download locations and persistent identifiers are listed in `DATA_SOURCES.md`.

## Code use

The public script intentionally contains only the core equations rather than
the full internal workflow. It demonstrates template metrics directly in the
released radial-gravity representation and provides reusable implementations
of the temporal-persistence and spatial-calibration principles. NumPy is the
only dependency.

## Citation

Please cite the associated manuscript and the original data providers. Until a
journal DOI is assigned, citation metadata for this repository are available
in `CITATION.cff`.

## License

No reuse license has yet been assigned to the authors' code and derived data.
Third-party data remain governed by their original provider terms. A license
should be selected before the first public release.
