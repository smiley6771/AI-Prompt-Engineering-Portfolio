"""Evaluate saved predictions against the fictional helpdesk dataset.

Usage:
  python tools/evaluate.py results/baseline_predictions.csv
Prediction CSV columns: id,predicted_category
"""
import csv
import sys
from pathlib import Path

CATEGORIES = {"security", "networking", "hardware", "software"}
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "support_cases.csv"

def load_rows(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    predictions = Path(sys.argv[1])
    if not predictions.is_file():
        print(f"Missing file: {predictions}")
        return 2
    truth = load_rows(DATA)
    guesses = load_rows(predictions)
    expected = {r["id"]: r["expected_category"] for r in truth}
    ids = [r.get("id", "") for r in guesses]
    if len(ids) != len(set(ids)):
        print("Error: duplicate IDs in prediction file")
        return 2
    observed = {r["id"]: r.get("predicted_category", "").strip().lower() for r in guesses}
    if set(observed) != set(expected):
        print("Error: predictions must include exactly the IDs in data/support_cases.csv")
        return 2
    if any(p not in CATEGORIES for p in observed.values()):
        print("Error: fill every predicted_category with one of: " + ", ".join(sorted(CATEGORIES)))
        return 2
    correct = sum(observed[k] == v for k, v in expected.items())
    print(f"Accuracy: {correct}/{len(expected)} ({correct / len(expected):.1%})")
    for cat in sorted(CATEGORIES):
        members = [k for k, v in expected.items() if v == cat]
        matches = sum(observed[k] == cat for k in members)
        print(f"{cat}: {matches}/{len(members)} correct")
    mistakes = [(k, expected[k], observed[k]) for k in expected if expected[k] != observed[k]]
    if mistakes:
        print("Mismatches (id, expected, predicted):")
        for k, want, got in mistakes:
            print(f"  {k}: {want} -> {got}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
