# Core analysis code

`core_analysis.py` is the complete public code component. It contains only the
methods needed to understand the paper's central tests:

- area-weighted template scale, spatial correlation, and aligned energy;
- ridge-regularized joint autoregression for the three processing centers;
- simulated sign-persistence probability;
- standardized spatial score and finite-sample add-one fraction.

Run the direct event-field calculation from the repository root:

```bash
python code/core_analysis.py
```

The script reads the two released gravity-field files and prints monthly
field-to-template metrics. Raw-data download, preprocessing, caches,
exploratory analyses, and internal workflow code are intentionally not
included.
