# Released gravity fields

Only two compact data products are included.

## `monthly_gravity_fields.npz`

- `latitude_deg`, `longitude_deg_east`: grid coordinates;
- `month`: nine complete months from 2025-08 through 2026-04;
- `csr_microgal`, `gfz_microgal`, `jpl_microgal`: final environmentally
  corrected radial-gravity residuals for the three processing centers;
- `center_median_microgal`: grid-cell median of the three fields.

## `finite_fault_gravity_fields.npz`

- `latitude_deg`, `longitude_deg_east`: grid coordinates;
- `usgs_microgal`: USGS finite-fault gravity prediction;
- `gnss_microgal`: independent GNSS finite-fault gravity prediction;
- `usgs_moment_nm`, `gnss_moment_nm`: scalar moments used by the two models;
- `maximum_degree`, `decorrelation_filter`, `gaussian_radius_km`: common
  satellite-gravity spatial operator.

All fields use microGal and the positive-downward radial-gravity convention.
Load either file with `numpy.load(path, allow_pickle=False)`.
