# System_Architecture

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Define the complete system architecture of HCDS.

---

# 1. Purpose

This document defines the overall architecture of HCDS.

It specifies:

* system boundaries
* core components
* architectural principles
* responsibility of each subsystem
* interaction between modules

This document does not define implementation details.

---

# 2. System Position

HCDS is a data foundation.

It is not:

* a LoRA project
* a ComfyUI workflow
* a Prompt library
* an image generation tool

HCDS is the standardized data layer that drives the entire historical character AI production pipeline.

---

# 3. System Architecture

```text
                        +--------------------+
                        | Dataset_Master.xlsx|
                        +---------+----------+
                                  |
                                  |
                      (Single Source of Truth)
                                  |
         -------------------------------------------------
         |                 |              |              |
         |                 |              |              |
         ▼                 ▼              ▼              ▼

 Character Profile   Prompt Builder   Metadata Builder  Validator

         |                 |              |              |
         -------------------------------------------------
                                  |
                                  ▼

                      Intermediate Structured Data
                                  |
         -------------------------------------------------------
         |            |            |            |              |
         ▼            ▼            ▼            ▼              ▼

      Prompt      Caption       txt      Batch JSON      Manifest

         |            |            |            |              |
         -------------------------------------------------------
                                  |
                                  ▼

                     AI Model Consumption Layer
         -------------------------------------------------------
         |           |            |            |              |
         ▼           ▼            ▼            ▼              ▼

      Flux      Qwen Edit    ComfyUI     OneTrainer      Wan Video
                                  |
                                  ▼
                           Generated Assets
```

---

# 4. Core Principles

The architecture follows seven immutable principles.

---

## Principle 1

Single Source of Truth

Only Dataset_Master.xlsx stores editable data.

Everything else is generated.

---

## Principle 2

Schema First

Every output must originate from HCDS Schema.

No generator may invent additional fields.

---

## Principle 3

Generation Never Edits Source

Generators are read-only.

Dataset_Master.xlsx is never modified automatically.

---

## Principle 4

Stateless Generators

Generators produce outputs.

They never store project state.

---

## Principle 5

Machine Readable First

Every specification must be directly consumable by software.

Natural language explanations are secondary.

---

## Principle 6

No Business Logic in Data

Excel stores facts.

Business logic belongs inside generators.

---

## Principle 7

One Responsibility per Module

Each module has exactly one responsibility.

---

# 5. System Modules

The HCDS system consists of six major modules.

---

## Module A

Dataset Layer

Responsibility:

Store all structured data.

Input:

Human editing.

Output:

Structured records.

---

## Module B

Validation Layer

Responsibility:

Validate data integrity.

Checks include:

* required fields
* enum values
* duplicate IDs
* invalid references
* naming rules

---

## Module C

Generation Layer

Responsibility:

Convert structured records into production artifacts.

Outputs include:

* prompts
* captions
* metadata
* txt
* filenames
* JSON

---

## Module D

Export Layer

Responsibility:

Package outputs for downstream systems.

---

## Module E

Consumer Layer

Consumers include:

* ComfyUI
* Flux
* Qwen Image Edit
* OneTrainer
* Wan
* Future AI models

Consumers never modify HCDS.

---

## Module F

Asset Layer

Stores:

generated images

generated captions

generated datasets

training packages

video assets

Assets are disposable.

They can always be regenerated.

---

# 6. Architectural Boundary

Editable:

Dataset_Master.xlsx

Configuration

Schema

Specifications

Generated:

Prompt

Caption

Metadata

txt

JSON

Manifest

Images

Videos

Training Dataset

Generated files must never become editable source data.

---

# 7. Dependency Direction

Allowed:

```text
Dataset

↓

Schema

↓

Validation

↓

Generation

↓

Export

↓

Consumers

↓

Assets
```

Reverse dependency is forbidden.

---

# 8. Consumer Independence

Consumers must not depend on each other.

Example:

```text
Flux
```

must not require

```text
OneTrainer
```

Example:

```text
Wan
```

must not require

```text
Qwen Edit
```

All consumers depend only on HCDS.

---

# 9. Regeneration Principle

Any generated artifact may be deleted.

The system must regenerate identical outputs from Dataset_Master.xlsx.

Regeneration must be deterministic whenever the generator configuration is unchanged.

---

# 10. Extension Principle

Future consumers can be added without changing HCDS Schema.

Example:

```text
Cosmos

LTX

OpenAI Video

Kling

Runway

Pika

future models
```

Only a new Export Specification should be required.

---

# 11. Technology Independence

HCDS is independent of:

Programming language

AI model

Workflow engine

Training framework

Image model

Video model

Future implementations may use Python, Rust, Go, JavaScript or other languages without altering HCDS itself.

---

# 12. Failure Isolation

A failure in one consumer must not affect:

Dataset

Schema

Validation

Other consumers

Example:

If Wan export fails,

Prompt generation must still succeed.

---

# 13. Version Compatibility

Schema version

Generator version

Export version

Consumer version

must all be independently versioned.

Version coupling is forbidden.

---

# 14. Final Architecture

```text
                 DATA

                  │

                  ▼

          Dataset_Master.xlsx

                  │

                  ▼

             HCDS Schema

                  │

                  ▼

             Validation

                  │

                  ▼

             Generation

                  │

                  ▼

               Export

                  │

                  ▼

      -----------------------------

      Flux

      ComfyUI

      OneTrainer

      Qwen Edit

      Wan Video

      Future AI

      -----------------------------

                  │

                  ▼

               Assets
```

---

# 15. Freeze Decision

The HCDS system architecture defined in this document is frozen.

All future implementations must conform to this architecture.

No implementation may bypass the HCDS Schema or the Dataset_Master.xlsx single source of truth.

End of document.
