# AI Prompt Engineering Portfolio

**Practical prompt design, AI-assisted development, agent architecture and reproducible evaluation.**

I am a UK student interested in artificial intelligence, programming, cybersecurity and networking. This repository documents how I design AI instructions, refine them, evaluate results and learn from failures. It contains **planned experiments and documented concepts** alongside reusable testing tools; it does not claim professional experience or unverified model performance.

> **Portfolio status:** Under development. No experimental accuracy figures have been collected yet.

## Project index

| Project | Focus | Evidence status |
|---|---|---|
| [Cybersecurity Support Assistant](projects/cybersecurity-support-assistant/README.md) | Structured vs baseline prompts for classifying fictional helpdesk tickets | Test cases and evaluation tooling prepared; results pending |
| [Multi-Agent Architecture](projects/multi-agent-architecture/README.md) | Coordinator and specialist subagent workflow design | Design concept documented; implementation pending |
| [AI Coding Experiments](projects/ai-coding-experiments/README.md) | Requirements, iterations, acceptance tests and working demos | Documentation template; case studies to add |
| [AI Model Comparisons](projects/model-comparisons/README.md) | Fair comparisons using shared tasks and scoring | Protocol prepared; data pending |
| [Prompt Optimisation](projects/prompt-optimisation/README.md) | Controlled prompt revisions and measurable improvements | Template prepared; testing pending |

## Start here: first experiment

The first project compares a minimal classification instruction with a structured prompt for fictional IT support tickets. It includes 30 labelled examples and an offline Python scoring script.

1. Open [the cybersecurity experiment guide](projects/cybersecurity-support-assistant/README.md).
2. Use [baseline prompt](prompts/baseline.md) with every case in [the dataset](data/support_cases.csv); save each category prediction.
3. Repeat using [structured prompt](prompts/structured.md), holding the model and settings fixed.
4. Copy [the CSV template](results/predictions-template.csv) to `results/baseline_predictions.csv` and `results/structured_predictions.csv`, and fill the predicted categories.
5. Run:
   ```bash
   python tools/evaluate.py results/baseline_predictions.csv
   python tools/evaluate.py results/structured_predictions.csv
   ```
6. Record your **real scores, errors, limitations and lessons** in the project guide. The dataset is small and synthetic; results should not be treated as broad real-world performance claims.

## What counts as evidence?

- Exact original and revised prompts, with personal data removed
- Model/version and the conditions of each test
- Reproducible test cases, ground truth and raw outputs
- Quantitative scores and examples of failures
- Screenshots, commit links or working code where available
- An explanation of **my contribution**, including where AI tools helped

See [GUIDE.md](GUIDE.md) for what to add next and [the case-study template](templates/project-case-study.md) for documenting new projects.

## Tools and learning areas

ChatGPT, OpenAI Codex, Python, HTML/CSS/JavaScript, AI agent workflows, prompt iteration and cybersecurity-related support scenarios.

**Notes:** Prompts and tests here are educational. Never commit API keys, private conversations or real credentials. Project statuses are deliberately conservative until evidence exists.
