<h1 align="center">TCM-RAGF: A Four-Diagnostic Structured Dataset for TCM-Oriented Reasoning</h1>

<p align="center">
  <b>A structured Traditional Chinese Medicine (TCM) diagnostic dataset derived from the open ShenNong_TCM_Dataset and reorganized according to the four diagnostic methods.</b>
</p>

<p align="center">
  <b>Language:</b> English
</p>

---

## ⚡ Overview

**TCM-RAGF** is a structured dataset designed for Traditional Chinese Medicine (TCM)-oriented large language model research. It was constructed from the open **ShenNong_TCM_Dataset (v0.2)** and reorganized according to the classical four diagnostic methods of TCM:

- **Inspection (望, Wang)**
- **Auscultation/Olfaction (闻, Wen)**
- **Inquiry (问, Wen)**
- **Palpation (切, Qie)**

Unlike ordinary medical dialogue datasets or flat instruction-response corpora, TCM-RAGF explicitly separates clinically available evidence into four diagnostic fields and attaches syndrome-oriented reasoning and risk-aware responses. The dataset is intended to support research on TCM diagnostic reasoning, structured medical instruction tuning, retrieval-augmented generation (RAG), and clinical-safety-aware medical AI systems.

The strict released version contains **99,611 structured diagnostic samples**, obtained after filtering **12,954** non-diagnostic or abnormal records from **112,565** original ShenNong-derived samples. The filtering rate is **11.51%**, and the retention rate is **88.49%**.

> **Important medical disclaimer:** TCM-RAGF is intended only for academic research, benchmark evaluation, and non-commercial development of TCM-oriented AI systems. It must not be used as a substitute for professional medical diagnosis, treatment, prescription, dosage recommendation, or emergency medical guidance. See [Medical_Disclaimer.md](Medical_Disclaimer.md).

---

## 📌 Key Features

- **Four-diagnostic structure:** Each retained sample is rewritten into inspection, auscultation/olfaction, inquiry, and palpation fields.
- **Multi-label diagnostic evidence:** The four diagnostic methods are not mutually exclusive. A sample may contain evidence from one or more diagnostic methods.
- **No hallucinated clinical evidence:** Unreported fields are kept empty rather than completed by inference.
- **Filtered symptom field:** Request-like or non-diagnostic components are removed or weakened, while clinically relevant symptoms are preserved in `filtered_symptom`.
- **Teacher-checker refinement:** DeepSeek-R1-Distill-Llama-70B is used as the primary refinement model, and Baichuan-M2 is used as the professional medical checking model.
- **Risk-aware responses:** The dataset emphasizes clinical caution, evidence-recommendation alignment, and avoidance of unsupported prescription or dosage advice.
- **Open release:** The dataset is released for non-commercial academic research under **CC BY-NC 4.0**.

---

## 📊 Dataset Statistics

### Overall Quality Statistics

| Item | Value |
|---|---:|
| Original ShenNong-derived dataset size | 112,565 |
| Filtered strict TCM-RAGF dataset size | 99,611 |
| Removed samples | 12,954 |
| Filtering rate | 11.51% |
| Retention rate | 88.49% |

### Distribution of Four Diagnostic Methods

| Diagnostic method | Original count | Original percentage | Filtered count | Filtered percentage |
|---|---:|---:|---:|---:|
| Inspection, Wang (望) | 4,369 | 3.88% | 4,106 | 4.12% |
| Auscultation/Olfaction, Wen (闻) | 15,288 | 13.58% | 14,871 | 14.93% |
| Inquiry, Wen (问) | 112,558 | 99.99% | 99,611 | 100.00% |
| Palpation, Qie (切) | 768 | 0.68% | 566 | 0.57% |
| Total samples | 112,565 | 100.00% | 99,611 | 100.00% |

> The four diagnostic methods are treated as **multi-label evidence categories** rather than mutually exclusive classes. Therefore, the sum of modality counts may exceed the total number of samples.

### Diagnostic Combination Patterns

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

## 🧬 Dataset Construction

TCM-RAGF was built from the open **ShenNong_TCM_Dataset (v0.2)** through strict preprocessing, symptom extraction, four-diagnostic restructuring, and multi-agent verification.

### Construction Pipeline

1. **Source field extraction**  
   Extract the original `instruction`, `input`, and `output` fields.

2. **Empty-value and format checking**  
   Remove invalid records with missing or unusable instruction/response fields.

3. **Non-diagnostic query filtering**  
   Remove or weaken non-diagnostic and weakly diagnostic request components, including academic writing requests, generic explanation requests, pure recommendation requests, and unrelated analytical requests.

4. **Symptom extraction**  
   Preserve clinically relevant symptom information in the `filtered_symptom` field.

5. **Four-diagnostic restructuring**  
   Rewrite retained samples into standardized four-diagnostic fields: inspection, auscultation/olfaction, inquiry, and palpation.

6. **Multi-agent refinement and safety verification**  
   Apply teacher-checker verification to detect abnormal samples, hallucinated diagnostic cues, unsupported treatment suggestions, and unsafe medical claims.

---

## 🧾 Data Schema

Each sample follows the schema below:

```json
{
  "instruction": "string",
  "input": "string",
  "output": "string",
  "filtered_symptom": "string"
}
```

### Field Description

| Field | Type | Description |
|---|---|---|
| `instruction` | string | Original or rewritten user instruction/question. |
| `input` | string | Optional supplementary input. Often empty. |
| `filtered_symptom` | string | Clinically relevant symptom description after removing non-diagnostic request components. |
| `output` | string | Structured four-diagnostic output followed by reasoning, TCM advice, and cautious formula/herbal suggestion when applicable. |

### Output Template

The `output` field generally follows this structure:

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

### Missing Information Rule

If the original query does not provide tongue, pulse, odor, complexion, palpation, or other diagnostic evidence, the corresponding field is left empty. TCM-RAGF does **not** forcibly complete missing diagnostic information.

---

## 📝 Representative Example

```json
{
  "instruction": "请根据以下症状描述，进行中医诊断：\n\n症状描述：我只有咳嗽这一个症状，请帮我推荐中药或者方剂。",
  "input": "",
  "filtered_symptom": "我只有咳嗽这一个症状",
  "output": "望：\n闻：咳嗽\n问：我只有咳嗽这一个症状\n切：\n\n根据以上情况可能是肺气失宣证，以下是一些从中医方面对此次的基本诊断建议，但请注意，这些信息仅供参考，不能替代专业医生的诊断和治疗。\n\n推理过程：症状描述中可直接依据的信息为“我只有咳嗽这一个症状”。望闻问切中未提供依据的项目不作臆测，仅保留症状描述中可直接对应的问诊或可观察信息。\n中医建议：建议观察症状持续时间和伴随表现。若症状持续不缓解或加重，应及时到正规医院就诊。\n中药或方剂推荐：具体用药和方剂选择需结合体质、舌脉、病程及合并疾病，由专业中医师面诊后确定。"
}
```

---

## 🤖 Multi-Agent Refinement

TCM-RAGF uses a two-stage **teacher-checker** strategy.

| Role | Model | Function |
|---|---|---|
| Primary refinement model | `DeepSeek-R1-Distill-Llama-70B` | Non-diagnostic query removal, symptom extraction, four-diagnostic restructuring, content rewriting, consistency verification, and risk detection. |
| Professional medical checking model | `Baichuan-M2` | Medical quality control, abnormal-sample verification, diagnostic relevance checking, reasoning validity checking, and clinical safety verification. |

### Consistency Definition

Consistency is measured as agreement between the primary refinement model and the checking model on three operational judgments:

1. Whether the sample contains clinically relevant TCM diagnostic information.
2. Whether the extracted evidence is assigned to appropriate diagnostic fields.
3. Whether the reasoning and advice are supported by the available evidence.

A sample is retained in the strict version only when it passes diagnostic relevance, four-diagnostic attribution, reasoning validity, evidence-recommendation alignment, and safety verification.

### Risk Definition

In this dataset, risk refers to content that may cause unsafe, unsupported, or misleading medical behavior, including:

- non-diagnostic requests disguised as consultation;
- unsupported medication or formula recommendation;
- hallucinated tongue, pulse, odor, or observable signs;
- contradictions between symptoms and syndrome inference;
- exaggerated therapeutic claims;
- ignored emergency symptoms;
- responses lacking appropriate clinical caution.

---

## 📁 Repository Structure

```text
TCM-RAGF/
├── README.md
├── LICENSE.md
├── Medical_Disclaimer.md
├── CITATION.cff
├── data/
│   ├── TCM-RAGF_processed_strict.json
│   └── sample_3.json
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

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Arthur20240124/TCM-RAGF.git
cd TCM-RAGF
```

### 2. Validate Dataset Schema

```bash
python scripts/validate_schema.py data/TCM-RAGF_processed_strict.json
```

### 3. Reproduce Dataset Statistics

```bash
python scripts/compute_statistics.py data/TCM-RAGF_processed_strict.json
```

---

## 📦 Files

| File | Description |
|---|---|
| `data/TCM-RAGF_processed_strict.json` | Full strict released dataset. |
| `data/sample_3.json` | Small sample file for schema demonstration. |
| `docs/dataset_schema.md` | Data schema and four-diagnostic field explanation. |
| `docs/preprocessing_rules.md` | Preprocessing and non-diagnostic query filtering rules. |
| `docs/refinement_criteria.md` | Teacher-checker refinement criteria and risk definitions. |
| `docs/four_diagnostic_statistics.md` | Four-diagnostic distribution and quality statistics. |
| `tables/four_diagnostic_distribution.csv` | Four-diagnostic modality statistics. |
| `tables/diagnostic_combination_patterns.csv` | Four-diagnostic combination statistics. |
| `scripts/validate_schema.py` | Minimal schema validation script. |
| `scripts/compute_statistics.py` | Script for reproducing core dataset statistics. |

---

## ⚖️ License

TCM-RAGF is released for **non-commercial academic research** under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

See [LICENSE.md](LICENSE.md).

---

## ⚕️ Medical Disclaimer

The TCM-RAGF dataset and the TCM-FDiag model are intended solely for academic research, benchmark evaluation, and non-commercial development of TCM-oriented artificial intelligence systems.

They are **not** intended to provide medical diagnosis, treatment decisions, prescription, dosage recommendation, or emergency medical guidance. Any diagnostic interpretation, herbal or formula-related suggestion, or health-related output generated from the dataset or model should be regarded only as **medical-theory-assisted reference information** and must not replace consultation, diagnosis, or treatment by licensed physicians or qualified TCM practitioners.

Users should not rely on the dataset or model outputs for self-diagnosis or self-medication. For persistent, worsening, acute, or high-risk symptoms, users should seek timely evaluation and treatment from qualified medical professionals.

This disclaimer is included to clarify the medical safety, ethical, and responsibility boundaries of the dataset and model.

---

## 📚 Citation

If you use TCM-RAGF in your research, please cite:

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

## 🙏 Acknowledgements

We sincerely acknowledge the open-source datasets, model families, benchmark projects, and toolkits that inspired or supported this work.

### Dataset and Benchmark Resources

- **ShenNong_TCM_Dataset**: the source dataset from which TCM-RAGF was restructured.
- **MedBench**: used for multidimensional Chinese medical LLM evaluation.
- **TCM-Eval** and **TCM-3CEval**: used as expert-level TCM evaluation references.
- **TCM-BEST4SDT**: an open benchmark for syndrome differentiation and treatment evaluation, whose public documentation style helped inspire the organization of this README.

### Large Language Models and Medical LLMs Mentioned or Referenced in the Paper

- `TCM-FDiag`
- `Qwen2.5-7B-Instruct`
- `Qwen2.5-VL-7B-Instruct`
- `DeepSeek-R1-Distill-Llama-70B`
- `DeepSeek-V3.2-Thinking`
- `DeepSeek-V3.2-Instruct`
- `Baichuan-M2`
- `GLM-4.5`
- `Kimi-K2`
- `GPT-5.1`
- `Gork4.1`
- `HuatuoGPT`
- `ChatMed`
- `BianQue`
- `PMC-LLaMA`
- `MedAlpaca`
- `Zhongjing`
- `Med-PaLM`
- `Med-Flamingo`

### Frameworks and Libraries

- **Hugging Face Transformers**
- **LoRA / parameter-efficient fine-tuning methods**
- **Retrieval-Augmented Generation (RAG)**
- **Self-RAG**
- **Python open-source ecosystem**

We also thank the TCM practitioners involved in clinical expert review and the broader open-source medical AI community for promoting reproducible and responsible research.

---
