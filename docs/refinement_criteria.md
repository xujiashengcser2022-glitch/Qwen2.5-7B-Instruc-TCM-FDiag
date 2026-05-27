# Multi-Agent Refinement Criteria

TCM-RAGF uses a two-stage teacher-checker strategy.

## Models

| Role | Model | Function |
|---|---|---|
| Primary teacher model | DeepSeek-R1-Distill-Llama-70B | Non-diagnostic query removal, symptom extraction, four-diagnostic restructuring, content rewriting, consistency verification, and risk detection. |
| Professional medical checking model | Baichuan-M2 | Diagnostic relevance verification, four-diagnostic attribution checking, reasoning validity, evidence-recommendation alignment, and clinical safety checking. |

## Verification Dimensions

| Dimension | Verification criterion | Risk or rejection condition | Action |
|---|---|---|---|
| Diagnostic relevance | The sample must contain clinically relevant TCM diagnostic information. | General writing, academic review, explanation-only request, or unrelated recommendation request. | Remove |
| Symptom extraction | Clinically relevant symptom description must be preserved in `filtered_symptom`. | Request-like expressions dominate the query or symptom information is missing. | Remove or rewrite |
| Four-diagnostic attribution | Evidence must be assigned to inspection, auscultation/olfaction, inquiry, palpation, or valid combinations. | Incorrect modality assignment or hallucinated tongue, pulse, odor, or observable signs. | Regenerate or remove |
| Structural completeness | The output should contain four diagnostic fields and a structured reasoning/advice section. | Missing four-diagnostic structure, empty key reasoning, or fragmented response. | Regenerate |
| Reasoning consistency | Syndrome reasoning must be supported by available symptoms and diagnostic evidence. | Contradiction between symptom evidence and syndrome inference. | Regenerate or remove |
| Evidence-recommendation alignment | Advice and formula suggestions must not exceed available evidence. | Unsupported prescription, over-specific dosage, or premature clinical conclusion. | Remove or rewrite with caution |
| Safety control | The response should include clinical caution when needed. | Emergency symptoms ignored, exaggerated efficacy, or lack of medical disclaimer. | Remove or rewrite |
| Teacher-checker agreement | DeepSeek-R1-Distill-Llama-70B and Baichuan-M2 must agree on relevance, attribution, and reasoning validity. | Disagreement on any key judgment. | Remove from the strict version or reverify after regeneration |

## Consistency Definition

Consistency is measured as agreement between the primary refinement model and the checking model on three judgments:

1. Whether the sample contains clinically relevant TCM diagnostic information.
2. Whether the extracted evidence is assigned to appropriate diagnostic fields.
3. Whether the reasoning and advice are supported by the available evidence.

A sample is retained in the strict version only when it passes diagnostic relevance, four-diagnostic attribution, reasoning validity, evidence-recommendation alignment, and safety verification.

## Risk Definition

Risk refers to content that may cause unsafe, unsupported, or misleading medical behavior, including:

- non-diagnostic requests disguised as consultation;
- unsupported medication or formula recommendation;
- hallucinated tongue or pulse information;
- contradictions between symptoms and syndrome inference;
- exaggerated therapeutic claims;
- ignored emergency symptoms;
- responses lacking appropriate clinical caution.
