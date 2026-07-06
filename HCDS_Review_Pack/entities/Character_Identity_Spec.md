# Character Identity Specification

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Define the logical identity model for historical characters in HCDS.

---

# 1. Purpose

This specification defines the Identity entity of HCDS.

Identity answers one question only:

> **Who is this historical character?**

Identity does not describe appearance, clothing, pose, camera, scene, or generation behavior.

It defines the immutable historical identity of a character.

---

# 2. Scope

This specification defines:

* Identity responsibilities
* logical fields
* field constraints
* entity relationships
* validation requirements

This specification does not define:

* physical appearance
* costume
* pose
* expression
* camera
* scene
* metadata
* implementation storage

---

# 3. Relationship to Other Specifications

The Identity entity is defined within the HCDS entity model.

```text
HCDS_Schema.md
        ↓
Field_Model_Spec.md
        ↓
Controlled_Vocabulary_Spec.md
        ↓
Dataset_Master_Spec.md
        ↓
Character_Identity_Spec.md
```

This specification SHALL use the canonical Field Model.

It SHALL NOT redefine field metadata.

---

# 4. Responsibilities

The Identity entity is responsible for describing the historical identity of one character.

It SHALL define:

* canonical identity
* historical classification
* historical role
* historical affiliation

It SHALL NOT define visual characteristics.

---

# 5. Identity Categories

The Identity entity SHALL organize logical fields into Identity Categories.

Identity Categories define the domain structure of historical identity.

They SHALL prevent unrelated identity concepts from being represented as a flat field list.

The following Identity Categories are defined.

| Category                  | Responsibility                              |
| ------------------------- | ------------------------------------------- |
| Core Identity             | Stable character identity                   |
| Historical Names          | Names and name variants                     |
| Historical Classification | Dynasty, ethnicity, status, and affiliation |
| Historical Titles         | Titles and formal roles                     |
| Historical Timeline       | Known temporal identity information         |
| Historical Notes          | Supplemental identity remarks               |

Each Identity field SHALL belong to exactly one Identity Category.

---

# 6. Logical Fields

The Identity entity SHALL define logical fields within Identity Categories.

## 6.1 Core Identity

| Field       | Purpose                     |
| ----------- | --------------------------- |
| CharacterId | Stable character identifier |

## 6.2 Historical Names

| Field            | Purpose                      |
| ---------------- | ---------------------------- |
| CanonicalName    | Official historical name     |
| AlternativeNames | Alternative historical names |
| CourtesyName     | Courtesy name, if applicable |
| TempleName       | Temple name, if applicable   |
| PosthumousName   | Posthumous name, if applicable |

## 6.3 Historical Classification

| Field        | Purpose               |
| ------------ | --------------------- |
| Dynasty      | Historical dynasty    |
| Ethnicity    | Historical ethnicity  |
| SocialStatus | Social classification |

## 6.4 Historical Titles

| Field          | Purpose                            |
| -------------- | ---------------------------------- |
| HistoricalRole | Primary historical role            |
| OfficialTitle  | Highest official title represented |

## 6.5 Historical Timeline

| Field        | Purpose                  |
| ------------ | ------------------------ |
| BirthYear    | Birth year, if known     |
| DeathYear    | Death year, if known     |
| ActivePeriod | Historical active period |

## 6.6 Historical Notes

| Field           | Purpose                         |
| --------------- | ------------------------------- |
| HistoricalNotes | Supplemental historical remarks |

The exact field definitions SHALL conform to the Field Model.

Optional historical name and timeline fields MAY be omitted when not applicable or unknown.

---

# 7. Field Constraints

The following constraints apply.

## 7.1 Category Ownership

Each Identity field SHALL belong to exactly one Identity Category.

Identity Categories SHALL NOT redefine Field Model metadata.

---

## 7.2 CharacterId

* SHALL be unique.
* SHALL remain stable.
* SHALL never be reused.

---

## 7.3 CanonicalName

* SHALL contain exactly one canonical historical name.
* SHALL NOT contain aliases.

---

## 7.4 AlternativeNames

* MAY contain zero or more historical aliases.
* SHALL NOT replace CanonicalName.

---

## 7.5 CourtesyName / TempleName / PosthumousName

* MAY be omitted when not applicable.
* SHALL NOT be required for all historical characters.
* SHALL remain under Historical Names.

---

## 7.6 Dynasty

* SHALL reference the `Dynasty` controlled vocabulary whenever applicable.

---

## 7.7 HistoricalRole

* SHALL reference a controlled vocabulary where defined.
* SHALL describe historical function rather than visual occupation.

Example:

```text
Emperor
General
Scholar
Official
Queen Dowager
```

---

## 7.8 BirthYear / DeathYear

Unknown values MAY be omitted.

Estimated values SHALL follow future date representation specifications.

BirthYear and DeathYear SHALL remain under Historical Timeline.

---

# 8. Entity Relationships

Identity belongs to exactly one Character Record.

Identity SHALL relate to:

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
        └── Metadata
```

Identity SHALL remain independent of all sibling entities.

---

# 9. Validation Requirements

An Identity entity SHALL satisfy the following requirements.

Mandatory:

* valid CharacterId
* valid CanonicalName
* valid Dynasty (if applicable)
* unique identity within the dataset

Validation SHALL reject duplicate CharacterId values.

Validation SHALL reject missing required fields.

---

# 10. Examples (Informative)

Example:

| Field          | Example            |
| -------------- | ------------------ |
| CharacterId    | LIAO_XIAO_CHUO_001 |
| CanonicalName  | Xiao Chuo          |
| Dynasty        | Liao               |
| HistoricalRole | Empress Dowager    |
| OfficialTitle  | Empress Dowager    |
| Ethnicity      | Khitan             |

This example is informative only.

Implementations MAY use equivalent representations while preserving semantics.

---

## Part 1 Completion

The remaining sections define:

* compatibility
* lifecycle
* implementation conformance
* prohibited practices
* normative references
* freeze decision
* end of specification

These sections continue in Part 2 without restarting numbering.

End of Part 1.

---

# 11. Identity Domain Structure

## 11.1 Purpose

The Identity entity SHALL organize its logical fields into domain categories.

Domain categories improve readability and maintainability.

They SHALL NOT alter field ownership or field semantics.

---

## 11.2 Identity Categories

The Identity entity SHALL organize logical fields into the following categories.

| Category                  | Responsibility                            |
| ------------------------- | ----------------------------------------- |
| Core Identity             | Stable identifiers and canonical identity |
| Historical Names          | Historical naming system                  |
| Historical Classification | Historical affiliation and classification |
| Historical Timeline       | Historical temporal information           |
| Historical Position       | Official titles and historical roles      |
| Historical Notes          | Supplemental historical information       |

Categories are organizational only.

Logical fields remain individually defined by the Field Model.

---

# 12. Core Identity

The Core Identity category establishes the permanent identity of a historical character.

Typical logical fields include:

* CharacterId
* CanonicalName

Core Identity fields SHALL exist for every Character Record.

---

# 13. Historical Names

The Historical Names category records alternative historical naming conventions.

Possible logical fields include:

* AlternativeNames
* CourtesyName
* TempleName
* PosthumousName

These fields are optional unless required by a future business specification.

Absence of these fields SHALL NOT invalidate the Identity entity.

---

# 14. Historical Classification

The Historical Classification category describes how a character is classified historically.

Typical logical fields include:

* Dynasty
* Ethnicity
* SocialStatus

Controlled vocabularies SHOULD be used whenever available.

---

# 15. Historical Timeline

The Historical Timeline category records chronological information.

Possible logical fields include:

* BirthYear
* DeathYear
* ActivePeriod

Historical dates MAY be:

* known
* estimated
* unknown

Unknown values SHALL NOT require placeholder values.

Implementations SHALL distinguish between:

* unknown
* not applicable
* intentionally omitted

---

# 16. Historical Position

The Historical Position category describes the character's historical function.

Typical logical fields include:

* HistoricalRole
* OfficialTitle

These fields describe historical identity.

They SHALL NOT describe visual appearance, costume, or pose.

---

# 17. Historical Notes

Historical Notes provide supplementary information that does not belong to another category.

Typical examples include:

* disputed historical records
* alternative historical interpretations
* explanatory remarks

Historical Notes SHALL NOT replace structured logical fields.

---

# 18. Identity Consistency Rules

An Identity entity SHALL remain internally consistent.

Examples include:

* CanonicalName SHALL identify the same person referenced by CharacterId.
* Dynasty SHALL be compatible with Historical Timeline where applicable.
* OfficialTitle SHALL not contradict HistoricalRole.

Implementations SHOULD report inconsistencies during validation.

---

# 19. Identity Independence

Identity SHALL remain independent from:

* Appearance
* Costume
* Pose
* Expression
* Camera
* Scene
* Metadata

Changing any of the above entities SHALL NOT alter Identity.

Likewise, correcting historical identity SHALL NOT require changes to visual entities unless explicitly justified.

---

# 20. Part 2 Completion

The remaining sections define:

* compatibility
* lifecycle
* implementation conformance
* prohibited practices
* normative references
* freeze decision
* end of specification

These sections continue in Part 3 without restarting numbering.

End of Part 2.

---

# 21. Identity Lifecycle

## 21.1 Purpose

The Identity entity SHALL follow a controlled lifecycle to ensure historical consistency and traceability.

Lifecycle management applies to the logical definition of the Identity entity, not to the historical person.

---

## 21.2 Lifecycle States

An Identity entity SHALL exist in one of the following states.

| State      | Description                             |
| ---------- | --------------------------------------- |
| Draft      | Initial definition under construction   |
| Review     | Historical review in progress           |
| Approved   | Accepted as an official HCDS definition |
| Active     | Used in production datasets             |
| Deprecated | Replaced by a newer identity definition |
| Archived   | Retained for historical reference       |

Only **Active** Identity definitions SHALL be used in production datasets.

---

# 22. Identity Compatibility

## 22.1 Compatible Changes

The following changes are considered compatible.

* improving descriptions
* adding optional logical fields
* correcting typographical errors
* adding implementation notes
* adding historical references

Such changes SHALL preserve the semantic meaning of the Identity entity.

---

## 22.2 Incompatible Changes

The following changes SHALL be considered incompatible.

* changing CharacterId
* changing the semantic meaning of CanonicalName
* changing entity ownership
* redefining HistoricalRole
* changing controlled vocabulary semantics

Incompatible changes SHALL require an appropriate schema version update.

---

# 23. Identity Validation

Identity validation SHALL verify:

* CharacterId uniqueness
* required field completeness
* controlled vocabulary consistency
* historical consistency
* schema compatibility
* field model compliance

Validation SHALL produce machine-readable results.

Business-specific historical verification MAY be implemented by future validators.

---

# 24. Prohibited Practices

The following practices are prohibited.

Using visual characteristics to define Identity.

Duplicating Identity definitions across multiple Character Records.

Using implementation-specific identifiers as CharacterId.

Embedding prompt wording inside Identity fields.

Embedding workflow logic inside Identity definitions.

Using generated content as the authoritative historical identity.

---

# 25. Implementation Conformance

Any implementation claiming compatibility with the HCDS Identity Model SHALL preserve:

* logical field definitions
* field ownership
* domain category structure
* entity relationships
* implementation independence

Different physical implementations SHALL preserve identical logical semantics.

---

# 26. Normative References

This specification depends upon:

* HCDS_Schema.md
* Field_Model_Spec.md
* Controlled_Vocabulary_Spec.md
* Dataset_Master_Spec.md

The following specifications SHALL reference the Identity entity where appropriate:

* Character_Profile_Spec.md
* Appearance_Spec.md
* Costume_Spec.md
* Pose_Action_Spec.md
* Expression_Spec.md
* Camera_Spec.md
* Scene_Context_Spec.md
* Metadata_Spec.md

Identity SHALL remain the authoritative source of historical identity information.

---

# 27. Identity Authority

This specification is the sole authority defining the HCDS Identity entity.

Other specifications MAY reference Identity.

They SHALL NOT redefine:

* Identity responsibilities
* Identity logical categories
* Identity field semantics
* Identity validation principles

---

# 28. Freeze Decision

The Character Identity Model defined by this specification is hereby frozen for HCDS v2.0.

Future modifications SHALL preserve:

* logical identity
* field ownership
* domain category organization
* implementation independence

Changes affecting semantic meaning SHALL require a future schema version.

---

# 29. Completion Statement

The Identity entity establishes the canonical historical identity model for HCDS.

Together with:

* HCDS_Schema.md
* Field_Model_Spec.md
* Controlled_Vocabulary_Spec.md
* Dataset_Master_Spec.md

it forms the authoritative foundation for representing historical persons independently of appearance, costume, pose, or implementation technology.

---

# 30. End of Specification

This document is the authoritative Character Identity specification for HCDS v2.0.

End of document.
