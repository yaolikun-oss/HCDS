# RFC0002: HCDS Language Strategy

Status: Draft
Version: v1.0
Project: HCDS
Owner: HCDS Architecture Team
Created: 2026-07-07
Related: RFC0001, HCDS v2.0 Schema, HCDS Production Phase v1.0

---

## 1. Purpose

This RFC defines the language architecture strategy for HCDS.

HCDS serves multiple consumers:

* Human creators
* Prompt generators
* Image generation systems
* Training pipelines

Because these consumers have different language requirements, HCDS adopts a layered language architecture.

---

## 2. Motivation

Historical character datasets are created by humans but consumed by AI systems.

Human users naturally describe historical identity, costume, behavior, and scenes in Chinese.

Current image generation and training ecosystems often produce more stable results with English semantic descriptions.

Therefore, HCDS must separate human language from model language.

---

## 3. Decision

HCDS adopts a Dual Language Architecture.

The language layers are:

* Human Layer: Chinese preferred
* Structured Dataset Layer: language independent
* Generation Layer: Chinese Prompt and English Prompt
* Training Layer: English caption preferred

Canonical flow:

```text
Human Chinese Input
        ↓
HCDS Structured Data
        ↓
Prompt Generation
        ↓
Prompt_CN
Prompt_EN
        ↓
Image Generation
        ↓
Image
        ↓
Caption Generation
        ↓
Caption_EN
        ↓
Training Dataset
```

---

## 4. Scope

### 4.1 Character Profile

Character Profile describes:

"Who is this person?"

Allowed language fields:

* Description_CN
* Description_EN (optional)
* Prompt_CN (optional)
* Prompt_EN (optional)

Character Profile does not contain:

* Scene
* Camera
* Background
* Training caption

---

### 4.2 Dataset Master

Dataset Master describes:

"What is this sample?"

Dataset Master is responsible for:

* Image identity
* Pose
* Action
* Camera
* Environment
* Prompt
* Caption
* Metadata

Caption fields belong to Dataset Master or downstream dataset-generation artifacts, not Character Profile.

---

### 4.3 Training Caption

Training caption is a model-facing artifact.

Default rule:

* English caption preferred

Chinese caption is not required for the training layer.

---

## 5. Compatibility

This RFC does not modify frozen schemas immediately.

Implementation changes require:

RFC
→ Review
→ Acceptance
→ Schema review
→ Version decision
→ Migration plan

Until accepted and implemented, this RFC is advisory only.

---

## 6. Implementation Impact

Affected future components may include:

* Character Profile Template
* Prompt Generator
* Dataset Master Schema
* Caption Generator
* Training Dataset Builder

No implementation changes are made by this RFC document.

---

## 7. Non Goals

This RFC does not:

* Redesign HCDS schema
* Change Generator MVP
* Add an automatic translation system
* Modify existing frozen documents
* Modify schemas
* Modify generators
* Modify PR #1

---

## 8. Future Work

Potential future RFCs may define:

* Prompt Translation Layer
* Caption Generation Pipeline
* Multilingual Metadata Standard

---

## 9. Decision Status

Pending Review.

This RFC must be reviewed before any schema, generator, or production pipeline change is made.

---

## 10. Final Rule

HCDS separates human authoring language from model-facing generation language.

Chinese is preferred for human authoring.
Structured data remains language independent.
Prompt generation may produce both Chinese and English prompts.
Training captions prefer English.

---

## 11. Language Ownership Rule

1. The Chinese semantic layer is the canonical human source. It is the authoritative record of historical meaning; all other language layers are derived from it.
2. The English generation prompt is a model adaptation layer. Prompt_EN exists to improve generation stability with English-trained systems, not to establish or redefine meaning.
3. Caption generation belongs to the training pipeline, under Dataset Master and downstream training artifacts, not to Character Profile.
4. Generated English text must not override historical meaning. Where Prompt_EN or Caption_EN diverges from the Chinese semantic layer, the divergence is a translation defect to be corrected, not an alternate authoritative source.
