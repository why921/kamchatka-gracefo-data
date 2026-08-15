# Kamchatka GRACE-FO gravity fields

Minimal data and code release accompanying the manuscript:

> *GRACE-FO Reveals a Persistent Gravity-Field Anomaly Following the 2025
> Mw 8.8 Kamchatka Earthquake*

This repository contains only the final monthly radial-gravity fields, two
finite-fault gravity predictions, the final paper figures, and a compact
implementation of the core comparison metrics.

## Contents

```text
data/
  monthly_gravity_fields.npz
  finite_fault_gravity_fields.npz
code/
  core_analysis.py
figures/
  main/          Figures 1--3
  supporting/    Figures S1--S2
```

### Monthly gravity fields

`data/monthly_gravity_fields.npz` contains the final environmentally corrected
radial-gravity residuals for CSR, GFZ, and JPL, together with their grid-cell
median. The archive covers the nine complete post-event months from August
2025 through April 2026 on a 49 × 71 regional grid.

### Finite-fault predictions

`data/finite_fault_gravity_fields.npz` contains the USGS and independent GNSS
finite-fault gravity predictions after the common degree-60, Swenson--Wahr,
300-km Gaussian spatial operator.

All released fields use microGal and the positive-downward radial-gravity
convention. Variable names and metadata are documented in `data/README.md`.
File sizes and SHA-256 checksums are listed in `DATA_MANIFEST.csv`.

## Quick use

Python 3 and NumPy are sufficient:

```bash
pip install -r requirements.txt
python code/core_analysis.py
```

The script calculates area-weighted template scale, spatial correlation, and
aligned-energy fraction for each monthly field. It also provides compact
functions expressing the joint temporal-persistence and spatial-calibration
principles used in the study.

## Scope

This is a focused result release, not the complete internal processing
workspace. It intentionally excludes raw provider data, download credentials,
environmental branches, intermediate products, exploratory analyses, caches,
submission files, and internal reports.

Raw GRACE/GRACE-FO and environmental products remain subject to their provider
terms. Their authoritative locations and persistent identifiers are listed in
`DATA_SOURCES.md`.

CSR, GFZ, and JPL solutions are processing realizations of the same satellite
tracking record and should not be treated as statistically independent
observations. July 2025 is excluded because it contains both pre- and
post-earthquake days.

## Citation

Please cite the associated manuscript and the original data providers.
Repository citation metadata are provided in `CITATION.cff`; the journal DOI
will be added when available.

## License

No reuse license has yet been assigned to the authors' code and derived data.
Third-party products remain governed by their original provider terms.
