# Documentation Tree

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Provide the official index of all HCDS documentation.

---

# 1. Purpose

This document is the official documentation index for HCDS.

Its responsibilities are:

* define the official documentation directory structure
* define the official location of every document
* provide a navigation entry point for developers and AI agents
* ensure every document has a unique location

This document does **not** define documentation principles.

Documentation principles are defined in:

```text
Documentation_Architecture.md
```

---

# 2. Scope

This document defines only:

* directory hierarchy
* document names
* document locations
* document grouping

This document does not define:

* schema
* implementation
* data flow
* prompt generation
* validation logic

---

# 3. Repository Documentation Structure

```text
docs/

├── 00_governance/
│   ├── README.md
│   ├── AI_Collaboration.md
│   ├── AI_Agents.md
│   ├── Repository_Structure.md
│   └── Long_Document_Assembly_Spec.md
│
├── 01_architecture/
│   ├── Documentation_Architecture.md
│   ├── Documentation_Tree.md
│   ├── System_Architecture.md
│   ├── Data_Flow_Architecture.md
│   └── Single_Source_of_Truth.md
│
├── 02_schema/
│   ├── HCDS_Schema.md
│   ├── Dataset_Master_Spec.md
│   ├── Character_Profile_Spec.md
│   ├── Character_Identity_Spec.md
│   ├── Appearance_Spec.md
│   ├── Costume_Spec.md
│   ├── Pose_Action_Spec.md
│   ├── Expression_Spec.md
│   ├── Camera_Spec.md
│   ├── Scene_Context_Spec.md
│   ├── Negative_Prompt_Spec.md
│   └── Metadata_Spec.md
│
├── 03_generation/
│   ├── Prompt_Generation_Spec.md
│   ├── Image_Filename_Spec.md
│   ├── Caption_Generation_Spec.md
│   ├── Txt_Sidecar_Spec.md
│   ├── ComfyUI_Batch_Spec.md
│   ├── Qwen_Image_Edit_Spec.md
│   ├── Flux_Generation_Spec.md
│   └── Wan_Video_Generation_Spec.md
│
├── 04_pipeline/
│   ├── Excel_Implementation_Guide.md
│   ├── Python_Generator_Spec.md
│   ├── Validation_Rules.md
│   ├── Export_Pipeline_Spec.md
│   ├── OneTrainer_Dataset_Spec.md
│   ├── LoRA_Training_Spec.md
│   ├── Testing_Spec.md
│   └── Release_Process.md
│
└── 05_reference/
    ├── Naming_Convention.md
    ├── Glossary.md
    ├── Version_History.md
    └── RFC_Index.md
```

---

# 4. Directory Responsibilities

## 00_governance

Purpose:

Project governance and collaboration.

Contains:

* project introduction
* AI collaboration rules
* repository conventions
* long-document generation rules

---

## 01_architecture

Purpose:

System-level architecture.

Contains:

* documentation architecture
* documentation index
* system architecture
* data flow architecture
* single source of truth

---

## 02_schema

Purpose:

Define all HCDS data structures.

Contains:

* schema definition
* dataset specification
* character specification
* appearance specification
* costume specification
* pose specification
* metadata specification

This directory is the authoritative definition of all HCDS data fields.

---

## 03_generation

Purpose:

Transform HCDS schema into production artifacts.

Contains specifications for generating:

* prompts
* filenames
* captions
* txt sidecars
* ComfyUI batch files
* Flux inputs
* Qwen Image Edit inputs
* Wan video inputs

No schema definitions are permitted in this directory.

---

## 04_pipeline

Purpose:

Describe implementation and execution.

Contains:

* Excel implementation
* Python generators
* validation
* export pipeline
* OneTrainer dataset generation
* LoRA dataset generation
* testing
* release workflow

---

## 05_reference

Purpose:

Shared reference material.

Contains:

* naming conventions
* terminology
* version history
* RFC index

Reference documents do not define implementation behavior.

---

# 5. Naming Rules

Every official documentation file must:

* use English
* use Pascal_Case_With_Underscores
* end with `.md`

Example:

```text
Prompt_Generation_Spec.md
```

Forbidden:

```text
prompt.md
prompt-spec.md
最终版.md
Spec_v5.md
```

---

# 6. Directory Rules

Each document belongs to exactly one directory.

A document must never exist in multiple locations.

Moving a document between directories requires an architecture review.

---

# 7. Adding New Documents

A new document may be added only if:

* it has one clear responsibility
* it does not duplicate an existing document
* its dependency position is defined
* its directory is appropriate
* it follows HCDS naming conventions

---

# 8. Reading Order

AI agents should read documentation in the following order:

```text
00_governance
        ↓
01_architecture
        ↓
02_schema
        ↓
03_generation
        ↓
04_pipeline
        ↓
05_reference
```

Within each directory, documents should be read according to their dependency relationships rather than alphabetical order.

---

# 9. Maintenance Rules

This document serves as the official documentation index.

Whenever documentation is added, removed, or relocated, this index must be updated accordingly.

The architectural principles governing the documentation system remain defined exclusively in `Documentation_Architecture.md`.

---

# 10. Freeze Decision

The documentation tree defined in this document is the official structure of the HCDS repository.

All future documentation shall conform to this hierarchy.

End of document.
