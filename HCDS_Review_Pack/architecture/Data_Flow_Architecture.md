# Data Flow Architecture

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Define the end-to-end data flow architecture of HCDS.

---

# 1. Purpose

This document defines the complete data flow architecture of HCDS.

It specifies how structured data progresses from the authoritative source to all downstream consumers while preserving consistency, determinism, and traceability.

This specification is normative.

All implementations SHALL conform to the data flow defined herein.

---

# 2. Scope

This specification governs:

* data lifecycle
* data ownership
* transformation pipeline
* generator responsibilities
* export responsibilities
* consumer responsibilities
* artifact lifecycle
* regeneration behavior
* dependency direction

This specification does **not** define:

* schema field definitions
* Excel worksheet layouts
* prompt templates
* LoRA training parameters
* ComfyUI workflow internals

Those are specified in their respective documents.

---

# 3. Definitions

For the purposes of this specification:

**Source Data**

Editable structured data maintained by project contributors.

---

**Structured Record**

A validated in-memory representation of one logical dataset entry.

---

**Generator**

A deterministic component that transforms structured records into derived artifacts.

---

**Exporter**

A component that converts generated artifacts into consumer-specific formats.

---

**Consumer**

Any external system that reads HCDS outputs.

Examples include:

* ComfyUI
* Flux
* Qwen Image Edit
* OneTrainer
* Wan Video
* future AI systems

---

**Generated Artifact**

Any file produced from HCDS source data.

Examples:

* prompt
* caption
* txt
* metadata
* filename
* manifest
* JSON
* dataset package

---

**Asset**

Media produced by AI systems.

Examples:

* images
* videos
* training datasets

Assets are never authoritative source data.

---

# 4. Data Flow Principles

The HCDS pipeline SHALL satisfy the following principles.

---

## Principle 1 — Single Source of Truth

Dataset_Master.xlsx SHALL be the only editable source of production data.

No generated artifact SHALL become a source of truth.

---

## Principle 2 — One-Way Data Flow

Data SHALL always move forward.

The permitted direction is:

```text
Dataset
    ↓
Validation
    ↓
Structured Records
    ↓
Generation
    ↓
Export
    ↓
Consumers
    ↓
Generated Assets
```

Reverse data flow is prohibited.

---

## Principle 3 — Immutable Source

Generators SHALL NOT modify Dataset_Master.xlsx.

Validation SHALL NOT modify Dataset_Master.xlsx.

Consumers SHALL NOT modify Dataset_Master.xlsx.

Only human editors may update source data.

---

## Principle 4 — Deterministic Transformation

Given:

* identical source data
* identical schema version
* identical generator version
* identical configuration

the generated outputs SHALL be identical.

Implementations SHALL avoid hidden state or non-deterministic behavior.

---

## Principle 5 — Layer Isolation

Each processing layer SHALL perform only its assigned responsibility.

A layer SHALL NOT assume responsibilities belonging to another layer.

Example:

Validation SHALL NOT generate prompts.

Prompt generation SHALL NOT perform dataset editing.

Export SHALL NOT validate schema definitions.

---

## Principle 6 — Disposable Outputs

All generated artifacts SHALL be considered disposable.

Deletion of generated artifacts SHALL NOT result in data loss.

The complete output set SHALL be reproducible from the authoritative source.

---

## Principle 7 — Consumer Independence

Consumers SHALL operate independently.

Adding or removing one consumer SHALL NOT require modification of unrelated consumers.

---

# 5. High-Level Pipeline

The canonical HCDS pipeline is:

```text
                   Dataset_Master.xlsx
                            │
                            ▼
                    Schema Validation
                            │
                            ▼
                   Structured Records
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            ▼               ▼               ▼
      Prompt Generator  Metadata Generator  Caption Generator
            │               │               │
            └───────────────┼───────────────┘
                            │
                            ▼
                  Generated Artifacts
                            │
                    Export Pipeline
                            │
      ┌────────────┬────────────┬────────────┬────────────┐
      ▼            ▼            ▼            ▼
   ComfyUI      Flux        OneTrainer      Wan
                            │
                            ▼
                    Generated Assets
```

Every implementation SHALL preserve this logical processing order.

Internal implementation details MAY vary provided that externally observable behavior remains equivalent.

---

# 6. Pipeline Stages

The HCDS pipeline is divided into seven logical stages.

| Stage | Name                | Responsibility                                       |
| ----- | ------------------- | ---------------------------------------------------- |
| S1    | Source              | Store authoritative project data                     |
| S2    | Validation          | Verify correctness and completeness                  |
| S3    | Record Construction | Build structured records                             |
| S4    | Generation          | Produce implementation-independent artifacts         |
| S5    | Export              | Convert artifacts into consumer-specific formats     |
| S6    | Consumption         | AI systems consume exported artifacts                |
| S7    | Asset Production    | Images, videos, datasets, and other generated assets |

Each stage SHALL expose clearly defined inputs and outputs.

No stage SHALL bypass an earlier stage.

---

# 7. Stage S1 — Source Layer

Purpose:

Maintain the authoritative project dataset.

Input:

Human-authored data.

Output:

Dataset_Master.xlsx

Characteristics:

* editable
* version controlled
* schema-compliant
* implementation-independent

No downstream process may directly alter this layer.

---

# 8. Stage S2 — Validation Layer

Purpose:

Verify source integrity before generation.

Validation SHALL include, at minimum:

* required fields
* field types
* enumerated values
* identifier uniqueness
* reference integrity
* naming conventions

Validation failures SHALL prevent downstream processing.

Validation SHALL NOT perform automatic correction unless explicitly defined by another specification.

---

# 9. Stage S3 — Record Construction

Purpose:

Transform validated spreadsheet rows into structured records.

A structured record SHALL represent exactly one logical entity.

Record construction SHALL:

* normalize field values
* resolve internal references
* preserve identifiers
* remain implementation-independent

Structured records SHALL become the canonical input for all generators.

---


# 10. Stage S4 — Generation Layer

## 10.1 Purpose

The Generation Layer transforms validated structured records into implementation-independent artifacts.

Generation SHALL NOT target any specific downstream consumer.

Its responsibility is to produce canonical outputs that can later be exported into multiple consumer formats.

---

## 10.2 Inputs

The Generation Layer SHALL accept only:

* validated structured records
* active schema version
* generator configuration

Generators SHALL NOT read directly from:

* Dataset_Master.xlsx
* generated artifacts
* consumer outputs

---

## 10.3 Outputs

The Generation Layer MAY produce:

* prompts
* captions
* metadata
* filenames
* txt sidecars
* manifests
* intermediate structured objects

All outputs SHALL conform to the active HCDS Schema.

---

## 10.4 Generator Independence

Each generator SHALL perform one logical task.

Examples:

Prompt Generator

→ generates prompts only.

Caption Generator

→ generates captions only.

Filename Generator

→ generates filenames only.

Generators SHALL NOT generate outputs belonging to other generators.

---

## 10.5 Generator Isolation

Generators SHALL NOT communicate with one another.

Example:

Prompt Generator

SHALL NOT request information from Caption Generator.

Instead, both SHALL consume the same structured record independently.

---

# 11. Generator Contract

Every generator SHALL satisfy the following contract.

---

## 11.1 Deterministic Execution

Given identical:

* input records
* schema version
* generator version
* configuration

the generator SHALL always produce identical output.

---

## 11.2 Read-Only Behavior

Generators SHALL be read-only.

Generators SHALL NOT:

* modify source records
* modify Dataset_Master.xlsx
* modify schema definitions
* modify validation results

---

## 11.3 Stateless Design

Generators SHALL NOT depend upon:

* previous executions
* cached project state
* historical outputs
* execution order

A generator SHALL behave as a pure transformation function.

---

## 11.4 Stable Interface

Each generator SHALL expose:

Input

Output

Version

Configuration

Error Report

No hidden interfaces are permitted.

---

## 11.5 Error Reporting

Generation errors SHALL be reported explicitly.

Silent failure is prohibited.

Partial output SHALL be clearly identified.

---

# 12. Stage S5 — Export Layer

## 12.1 Purpose

The Export Layer converts canonical generated artifacts into formats required by downstream consumers.

The Export Layer SHALL NOT regenerate business content.

Its responsibility is formatting and packaging only.

---

## 12.2 Inputs

Exporters SHALL consume only canonical generated artifacts.

Exporters SHALL NOT regenerate:

* prompts
* captions
* filenames
* metadata

---

## 12.3 Outputs

Examples include:

ComfyUI Batch JSON

OneTrainer Dataset

Flux Input Package

Wan Input Package

Qwen Image Edit Package

Future consumer packages

---

## 12.4 Export Independence

Each exporter SHALL be independent.

Adding a new exporter SHALL NOT require modifications to existing exporters.

---

## 12.5 Packaging Only

Exporters SHALL:

transform

serialize

package

organize

Exporters SHALL NOT:

rewrite prompts

rewrite captions

modify metadata

edit filenames

---

# 13. Export Contract

Every exporter SHALL satisfy the following requirements.

---

## 13.1 Canonical Input

Exporters SHALL consume canonical outputs generated by the Generation Layer.

They SHALL NOT consume raw spreadsheet data.

---

## 13.2 Consumer Separation

Each exported package SHALL target exactly one consumer specification.

Example:

ComfyUI Export

shall not contain

OneTrainer-specific fields.

---

## 13.3 Version Awareness

Every exported package SHALL identify:

Schema Version

Generator Version

Export Version

Consumer Version (if applicable)

---

## 13.4 Reproducibility

Export packages SHALL be reproducible.

Equivalent inputs SHALL generate equivalent exported packages.

---

# 14. Stage S6 — Consumer Layer

## 14.1 Purpose

Consumers execute AI workflows using exported packages.

Consumers are external to HCDS.

---

## 14.2 Examples

Consumers include:

ComfyUI

Flux

Qwen Image Edit

OneTrainer

Wan Video

Future AI systems

---

## 14.3 Consumer Responsibilities

Consumers SHALL:

consume exported packages

produce requested assets

report execution status

Consumers SHALL NOT:

modify HCDS Schema

modify Dataset_Master.xlsx

rewrite generated artifacts

---

## 14.4 Consumer Independence

Consumers SHALL remain independent.

Failure of one consumer SHALL NOT interrupt another consumer.

---

# 15. Consumer Contract

Every consumer SHALL satisfy the following requirements.

---

## 15.1 Read-Only Consumption

Consumers SHALL treat exported packages as read-only.

---

## 15.2 No Upstream Modification

Consumers SHALL NOT update:

Dataset_Master.xlsx

structured records

generated artifacts

schema

---

## 15.3 Replaceability

Any consumer MAY be replaced by another implementation provided that the exported package format remains supported.

---

# 16. Stage S7 — Asset Production

The final stage produces user-facing assets.

Examples include:

generated images

generated videos

training datasets

preview images

evaluation datasets

These assets are downstream products.

They SHALL NOT become authoritative project data.

---

# 17. Artifact Classification

Artifacts SHALL be classified into two categories.

## Authoritative Artifacts

Examples:

Dataset_Master.xlsx

Schema Specifications

Architecture Specifications

These artifacts are editable.

---

## Generated Artifacts

Examples:

Prompt

Caption

Metadata

txt

JSON

Training Package

Generated Images

Generated Videos

These artifacts are disposable.

Deletion SHALL NOT result in permanent data loss.

Generation SHALL always be reproducible from the authoritative source.

---


# 18. Artifact Lifecycle

## 18.1 Purpose

This section defines the lifecycle of all artifacts produced within HCDS.

Every artifact SHALL belong to exactly one lifecycle stage.

---

## 18.2 Lifecycle States

Every generated artifact SHALL transition through the following states.

```text
Source
    ↓
Validated
    ↓
Generated
    ↓
Exported
    ↓
Consumed
    ↓
Archived or Deleted
```

No artifact SHALL skip required lifecycle stages.

---

## 18.3 State Descriptions

### Source

Editable project data.

Examples:

* Dataset_Master.xlsx
* project configuration

Only this state permits manual modification.

---

### Validated

Source data that has successfully passed validation.

Validated records become eligible for generation.

---

### Generated

Canonical outputs produced by generators.

Examples:

* prompt
* caption
* filename
* metadata
* txt

Generated artifacts remain implementation-independent.

---

### Exported

Consumer-specific packages.

Examples:

* ComfyUI Batch JSON
* OneTrainer Dataset
* Wan Package

Exported artifacts SHALL NOT be manually edited.

---

### Consumed

Artifacts actively used by downstream AI systems.

Consumption SHALL NOT modify upstream artifacts.

---

### Archived or Deleted

Generated artifacts MAY be archived or deleted.

Deletion SHALL NOT affect the authoritative project data.

---

# 19. Artifact Ownership

Ownership SHALL be clearly defined.

| Artifact            | Owner                     |
| ------------------- | ------------------------- |
| Dataset_Master.xlsx | Source Layer              |
| Structured Record   | Record Construction Layer |
| Prompt              | Generation Layer          |
| Caption             | Generation Layer          |
| Metadata            | Generation Layer          |
| Export Package      | Export Layer              |
| Images              | Consumer Layer            |
| Videos              | Consumer Layer            |

Ownership SHALL NOT overlap.

---

# 20. Dependency Rules

## 20.1 Forward Dependencies

The only permitted dependency direction is:

```text
Source
    ↓
Validation
    ↓
Record Construction
    ↓
Generation
    ↓
Export
    ↓
Consumer
    ↓
Assets
```

Implementations SHALL preserve this direction.

---

## 20.2 Forbidden Reverse Dependencies

The following dependencies are prohibited.

Export depending upon Consumers.

Generation depending upon Export.

Validation depending upon Generation.

Schema depending upon Generated Artifacts.

Assets depending upon Dataset editing.

---

## 20.3 Cross-Layer Independence

Each layer SHALL communicate only with its adjacent layer unless otherwise specified.

Direct coupling between distant layers SHALL be avoided.

Example:

Consumers SHALL NOT access Dataset_Master.xlsx directly.

---

# 21. Failure Isolation

## 21.1 Principle

Failures SHALL remain isolated within the affected layer.

A downstream failure SHALL NOT invalidate upstream data.

---

## 21.2 Validation Failure

If validation fails:

Generation SHALL NOT execute.

Export SHALL NOT execute.

Consumers SHALL receive no output.

Source data SHALL remain unchanged.

---

## 21.3 Generation Failure

If one generator fails:

Other independent generators MAY continue.

Example:

Caption generation failure SHALL NOT invalidate filename generation.

---

## 21.4 Export Failure

Failure of one exporter SHALL NOT prevent execution of another exporter.

Example:

Failure to generate a Wan package SHALL NOT prevent generation of a OneTrainer dataset.

---

## 21.5 Consumer Failure

Failure within a consumer SHALL NOT modify:

* generated artifacts
* export packages
* structured records
* source data

Consumer failures SHALL remain external to HCDS.

---

# 22. Deterministic Regeneration

## 22.1 Principle

Generated artifacts SHALL always be reproducible.

---

## 22.2 Regeneration Inputs

Regeneration SHALL depend only upon:

* Dataset_Master.xlsx
* active schema
* generator version
* exporter version
* configuration

No hidden project state is permitted.

---

## 22.3 Disposable Outputs

The following artifacts MAY be deleted without loss of project information.

Examples:

* prompts
* captions
* metadata
* txt
* JSON
* generated images
* generated videos

Equivalent outputs SHALL be reproducible.

---

## 22.4 Version Consistency

When generator versions change:

Regeneration MAY produce different outputs.

Version identifiers SHALL accompany regenerated artifacts.

---

# 23. Pipeline Validation

Every implementation SHALL verify the integrity of the complete pipeline.

At minimum, validation SHALL include:

* schema compliance
* successful record construction
* successful artifact generation
* successful export
* package completeness
* version consistency

Implementations SHOULD provide machine-readable validation reports.

---

# 24. Extensibility

Future generators MAY be added.

Future exporters MAY be added.

Future consumers MAY be added.

Provided that:

* the HCDS Schema remains authoritative
* dependency direction is preserved
* generator contracts remain satisfied
* existing interfaces remain compatible

Extensions SHALL NOT require modification of upstream architecture.

---

# 25. Non-Goals

This specification does not define:

* prompt wording
* Excel worksheet design
* LoRA training parameters
* ComfyUI node graphs
* Flux workflow configuration
* Wan inference parameters
* model selection

These subjects belong to dedicated specifications.

---

# 26. Compliance Requirements

An implementation SHALL be considered compliant only if it satisfies all mandatory requirements defined in this specification.

Implementations SHALL NOT:

* bypass validation
* modify source data during generation
* reverse pipeline direction
* introduce hidden state
* create additional authoritative data sources

Non-compliant implementations SHALL NOT be described as HCDS-compatible.

---

# 27. Relationship to Other Specifications

This specification SHALL be read together with:

* Documentation_Architecture.md
* System_Architecture.md
* Single_Source_of_Truth.md
* HCDS_Schema.md

Subsequent specifications SHALL inherit the pipeline architecture defined herein.

No subsequent specification may redefine the pipeline.

---

# 28. Freeze Decision

The HCDS data flow architecture defined in this document is hereby frozen.

All future generators, exporters, consumers, validation mechanisms, and implementation pipelines SHALL conform to this specification.

Changes to this document constitute architectural changes and require formal review before adoption.

---

# 29. End of Specification

This document establishes the authoritative end-to-end data flow architecture for HCDS.

All downstream specifications and implementations SHALL treat this document as the normative definition of HCDS data movement.

End of document.
