# Three task contracts

These are general research design templates, not a disclosure of a particular team's protocol. Before using them, specify the disease, endpoint definition, time origin, treatment strategy, intercurrent-event handling, and target population. Distinguish prediction accuracy from causal treatment-effect identification.

| Contract | Prediction-time information | Target | Evaluation and reference | Main risk |
|---|---|---|---|---|
| A. Enrollment control prognosis | Baseline measurements genuinely available at time zero; intended control strategy | Individual survival curve under the specified control setting | Horizon-matched calibration, survival-curve error, and follow-up support in held-out trial families | Trial shift, unavailable baseline information, unsupported tail |
| B. Landmark dynamic prognosis | Baseline and history available by a prespecified landmark L | Event probability over (L, H] among those event-free at L | Censoring-aware Brier score and calibration in the same landmark population | Future information, observation-pattern confounding, early censoring |
| C. Treatment-effect estimation with a virtual control | Prespecified baseline information and control strategy, plus observed treatment-arm outcomes for an outcome-informed estimator | A precisely defined contrast between treatment and control | Known-truth simulations followed by independent randomized-trial reference estimates with uncertainty | Transportability, confounding, estimand mismatch, shared-outcome dependence |

## A: Enrollment prediction

Choose a time origin before constructing features. A sample collected before enrollment but reported later is not necessarily available at enrollment. Separate prediction of an observed control population from a causal claim about outcomes under a different treatment.

The implemented example uses hazard calibration. With observed time Y=min(T,C), event indicator delta, and predicted cumulative hazard Hhat:

```
O(tau) = sum(delta_i * I(Y_i <= tau))
E(tau) = sum(Hhat_i(min(Y_i, tau)))
O/E(tau) = O(tau) / E(tau)
```

Both quantities use the same people and cutoff. E is expected event accumulation over observed exposure under the reference hazard; it is not the sum of fixed-horizon event probabilities. Zero events produce O/E=0 when E>0; log(O/E) is then undefined. E=0 makes the ratio undefined. Do not add arbitrary pseudo-events to conceal these cases.

## B: Dynamic prediction

An illustrative landmark is day 90 with prediction through day 180. These dates are educational choices. Use people known to be event-free and observed at the landmark; define whether events exactly at the landmark are excluded. Features must be available by that time, not merely carry an earlier collection timestamp.

A person censored between L and H has an unknown binary outcome at H. Do not label that person a non-event. A censoring-adjusted score requires a justified estimate of the censoring distribution and sufficient support. Conditional censoring may require covariates. Define time ties, weighting, and the eligible denominator before comparison.

This repository does not implement that score. See the survival-evaluation references for IPCW assumptions and methods.

## C: Treatment effects

A hazard ratio compares instantaneous hazards; a hazard ratio of 0.5 does not generally imply a 50% reduction in fixed-time event risk. Proportional hazards does not require exponential survival. An O/E multiplier relative to an individual predicted control hazard is not automatically the same estimand as an unadjusted two-arm Cox estimate.

If the estimator uses observed treatment-arm outcomes, call it outcome-informed treatment-effect estimation, not prospective prediction of efficacy from baseline alone. Specify the population, treatment conditions, endpoint, intercurrent-event strategy, follow-up window, and population summary before choosing a reference estimator. See ICH E9(R1) in [references](REFERENCES.md).

A randomized-trial estimate has sampling error. When it shares treatment outcomes with a virtual-control estimator, their errors may be dependent. Assess null calibration, bias, interval coverage, power, and Monte Carlo error in known-truth simulations. Under non-proportional hazards, prespecify an interpretable alternative such as a restricted mean survival-time contrast.

Trial families must stay together across development and evaluation. Repeated inspection turns a test set into development evidence; new independence requires new data or a genuinely untouched evaluation design.
