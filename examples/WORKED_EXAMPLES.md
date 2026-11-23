# Two worked examples

Both examples use small, invented records. Run the Python files from the repository root to see the same results.

## Which lab was available?

Imagine making a prediction at the **end of day 10** about death through day 20. Include people known to be alive at the prediction time. Use the most recently drawn lab whose result had already been released. The invented records each have at most one result per draw day.

| Case | Timeline | Day-10 input | Day-20 outcome |
|---|---|---|---|
| A | Value 4 drawn day 6 and released day 8. Value 7 drawn day 9 and released day 12. Last contact day 22. | 4 | Alive |
| B | A result from day 8 was released day 11. Death recorded on day 16. | Missing | Died |
| C | Draw on day 7 has no known release date. Last contact day 15. | Missing | Unknown |
| D | Death on day 10. | Outside the day-10 cohort | |
| E | Last seen on day 8 with no subsequent vital-status information. | Eligibility unknown, excluded | |
| F | Value 6 drawn and released on day 10. Last seen alive on day 20. | 6 | Alive |

Case B remains eligible even though the lab could not have been used. Case C remains in the prediction cohort even though the fixed-horizon outcome is unknown. Counting C as alive through day 20 would introduce an outcome error. [Run the cohort example](../landmark.py)

## What happens with fewer controls?

In a fictional trial, two of eight treated patients and four of eight controls experience an event by the same time. The full treatment-minus-control risk difference is 25% − 50% = **−25 percentage points**. Suppose outcomes are observed for only three controls, but everyone has a score at enrollment. We replay every one of the 56 possible subsets with equal weight. Treated outcomes stay fixed.

For each subset, first use the observed control event proportion. Then adjust it by adding the difference between the mean score of **all eight** controls and the mean score of the **three selected** controls. This uses baseline information from all controls. Only the benchmark calculation gets all eight outcomes. The score weight is fixed at one throughout.

For example, select three controls with zero events and scores of 0.25 each. The full control group's mean score is 0.50. The unadjusted treatment difference is +25 points. The adjusted control risk is 0 + (0.50 − 0.25) = 0.25, giving a treatment difference of zero. The errors relative to the full trial are 50 points and 25 points for this particular draw.

| Assumed score relationship | Unadjusted error | Adjusted error |
|---|---:|---:|
| Higher scores in the higher-event group | 24.4 percentage points | 21.1 percentage points |
| Same scores assigned to the opposite groups | 24.4 percentage points | 32.3 percentage points |

With the informative score, adjustment moves 38 of 56 estimates closer to the full-trial value and 18 farther away. With reversed scores, 18 move closer and 38 farther away. The replay counts each subset once and compares absolute errors within that same subset.

Error is the root mean squared distance to the full-trial risk difference across all subsets. Average signed error is zero in both scenarios by construction. A reversed score makes individual estimates less precise even though their average is unchanged. This replay assumes complete outcomes at one horizon and baseline scores available for the entire control roster. It does not estimate a hazard ratio, establish how many people a trial can forgo enrolling, or measure the benefit of a clinical model. [Run the paired replay](../control_subsets.py) · [See the tests](../tests/test_worked_examples.py)
