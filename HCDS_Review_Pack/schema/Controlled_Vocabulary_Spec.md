# Controlled Vocabulary Specification

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Define the standard model for controlled vocabularies used throughout HCDS.

---

# 1. Purpose

This specification defines the official Controlled Vocabulary Model for HCDS.

Controlled vocabularies provide standardized values for logical fields whose values SHALL be selected from predefined sets.

This specification establishes:

* vocabulary structure
* vocabulary identifiers
* value definitions
* version management
* extensibility
* compatibility rules

It does not define business-specific vocabulary values.

---

# 2. Scope

This specification governs:

* vocabulary definitions
* enumeration identifiers
* vocabulary metadata
* vocabulary versioning
* vocabulary lifecycle
* vocabulary references

This specification does not define:

* Character entities
* Appearance entities
* Costume entities
* business field definitions
* generator behavior
* implementation storage

---

# 3. Relationship to Other Specifications

The HCDS Schema defines entities.

The Field Model defines logical fields.

This specification defines controlled vocabularies referenced by those logical fields.

The dependency relationship is:

```text
HCDS_Schema.md
        ↓
Field_Model_Spec.md
        ↓
Controlled_Vocabulary_Spec.md
        ↓
Entity Specifications
```

Logical fields using DataType `Enum` SHALL reference a controlled vocabulary defined according to this specification.

---

# 4. Design Principles

Controlled vocabularies SHALL satisfy the following principles.

---

## Principle 1 — Single Authority

Each vocabulary SHALL have exactly one authoritative definition.

Duplicate vocabulary definitions are prohibited.

---

## Principle 2 — Stable Identifier

Each vocabulary SHALL possess a permanent identifier.

Vocabulary identifiers SHALL remain stable across compatible schema versions.

---

## Principle 3 — Machine Readable

Vocabulary definitions SHALL be processable without human interpretation.

Vocabulary values SHALL use canonical machine-readable identifiers.

---

## Principle 4 — Semantic Stability

The meaning of an existing vocabulary value SHALL remain stable.

If semantics change, a new value SHALL be introduced.

---

## Principle 5 — Implementation Independence

Controlled vocabularies SHALL remain independent of:

* Excel
* JSON
* databases
* programming languages
* AI models

---

# 5. Vocabulary Definition Record

Every controlled vocabulary SHALL be defined using the following structure.

| Property     | Required | Description                                  |
| ------------ | -------- | -------------------------------------------- |
| VocabularyId | Yes      | Unique identifier                            |
| Name         | Yes      | Human-readable vocabulary name               |
| Description  | Yes      | Vocabulary purpose                           |
| Owner        | Yes      | Responsible entity                           |
| Version      | Yes      | Vocabulary version                           |
| Values       | Yes      | Collection of vocabulary values              |
| SinceVersion | Yes      | First HCDS version supporting the vocabulary |
| Deprecated   | Yes      | Deprecation status                           |
| Notes        | No       | Supplementary remarks                        |

This structure is normative.

---

# 6. VocabularyId

## 6.1 Purpose

VocabularyId uniquely identifies a controlled vocabulary.

---

## 6.2 Requirements

VocabularyId SHALL:

* be unique
* remain stable
* be machine-readable
* use English
* avoid implementation-specific terminology

Examples:

```text
Dynasty
Gender
CameraAngle
ArmorType
```

VocabularyId SHALL NOT depend upon filenames or storage locations.

---

# 7. Vocabulary Value Model

Each vocabulary SHALL consist of one or more Vocabulary Values.

Each Vocabulary Value SHALL contain the following properties.

| Property     | Required | Description                        |
| ------------ | -------- | ---------------------------------- |
| ValueId      | Yes      | Stable machine-readable identifier |
| DisplayName  | Yes      | Human-readable name                |
| Description  | Yes      | Semantic meaning                   |
| SortOrder    | No       | Recommended ordering               |
| Deprecated   | Yes      | Deprecation status                 |
| SinceVersion | Yes      | First supported version            |
| Notes        | No       | Additional remarks                 |

Vocabulary Values SHALL NOT redefine field semantics.

---

# 8. ValueId

## 8.1 Purpose

ValueId uniquely identifies one vocabulary value.

---

## 8.2 Requirements

ValueId SHALL:

* remain stable
* be unique within its vocabulary
* be machine-readable
* avoid spaces
* avoid ambiguity

Display names MAY change.

ValueId SHALL remain unchanged.

---

# 9. DisplayName

DisplayName provides a human-readable label.

DisplayName MAY be localized by future implementation specifications.

Localization SHALL NOT alter ValueId.

---

# 10. Part 1 Completion

The remaining sections define:

* vocabulary lifecycle
* compatibility rules
* deprecation
* localization
* extension model
* compliance requirements
* implementation readiness
* freeze decision

These sections continue in Part 2 without restarting numbering.

End of Part 1.

---

# 11. Vocabulary Lifecycle

## 11.1 Purpose

Every controlled vocabulary SHALL follow a defined lifecycle.

The lifecycle ensures predictable evolution while preserving backward compatibility.

---

## 11.2 Lifecycle States

A vocabulary SHALL exist in one of the following states.

| State      | Description                                          |
| ---------- | ---------------------------------------------------- |
| Proposed   | Under review and not yet part of the official schema |
| Accepted   | Approved for inclusion                               |
| Active     | Available for production use                         |
| Deprecated | Scheduled for future removal                         |
| Removed    | No longer supported                                  |

Only **Active** vocabularies SHALL be referenced by newly introduced logical fields.

---

## 11.3 Lifecycle Transition

The permitted lifecycle is:

```text
Proposed
    ↓
Accepted
    ↓
Active
    ↓
Deprecated
    ↓
Removed
```

Reverse transitions SHALL NOT occur.

---

# 12. Vocabulary Compatibility

## 12.1 Compatible Changes

The following changes are considered backward compatible.

* adding new vocabulary values
* improving descriptions
* improving documentation
* adding localization resources

Existing ValueId values SHALL remain unchanged.

---

## 12.2 Incompatible Changes

The following changes SHALL be considered incompatible.

* removing an active ValueId
* changing the semantic meaning of a ValueId
* changing VocabularyId
* reusing a deprecated ValueId for another meaning

Such changes SHALL require an appropriate schema version update.

---

# 13. Deprecation Policy

## 13.1 Vocabulary Deprecation

A vocabulary MAY be deprecated.

Deprecation SHALL occur before removal.

Deprecated vocabularies SHALL remain documented.

---

## 13.2 Value Deprecation

Individual vocabulary values MAY be deprecated independently.

Deprecated values SHALL continue to be recognized until officially removed.

New specifications SHOULD avoid introducing deprecated values.

---

# 14. Localization

## 14.1 Principle

Localization SHALL affect presentation only.

Localization SHALL NOT modify:

* VocabularyId
* ValueId
* semantic meaning

---

## 14.2 Language Independence

Implementations MAY provide localized DisplayName values.

Logical processing SHALL always use ValueId.

---

# 15. Extension Rules

## 15.1 Adding Values

New values MAY be added to an Active vocabulary when required.

Each new value SHALL define:

* ValueId
* DisplayName
* Description
* SinceVersion
* Deprecated

---

## 15.2 Creating New Vocabularies

A new vocabulary SHALL be created when:

* no existing vocabulary accurately represents the concept
* extending an existing vocabulary would introduce semantic ambiguity

Duplicate vocabularies are prohibited.

---

# 16. Vocabulary References

Logical fields SHALL reference vocabularies using VocabularyId.

Example:

```text
Field:
Dynasty

EnumRef:
Dynasty
```

Implementations SHALL resolve EnumRef through the authoritative vocabulary definition.

---

# 17. Quality Requirements

Every controlled vocabulary SHALL satisfy the following requirements.

* complete
* internally consistent
* semantically unambiguous
* machine-readable
* version controlled
* implementation independent

Vocabulary values SHALL be mutually exclusive whenever practical.

---

# 18. Relationship to Entity Specifications

Business specifications SHALL reference controlled vocabularies.

They SHALL NOT redefine vocabulary structures.

Example:

```text
Character_Identity_Spec.md

Field:
Dynasty

EnumRef:
Dynasty
```

The business specification defines the field.

This specification defines the vocabulary model.

---

# 19. Part 2 Completion

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

# 20. Implementation Conformance

## 20.1 General Requirement

Any implementation claiming compatibility with the HCDS Controlled Vocabulary Model SHALL conform to this specification.

Conformance SHALL include:

* vocabulary definition structure
* stable VocabularyId
* stable ValueId
* semantic consistency
* version compatibility
* implementation independence

---

## 20.2 Accepted Implementations

The following implementations are expected to consume controlled vocabularies.

Examples include:

* Schema validators
* Schema compilers
* Excel generators
* JSON Schema generators
* YAML Schema generators
* Documentation generators
* Prompt generators
* Caption generators
* Export pipelines
* Future HCDS tooling

Implementations SHALL use `ValueId` for logical processing.

`DisplayName` SHALL be treated as presentation data.

---

# 21. Vocabulary Resolution

## 21.1 Purpose

Vocabulary resolution defines how an implementation locates the authoritative definition of a referenced vocabulary.

---

## 21.2 Resolution Rule

Every `EnumRef` SHALL resolve to exactly one vocabulary identified by `VocabularyId`.

Failure to resolve a vocabulary SHALL invalidate the associated field definition.

---

## 21.3 Resolution Consistency

All implementations SHALL resolve the same `VocabularyId` to the same authoritative definition.

Implementations SHALL NOT substitute alternative vocabularies.

---

# 22. Compiler Readiness

## 22.1 Purpose

The Controlled Vocabulary Model is designed for automatic compilation.

Vocabulary definitions SHALL be sufficiently structured for software to generate implementation-specific outputs.

---

## 22.2 Compiler Inputs

A schema compiler SHALL consume:

* HCDS Schema
* Field Model
* Controlled Vocabulary definitions
* Entity Specifications

---

## 22.3 Compiler Outputs

Future compiler targets MAY include:

* JSON enumerations
* YAML enumerations
* Excel validation lists
* SQL lookup tables
* Python Enum classes
* TypeScript enums
* Rust enums
* Go constants
* API enumeration definitions
* Documentation tables

Logical vocabulary definitions SHALL remain independent of these targets.

---

# 23. Prohibited Practices

The following practices are prohibited.

Defining vocabulary values directly inside business specifications.

Duplicating VocabularyId definitions.

Changing the semantic meaning of an existing ValueId.

Encoding implementation-specific information inside vocabulary definitions.

Using localized display names for logical processing.

Using generated artifacts as authoritative vocabulary definitions.

Reusing removed ValueId identifiers for unrelated meanings.

---

# 24. Normative References

This specification depends upon:

* HCDS_Schema.md
* Field_Model_Spec.md

The following specifications SHALL reference this document when defining Enum fields:

* Dataset_Master_Spec.md
* Character_Profile_Spec.md
* Character_Identity_Spec.md
* Appearance_Spec.md
* Costume_Spec.md
* Pose_Action_Spec.md
* Expression_Spec.md
* Camera_Spec.md
* Scene_Context_Spec.md
* Metadata_Spec.md

Implementation specifications MAY reference this document when generating physical enumeration representations.

---

# 25. Controlled Vocabulary Authority

This specification is the sole authority defining the HCDS Controlled Vocabulary Model.

Business specifications SHALL define:

* which vocabulary is referenced

Business specifications SHALL NOT define:

* vocabulary structure
* vocabulary metadata
* vocabulary lifecycle
* vocabulary compatibility rules

Those responsibilities belong exclusively to this specification.

---

# 26. Freeze Decision

The Controlled Vocabulary Model defined by this specification is hereby frozen for HCDS v2.0.

Future vocabulary definitions SHALL conform to this model.

Changes affecting vocabulary structure or metadata SHALL require a future schema version.

---

# 27. Completion Statement

The Controlled Vocabulary Model establishes a standardized method for defining and managing controlled vocabularies throughout the HCDS ecosystem.

Together with:

* HCDS_Schema.md
* Field_Model_Spec.md

it provides the complete logical foundation for consistent field definitions, validation, schema compilation, and implementation across all HCDS tooling.

---

# 28. Implementation Readiness

This specification is implementation-ready.

It is intended for direct consumption by:

* Claude Code
* Codex
* Schema compilers
* Validation engines
* Documentation generators
* Generator implementations
* Future HCDS tooling

No additional architectural interpretation should be required before implementation.

---

# 29. End of Specification

This document is the authoritative Controlled Vocabulary specification for HCDS v2.0.

It defines the canonical model for all controlled vocabularies referenced by HCDS logical fields.

End of document.
