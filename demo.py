"""Synthetic O/E teaching example. Standard library only; no clinical inputs."""
from dataclasses import dataclass
from pathlib import Path
import csv
import math
import random


@dataclass(frozen=True)
class Observation:
    time: float
    event: bool
    reference_rate: float


def summarize(rows, horizon, scale=1.0):
    """Match events and integrated reference hazard through min(Y, horizon).

    Times are months. At-risk is immediately before horizon, so Y == horizon
    is included. Censoring before horizon is strict. Zero events yield ratio 0
    if exposure > 0; zero exposure yields None, never an invented pseudocount.
    """
    if not math.isfinite(horizon) or horizon <= 0:
        raise ValueError('horizon must be positive and finite')
    if not math.isfinite(scale) or scale <= 0:
        raise ValueError('scale must be positive and finite')
    rows = tuple(rows)
    for row in rows:
        if (not math.isfinite(row.time) or row.time < 0 or
                not math.isfinite(row.reference_rate) or row.reference_rate < 0 or
                type(row.event) is not bool):
            raise ValueError('invalid observation')
    observed = sum(r.event and r.time <= horizon for r in rows)
    expected = math.fsum(r.reference_rate * scale * min(r.time, horizon)
                         for r in rows)
    at_risk = sum(r.time >= horizon for r in rows)
    censored = sum(not r.event and r.time < horizon for r in rows)
    threshold = max(20, math.ceil(0.10 * len(rows)))
    return dict(n=len(rows), events=observed, expected=expected,
                oe=observed / expected if expected > 0 else None,
                at_risk=at_risk, censored_before=censored,
                illustrative_support='passes_count_rule' if at_risk >= threshold
                else 'low_or_absent_followup')


def simulate(seed=2026, n=1000, administrative_months=30.0):
    """Arbitrary independent exponential clocks; no fit to real-world data."""
    if type(n) is not int or n <= 0:
        raise ValueError('n must be a positive integer')
    if not math.isfinite(administrative_months) or administrative_months <= 0:
        raise ValueError('administrative follow-up must be positive and finite')
    rng = random.Random(seed)
    event_rate, censor_rate = 0.04, 0.025
    rows = []
    for _ in range(n):
        event_time = rng.expovariate(event_rate)
        censor_time = min(rng.expovariate(censor_rate), administrative_months)
        rows.append(Observation(min(event_time, censor_time),
                                event_time <= censor_time, event_rate))
    return rows


def main():
    output = Path(__file__).resolve().parent / 'examples'
    output.mkdir(exist_ok=True)
    results = []
    for scenario, admin in [('long_followup', 30.0), ('short_followup', 12.0)]:
        rows = simulate(administrative_months=admin)
        for name, scale in [('matched_reference', 1.0),
                            ('half_reference_hazard', 0.5),
                            ('double_reference_hazard', 2.0)]:
            for horizon in [6, 12, 18, 24]:
                result = summarize(rows, horizon, scale)
                result.update(scenario=scenario, reference=name, months=horizon)
                results.append(result)
    fields = ['scenario', 'reference', 'months', 'n', 'events', 'expected',
              'oe', 'at_risk', 'censored_before', 'illustrative_support']
    with (output / 'summary.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for result in results:
            writer.writerow({k: f'{v:.6f}' if isinstance(v, float) else
                             'NA' if v is None else v for k, v in result.items()})
    lines = ['# Synthetic O/E walkthrough', '',
             '**All numbers below are artificial. No model training or clinical data.**', '',
             'Fixed seed: 2026. Each scenario has 1,000 synthetic individuals. Event rate: '
             '0.04/month; independent censoring rate: 0.025/month. Administrative '
             'follow-up is 30 or 12 months. Both scenarios use the same latent draws.', '',
             'The reference hazards are prespecified, not estimated. The matched reference '
             'uses the generating event rate; half/double references illustrate mis-scaling.', '',
             '| Follow-up | Reference | Month | Events | E | O/E | At risk | Count rule |',
             '|---|---|---:|---:|---:|---:|---:|---|']
    for r in results:
        ratio = 'NA' if r['oe'] is None else f"{r['oe']:.3f}"
        lines.append(f"| {r['scenario']} | {r['reference']} | {r['months']} | "
                     f"{r['events']} | {r['expected']:.2f} | {ratio} | "
                     f"{r['at_risk']} | {r['illustrative_support']} |")
    lines += ['', '## What to look for', '',
              '- Scaling the reference hazard by 0.5 doubles O/E on the same observations; '
              'scaling by 2 halves it. This is algebra, not evidence of model superiority.',
              '- In the 12-month follow-up scenario, O/E is unchanged after month 12 even '
              'though nobody remains observed at months 18 and 24. Earlier calibration '
              'does not validate that tail.',
              '- The count rule is at least max(20, 10% of N) at risk just before the horizon. '
              'It is a teaching rule, not an endorsed statistical threshold.',
              '- At month 12, people administratively censored exactly at 12 count as at risk '
              'immediately before 12. They do not supply information beyond 12.', '',
              'One synthetic draw illustrates the mechanics. It does not quantify Monte Carlo '
              'uncertainty, coverage, discrimination, subgroup calibration, or causal effects.', '']
    (output / 'REPORT.md').write_text('\n'.join(lines))
    print('Wrote synthetic aggregate outputs to examples/summary.csv and examples/REPORT.md')


if __name__ == '__main__':
    main()
