# Clinical Trial Model Evaluation

**A research portfolio by Hongrui Liu | Biomedical Sciences PhD candidate, Johns Hopkins University**

How do we decide whether a patient-outcome model is reliable enough to inform a clinical trial research question?

This portfolio connects biological and clinical questions to explicit prediction tasks, fair comparisons, and reproducible evaluation. It includes a small, independently written synthetic example of survival calibration and follow-up support, plus a research design framework for evaluating patient models.

## My contribution

My role in the broader collaborative research effort has focused on framing the scientific questions, directing evidence checks, and developing evaluation and next-experiment plans with AI assistance. In this portfolio, I organize that approach into three practical questions:

- What information is available at the moment a prediction is made?
- Are competing models answering the same question with comparable data and selection budgets?
- When does follow-up support justify a reported metric, and when should we withhold a conclusion?

See [contributions and authorship](docs/CONTRIBUTIONS.md) for the scope of my work and the role of AI assistance. This repository contains newly prepared educational material. It does not reproduce the collaborative project's implementation or disclose its findings.

## Start here

| Artifact | What it demonstrates |
|---|---|
| [Three task contracts](docs/TASKS.md) | Separating enrollment prediction, dynamic prediction, and treatment-effect estimation |
| [Fair baseline matrix](docs/BASELINES.md) | Designing comparisons that can support a scientific conclusion |
| [Long-horizon support](docs/SUPPORT.md) | Interpreting calibration alongside censoring, coverage, and extrapolation |
| [Synthetic walkthrough](examples/REPORT.md) | Executable calculations with transparent assumptions |
| [Evaluation decisions](docs/DECISIONS.md) | Turning failure modes into bounded next experiments |
| [Public references](docs/REFERENCES.md) | Methodological sources and implementation scope |

## Run the synthetic example

Python 3.9 or newer; standard library only. No downloads, credentials, model weights, or training.

```bash
python3 demo.py
python3 -m unittest discover -s tests -v
```

The first command writes only aggregate synthetic outputs to `examples/summary.csv` and `examples/REPORT.md`. Repeating it with the default seed reproduces those files. No real patient information is read. The demo compares prespecified hazards, not fitted machine-learning models.

The example shows how the same observed events can give different O/E values when predicted hazards are mis-scaled, and why a finite long-horizon score can coexist with no follow-up at that horizon. It is an educational calculation, not a validation study or a drug-efficacy estimate.

## Scope and status

Implemented: synthetic data generation in memory, matched O/E truncation, follow-up summaries, aggregate outputs, and unit tests. Designed: dynamic prediction and treatment-effect evaluation contracts. No GRU training, clinical benchmark, counterfactual validation, or patient-level dataset is included.

The public package is intentionally self-contained. It contains no private source snapshots, internal results, correspondence, meeting records, or model weights. See [data and publication boundaries](docs/DATA_AND_PUBLICATION.md).
