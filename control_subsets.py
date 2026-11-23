"""Exact replay of all three-of-eight control subsets in a fictional trial."""

from itertools import combinations
from math import sqrt
from statistics import mean

# Complete binary outcomes at one fixed horizon, ordered by baseline score group.
CONTROL_EVENTS = (0, 0, 0, 1, 0, 1, 1, 1)
TREATED_EVENTS = (0, 0, 0, 0, 0, 0, 1, 1)
ALIGNED = (0.25,) * 4 + (0.75,) * 4
REVERSED = (0.75,) * 4 + (0.25,) * 4


def replay(control_events, treated_events, scores, sample_size):
    """Compare paired treatment-minus-control risk differences to the full trial.

    All control scores are available at enrollment. Reduced estimates access
    outcomes only for selected controls. Full outcomes define the reference.
    """
    if len(scores) != len(control_events) or not 1 <= sample_size <= len(scores):
        raise ValueError("Supply one score per control and a valid subset size.")
    reference = mean(treated_events) - mean(control_events)
    treated_risk = mean(treated_events)
    target_score = mean(scores)
    pairs = []
    for subset in combinations(range(len(scores)), sample_size):
        control_risk = mean(control_events[i] for i in subset)
        sample_score = mean(scores[i] for i in subset)
        unadjusted = treated_risk - control_risk
        adjusted = unadjusted - (target_score - sample_score)
        pairs.append((unadjusted, adjusted))
    return reference, pairs


def rmse(estimates, reference):
    return sqrt(mean((value - reference) ** 2 for value in estimates))


def main():
    print("Score | Subsets | Full difference | Unadjusted RMSE | Adjusted RMSE")
    for label, scores in (("aligned", ALIGNED), ("reversed", REVERSED)):
        reference, pairs = replay(CONTROL_EVENTS, TREATED_EVENTS, scores, 3)
        unadjusted, adjusted = zip(*pairs)
        print(f"{label} | {len(pairs)} | {reference:.3f} | "
              f"{rmse(unadjusted, reference):.3f} | {rmse(adjusted, reference):.3f}")


if __name__ == "__main__":
    main()
