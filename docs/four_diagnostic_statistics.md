# Four-Diagnostic Statistics

## Dataset Quality Statistics

| Item | Value |
|---|---:|
| Original ShenNong-derived dataset size | 112,565 |
| Filtered strict TCM-RAGF dataset size | 99,611 |
| Removed samples | 12,954 |
| Filtering rate | 11.51% |
| Retention rate | 88.49% |
| Inspection samples in the filtered dataset | 4,106 |
| Auscultation/Olfaction samples in the filtered dataset | 14,871 |
| Inquiry samples in the filtered dataset | 99,611 |
| Palpation samples in the filtered dataset | 566 |
| Most frequent diagnostic pattern | Inquiry only: 80,482 samples, 80.80% |
| Second most frequent diagnostic pattern | Auscultation/Olfaction + Inquiry: 14,460 samples, 14.52% |
| Teacher-checker consistency | Operationalized as a binary retention criterion. Only samples passing diagnostic relevance, modality attribution, reasoning validity, and safety verification are retained. |

## Interpretation

The dominance of inquiry reflects the fact that most source samples are user-provided symptom descriptions or consultation questions. Inspection, auscultation/olfaction, and palpation appear when observable signs, sound- or odor-related symptoms, or pulse/palpation evidence are explicitly available.
