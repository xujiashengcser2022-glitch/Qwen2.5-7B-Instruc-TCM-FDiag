#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate the minimal TCM-RAGF schema.

Usage:
  python scripts/validate_schema.py data/TCM-RAGF_processed_strict.json
"""

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = ["instruction", "input", "output", "filtered_symptom"]
FOUR_LABELS = ["望", "闻", "问", "切"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_schema.py data/TCM-RAGF_processed_strict.json")
        sys.exit(1)

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(data, list):
        raise ValueError("Dataset should be a JSON array.")

    errors = []
    for i, rec in enumerate(data):
        if not isinstance(rec, dict):
            errors.append((i, "record is not an object"))
            continue

        for field in REQUIRED_FIELDS:
            if field not in rec:
                errors.append((i, f"missing field: {field}"))

        output = str(rec.get("output", ""))
        for label in FOUR_LABELS:
            if label + "：" not in output and label + ":" not in output:
                errors.append((i, f"missing four-diagnostic label: {label}"))

    print(f"Total records checked: {len(data)}")
    print(f"Total errors: {len(errors)}")

    if errors:
        print("First 50 errors:")
        for idx, msg in errors[:50]:
            print(f"  record {idx}: {msg}")
        sys.exit(1)
    else:
        print("Schema validation passed.")

if __name__ == "__main__":
    main()
