# How I evaluated a virtual patient model

A trial team might want to predict the course of a patient's disease, or estimate a drug's effect with fewer control outcomes. A group average can be accurate even when everyone receives the same prediction. A score that distinguishes patients within one trial can lose that ability in another. These observations shaped how I organized the evaluation.

## From clinical records to a prediction question

I directed a review of the path from clinical source tables through endpoint construction and model inputs. Two checks mattered particularly for oncology. A record that a scan took place establishes an assessment date. Calling it disease progression also requires the assessment finding and a matching endpoint rule. Similarly, a specimen collection date establishes when blood was drawn. Using the value to make a prediction requires evidence that the result was available by then.

We preserved earlier inputs during correction and separated documented mapping changes from cases that still needed a clinical interpretation of the protocol. When later anticancer therapy intervenes before recorded progression, the trial's rules determine the endpoint and censoring. A suspicious sequence of dates alone cannot settle the label. The [public worked example](../examples/WORKED_EXAMPLES.md#which-lab-was-available) makes the time-availability decision visible one record at a time.

## Comparing patients fairly

I specified a landmark question for a pancreatic cancer control arm. Among participants known to be alive at a fixed point during follow-up, could earlier measurements of the tumor marker CA19-9 and albumin help predict death over the next window? The comparisons used the same eligible patients and outcome window for a group-average forecast, a forecast based on baseline performance status, and a longitudinal survival model. We kept patients with missing labs and examined their errors separately. Follow-up ending early leaves a person's eventual status unknown.

I also directed comparisons of the candidate world model against a simpler prognostic model, keeping related trials together when splitting the data. We inspected saved predictions within trial families to ask whether the models could rank individual patients who shared a clinical setting. Reviewing the weakest fold prompted a check of both the population represented during development and the definition of the outcome. A more complex model had to earn its place against those comparisons. [Comparator designs](BASELINES.md)

## Connecting prognosis to trial design

I designed a retrospective test of a reduced-control analysis. Start with a complete randomized trial, retain the treated arm and draw a smaller subset of controls. Estimate the effect twice on the same subset, with and without help from a prespecified prognostic score. Compare each estimate to the one from all controls. Using identical subsets makes the comparison fair. Repeating this under a deliberately misleading score reveals how much an adjustment can hurt if the relationship between score and outcome changes.

Our research question concerns time-to-event treatment effects. The [public replay](../examples/WORKED_EXAMPLES.md#what-happens-with-fewer-controls) uses a fixed-horizon difference in event proportions so a reader can check every estimate by hand. Recovering a full-trial estimate and recovering the true treatment effect are distinct goals. A full trial still has sampling error.

## What would change my confidence?

The next evidentiary step is an independent, two-arm trial with a documented development history. At randomization, a frozen score would be tested for added prognostic information among patients in the same arm with similar performance status and region. That requires the original allocation information, baseline result-availability times, a complete randomized roster and documented vital-status follow-up. A lab recorded during treatment can inform a later patient prediction but cannot justify an enrollment-time trial analysis. External clinical validation and prospective control-arm reduction remain open questions.

[Hongrui's contribution](CONTRIBUTIONS.md) · [Executable examples](../README.md#three-examples-you-can-inspect)
