# TCM-RAGF: A Four-Diagnostic Structured Dataset for TCM-Oriented Reasoning

**TCM-RAGF** is a structured Traditional Chinese Medicine (TCM) diagnostic dataset derived from the open ShenNong_TCM_Dataset. It reorganizes instruction-response samples into the classical four diagnostic methods of TCM: **inspection (望), auscultation/olfaction (闻), inquiry (问), and palpation (切)**.

This repository is released to support reproducibility, benchmarking, and non-commercial academic research for TCM-oriented large language models, retrieval-augmented generation (RAG), and diagnostic reasoning.

> **Medical disclaimer:** This dataset is for academic research and benchmark evaluation only. It must not be used as a substitute for professional medical diagnosis, treatment, prescription, dosage recommendation, or emergency medical guidance. See [Medical_Disclaimer.md](Medical_Disclaimer.md).

---

## 1. Dataset Overview

The strict released version of **TCM-RAGF** contains **99,611 structured diagnostic samples** after filtering **12,954** non-diagnostic or abnormal records from **112,565** original ShenNong-derived samples.

| Item | Value |
|---|---:|
| Original ShenNong-derived dataset size | 112,565 |
| Filtered strict TCM-RAGF dataset size | 99,611 |
| Removed samples | 12,954 |
| Filtering rate | 11.51% |
| Retention rate | 88.49% |

Each sample is formatted with four diagnostic fields. However, the four diagnostic methods are treated as **multi-label evidence categories** rather than mutually exclusive classes. Empty fields indicate that the corresponding diagnostic evidence was not provided in the original query and was not hallucinated or forcibly completed.

---

## 2. Four-Diagnostic Distribution

| Diagnostic method | Original count | Original percentage | Filtered count | Filtered percentage |
|---|---:|---:|---:|---:|
| Inspection, Wang (望) | 4,369 | 3.88% | 4,106 | 4.12% |
| Auscultation/Olfaction, Wen (闻) | 15,288 | 13.58% | 14,871 | 14.93% |
| Inquiry, Wen (问) | 112,558 | 99.99% | 99,611 | 100.00% |
| Palpation, Qie (切) | 768 | 0.68% | 566 | 0.57% |
| Total samples | 112,565 | 100.00% | 99,611 | 100.00% |

---

## 3. Diagnostic Combination Patterns

| Diagnostic combination | Original count | Original percentage | Filtered count | Filtered percentage |
|---|---:|---:|---:|---:|
| Inquiry only | 92,563 | 82.23% | 80,482 | 80.80% |
| Auscultation/Olfaction + Inquiry | 14,863 | 13.20% | 14,460 | 14.52% |
| Inspection + Inquiry | 3,969 | 3.53% | 3,721 | 3.74% |
| Inquiry + Palpation | 734 | 0.65% | 535 | 0.54% |
| Inspection + Auscultation/Olfaction + Inquiry | 395 | 0.35% | 382 | 0.38% |
| Auscultation/Olfaction + Inquiry + Palpation | 29 | 0.03% | 28 | 0.03% |
| Inspection + Inquiry + Palpation | 4 | 0.00% | 2 | 0.00% |
| All four diagnostic methods | 1 | 0.00% | 1 | 0.00% |
| Total samples | 112,565 | 100.00% | 99,611 | 100.00% |

---

## 4. Repository Structure

```text
TCM-RAGF/
├── README.md
├── LICENSE.md
├── Medical_Disclaimer.md
├── CITATION.cff
├── data/
│   ├── TCM-RAGF_processed_strict.json        # place the full released dataset here
│   └── sample_3.json                         # small representative sample
├── docs/
│   ├── dataset_schema.md
│   ├── preprocessing_rules.md
│   ├── refinement_criteria.md
│   └── four_diagnostic_statistics.md
├── scripts/
│   ├── compute_statistics.py
│   └── validate_schema.py
└── tables/
    ├── four_diagnostic_distribution.csv
    └── diagnostic_combination_patterns.csv
```

The full dataset file `TCM-RAGF_processed_strict.json` should be placed under `data/`. The small sample file is provided only to illustrate the schema.

---

## 5. Data Schema

Each record follows the schema below:

```json
{
  "instruction": "string",
  "input": "string",
  "output": "string",
  "filtered_symptom": "string"
}
```

The `output` field begins with four diagnostic fields:

```text
望：
闻：
问：
切：

推理过程：
中医建议：
中药或方剂推荐：
```

A missing four-diagnostic field should remain empty rather than being inferred.

---

## 6. Construction Pipeline

The preprocessing and restructuring pipeline contains six steps:

1. Extract the original `instruction`, `input`, and `output` fields.
2. Check empty or invalid instruction/response fields.
3. Remove non-diagnostic or weakly diagnostic queries using a predefined exclusion lexicon.
4. Extract clinically relevant symptom descriptions into `filtered_symptom`.
5. Rewrite retained content into standardized four-diagnostic fields.
6. Perform abnormal-sample verification, medical-risk annotation, and terminology normalization.

---

## 7. Multi-Agent Refinement

TCM-RAGF uses a two-stage teacher-checker strategy:

- **DeepSeek-R1-Distill-Llama-70B**: primary teacher model for non-diagnostic query removal, symptom extraction, four-diagnostic restructuring, content rewriting, consistency verification, and risk detection.
- **Baichuan-M2**: professional medical checking model for diagnostic relevance, four-diagnostic attribution, reasoning validity, evidence-recommendation alignment, and clinical safety checking.

A sample is retained in the strict version only when it passes diagnostic relevance, modality attribution, reasoning validity, evidence-recommendation alignment, and safety verification.

---

## 8. License

This dataset is released for **non-commercial academic research** under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

See [LICENSE.md](LICENSE.md).

---

## 9. Citation

If you use TCM-RAGF, please cite:

```bibtex
@article{xu2026tcmragf,
  title   = {A Structured TCM-Oriented Language Model Based on Four Diagnostic Methods},
  author  = {Xu, Jiasheng and Zhang, Yushi},
  journal = {Data Intelligence},
  year    = {2026},
  note    = {Manuscript ID: DI-2026-0115}
}
```

---

## 10. Contact

For questions about the dataset, please contact:

- Jiasheng Xu
- Corresponding author: Yushi Zhang, `zhangyushibest@126.com`
