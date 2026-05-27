# Preprocessing Rules

TCM-RAGF was constructed from the open ShenNong_TCM_Dataset (v0.2) through strict preprocessing, symptom extraction, four-diagnostic restructuring, and multi-agent verification.

## Pipeline

1. Extract original `instruction`, `input`, and `output` fields.
2. Check empty or invalid instruction/response fields.
3. Remove non-diagnostic or weakly diagnostic queries using the exclusion lexicon.
4. Extract clinically relevant symptoms into `filtered_symptom`.
5. Rewrite retained samples into standardized four-diagnostic fields.
6. Verify abnormal samples, annotate medical risks, and normalize TCM terminology.

## Exclusion Lexicon

| No. | Query type | English translation of exclusion patterns |
|---:|---|---|
| 1 | Fertility-related query | A couple has been together for more than two years but has not conceived. |
| 2 | Single medicine recommendation | Please recommend one Chinese medicine. |
| 3 | Academic writing | Literature review; write a paper; literature; research; review. |
| 4 | Analytical writing | Please analyze; discuss; elaborate; explain in an argumentative manner. |
| 5 | Explanation request | Please explain; introduce; give a lecture-style explanation; I would like to know. |
| 6 | Recommendation or learning request | Could you recommend; recommend one article; give me one article; I want to study; I would like to ask for advice. |
| 7 | Evaluation request | Please evaluate. |
| 8 | Other non-diagnostic requests | Please describe; please edit; article; please provide; please help me analyze; how to use plum-blossom needle; efficacy; dietary therapy plan; dietary therapy; sharing; summary. |

## Mixed Queries

If a query contains both clinically relevant symptoms and request-like expressions, the non-diagnostic request component is removed or weakened, while clinically relevant symptom evidence is retained in `filtered_symptom`.

Example:

```text
Original query:
我只有咳嗽这一个症状，请帮我推荐中药或者方剂。

filtered_symptom:
我只有咳嗽这一个症状
```
