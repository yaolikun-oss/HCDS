# HCDS Schema

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Define the authoritative data schema for all HCDS datasets.

---

# 1. Purpose

This specification defines the official HCDS Schema.

The HCDS Schema is the canonical data model for all HCDS implementations.

Every dataset, generator, validator, exporter, and downstream consumer SHALL conform to this schema.

This document is the only specification permitted to define HCDS data fields.

---

# 2. Scope

This specification defines:

* schema architecture
* entity model
* field ownership
* field classification
* naming rules
* data relationships
* validation principles
* schema versioning

This specification does **not** define:

* Excel worksheet layout
* prompt construction
* caption generation
* exporter formats
* implementation details

Those subjects are specified by dedicated documents.

---

# 3. Authority

This document is the authoritative definition of the HCDS Schema.

No other specification may redefine schema fields.

Other specifications MAY:

* reference fields
* constrain field usage
* define validation
* define generation behavior

Other specifications SHALL NOT:

* rename fields
* redefine meanings
* introduce conflicting definitions

---

# 4. Design Principles

The HCDS Schema SHALL satisfy the following principles.

---

## Principle 1 — Schema First

All downstream artifacts SHALL originate from schema-defined data.

No generator SHALL invent additional business fields.

---

## Principle 2 — Machine Readable

Every field SHALL be interpretable by software.

Field definitions SHALL avoid ambiguous natural language.

---

## Principle 3 — Single Responsibility

Each field SHALL represent exactly one concept.

A field SHALL NOT encode multiple independent meanings.

---

## Principle 4 — Normalization

Equivalent information SHALL be represented only once.

Duplicated semantic fields are prohibited.

---

## Principle 5 — Extensibility

New fields MAY be added in future schema versions.

Existing field semantics SHALL remain backward compatible whenever possible.

---

## Principle 6 — Consumer Independence

The schema SHALL remain independent of:

* image models
* video models
* training frameworks
* workflow engines
* programming languages

---

# 5. Schema Hierarchy

The HCDS Schema is organized into logical entities.

```text
Dataset
    │
    ├── Character
    │       │
    │       ├── Identity
    │       ├── Appearance
    │       ├── Costume
    │       ├── Pose
    │       ├── Expression
    │       └── Metadata
    │
    ├── Camera
    │
    ├── Scene
    │
    ├── Negative Prompt
    │
    └── Export Metadata
```

Each entity SHALL have an independent specification.

---

# 6. Canonical Entity Model

The following entities are defined by HCDS.

| Entity          | Responsibility               |
| --------------- | ---------------------------- |
| Dataset         | Dataset-level metadata       |
| Character       | One historical character     |
| Identity        | Historical identity          |
| Appearance      | Physical appearance          |
| Costume         | Clothing and equipment       |
| Pose            | Observable body posture      |
| Expression      | Observable facial expression |
| Camera          | Camera composition           |
| Scene           | Environmental context        |
| Negative Prompt | Generation exclusions        |
| Metadata        | Generation metadata          |

Each entity SHALL own its own fields.

---

# 7. Schema Ownership

Ownership SHALL be exclusive.

Example:

Identity owns:

* name
* dynasty
* title
* role

Appearance owns:

* face
* hair
* body
* age

Costume owns:

* clothing
* accessories
* armor

No field SHALL belong to multiple entities.

---

# 8. Schema Layering

The HCDS Schema is divided into four logical layers.

```text
Layer 1
Dataset

↓

Layer 2
Character

↓

Layer 3
Visual Description

↓

Layer 4
Generation Metadata
```

Responsibilities SHALL NOT cross layers.

---

# 9. Dataset Entity

The Dataset entity represents dataset-level information.

Examples include:

* dataset identifier
* schema version
* dataset version
* language
* author
* license

Dataset fields SHALL NOT contain character-specific information.

---

# 10. Character Entity

The Character entity represents exactly one historical character.

A Character SHALL be the primary unit of HCDS.

Each Character SHALL possess exactly one identity.

Each Character MAY possess multiple visual variations.

The Character entity SHALL serve as the parent entity for all character-related specifications.

---

# 11. Character Relationship Model

Relationships SHALL follow the structure below.

```text
Character
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

Sub-entities SHALL NOT exist independently of a Character.

---

# 12. Field Categories

Every schema field SHALL belong to exactly one category.

| Category       | Description                          |
| -------------- | ------------------------------------ |
| Identifier     | Stable identifiers                   |
| Classification | Taxonomy and categories              |
| Description    | Observable properties                |
| Constraint     | Validation or generation constraints |
| Metadata       | Processing information               |

Field categories SHALL remain stable across schema versions.

---

# 13. Identifier Rules

Identifiers SHALL satisfy the following requirements.

They SHALL:

* be unique
* remain stable
* be machine-readable
* avoid semantic ambiguity

Identifiers SHALL NOT depend upon filenames.

Identifiers SHALL NOT depend upon prompts.

Identifiers SHALL NOT depend upon generated outputs.

---

# 14. Field Naming Rules

Field names SHALL:

* use English
* use PascalCase or Snake_Case according to project convention
* remain stable across versions
* express one concept only

Field names SHALL NOT:

* contain spaces
* include implementation-specific terminology
* include model names
* include workflow names

---

# 15. Part 1 Completion

The remaining sections define:

* Identity Entity
* Appearance Entity
* Costume Entity
* Pose Entity
* Expression Entity
* Camera Entity
* Scene Entity
* Negative Prompt Entity
* Metadata Entity
* Validation Rules
* Schema Versioning
* Compliance Requirements

These sections continue in Part 2 without restarting numbering.

End of Part 1.

---

# 16. Identity Entity

## 16.1 Purpose

The Identity entity defines the immutable historical identity of a character.

Identity describes **who the character is**, not how the character appears.

Identity SHALL remain stable across all visual variations.

---

## 16.2 Responsibilities

The Identity entity SHALL own information such as:

* character identifier
* canonical name
* alternative names
* dynasty
* ethnicity
* historical role
* official title
* social status
* historical period

Identity SHALL NOT contain appearance information.

---

## 16.3 Stability

Identity fields SHALL remain unchanged unless historical research requires correction.

Changing clothing, age, pose, or camera SHALL NOT modify Identity.

---

# 17. Appearance Entity

## 17.1 Purpose

The Appearance entity defines the intrinsic physical characteristics of a character.

Appearance describes permanent or semi-permanent observable features.

---

## 17.2 Responsibilities

Appearance MAY include:

* biological sex
* estimated age
* body type
* facial structure
* skin tone
* eye characteristics
* eyebrow characteristics
* nose characteristics
* mouth characteristics
* beard characteristics
* hairstyle
* hair color
* distinguishing physical traits

Appearance SHALL describe observable facts.

Appearance SHALL NOT describe emotions or poses.

---

## 17.3 Persistence

Appearance SHALL remain consistent across different images unless an explicit appearance variation is defined.

---

# 18. Costume Entity

## 18.1 Purpose

The Costume entity defines everything worn or carried by the character.

Costume is independent of identity and appearance.

---

## 18.2 Responsibilities

Costume MAY include:

* robe
* armor
* hat
* crown
* belt
* boots
* gloves
* jewelry
* weapon
* handheld objects
* official insignia

---

## 18.3 Separation

Costume SHALL NOT define:

* facial characteristics
* body shape
* emotions
* pose
* camera

---

## 18.4 Variations

A Character MAY own multiple Costume definitions.

Each Costume SHALL have its own identifier.

---

# 19. Pose Entity

## 19.1 Purpose

Pose defines the observable posture of the body.

Pose SHALL be directly observable.

---

## 19.2 Principles

Pose descriptions SHALL be objective.

Examples:

* both hands behind back
* right hand holding sword
* seated upright
* walking forward
* kneeling on one knee

The following are prohibited:

* majestic stance
* heroic posture
* elegant standing

because they are subjective.

---

## 19.3 Independence

Pose SHALL NOT define:

* emotion
* clothing
* camera
* scene

---

# 20. Expression Entity

## 20.1 Purpose

Expression defines observable facial expression.

Expression SHALL describe visible facial configuration rather than inferred emotion.

---

## 20.2 Examples

Permitted examples include:

* neutral face
* slight smile
* closed mouth
* eyes focused forward
* eyebrows slightly raised

Prohibited examples include:

* loyal
* brave
* determined
* wise

These describe interpretation rather than observation.

---

## 20.3 Independence

Expression SHALL remain independent of Pose.

Changing expression SHALL NOT require changing pose.

---

# 21. Camera Entity

## 21.1 Purpose

The Camera entity defines how the character is viewed.

Camera describes image composition rather than character properties.

---

## 21.2 Responsibilities

Camera MAY include:

* framing
* viewing angle
* camera height
* focal perspective
* aspect ratio
* crop type
* viewing direction

---

## 21.3 Independence

Camera SHALL NOT describe:

* clothing
* identity
* appearance
* emotion

---

# 22. Scene Entity

## 22.1 Purpose

Scene defines the environmental context surrounding the character.

Scene SHALL remain external to the character.

---

## 22.2 Responsibilities

Scene MAY define:

* location
* architecture
* terrain
* weather
* lighting environment
* vegetation
* furniture
* decorative objects

---

## 22.3 Independence

Scene SHALL NOT redefine:

* clothing
* body
* face
* pose
* identity

Characters SHALL remain reusable across different scenes.

---

# 23. Negative Prompt Entity

## 23.1 Purpose

The Negative Prompt entity defines unwanted generation outcomes.

Negative prompts are constraints rather than descriptions.

---

## 23.2 Responsibilities

Negative prompts MAY include exclusions for:

* anatomy defects
* rendering artifacts
* incorrect costume
* unwanted accessories
* duplicate limbs
* malformed hands
* incorrect facial features

---

## 23.3 Scope

Negative prompts SHALL NOT redefine positive descriptions.

Negative prompts SHALL complement generation rather than replace descriptive fields.

---

# 24. Metadata Entity

## 24.1 Purpose

Metadata records information required for generation, validation, and reproducibility.

Metadata SHALL describe processing context rather than historical content.

---

## 24.2 Responsibilities

Metadata MAY include:

* schema version
* dataset version
* record version
* creation timestamp
* modification timestamp
* generator version
* exporter version
* validation status
* language

---

## 24.3 Independence

Metadata SHALL NOT modify business meaning.

Changing metadata SHALL NOT alter the historical description of the character.

---

# 25. Entity Relationships

The relationships between entities SHALL follow the model below.

```text id="j0bfmz"
Dataset
    │
    └── Character
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

Each Character SHALL own exactly one complete entity graph.

No entity SHALL be shared between unrelated Characters unless explicitly defined by a future specification.

---

# 26. Entity Independence Rules

Every entity SHALL satisfy the following requirements.

* one responsibility
* independent ownership
* stable semantics
* machine-readable definition
* implementation independence

Cross-entity duplication is prohibited.

---

# 27. Part 2 Completion

The remaining sections define:

* field data types
* validation model
* cardinality rules
* required versus optional fields
* schema evolution
* backward compatibility
* compliance requirements
* freeze decision

These sections continue in Part 3 without restarting numbering.

End of Part 2.

---

# 28. Field Data Model

## 28.1 Purpose

This section defines the common data model shared by all HCDS entities.

Every field defined by HCDS SHALL conform to one of the data types specified herein.

Entity-specific field definitions are provided in their respective specifications.

---

## 28.2 Supported Data Types

The HCDS Schema recognizes the following logical data types.

| Data Type   | Description                                     |
| ----------- | ----------------------------------------------- |
| String      | Text value                                      |
| Integer     | Whole number                                    |
| Decimal     | Numeric value with fractional precision         |
| Boolean     | True or False                                   |
| Enumeration | One value selected from a controlled vocabulary |
| Array       | Ordered collection of values                    |
| Object      | Structured sub-entity                           |
| Reference   | Identifier pointing to another entity           |
| Version     | Structured version identifier                   |

Implementations MAY use equivalent native language types.

---

## 28.3 Null Values

Null values SHALL be permitted only when explicitly allowed by the corresponding specification.

Required fields SHALL NOT contain null values.

Empty strings SHALL NOT be used as substitutes for null values.

---

# 29. Cardinality Rules

Every field SHALL declare its cardinality.

The following cardinalities are supported.

| Cardinality | Meaning               |
| ----------- | --------------------- |
| 1           | Exactly one value     |
| 0..1        | Optional single value |
| 1..N        | One or more values    |
| 0..N        | Zero or more values   |

Each field specification SHALL define exactly one cardinality.

---

# 30. Required and Optional Fields

## 30.1 Required Fields

Required fields SHALL:

* exist
* satisfy type requirements
* satisfy validation rules

Missing required fields SHALL invalidate the record.

---

## 30.2 Optional Fields

Optional fields MAY be omitted.

If present, they SHALL satisfy all validation requirements applicable to their type.

Optional fields SHALL NOT alter the semantics of required fields.

---

# 31. Controlled Vocabularies

Fields defined as Enumeration SHALL reference controlled vocabularies.

Controlled vocabularies SHALL:

* define canonical values
* avoid synonyms
* avoid ambiguous wording
* remain version controlled

Free-text values SHALL NOT replace controlled vocabularies where an enumeration exists.

---

# 32. Reference Model

References SHALL link entities through stable identifiers.

References SHALL NOT rely upon:

* filenames
* prompts
* display names
* spreadsheet row numbers

Broken references SHALL invalidate the affected record.

---

# 33. Validation Model

Validation SHALL occur before any generation process.

Validation SHALL include at minimum:

* field existence
* field type
* cardinality
* enumeration membership
* identifier uniqueness
* reference integrity
* schema version compatibility

Validation SHALL produce machine-readable results.

---

# 34. Record Integrity

Each Character record SHALL be internally consistent.

Integrity verification SHALL ensure:

* exactly one Identity entity
* valid Appearance entity
* valid Costume entity
* valid Pose entity
* valid Expression entity
* valid Metadata entity

Incomplete records SHALL fail validation.

---

# 35. Schema Evolution

The HCDS Schema SHALL evolve through explicit versioning.

Schema evolution SHALL prioritize:

* backward compatibility
* predictable migration
* stable identifiers

Existing field semantics SHALL NOT change without a new schema version.

---

# 36. Backward Compatibility

Minor schema versions MAY introduce:

* new optional fields
* additional enumeration values
* clarifications

Major schema versions MAY introduce:

* structural changes
* deprecated entities
* removed fields
* incompatible changes

Migration guidance SHALL accompany incompatible changes.

---

# 37. Deprecation Policy

Deprecated fields SHALL remain documented until officially removed.

Each deprecated field SHALL specify:

* replacement field (if any)
* deprecation version
* removal version (if planned)

Deprecated fields SHALL NOT be reused for unrelated purposes.

---

# 38. Schema Compliance

An implementation SHALL be considered HCDS Schema compliant only if it:

* preserves entity ownership
* preserves field semantics
* validates required fields
* validates references
* respects cardinality
* follows version compatibility rules

Partial implementations SHALL clearly identify unsupported features.

---

# 39. Relationship to Other Specifications

This specification defines the authoritative data model.

The following specifications SHALL build upon this schema without redefining it:

* Dataset_Master_Spec.md
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

Generation, export, validation, and implementation specifications SHALL reference this document as their schema authority.

---

# 40. Freeze Decision

The HCDS Schema defined by this specification is hereby frozen.

All future HCDS specifications SHALL extend or reference this schema rather than redefine it.

Changes affecting entity ownership, field semantics, or structural relationships constitute schema changes and SHALL require a new schema version.

---

# 41. End of Part 3

The remaining sections define:

* schema versioning strategy
* implementation conformance
* extension mechanism
* prohibited practices
* final compliance statement
* end of specification

These sections continue in Part 4 without restarting numbering.

End of Part 3.

---

# 42. Schema Versioning

## 42.1 Purpose

Schema versioning defines the compatibility relationship between different releases of the HCDS Schema.

Every implementation SHALL declare the schema version it supports.

---

## 42.2 Version Format

The HCDS Schema SHALL use Semantic Versioning.

```text
MAJOR.MINOR.PATCH
```

Examples:

```text
2.0.0
2.1.0
2.1.3
3.0.0
```

---

## 42.3 Major Version

A MAJOR version SHALL be incremented when introducing incompatible schema changes.

Examples include:

* entity restructuring
* removal of required fields
* incompatible field semantics
* incompatible relationship changes

---

## 42.4 Minor Version

A MINOR version SHALL be incremented when introducing backward-compatible improvements.

Examples include:

* new optional fields
* new entities
* additional enumeration values
* documentation clarifications

---

## 42.5 Patch Version

A PATCH version SHALL be incremented for non-structural improvements.

Examples include:

* documentation corrections
* typographical fixes
* clarification of validation rules

PATCH releases SHALL NOT modify schema behavior.

---

# 43. Schema Extension

## 43.1 Extension Principle

The HCDS Schema SHALL remain extensible.

Extensions SHALL preserve compatibility whenever reasonably possible.

---

## 43.2 Extension Requirements

Every extension SHALL:

* define a single responsibility
* specify ownership
* specify data type
* specify validation requirements
* specify version introduction
* avoid semantic duplication

---

## 43.3 Extension Restrictions

Extensions SHALL NOT:

* redefine existing entities
* redefine field semantics
* duplicate existing concepts
* violate entity ownership

---

# 44. Implementation Conformance

An implementation claiming HCDS compatibility SHALL satisfy all mandatory requirements defined by this specification.

Conformance SHALL include:

* schema interpretation
* entity relationships
* field ownership
* cardinality
* validation behavior
* version compatibility

Partial implementation SHALL explicitly declare unsupported features.

---

# 45. Compatibility Requirements

Schema compatibility SHALL be evaluated according to:

* entity compatibility
* field compatibility
* relationship compatibility
* validation compatibility

Compatibility SHALL be documented for every released schema version.

---

# 46. Prohibited Practices

The following practices are prohibited.

Creating multiple definitions for the same field.

Changing field semantics without a schema version update.

Embedding implementation-specific logic inside the schema.

Encoding workflow behavior inside schema definitions.

Using model-specific terminology as schema concepts.

Duplicating authoritative field definitions across specifications.

Treating generated artifacts as authoritative schema data.

---

# 47. Compliance Checklist

An HCDS-compliant implementation SHALL satisfy all of the following.

✓ Interpret the official HCDS Schema.

✓ Preserve entity ownership.

✓ Preserve field semantics.

✓ Validate required fields.

✓ Validate references.

✓ Respect cardinality.

✓ Respect schema version compatibility.

✓ Produce machine-readable data.

✓ Remain implementation independent.

---

# 48. Non-Goals

The HCDS Schema does not define:

* prompt engineering
* image generation quality
* AI model selection
* training parameters
* workflow configuration
* software architecture
* repository management

These subjects belong to dedicated specifications.

---

# 49. Future Evolution

Future HCDS releases MAY introduce:

* additional entities
* additional field types
* additional validation capabilities
* additional export metadata

Future evolution SHALL preserve the architectural principles defined by:

* Documentation_Architecture.md
* System_Architecture.md
* Data_Flow_Architecture.md
* Single_Source_of_Truth.md

---

# 50. Normative References

This specification is supported by the following companion specifications.

Architecture Layer

* Documentation_Architecture.md
* Documentation_Tree.md
* System_Architecture.md
* Data_Flow_Architecture.md
* Single_Source_of_Truth.md

Schema Layer

* Field_Model_Spec.md
* Dataset_Master_Spec.md
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

Generation and implementation specifications SHALL reference this schema rather than redefining it.

---

# 51. Schema Authority

This document is the only specification authorized to define the HCDS Entity Model.

Entity ownership, entity relationships, and schema structure SHALL originate exclusively from this specification.

Any conflicting definition SHALL be considered non-compliant.

---

# 52. Freeze Decision

The HCDS Schema defined by this specification is hereby frozen as the normative schema for HCDS v2.0.

All downstream specifications SHALL extend or reference this schema.

Architectural modifications SHALL require a future schema version.

---

# 53. Completion Statement

The HCDS Schema establishes the canonical data model for:

* Dataset definition
* Character definition
* Visual description
* Generation metadata
* Validation
* Schema evolution

It serves as the foundation for every subsequent HCDS specification.

---

# 54. Implementation Readiness

This specification is implementation-ready.

It is intended to be consumed directly by:

* Claude Code
* Codex
* Python generators
* Schema validators
* Export pipelines
* Future HCDS tooling

No additional architectural interpretation should be required before implementation.

---

# 55. End of Specification

This document is the authoritative HCDS Schema specification for version 2.0.

End of document.
