# HCDS Documentation Architecture

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Define the official documentation system for HCDS

---

## 1. Purpose

This document defines the official documentation architecture of HCDS.

It defines:

* what documents exist
* what each document is responsible for
* the order in which documents are written
* how AI agents should read and use the documentation
* how documentation maps to implementation

This document does not define HCDS fields, schemas, prompts, workflows, or training rules.

Those belong to their own documents.

---

## 2. Core Rule

HCDS documentation follows one rule:

```text
One File = One Responsibility
```

Each document must have a single clear purpose.

A document is not allowed to:

* repeat another document
* partially replace another document
* contain mixed responsibilities
* define implementation details outside its scope
* require human interpretation to be usable

---

## 3. Documentation Layers

HCDS documentation is organized into five layers.

```text
Layer 01: Project Governance
Layer 02: Architecture
Layer 03: Data Standard
Layer 04: Generation Standard
Layer 05: Implementation Standard
```

Each layer has a different responsibility.

---

## 4. Layer 01: Project Governance

Purpose:

Define what HCDS is, how the repository works, and how AI agents collaborate.

Documents:

```text
README.md
AI_Collaboration.md
AI_Agents.md
Repository_Structure.md
```

Responsibilities:

* project positioning
* collaboration rules
* AI agent roles
* repository directory rules

These documents do not define schema fields or production logic.

---

## 5. Layer 02: Architecture

Purpose:

Freeze the system architecture before implementation.

Documents:

```text
Documentation_Architecture.md
System_Architecture.md
Data_Flow_Architecture.md
Single_Source_of_Truth.md
```

Responsibilities:

* documentation system
* overall HCDS architecture
* data generation flow
* Dataset_Master.xlsx as the only source of truth

These documents do not define Excel columns or prompt templates.

---

## 6. Layer 03: Data Standard

Purpose:

Define all official HCDS data structures.

Documents:

```text
HCDS_Schema.md
Dataset_Master_Spec.md
Character_Profile_Spec.md
Character_Identity_Spec.md
Appearance_Spec.md
Costume_Spec.md
Pose_Action_Spec.md
Expression_Spec.md
Camera_Spec.md
Scene_Context_Spec.md
Negative_Prompt_Spec.md
Metadata_Spec.md
```

Responsibilities:

* official schema fields
* field naming rules
* allowed values
* required and optional fields
* machine-readable structure

These documents are the source for Excel, JSON, prompt generation, captions, and training metadata.

---

## 7. Layer 04: Generation Standard

Purpose:

Define how HCDS data becomes production outputs.

Documents:

```text
Prompt_Generation_Spec.md
Image_Filename_Spec.md
Caption_Generation_Spec.md
Txt_Sidecar_Spec.md
ComfyUI_Batch_Spec.md
Qwen_Image_Edit_Spec.md
Flux_Generation_Spec.md
Wan_Video_Generation_Spec.md
```

Responsibilities:

* prompt construction
* image naming
* caption generation
* txt sidecar generation
* ComfyUI batch input
* Qwen Image Edit input
* Flux generation rules
* Wan video generation rules

These documents consume HCDS Schema.

They must not redefine schema fields.

---

## 8. Layer 05: Implementation Standard

Purpose:

Define how developers implement HCDS.

Documents:

```text
Excel_Implementation_Guide.md
Python_Generator_Spec.md
Validation_Rules.md
Export_Pipeline_Spec.md
OneTrainer_Dataset_Spec.md
LoRA_Training_Spec.md
Testing_Spec.md
Release_Process.md
```

Responsibilities:

* Excel workbook structure
* Python generation logic
* validation rules
* export pipeline
* OneTrainer dataset output
* LoRA training dataset rules
* tests
* release workflow

These documents must be directly usable by Claude Code, Codex, Python, and future automation agents.

---

## 9. Official Documentation Tree

The official documentation tree is:

```text
docs/
├── 01_governance/
│   ├── README.md
│   ├── AI_Collaboration.md
│   ├── AI_Agents.md
│   └── Repository_Structure.md
│
├── 02_architecture/
│   ├── Documentation_Architecture.md
│   ├── System_Architecture.md
│   ├── Data_Flow_Architecture.md
│   └── Single_Source_of_Truth.md
│
├── 03_data_standard/
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
├── 04_generation_standard/
│   ├── Prompt_Generation_Spec.md
│   ├── Image_Filename_Spec.md
│   ├── Caption_Generation_Spec.md
│   ├── Txt_Sidecar_Spec.md
│   ├── ComfyUI_Batch_Spec.md
│   ├── Qwen_Image_Edit_Spec.md
│   ├── Flux_Generation_Spec.md
│   └── Wan_Video_Generation_Spec.md
│
└── 05_implementation_standard/
    ├── Excel_Implementation_Guide.md
    ├── Python_Generator_Spec.md
    ├── Validation_Rules.md
    ├── Export_Pipeline_Spec.md
    ├── OneTrainer_Dataset_Spec.md
    ├── LoRA_Training_Spec.md
    ├── Testing_Spec.md
    └── Release_Process.md
```

---

## 10. Documentation Writing Order

Official writing order:

```text
01. Documentation_Architecture.md
02. System_Architecture.md
03. Data_Flow_Architecture.md
04. Single_Source_of_Truth.md
05. HCDS_Schema.md
06. Dataset_Master_Spec.md
07. Character_Profile_Spec.md
08. Character_Identity_Spec.md
09. Appearance_Spec.md
10. Costume_Spec.md
11. Pose_Action_Spec.md
12. Expression_Spec.md
13. Camera_Spec.md
14. Scene_Context_Spec.md
15. Negative_Prompt_Spec.md
16. Metadata_Spec.md
17. Prompt_Generation_Spec.md
18. Image_Filename_Spec.md
19. Caption_Generation_Spec.md
20. Txt_Sidecar_Spec.md
21. ComfyUI_Batch_Spec.md
22. Qwen_Image_Edit_Spec.md
23. Flux_Generation_Spec.md
24. Wan_Video_Generation_Spec.md
25. Excel_Implementation_Guide.md
26. Python_Generator_Spec.md
27. Validation_Rules.md
28. Export_Pipeline_Spec.md
29. OneTrainer_Dataset_Spec.md
30. LoRA_Training_Spec.md
31. Testing_Spec.md
32. Release_Process.md
```

No document may depend on an unfinished later document.

---

## 11. AI Reading Rules

AI agents must read documents in this order:

```text
README.md
AI_Collaboration.md
AI_Agents.md
Repository_Structure.md
Documentation_Architecture.md
System_Architecture.md
Data_Flow_Architecture.md
Single_Source_of_Truth.md
HCDS_Schema.md
```

After that, agents should read only the document related to the current task.

Example:

```text
Task: implement filename generator
Required docs:
- HCDS_Schema.md
- Image_Filename_Spec.md
- Python_Generator_Spec.md
```

Example:

```text
Task: generate OneTrainer dataset
Required docs:
- HCDS_Schema.md
- Caption_Generation_Spec.md
- Txt_Sidecar_Spec.md
- OneTrainer_Dataset_Spec.md
```

---

## 12. Documentation Dependency Rules

Allowed dependency direction:

```text
Governance
↓
Architecture
↓
Data Standard
↓
Generation Standard
↓
Implementation Standard
```

Reverse dependency is forbidden.

Forbidden examples:

```text
HCDS_Schema.md depends on OneTrainer_Dataset_Spec.md
Costume_Spec.md depends on Flux_Generation_Spec.md
Prompt_Generation_Spec.md redefines Appearance fields
LoRA_Training_Spec.md modifies Dataset_Master fields
```

---

## 13. Schema Authority Rule

The only document allowed to define the complete HCDS schema is:

```text
HCDS_Schema.md
```

Other documents may reference schema fields.

Other documents may define usage rules.

Other documents may define validation rules.

Other documents may not redefine schema fields.

---

## 14. Excel Authority Rule

The only file allowed to act as the project data source is:

```text
Dataset_Master.xlsx
```

All generated outputs must derive from it.

This includes:

* prompts
* filenames
* captions
* txt sidecars
* metadata
* ComfyUI batch files
* OneTrainer datasets
* LoRA training datasets

Manual duplicate data sources are forbidden.

---

## 15. Implementation Readiness Standard

A document is considered implementation-ready only if Claude Code or Codex can directly use it to build code.

Each implementation-ready document must include:

```text
Purpose
Scope
Inputs
Outputs
Rules
Validation Requirements
Examples
Forbidden Behavior
Developer Tasks
```

Documents that only describe ideas are not accepted.

---

## 16. Naming Standard

All documentation filenames must use:

```text
Pascal_Case_With_Underscores.md
```

Allowed:

```text
Prompt_Generation_Spec.md
OneTrainer_Dataset_Spec.md
Validation_Rules.md
```

Forbidden:

```text
prompt spec.md
prompt-generation.md
OneTrainer说明.md
final_doc_v3.md
```

---

## 17. Document Header Standard

Every official document must start with:

```text
# Document Title

Version: v2.0
Status: Draft | Frozen
Owner: HCDS Chief Architect
Responsibility: Single responsibility statement
```

No official document may omit this header.

---

## 18. Status Rules

Allowed document status values:

```text
Draft
Frozen
Deprecated
```

Meaning:

```text
Draft       = can be edited
Frozen      = implementation reference
Deprecated  = no longer used
```

Implementation should only be based on Frozen documents unless explicitly approved.

---

## 19. Forbidden Documentation Behavior

The following are forbidden:

```text
mixing schema and implementation
mixing prompt rules and Excel rules
duplicating field definitions
using vague natural-language-only rules
creating temporary unofficial docs
creating multiple sources of truth
placing production rules in chat history only
requiring human interpretation before coding
```

---

## 20. Final Principle

HCDS documentation is not explanatory writing.

HCDS documentation is executable architecture.

Every official document must be readable by:

```text
Claude
Codex
Python
ComfyUI
OneTrainer
future AI agents
```

If a document cannot guide implementation directly, it is not complete.

---

## 21. Freeze Decision

This documentation architecture is now frozen.

All future HCDS documents must follow this structure.

No new document may be added unless it has:

```text
a single responsibility
a clear directory location
a defined dependency position
a valid implementation purpose
```

End of document.
