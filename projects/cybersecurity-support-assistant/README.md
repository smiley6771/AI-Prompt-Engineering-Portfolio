# Cybersecurity Support Assistant — Prompt Evaluation

**Status: Planned; experiment not yet run.**

## Goal
Evaluate whether an AI assistant can classify fictional IT support requests accurately and safely into `security`, `networking`, `hardware`, or `software`. This is a classification and evaluation project, **not** a deployed cybersecurity tool.

## Hypothesis
A prompt with explicit category definitions, decision rules and constrained output will improve classification consistency over a minimal prompt.

## Method
1. Review the 30 synthetic cases in `data/support_cases.csv`, including expected labels.
2. Run each case through the same AI model, version and settings using `prompts/baseline.md`. Save one prediction per row.
3. Repeat with `prompts/structured.md` using the same test cases.
4. Record predicted labels in `results/baseline_predictions.csv` and `results/structured_predictions.csv` (copy from the template); don't change expected labels after seeing predictions.
5. Run `python tools/evaluate.py results/baseline_predictions.csv`, and repeat for the structured predictions.
6. In this file, record model/version, date, settings, scores, examples of errors and what changed.
7. Add a second holdout set before making claims about generalisation.

## Results
| Prompt | Model/version | Correct / 30 | Accuracy | Notes |
|---|---|---:|---:|---|
| Baseline | Not tested | — | — | Awaiting experiment |
| Structured | Not tested | — | — | Awaiting experiment |

## Analysis to write after testing
- Which categories were most frequently confused?
- Did the structured prompt improve accuracy? By how much?
- Which instructions caused observable improvements or regressions?
- Did the model follow the one-word output format every time?
- How might selection bias or a small synthetic dataset limit the result?

**Ethics:** All tickets are fictional; do not upload real passwords, personal information or confidential support logs.
