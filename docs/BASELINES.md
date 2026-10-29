# Fair baseline comparison

This matrix proposes a benchmark; it reports no measured model ranking.

| Comparator | Information and fit | Purpose | Required fairness check |
|---|---|---|---|
| Historical Kaplan-Meier | Compatible historical controls only | Transparent reference for survival prediction | Freeze compatibility rules; report unavailable strata; no unmarked tail extrapolation |
| Cox or parametric survival regression | Prespecified baseline covariates | Strong, interpretable covariate-aware comparator | Check assumptions; train-only preprocessing; same endpoint and risk set |
| Flexible hazard model | Same baseline information with nonlinear effects | Test whether neural complexity adds value | Patient/family-aware validation; matched tuning budget |
| Dynamic baseline | Baseline features, fitted within the landmark risk set | Anchor a history-information experiment | Same eligible population and prediction window as history models |
| Observation-pattern model | Baseline plus counts, gaps, and missingness indicators | Separate measurement process from measured values | All timestamps available by prediction time; same feature provenance |
| History-value model | Baseline, observation pattern, and earlier measured values | Test incremental information from history | Compare against pattern model, not only baseline |
| Candidate patient world model | Explicitly declared state, action, and auxiliary supervision | Test a proposed modeling advantage | Match raw information or expose differences through separate ablations |

## Freeze before fitting

1. Clinical population, endpoint, time origin, prediction window, and allowed inputs.
2. Trial-family development and evaluation splits; all transformations learned from training data.
3. Hyperparameter search, early stopping, checkpoint selection, seeds, and compute budget.
4. Primary metric, uncertainty method, missing-prediction handling, and support rules.
5. An all-eligible coverage report plus a paired comparison on common estimable cases.

Separate an information advantage from an architecture advantage. Auxiliary longitudinal labels, additional regimen detail, extra training arms, and different feature encodings can change the question being answered. Equal epochs alone do not establish equal selection budgets.

Report trial-macro and patient-micro summaries separately. For cross-trial generalization, use trial/family-level uncertainty rather than treating correlated patient predictions, random seeds, or time points as independent trials. With few trial families, state how limited that inference is.

## A bounded proposed experiment

Compare baseline, baseline+observation-pattern, and baseline+pattern+history-value models within one frozen landmark contract. Use the same eligible population, split, selection rule, and budget. The principal contrast is history-value versus pattern, which asks whether measured values add information beyond when and how often patients were assessed.

Prespecify a clinically meaningful improvement threshold with domain and statistical collaborators. A small score change alone is not a reason to increase architecture complexity. This experiment is proposed, not run by this portfolio.
