# Dataset Schema

Each TCM-RAGF record is stored as a JSON object.

## Required Fields

| Field | Type | Description |
|---|---|---|
| `instruction` | string | Original or rewritten user instruction/question. |
| `input` | string | Optional supplementary input. Often empty. |
| `output` | string | Structured four-diagnostic output followed by reasoning, advice, and cautious formula/herbal suggestion if applicable. |
| `filtered_symptom` | string | Clinically relevant symptom description extracted after removing non-diagnostic request components. |

## Output Format

The `output` field is expected to follow this structure:

```text
望：
闻：
问：
切：

根据以上情况可能是……
推理过程：……
中医建议：……
中药或方剂推荐：……
```

## Four Diagnostic Fields

| Field | English name | Description |
|---|---|---|
| 望 | Inspection | Observable signs such as tongue, complexion, swelling, rash, and local appearance. |
| 闻 | Auscultation/Olfaction | Voice, cough, breathing, sound-related cues, and odor-related cues. |
| 问 | Inquiry | Subjective symptoms, chief complaint, duration, pain, sleep, appetite, stool, urine, cold/heat, and medical history. |
| 切 | Palpation | Pulse condition, abdominal palpation, tenderness, and palpation-related signs. |

## Missing Information Rule

Unreported diagnostic information must remain empty. The dataset construction explicitly avoids hallucinating tongue, pulse, odor, complexion, or palpation evidence when such information is not provided in the original query.
