"""Minimal equations used in the Kamchatka GRACE-FO analysis.

The script reads the two released gravity-field files. It demonstrates the
template metrics and states the temporal and spatial calibration principles
without exposing the private processing pipeline.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
MONTHLY_FIELDS = ROOT / "data/monthly_gravity_fields.npz"
FAULT_FIELDS = ROOT / "data/finite_fault_gravity_fields.npz"
CENTERS = ("CSR", "GFZ", "JPL")
MONTHS = (
    "2025-08", "2025-09", "2025-10", "2025-11", "2025-12",
    "2026-01", "2026-02", "2026-03", "2026-04",
)


def template_metrics(field, template, latitude, support_fraction=0.02):
    """Return area-weighted scale, correlation, and aligned-energy fraction."""
    field = np.asarray(field, dtype=float)
    template = np.asarray(template, dtype=float)
    latitude = np.asarray(latitude, dtype=float)
    weights = np.broadcast_to(np.cos(np.deg2rad(latitude))[:, None], field.shape)
    use = (
        np.isfinite(field)
        & np.isfinite(template)
        & (np.abs(template) >= support_fraction * np.nanmax(np.abs(template)))
    )
    x, t, w = field[use], template[use], weights[use]
    scale = np.sum(w * x * t) / np.sum(w * t * t)
    valid = np.isfinite(field) & np.isfinite(template)
    xc, tc, wc = field[valid], template[valid], weights[valid]
    x0 = xc - np.sum(wc * xc) / np.sum(wc)
    t0 = tc - np.sum(wc * tc) / np.sum(wc)
    correlation = np.sum(wc * x0 * t0) / np.sqrt(
        np.sum(wc * x0 * x0) * np.sum(wc * t0 * t0)
    )
    energy_fraction = np.sum(w * (scale * t) ** 2) / np.sum(w * x * x)
    return scale, correlation, energy_fraction


def fit_ridge_var(series, order=1, ridge_fraction=0.1):
    """Fit the pre-event joint autoregression used for persistence testing."""
    series = np.asarray(series, dtype=float)
    centered = series - series.mean(axis=0)
    response = centered[order:]
    predictors = np.column_stack(
        [centered[order - lag : -lag] for lag in range(1, order + 1)]
    )
    gram = predictors.T @ predictors
    penalty = ridge_fraction * np.trace(gram) / gram.shape[0]
    coefficients = np.linalg.solve(
        gram + penalty * np.eye(gram.shape[0]), predictors.T @ response
    )
    residuals = response - predictors @ coefficients
    return series.mean(axis=0), coefficients, np.cov(residuals, rowvar=False)


def sign_persistence_probability(
    pre_event, months=9, order=1, ridge_fraction=0.1,
    simulations=50_000, seed=20250729,
):
    """Simulate the probability that the three-center mean stays positive."""
    mean, coefficients, covariance = fit_ridge_var(
        pre_event, order=order, ridge_fraction=ridge_fraction
    )
    rng = np.random.default_rng(seed)
    history = np.repeat(np.asarray(pre_event)[-order:][None, :, :], simulations, 0)
    all_positive = np.ones(simulations, dtype=bool)
    for _ in range(months):
        predictors = np.concatenate([history[:, -lag, :] for lag in range(1, order + 1)], axis=1)
        innovation = rng.multivariate_normal(np.zeros(mean.size), covariance, simulations)
        next_value = (predictors - np.tile(mean, order)) @ coefficients + innovation + mean
        all_positive &= next_value.mean(axis=1) > 0
        history = np.concatenate([history[:, 1:, :], next_value[:, None, :]], axis=1)
    return (all_positive.sum() + 1) / (simulations + 1)


def standardized_score(observed, historical):
    """Standardize a source-location statistic by its pre-event distribution."""
    historical = np.asarray(historical, dtype=float)
    return (observed - historical.mean()) / historical.std(ddof=1)


def add_one_fraction(exceedances, historical_count):
    """Finite-sample exceedance fraction used for temporal/spatial calibration."""
    return (int(exceedances) + 1) / (int(historical_count) + 1)


def main():
    with np.load(MONTHLY_FIELDS, allow_pickle=False) as monthly, np.load(
        FAULT_FIELDS, allow_pickle=False
    ) as fault:
        latitude = monthly["latitude_deg"]
        template = fault["usgs_microgal"]
        print("center,month,scale,correlation,energy_fraction")
        for center in CENTERS:
            fields = monthly[f"{center.lower()}_microgal"]
            for index, month in enumerate(MONTHS):
                field = fields[index]
                scale, correlation, energy = template_metrics(field, template, latitude)
                print(f"{center},{month},{scale:.6f},{correlation:.6f},{energy:.6f}")


if __name__ == "__main__":
    main()
