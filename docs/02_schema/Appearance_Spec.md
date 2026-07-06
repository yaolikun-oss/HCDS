# Appearance Specification

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Define the logical appearance model for historical characters in HCDS.

---

# 1. Purpose

This specification defines the Appearance entity of HCDS.

Appearance answers one question only:

> **What does this historical character physically look like?**

Appearance defines intrinsic, observable physical characteristics.

Appearance SHALL NOT define:

* identity
* clothing
* equipment
* pose
* facial expression
* camera
* scene
* generation behavior

---

# 2. Scope

This specification defines:

* appearance responsibilities
* logical fields
* field constraints
* entity relationships
* validation requirements

This specification does not define:

* historical identity
* costume
* pose
* expression
* scene
* metadata
* implementation storage

---

# 3. Relationship to Other Specifications

The Appearance entity is defined within the HCDS entity model.

```text
HCDS_Schema.md
        ↓
Field_Model_Spec.md
        ↓
Controlled_Vocabulary_Spec.md
        ↓
Dataset_Master_Spec.md
        ↓
Appearance_Spec.md
```

This specification SHALL use the canonical Field Model.

It SHALL NOT redefine field metadata.

---

# 4. Responsibilities

The Appearance entity is responsible for describing the observable physical characteristics of a historical character.

Appearance SHALL describe only characteristics that belong to the individual.

Appearance SHALL remain independent of clothing, equipment, and environment.

---

# 5. Appearance Domain Structure

The Appearance entity SHALL organize logical fields into the following categories.

| Category                | Responsibility                |
| ----------------------- | ----------------------------- |
| Biological Profile      | Biological characteristics    |
| Facial Structure        | Stable facial morphology      |
| Hair Characteristics    | Hair-related characteristics  |
| Body Characteristics    | Body shape and build          |
| Distinguishing Features | Persistent identifying traits |

These categories are organizational only.

Field ownership remains unchanged.

---

# 6. Biological Profile

Typical logical fields include:

* BiologicalSex
* EstimatedAge
* AgeGroup

These fields describe biological characteristics rather than historical identity.

EstimatedAge represents the intended visual appearance, not necessarily the character's full historical lifespan.

---

# 7. Facial Structure

Typical logical fields include:

* FaceShape
* EyeShape
* EyeColor
* EyebrowShape
* NoseShape
* MouthShape
* EarShape
* BeardStyle
* MustacheStyle

These fields SHALL describe observable morphology.

They SHALL NOT describe emotion or expression.

---

# 8. Hair Characteristics

Typical logical fields include:

* HairStyle
* HairLength
* HairColor
* Hairline

Hair characteristics SHALL describe the character rather than the hairstyle imposed by costume.

Headwear belongs to the Costume entity.

---

# 9. Body Characteristics

Typical logical fields include:

* HeightCategory
* BodyBuild
* ShoulderWidth
* SkinTone
* HandCharacteristics

These fields SHALL describe stable physical appearance.

Temporary conditions SHALL NOT be represented here.

---

# 10. Distinguishing Features

Typical logical fields include:

* Scar
* Mole
* FacialMark
* MissingFinger
* OtherPermanentFeatures

Distinguishing features SHALL be:

* persistent
* observable
* intrinsic to the individual

Temporary injuries SHALL NOT be represented as Appearance.

---

# 11. Field Constraints

Appearance fields SHALL satisfy the following principles.

* They SHALL describe observable characteristics.
* They SHALL remain implementation independent.
* They SHALL avoid subjective interpretation.
* They SHALL avoid emotional language.
* They SHALL remain stable across costumes and scenes.

---

# 12. Appearance Independence

Appearance SHALL remain independent from:

* Identity
* Costume
* Pose
* Expression
* Camera
* Scene
* Metadata

Changing any of those entities SHALL NOT require modification of Appearance unless the physical appearance itself changes.

---

# 13. Validation Requirements

Appearance validation SHALL verify:

* required field completeness
* controlled vocabulary consistency
* field model compliance
* logical consistency
* schema compatibility

Validation SHALL reject contradictory appearance definitions.

---

# 14. Examples (Informative)

Example:

| Field         | Example    |
| ------------- | ---------- |
| BiologicalSex | Male       |
| EstimatedAge  | 42         |
| FaceShape     | Oval       |
| HairColor     | Black      |
| BeardStyle    | Full Beard |
| BodyBuild     | Athletic   |

These examples are informative only.

Implementations MAY use equivalent representations while preserving logical semantics.

---

# 15. Part 1 Completion

The remaining sections define:

* appearance lifecycle
* compatibility
* implementation conformance
* prohibited practices
* normative references
* freeze decision
* end of specification

These sections continue in Part 2 without restarting numbering.

End of Part 1.

---

# 16. Appearance Lifecycle

## 16.1 Purpose

The Appearance entity SHALL follow a controlled lifecycle to ensure consistency across all HCDS datasets.

The lifecycle applies to the logical definition of appearance rather than generated images.

---

## 16.2 Lifecycle States

An Appearance entity SHALL exist in one of the following states.

| State      | Description                                   |
| ---------- | --------------------------------------------- |
| Draft      | Initial appearance definition                 |
| Review     | Under technical review                        |
| Approved   | Accepted as an official appearance definition |
| Active     | Used in production datasets                   |
| Deprecated | Scheduled for replacement                     |
| Archived   | Retained for historical reference             |

Only **Active** Appearance definitions SHALL be used in production generation.

---

# 17. Appearance Compatibility

## 17.1 Compatible Changes

The following changes are considered compatible.

* improving descriptions
* adding optional logical fields
* improving documentation
* adding implementation notes
* refining controlled vocabulary references

Compatible changes SHALL preserve the semantic meaning of existing fields.

---

## 17.2 Incompatible Changes

The following changes SHALL be considered incompatible.

* changing field semantics
* changing entity ownership
* changing DataType
* changing Required status from optional to mandatory
* redefining biological characteristics

Such changes SHALL require an appropriate schema version update.

---

# 18. Appearance Consistency Rules

An Appearance entity SHALL remain internally consistent.

Examples include:

* EstimatedAge SHALL be compatible with AgeGroup.
* BeardStyle SHALL be compatible with BiologicalSex where applicable.
* HairLength SHALL NOT contradict HairStyle when defined.
* BodyBuild SHALL remain logically compatible with HeightCategory where constrained by future business specifications.

Implementations SHOULD report logical inconsistencies during validation.

---

# 19. Appearance Stability

Appearance SHALL represent characteristics that remain stable across visual variations.

The following SHALL NOT modify Appearance:

* changing clothing
* changing armor
* changing camera angle
* changing background
* changing lighting
* changing pose
* changing facial expression

If a permanent physical characteristic changes, a new Appearance definition MAY be required.

---

# 20. Relationship to Other Entities

Appearance SHALL cooperate with, but remain independent from, other entities.

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

Appearance SHALL NOT duplicate information owned by sibling entities.

---

# 21. Validation Requirements

Appearance validation SHALL verify:

* required field completeness
* logical consistency
* controlled vocabulary validity
* schema compatibility
* field model compliance

Appearance validation SHALL NOT evaluate:

* image quality
* artistic style
* prompt wording
* rendering results

Those responsibilities belong to downstream systems.

---

# 22. Prohibited Practices

The following practices are prohibited.

Using clothing descriptions inside Appearance.

Using emotional descriptions inside Appearance.

Using camera terminology inside Appearance.

Using scene descriptions inside Appearance.

Using prompt fragments as appearance definitions.

Using implementation-specific terminology inside logical fields.

---

# 23. Implementation Conformance

Any implementation claiming compatibility with the HCDS Appearance Model SHALL preserve:

* logical field definitions
* field ownership
* domain category structure
* implementation independence
* semantic consistency

Different physical implementations SHALL preserve identical logical meaning.

---

# 24. Part 2 Completion

The remaining sections define:

* normative references
* appearance authority
* freeze decision
* completion statement
* implementation readiness
* end of specification

These sections continue in Part 3 without restarting numbering.

End of Part 2.

---

# 25. Normative References

This specification depends upon:

* HCDS_Schema.md
* Field_Model_Spec.md
* Controlled_Vocabulary_Spec.md
* Dataset_Master_Spec.md

The following specifications SHALL reference the Appearance entity where appropriate:

* Character_Identity_Spec.md
* Costume_Spec.md
* Pose_Action_Spec.md
* Expression_Spec.md
* Camera_Spec.md
* Scene_Context_Spec.md
* Metadata_Spec.md

Appearance SHALL remain the authoritative source of intrinsic physical characteristics.

---

# 26. Appearance Authority

This specification is the sole authority defining the HCDS Appearance entity.

Other specifications MAY reference Appearance.

They SHALL NOT redefine:

* Appearance responsibilities
* Appearance logical categories
* Appearance field semantics
* Appearance validation principles

Business specifications SHALL extend Appearance only through new logical fields defined in accordance with the HCDS Field Model.

---

# 27. Appearance Evolution

The Appearance entity SHALL evolve conservatively.

Future schema versions MAY:

* introduce new optional logical fields
* introduce new controlled vocabulary references
* clarify documentation

Future schema versions SHALL NOT:

* redefine existing field semantics
* change entity ownership
* invalidate existing compliant datasets without a major schema version

Backward compatibility SHALL be preserved whenever reasonably possible.

---

# 28. Appearance Reusability

One Appearance definition SHOULD be reusable across multiple visual assets representing the same historical character.

Examples include:

* standing portrait
* seated portrait
* horseback portrait
* battle scene
* court scene

These variations SHALL reuse the same Appearance definition unless the character's intrinsic physical characteristics differ.

Appearance definitions SHALL NOT be duplicated solely because of changes in:

* clothing
* equipment
* pose
* expression
* scene
* camera

---

# 29. Completion Statement

The Appearance entity establishes the canonical physical appearance model for historical characters in HCDS.

Together with:

* HCDS_Schema.md
* Field_Model_Spec.md
* Controlled_Vocabulary_Spec.md
* Dataset_Master_Spec.md
* Character_Identity_Spec.md

it provides a stable and implementation-independent representation of intrinsic human appearance for all downstream generators, validators, exporters, and AI systems.

---

# 30. Implementation Readiness

This specification is implementation-ready.

It is intended for direct consumption by:

* Claude Code
* Codex
* Schema compilers
* Validation engines
* Dataset generators
* Documentation generators
* Future HCDS tooling

No additional architectural interpretation should be required before implementation.

---

# 31. Freeze Decision

The HCDS Appearance Model defined by this specification is hereby frozen for HCDS v2.0.

Future modifications SHALL preserve:

* logical appearance semantics
* field ownership
* domain category organization
* implementation independence

Changes affecting semantic meaning SHALL require a future schema version.

---

# 32. End of Specification

This document is the authoritative Appearance specification for HCDS v2.0.

It defines the canonical logical model for describing the intrinsic physical appearance of historical characters.

End of document.
