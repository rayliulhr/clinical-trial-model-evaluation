# Long-horizon calibration and support

A model can return a number long after the data stop being informative. Always read calibration together with follow-up and transport support.

## Per-horizon record

| Field | Why it is needed |
|---|---|
| Eligible and predicted counts | Distinguishes coverage from performance on selected cases |
| Observed events by tau | Shows how much event information contributes |
| Sum of cumulative hazard through min(Y,tau) | Defines the matched O/E denominator |
| At risk immediately before tau | Shows observable follow-up near the requested horizon |
| Censored before tau | Describes lost follow-up without calling it a non-event |
| Number of contributing trial families | Shows the independent support for cross-trial claims |
| Censoring survival and effective sample size, if weighted | Exposes unstable weighting and non-identifiability |
| Covariate/regimen overlap and endpoint compatibility | Separates temporal support from transport support |
| Missing predictions, exclusions, and failures | Prevents silent selection of easy cases |

The synthetic demo implements events, cumulative hazard, risk-set count, and censoring summaries only. It does not estimate a censoring model, effective sample size, transport support, or uncertainty intervals.

## Interpretation

O/E near one is a useful aggregate calibration signal under appropriate hazard and censoring assumptions. It cannot establish individual discrimination, correct curve shape, or valid counterfactual effects. Different subgroups can have offsetting errors.

Truncating both O and E at tau avoids comparing events over one window with exposure over another. With no follow-up after an administrative cutoff, later O/E values can remain numerically unchanged. They describe accumulated earlier exposure and do not validate predictions in the unobserved tail.

Risk sets may shrink through events as well as censoring. A small risk set is therefore a diagnostic flag, not proof of model failure or a universal reason to reject a horizon. The demo's rule, at least max(20, 10% of the initial population) remaining, is explicitly illustrative. Real thresholds need endpoint-specific event information, precision targets, and statistical review before seeing comparative scores.

## Proposed next evidence step

Before another fit, inventory existing predictions and labels at prespecified horizons. Verify version, row order, endpoint, and time units. Produce a support map and matched-window O/E only where saved predictions permit it. If only a scalar short-window risk is saved, do not reconstruct a long-horizon curve from it. A support-only report is a valid bounded deliverable.

End that task with three categories: estimable under the stated assumptions; estimable only within a narrower scope; or missing essential evidence. List the smallest missing artifact needed for each unresolved case. This is a design recommendation, not a report of analysis performed on clinical data here.
