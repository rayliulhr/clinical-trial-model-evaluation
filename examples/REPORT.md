# Synthetic O/E walkthrough

**All numbers below are artificial. No model training or clinical data.**

Fixed seed: 2026. Each scenario has 1,000 synthetic individuals. Event rate: 0.04/month; independent censoring rate: 0.025/month. Administrative follow-up is 30 or 12 months. Both scenarios use the same latent draws.

The reference hazards are prespecified, not estimated. The matched reference uses the generating event rate; half/double references illustrate mis-scaling.

| Follow-up | Reference | Month | Events | E | O/E | At risk | Count rule |
|---|---|---:|---:|---:|---:|---:|---|
| long_followup | matched_reference | 6 | 214 | 198.28 | 1.079 | 664 | passes_count_rule |
| long_followup | matched_reference | 12 | 356 | 331.89 | 1.073 | 461 | passes_count_rule |
| long_followup | matched_reference | 18 | 448 | 423.97 | 1.057 | 310 | passes_count_rule |
| long_followup | matched_reference | 24 | 517 | 484.28 | 1.068 | 199 | passes_count_rule |
| long_followup | half_reference_hazard | 6 | 214 | 99.14 | 2.159 | 664 | passes_count_rule |
| long_followup | half_reference_hazard | 12 | 356 | 165.95 | 2.145 | 461 | passes_count_rule |
| long_followup | half_reference_hazard | 18 | 448 | 211.99 | 2.113 | 310 | passes_count_rule |
| long_followup | half_reference_hazard | 24 | 517 | 242.14 | 2.135 | 199 | passes_count_rule |
| long_followup | double_reference_hazard | 6 | 214 | 396.57 | 0.540 | 664 | passes_count_rule |
| long_followup | double_reference_hazard | 12 | 356 | 663.78 | 0.536 | 461 | passes_count_rule |
| long_followup | double_reference_hazard | 18 | 448 | 847.94 | 0.528 | 310 | passes_count_rule |
| long_followup | double_reference_hazard | 24 | 517 | 968.56 | 0.534 | 199 | passes_count_rule |
| short_followup | matched_reference | 6 | 214 | 198.28 | 1.079 | 664 | passes_count_rule |
| short_followup | matched_reference | 12 | 356 | 331.89 | 1.073 | 461 | passes_count_rule |
| short_followup | matched_reference | 18 | 356 | 331.89 | 1.073 | 0 | low_or_absent_followup |
| short_followup | matched_reference | 24 | 356 | 331.89 | 1.073 | 0 | low_or_absent_followup |
| short_followup | half_reference_hazard | 6 | 214 | 99.14 | 2.159 | 664 | passes_count_rule |
| short_followup | half_reference_hazard | 12 | 356 | 165.95 | 2.145 | 461 | passes_count_rule |
| short_followup | half_reference_hazard | 18 | 356 | 165.95 | 2.145 | 0 | low_or_absent_followup |
| short_followup | half_reference_hazard | 24 | 356 | 165.95 | 2.145 | 0 | low_or_absent_followup |
| short_followup | double_reference_hazard | 6 | 214 | 396.57 | 0.540 | 664 | passes_count_rule |
| short_followup | double_reference_hazard | 12 | 356 | 663.78 | 0.536 | 461 | passes_count_rule |
| short_followup | double_reference_hazard | 18 | 356 | 663.78 | 0.536 | 0 | low_or_absent_followup |
| short_followup | double_reference_hazard | 24 | 356 | 663.78 | 0.536 | 0 | low_or_absent_followup |

## What to look for

- Scaling the reference hazard by 0.5 doubles O/E on the same observations; scaling by 2 halves it. This is algebra, not evidence of model superiority.
- In the 12-month follow-up scenario, O/E is unchanged after month 12 even though nobody remains observed at months 18 and 24. Earlier calibration does not validate that tail.
- The count rule is at least max(20, 10% of N) at risk just before the horizon. It is a teaching rule, not an endorsed statistical threshold.
- At month 12, people administratively censored exactly at 12 count as at risk immediately before 12. They do not supply information beyond 12.

One synthetic draw illustrates the mechanics. It does not quantify Monte Carlo uncertainty, coverage, discrimination, subgroup calibration, or causal effects.
