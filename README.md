# Virtual Patient | Clinical Trial Model Evaluation

**Hongrui Liu · Biomedical Sciences PhD candidate, Johns Hopkins University**

I lead a line of model evaluation in a collaborative oncology research project exploring patient world models. We ask two questions. Can a model tell which patients face greater near-term risk? If we observe outcomes for fewer controls, can a prognostic score help us recover the treatment effect we would have estimated with the full control group?

My contribution is deciding how to test those claims. I traced clinical endpoints and lab times back to their sources, specified comparisons against simple clinical baselines, and investigated where a model lost accuracy across trials or in patients with missing measurements. I used AI-assisted coding and review to turn these questions into reproducible checks. [Project case study](docs/PROJECT.md) · [Contributions and authorship](docs/CONTRIBUTIONS.md)

## Three examples you can inspect

| Question | What you can see | Code |
|---|---|---|
| What did the model know when it made a prediction? | A blood draw precedes the prediction, but its result arrives later. Four of six fictional cases qualify for prediction, including two with no usable lab. [See the timelines](examples/WORKED_EXAMPLES.md#which-lab-was-available) | [Landmark cohort](landmark.py) |
| Does good group calibration tell us how far ahead we can predict? | There are 461 people under observation at month 12 and zero at month 18 in the short-follow-up example. The observed/expected ratio stays at 1.073. [See the report](examples/REPORT.md) | [Survival calibration](demo.py) |
| Can a score help when fewer control outcomes are observed? | Across all 56 ways to select three of eight fictional controls, the estimation error falls from 24.4 to 21.1 percentage points with an informative score. Reversing its direction raises the error to 32.3 points. [See the calculation](examples/WORKED_EXAMPLES.md#what-happens-with-fewer-controls) | [Paired subset replay](control_subsets.py) |

These numbers come from the public synthetic examples. The clinical study designs, decisions and remaining validation questions are described in the [case study](docs/PROJECT.md).

## Run it locally

From the repository root, with Python 3.9+ and its standard library:

```bash
python3 landmark.py
python3 control_subsets.py
python3 demo.py
python3 -m unittest discover -s tests -v
```

The first two programs print their results. The calibration example regenerates its [CSV](examples/summary.csv) and [report](examples/REPORT.md) from a fixed seed.

## Methods

[Clinical prediction and treatment-effect questions](docs/TASKS.md) · [Choosing fair comparators](docs/BASELINES.md) · [Checking follow-up support](docs/SUPPORT.md) · [Research decisions](docs/DECISIONS.md) · [Public references](docs/REFERENCES.md) · [Data and publication scope](docs/DATA_AND_PUBLICATION.md)
