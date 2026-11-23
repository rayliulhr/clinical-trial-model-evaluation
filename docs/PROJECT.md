# From an uncertain endpoint to a testable patient prediction

**My contribution.** I led a line of scientific evaluation within our collaborative virtual patient project. My work connected the clinical meaning of an endpoint to cohort construction, model comparisons and the decision about which question to test next. Three decisions illustrate that work.

## 1. Establish what happened to the patient

An oncology trial can record a scan, a new treatment and a later progression entry for the same patient. Reproducing a label from those dates shows how the software behaved. Determining which one counts as the endpoint requires the assessment finding and the version of the trial protocol that defines progression and censoring.

I directed a trace from the original tables and field labels through the transformation code to the derived outcomes. We isolated supported corrections, including where the software looked for a documented death date, and preserved the original inputs. When the applicable censoring rule remained uncertain, I kept those cases open for clinical adjudication. This let the project advance on a mortality question with a defined follow-up window while preserving the progression question for review.

## 2. Make a fair test of individual prediction

For a pancreatic cancer control arm, I specified a comparison among patients alive at day 84. Could baseline physical functioning and earlier measurements of **CA19-9** and **albumin** improve prediction of death by day 168? CA19-9 is a tumor marker. Albumin is a blood protein routinely measured in clinical care.

| Design choice | Why it mattered |
|---|---|
| Compare a group-average forecast, baseline performance status and the longitudinal model on the same patients and time window. | Otherwise one model could look better because it was evaluated on an easier group. |
| Keep people who have no usable lab and examine them separately. | Dropping them would conceal how the model behaves when a clinician has less information. |
| Distinguish collection time from result availability, and early loss to follow-up from survival. | The first distinction prevents future information from entering the model. The second prevents an unknown outcome from being labeled as survival. |

In a separate cross-trial comparison, I kept related trials together in the evaluation split and examined the group on which performance deteriorated most. I checked the representation of that clinical population in development and the endpoint mapping before considering changes to the model. [Matched comparator designs](BASELINES.md) · [Prediction-time rules in six fictional records](../examples/WORKED_EXAMPLES.md#which-lab-was-available)

## 3. Test what a smaller control group could recover

A team considering fewer control outcomes needs to know how far its treatment-effect estimate might move. I designed a paired comparison that holds the treatment arm fixed, selects a smaller control group, and calculates the effect twice on exactly those patients. Both estimates are judged against the estimate from the complete trial. I included a score whose relationship with outcome reverses, so the design exposes a circumstance in which adjustment can hurt.

The public example uses an event proportion at a fixed time, which makes every calculation checkable by hand. It reproduces the logic of the comparison. The clinical research question uses a time-to-event endpoint and requires a separate hazard-ratio analysis. The full-trial estimate also has sampling error. [Worked example and exact replay](../examples/WORKED_EXAMPLES.md#what-happens-with-fewer-controls)

## What would justify the next step?

I specified a test on a two-arm trial held out of development. At randomization, can a frozen score distinguish prognosis among patients in the same arm with similar performance status and region? The prerequisites are documented independence, original allocation records, evidence of which baseline labs had been reported, and complete rules for death follow-up. An independent clinical evaluation remains the next milestone.

[Contributions and authorship](CONTRIBUTIONS.md) · [Public implementations](../README.md#three-examples-you-can-inspect)
