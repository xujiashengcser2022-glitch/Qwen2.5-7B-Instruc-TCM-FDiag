#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compute basic TCM-RAGF statistics.

Usage:
  python scripts/compute_statistics.py data/TCM-RAGF_processed_strict.json

The script expects a JSON array of records. Each record should contain at least:
  instruction, output, filtered_symptom
"""

import json
import sys
from pathlib import Path
from collections import Counter

def load_json(path: Path):
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("Expected a JSON array of records.")
    return data

def has_nonempty_after_label(output: str, label: str) -> bool:
    """
    Detect whether a four-diagnostic label has non-empty content on the same line.
    Example labels: 望, 闻, 问, 切
    """
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith(label + "：") or stripped.startswith(label + ":"):
            content = stripped.split("：", 1)[-1] if "：" in stripped else stripped.split(":", 1)[-1]
            return bool(content.strip())
    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/compute_statistics.py data/TCM-RAGF_processed_strict.json")
        sys.exit(1)

    path = Path(sys.argv[1])
    data = load_json(path)

    total = len(data)
    modality_counts = Counter()
    combination_counts = Counter()
    missing_required = Counter()

    required = ["instruction", "output", "filtered_symptom"]

    for rec in data:
        for key in required:
            if key not in rec or not str(rec.get(key, "")).strip():
                missing_required[key] += 1

        output = str(rec.get("output", ""))
        modalities = []
        if has_nonempty_after_label(output, "望"):
            modalities.append("Inspection")
        if has_nonempty_after_label(output, "闻"):
            modalities.append("Auscultation/Olfaction")
        if has_nonempty_after_label(output, "问"):
            modalities.append("Inquiry")
        if has_nonempty_after_label(output, "切"):
            modalities.append("Palpation")

        for m in modalities:
            modality_counts[m] += 1

        if modalities:
            combination_counts[" + ".join(modalities)] += 1
        else:
            combination_counts["No explicit four-diagnostic evidence"] += 1

    print("Total records:", total)
    print("\nMissing required fields:")
    for k in required:
        print(f"  {k}: {missing_required[k]}")

    print("\nModality counts:")
    for key in ["Inspection", "Auscultation/Olfaction", "Inquiry", "Palpation"]:
        count = modality_counts[key]
        pct = count / total * 100 if total else 0
        print(f"  {key}: {count} ({pct:.2f}%)")

    print("\nTop diagnostic combinations:")
    for combo, count in combination_counts.most_common(20):
        pct = count / total * 100 if total else 0
        print(f"  {combo}: {count} ({pct:.2f}%)")

if __name__ == "__main__":
    main()
