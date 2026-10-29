# Public methodological references

1. [ICH E9(R1), FDA guidance (2021)](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e9r1-statistical-principles-clinical-trials-addendum-estimands-and-sensitivity-analysis-clinical). Supports defining the treatment effect of interest and aligning design, analysis, and sensitivity analysis. It is not an endorsement of this portfolio.
2. [Haider et al., Effective Ways to Build and Evaluate Individual Survival Distributions, JMLR (2020)](https://jmlr.csail.mit.edu/papers/volume21/18-772/18-772.pdf). Discusses survival-distribution evaluation, calibration, and censoring-adjusted Brier scores.
3. [Kvamme and Borgan, The Brier Score under Administrative Censoring: Problems and Solutions](https://arxiv.org/abs/1912.08581). Explains why censoring assumptions and administrative follow-up deserve explicit attention when scoring survival predictions.

The demo's O/E expression is implemented directly from the definitions of observed events and integrated reference hazard over observed exposure. For a constant reference rate lambda, Hhat(t)=lambda*t. It does not implement IPCW Brier, Cox regression, Kaplan-Meier, GRUs, or a causal effect estimator. No source code was copied from these references.

References were checked during portfolio preparation on October 28, 2026 (America/New_York). The repository's task templates are author-developed educational designs, not validated protocols.
