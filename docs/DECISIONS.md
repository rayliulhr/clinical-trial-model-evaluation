# Research decisions and next experiments

This case study describes general evaluation decisions. It contains no internal findings about a particular model or collaborator.

| Research question | Failure mode to check | Evidence that would resolve it | Next action |
|---|---|---|---|
| Why does accuracy weaken at late times? | Follow-up support changes with horizon | Risk-set/event/censoring map with aligned truncation | Restrict the horizon or collect missing support evidence before fitting |
| Does longitudinal information help? | Assessment patterns explain the apparent gain | Matched baseline / pattern / values comparison | Test incremental value under a frozen contract |
| Does the neural architecture help? | Model sees richer information or more supervision | Same-information benchmark and declared budget | Run a controlled architecture ablation |
| Can a virtual control estimate efficacy? | Different estimands and transport assumptions | Known-truth simulation plus independent trial evaluation | Validate calibration and coverage before hybrid-trial claims |

## Proposed sequence

1. Freeze task contracts and identify untouched evaluation data.
2. Audit support and saved-output provenance without fitting.
3. Run one prespecified information-ablation experiment if it addresses an unresolved scientific question.
4. Compare architectural candidates after the benchmark is stable.
5. Evaluate treatment-effect and hybrid-trial use separately with statistical collaborators.

A negative result can change the research decision productively: narrower deployment scope, a stronger baseline, a better measurement strategy, or a revised estimand. The goal is a defensible prediction system, not a predetermined model winning every comparison.

## Roles in a future collaboration

Hongrui can own biomedical question formulation, task contracts, evidence organization, and interpretation across wet-lab and computational perspectives. Modeling collaborators can own architecture and training implementation; a biostatistics collaborator should jointly define estimands, censoring assumptions, and inferential acceptance criteria. These are suggested responsibilities, not commitments made on anyone's behalf.
