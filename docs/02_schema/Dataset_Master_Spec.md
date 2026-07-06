# Dataset Master Specification

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Define the logical master dataset structure for HCDS.

---

# 1. Purpose

This specification defines the HCDS Dataset Master.

The Dataset Master is the authoritative logical dataset used by HCDS.

It serves as the single structured source from which downstream artifacts are generated.

The Dataset Master is a logical concept.

It is not tied to any physical storage implementation.

---

# 2. Scope

This specification defines:

* logical dataset structure
* record organization
* entity relationships
* dataset ownership
* logical constraints
* dataset lifecycle

This specification does not define:

* Excel workbook layout
* worksheet organization
* column positions
* database schema
* JSON serialization
* API contracts

These belong to implementation specifications.

---

# 3. Relationship to Other Specifications

The Dataset Master is built upon the HCDS meta specifications.

```text
HCDS_Schema.md
        ↓
Field_Model_Spec.md
        ↓
Controlled_Vocabulary_Spec.md
        ↓
Dataset_Master_Spec.md
        ↓
Entity Specifications
        ↓
Implementation Specifications
```

The Dataset Master SHALL reference, but SHALL NOT redefine, those specifications.

---

# 4. Design Principles

The Dataset Master SHALL satisfy the following principles.

---

## Principle 1 — Single Source of Truth

The Dataset Master SHALL be the only authoritative logical dataset.

All generated artifacts SHALL originate from it.

---

## Principle 2 — Logical First

The Dataset Master SHALL describe logical information only.

Physical storage SHALL be implementation-specific.

---

## Principle 3 — Entity Composition

The Dataset Master SHALL consist of HCDS entities.

It SHALL NOT duplicate entity definitions.

---

## Principle 4 — Implementation Independence

The Dataset Master SHALL remain independent of:

* Excel
* databases
* JSON
* YAML
* programming languages
* AI models

---

# 5. Dataset Composition

A Dataset Master SHALL consist of one or more Character Records.

```text
Dataset Master
        │
        ├── Character Record
        ├── Character Record
        ├── Character Record
        └── Character Record
```

Each Character Record SHALL represent exactly one historical character.

---

# 6. Character Record

A Character Record is the fundamental logical unit of the Dataset Master.

Each Character Record SHALL contain one complete HCDS entity graph.

```text
Character Record
        │
        ├── Identity
        ├── Appearance
        ├── Costume
        ├── Pose
        ├── Expression
        ├── Camera
        ├── Scene
        ├── Negative Prompt
        └── Metadata
```

Each entity SHALL conform to its corresponding specification.

---

# 7. Dataset Ownership

The Dataset Master owns:

* Character Records
* dataset metadata
* dataset version
* dataset identity

Individual entities remain owned by their respective entity specifications.

---

# 8. Record Identity

Every Character Record SHALL possess a stable unique identifier.

Record identifiers SHALL:

* be globally unique within the dataset
* remain stable
* be implementation independent
* remain unaffected by storage format

Record identifiers SHALL NOT depend upon:

* Excel row numbers
* filenames
* prompt text
* generation order

---

# 9. Dataset Integrity

The Dataset Master SHALL preserve logical integrity.

Integrity requirements include:

* unique Character Records
* complete entity relationships
* valid references
* schema compatibility
* version compatibility

Integrity SHALL be verified before generation begins.

---

# 10. Part 1 Completion

The remaining sections define:

* dataset lifecycle
* record lifecycle
* dataset validation
* logical constraints
* version compatibility
* implementation conformance
* freeze decision

These sections continue in Part 2 without restarting numbering.

End of Part 1.

---

# 11. Dataset Lifecycle

## 11.1 Purpose

The Dataset Master SHALL follow a controlled lifecycle.

The lifecycle defines how a dataset progresses from initial definition to production use.

---

## 11.2 Lifecycle States

Each Dataset Master SHALL exist in one of the following states.

| State    | Description                       |
| -------- | --------------------------------- |
| Draft    | Under construction                |
| Review   | Under technical review            |
| Approved | Approved for production           |
| Active   | Used by generators and validators |
| Archived | Retained for historical reference |

Only **Active** datasets SHALL be used for production generation.

---

## 11.3 Lifecycle Transition

The permitted lifecycle is:

```text
Draft
    ↓
Review
    ↓
Approved
    ↓
Active
    ↓
Archived
```

Reverse transitions SHALL NOT occur.

---

# 12. Character Record Lifecycle

Each Character Record SHALL possess an independent lifecycle.

A Character Record MAY be:

* Proposed
* Approved
* Active
* Deprecated
* Archived

A dataset MAY contain records in different lifecycle states.

Only Active records SHALL participate in production generation.

---

# 13. Dataset Validation

## 13.1 Purpose

Validation ensures the Dataset Master satisfies all HCDS requirements before generation.

---

## 13.2 Validation Scope

Validation SHALL include:

* schema validation
* field validation
* controlled vocabulary validation
* identifier uniqueness
* reference integrity
* required entity verification
* version compatibility

Validation SHALL complete successfully before generation begins.

---

## 13.3 Validation Result

Validation SHALL produce one of the following outcomes.

| Status               | Meaning                                             |
| -------------------- | --------------------------------------------------- |
| Passed               | Dataset satisfies all mandatory requirements        |
| Passed with Warnings | Dataset is usable but contains non-blocking issues  |
| Failed               | Dataset SHALL NOT be used for production generation |

---

# 14. Logical Constraints

The Dataset Master SHALL satisfy the following logical constraints.

Every Character Record SHALL contain exactly one:

* Identity
* Appearance
* Metadata

Optional entities MAY be omitted only where explicitly permitted by their own specifications.

No Character Record SHALL contain duplicate entities of the same type unless explicitly supported.

---

# 15. Dataset Consistency

The Dataset Master SHALL remain internally consistent.

Consistency requirements include:

* no duplicate record identifiers
* no broken references
* no conflicting entity ownership
* no conflicting vocabulary references
* no incompatible schema versions

Implementations SHALL reject inconsistent datasets.

---

# 16. Dataset Version

Each Dataset Master SHALL define:

* Dataset Version
* HCDS Schema Version
* Field Model Version
* Controlled Vocabulary Version

These versions SHALL be recorded independently.

Changing one version SHALL NOT implicitly change another.

---

# 17. Dataset Compatibility

Dataset compatibility SHALL be evaluated against:

* supported schema version
* supported field model version
* supported vocabulary version

Implementations SHALL reject unsupported datasets or provide explicit compatibility reports.

---

# 18. Dataset Independence

The Dataset Master SHALL remain independent of:

* spreadsheet software
* relational databases
* document databases
* serialization formats
* workflow engines
* AI models

The logical dataset SHALL remain identical regardless of physical representation.

---

# 19. Dataset as the Generation Source

The Dataset Master SHALL be the only logical source consumed by:

* generators
* validators
* schema compilers
* exporters

Consumers SHALL NOT bypass the Dataset Master by reading implementation-specific representations directly.

---

# 20. Part 2 Completion

The remaining sections define:

* implementation conformance
* compiler readiness
* prohibited practices
* normative references
* freeze decision
* end of specification

These sections continue in Part 3 without restarting numbering.

End of Part 2.

---

# 21. Implementation Conformance

## 21.1 General Requirement

Any implementation claiming compatibility with the HCDS Dataset Master SHALL conform to this specification.

Conformance SHALL include:

* logical dataset structure
* character record organization
* entity relationships
* version compatibility
* implementation independence

---

## 21.2 Accepted Implementations

The Dataset Master MAY be represented by different physical implementations.

Examples include:

* Excel workbook
* JSON document
* YAML document
* SQL database
* NoSQL database
* API resource
* Binary package

All implementations SHALL preserve the same logical dataset semantics.

---

# 22. Physical Representation

## 22.1 Principle

The Dataset Master defines a logical dataset only.

Physical storage SHALL be implementation-specific.

---

## 22.2 Examples

Possible physical representations include:

* Dataset_Master.xlsx
* Dataset_Master.json
* Dataset_Master.yaml
* Dataset_Master.sqlite
* Dataset_Master.db

These examples are informative.

They SHALL NOT redefine the logical dataset.

---

## 22.3 Mapping

Each physical implementation SHALL define an explicit mapping from the logical dataset to its storage representation.

The mapping SHALL preserve:

* entity ownership
* logical relationships
* field semantics
* identifiers
* version metadata

---

# 23. Compiler Readiness

## 23.1 Purpose

The Dataset Master is designed to support automatic compilation.

Implementations SHOULD be able to generate physical dataset representations without manual restructuring.

---

## 23.2 Compiler Inputs

A Dataset Compiler SHALL consume:

* HCDS Schema
* Field Model
* Controlled Vocabulary definitions
* Dataset Master definition
* Entity specifications

---

## 23.3 Compiler Outputs

Future compiler targets MAY include:

* Excel workbook templates
* JSON datasets
* YAML datasets
* SQL schemas
* API payload templates
* Documentation
* Validation templates

The logical dataset SHALL remain unchanged across compiler outputs.

---

# 24. Prohibited Practices

The following practices are prohibited.

Treating a physical representation as the authoritative logical dataset.

Defining business rules inside physical storage mappings.

Duplicating Character Records across multiple authoritative datasets.

Changing logical semantics to accommodate implementation limitations.

Using spreadsheet row numbers as logical identifiers.

Embedding generator-specific behavior inside the Dataset Master.

---

# 25. Normative References

This specification depends upon:

* HCDS_Schema.md
* Field_Model_Spec.md
* Controlled_Vocabulary_Spec.md

The following specifications SHALL build upon this document:

* Character_Profile_Spec.md
* Character_Identity_Spec.md
* Appearance_Spec.md
* Costume_Spec.md
* Pose_Action_Spec.md
* Expression_Spec.md
* Camera_Spec.md
* Scene_Context_Spec.md
* Negative_Prompt_Spec.md
* Metadata_Spec.md

Implementation specifications MAY reference this document when defining physical dataset formats.

---

# 26. Dataset Master Authority

This specification is the sole authority defining the logical Dataset Master model.

Business specifications SHALL define the contents of Character Records.

Implementation specifications SHALL define physical storage.

Neither SHALL redefine the logical Dataset Master.

---

# 27. Freeze Decision

The Dataset Master model defined by this specification is hereby frozen for HCDS v2.0.

Future changes affecting logical dataset organization SHALL require a new schema version.

Physical implementation changes SHALL NOT modify this specification.

---

# 28. Completion Statement

The Dataset Master establishes the canonical logical organization of HCDS data.

Together with:

* HCDS_Schema.md
* Field_Model_Spec.md
* Controlled_Vocabulary_Spec.md

it provides the foundation for:

* Character specifications
* Dataset validation
* Schema compilation
* Generator execution
* Export pipelines
* Future HCDS tooling

---

# 29. Implementation Readiness

This specification is implementation-ready.

It is intended for direct consumption by:

* Claude Code
* Codex
* Dataset compilers
* Validation engines
* Generator implementations
* Documentation generators
* Future HCDS tooling

No additional architectural interpretation should be required before implementation.

---

# 30. End of Specification

This document is the authoritative Dataset Master specification for HCDS v2.0.

It defines the canonical logical dataset organization upon which all HCDS business specifications SHALL be built.

End of document.
