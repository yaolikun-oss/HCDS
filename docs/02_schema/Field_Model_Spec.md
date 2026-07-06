# Field Model Specification

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Define the standard field definition model used by all HCDS schema specifications.

---

# 1. Purpose

This specification defines the official HCDS Field Model.

The Field Model defines how every HCDS field SHALL be described, validated, versioned, and implemented.

This document does not define business fields.

It defines the metadata structure used to describe fields.

---

# 2. Scope

This specification governs:

* field definition format
* field metadata
* field ownership
* field type declaration
* required status
* cardinality
* default values
* enumeration references
* validation rule references
* version metadata
* deprecation metadata

This specification does not define:

* Character fields
* Appearance fields
* Costume fields
* Pose fields
* Excel column layout
* prompt generation
* exporter behavior

---

# 3. Relationship to HCDS Schema

`HCDS_Schema.md` defines the HCDS Entity Model.

This document defines the HCDS Field Model.

The relationship is:

```text
HCDS_Schema.md
        ↓
Field_Model_Spec.md
        ↓
Entity Specifications
        ↓
Dataset_Master_Spec.md
        ↓
Validators / Generators / Exporters
```

Entity specifications SHALL use this Field Model when defining concrete fields.

---

# 4. Core Principle

Every HCDS field SHALL be defined using one standard field definition structure.

No specification may define fields using an ad-hoc format.

---

# 5. Field Definition Record

Each field SHALL be represented as a Field Definition Record.

A Field Definition Record SHALL contain the following properties:

| Property        | Required | Description                                   |
| --------------- | -------- | --------------------------------------------- |
| FieldName       | Yes      | Stable machine-readable field name            |
| Owner           | Yes      | Entity that owns the field                    |
| DataType        | Yes      | Logical data type                             |
| Required        | Yes      | Whether the field is mandatory                |
| Cardinality     | Yes      | Number of allowed values                      |
| EnumRef         | No       | Controlled vocabulary reference               |
| Default         | No       | Default value                                 |
| Validation      | No       | Validation rule reference                     |
| Description     | Yes      | Human-readable field meaning                  |
| Example         | No       | Example value                                 |
| SinceVersion    | Yes      | Schema version where the field was introduced |
| Deprecated      | Yes      | Whether the field is deprecated               |
| DeprecatedSince | No       | Version where deprecation began               |
| Replacement     | No       | Replacement field if deprecated               |
| Notes           | No       | Additional implementation notes               |

---

# 6. FieldName

## 6.1 Purpose

`FieldName` defines the stable machine-readable identifier of a field.

## 6.2 Requirements

FieldName SHALL:

* be unique within its Owner
* use English
* avoid spaces
* avoid punctuation except underscore if permitted by implementation convention
* remain stable across schema versions
* describe exactly one concept

FieldName SHALL NOT:

* contain prompt text
* contain model names
* contain workflow names
* depend on Excel column position
* depend on generated filenames

---

# 7. Owner

## 7.1 Purpose

`Owner` identifies the entity responsible for the field.

## 7.2 Allowed Values

Owner SHALL reference an HCDS entity defined in `HCDS_Schema.md`.

Examples:

* Dataset
* Character
* Identity
* Appearance
* Costume
* Pose
* Expression
* Camera
* Scene
* NegativePrompt
* Metadata

## 7.3 Ownership Rule

A field SHALL have exactly one Owner.

Shared ownership is prohibited.

---

# 8. DataType

## 8.1 Purpose

`DataType` defines the logical value type of the field.

## 8.2 Allowed Data Types

DataType SHALL use one of the following values:

| DataType  | Meaning                               |
| --------- | ------------------------------------- |
| String    | Text value                            |
| Integer   | Whole number                          |
| Decimal   | Numeric value                         |
| Boolean   | True or False                         |
| Enum      | Controlled vocabulary value           |
| Array     | Ordered collection                    |
| Object    | Structured sub-entity                 |
| Reference | Identifier pointing to another entity |
| Version   | Semantic version value                |
| DateTime  | Timestamp value                       |

## 8.3 Implementation Mapping

Implementations MAY map these logical types to native language types.

The logical meaning SHALL remain unchanged.

---

# 9. Required

## 9.1 Purpose

`Required` defines whether a field must be present.

## 9.2 Allowed Values

Required SHALL be Boolean.

```text
true
false
```

## 9.3 Rule

If Required is `true`, the field SHALL exist and SHALL contain a valid non-null value.

If Required is `false`, the field MAY be omitted.

---

# 10. Cardinality

## 10.1 Purpose

`Cardinality` defines how many values a field may contain.

## 10.2 Allowed Values

| Cardinality | Meaning             |
| ----------- | ------------------- |
| 1           | Exactly one value   |
| 0..1        | Zero or one value   |
| 1..N        | One or more values  |
| 0..N        | Zero or more values |

## 10.3 Rule

Cardinality SHALL be explicitly declared for every field.

Cardinality SHALL NOT be inferred from DataType alone.

---

# 11. Part 1 Completion

Part 2 continues with:

* EnumRef
* Default
* Validation
* Description
* Example
* Version metadata
* Deprecation metadata
* Field definition examples
* Compliance requirements

End of Part 1.

---

# 12. EnumRef

## 12.1 Purpose

`EnumRef` identifies the controlled vocabulary associated with a field.

It establishes a reference to a canonical enumeration rather than embedding allowable values directly into the field definition.

---

## 12.2 Requirements

EnumRef SHALL reference exactly one controlled vocabulary.

If a field is not of DataType `Enum`, EnumRef SHALL be omitted.

Enumeration definitions SHALL be version controlled.

---

## 12.3 Independence

Enumeration values SHALL be maintained independently of field definitions.

A field SHALL reference an enumeration rather than duplicate its values.

---

# 13. Default

## 13.1 Purpose

`Default` defines the value assigned when a field is omitted and such behavior is explicitly permitted.

---

## 13.2 Requirements

Default values SHALL:

* conform to the declared DataType
* satisfy validation rules
* satisfy cardinality constraints

Default values SHALL NOT change the semantic meaning of required fields.

---

## 13.3 Optionality

Fields without meaningful defaults SHALL omit the Default property.

---

# 14. Validation

## 14.1 Purpose

`Validation` identifies the validation rules associated with a field.

Validation rules SHALL be referenced rather than embedded.

---

## 14.2 Validation Scope

Validation MAY include:

* format validation
* range validation
* enumeration validation
* uniqueness validation
* reference validation
* regular expression validation
* custom validator references

---

## 14.3 Separation of Responsibility

The Field Model defines validation references only.

Validation behavior SHALL be specified by `Validation_Rules.md`.

---

# 15. Description

## 15.1 Purpose

`Description` defines the semantic meaning of a field.

Description SHALL explain what the field represents.

It SHALL NOT describe implementation behavior.

---

## 15.2 Requirements

Descriptions SHALL:

* be implementation-independent
* describe observable meaning
* avoid ambiguity
* remain stable across schema versions

Descriptions SHALL NOT:

* contain prompt fragments
* contain workflow instructions
* describe Excel locations
* describe generator logic

---

# 16. Example

## 16.1 Purpose

`Example` provides a representative value illustrating expected usage.

Examples improve readability.

Examples are informative rather than normative.

---

## 16.2 Requirements

Example values SHALL:

* satisfy DataType
* satisfy validation
* represent realistic data

Examples SHALL NOT replace formal validation.

---

# 17. SinceVersion

## 17.1 Purpose

`SinceVersion` records the first schema version supporting the field.

---

## 17.2 Requirements

Every field SHALL specify SinceVersion.

The version SHALL follow Semantic Versioning.

Example:

```text
2.0.0
```

---

# 18. Deprecated

## 18.1 Purpose

`Deprecated` indicates whether a field is scheduled for future removal.

---

## 18.2 Requirements

Deprecated SHALL be Boolean.

```text
true
false
```

Deprecated fields SHALL remain valid until officially removed.

---

# 19. DeprecatedSince

## 19.1 Purpose

`DeprecatedSince` identifies the schema version in which deprecation began.

---

## 19.2 Requirements

If Deprecated is false, DeprecatedSince SHALL be omitted.

If Deprecated is true, DeprecatedSince SHALL be specified.

---

# 20. Replacement

## 20.1 Purpose

`Replacement` identifies the recommended successor field.

---

## 20.2 Requirements

Replacement SHALL reference another logical field.

Replacement SHALL NOT duplicate semantic meaning.

If no replacement exists, the property MAY be omitted.

---

# 21. Notes

## 21.1 Purpose

`Notes` provides supplementary implementation guidance.

Notes are informative.

Notes SHALL NOT alter normative field semantics.

---

## 21.2 Scope

Notes MAY include:

* migration guidance
* implementation considerations
* compatibility remarks

Notes SHALL NOT introduce new business rules.

---

# 22. Canonical Field Definition Template

Every logical field SHALL conform to the following canonical template.

| Property        | Required    |
| --------------- | ----------- |
| FieldName       | Yes         |
| Owner           | Yes         |
| DataType        | Yes         |
| Required        | Yes         |
| Cardinality     | Yes         |
| EnumRef         | Conditional |
| Default         | Optional    |
| Validation      | Optional    |
| Description     | Yes         |
| Example         | Optional    |
| SinceVersion    | Yes         |
| Deprecated      | Yes         |
| DeprecatedSince | Conditional |
| Replacement     | Optional    |
| Notes           | Optional    |

This template is normative.

Entity specifications SHALL use this structure when defining fields.

---

# 23. Logical Field Principle

A logical field represents a domain concept.

It SHALL NOT represent a storage location.

Examples of prohibited concepts include:

* Excel Column B
* JSON Property Position
* Database Column Index
* CSV Column Number

Logical fields SHALL remain independent of physical implementation.

---

# 24. Physical Representation

Physical representations are implementation-specific mappings.

Examples include:

* Excel columns
* JSON properties
* YAML nodes
* SQL columns
* API payloads
* Programming language structures

Physical mappings SHALL be defined by implementation specifications.

They SHALL NOT be defined by the Field Model.

---

# 25. Part 2 Completion

The remaining sections define:

* field lifecycle
* field compatibility
* field evolution
* field inheritance rules
* field compliance
* canonical examples
* freeze decision

These sections continue in Part 3 without restarting numbering.

End of Part 2.

---

# 26. Field Lifecycle

## 26.1 Purpose

Every logical field SHALL progress through a defined lifecycle.

The lifecycle ensures stable evolution while preserving backward compatibility.

---

## 26.2 Lifecycle States

Each field SHALL exist in one of the following states.

| State      | Description                                          |
| ---------- | ---------------------------------------------------- |
| Proposed   | Under review and not yet part of the official schema |
| Accepted   | Approved for inclusion in the schema                 |
| Active     | Available for production use                         |
| Deprecated | Scheduled for future removal                         |
| Removed    | No longer part of the active schema                  |

Only **Active** fields SHALL be used in new specifications.

---

## 26.3 Lifecycle Transition

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

# 27. Field Compatibility

## 27.1 Purpose

Field compatibility ensures that schema evolution does not unnecessarily break downstream implementations.

---

## 27.2 Compatible Changes

The following changes are generally compatible:

* adding an optional field
* clarifying documentation
* adding implementation notes
* adding example values
* extending referenced enumerations where permitted

---

## 27.3 Incompatible Changes

The following changes SHALL be considered incompatible:

* changing field semantics
* changing DataType
* changing Owner
* changing Cardinality
* changing Required from `false` to `true`
* removing an Active field without deprecation

Such changes SHALL require an appropriate schema version update.

---

# 28. Field Evolution

## 28.1 Principle

Logical fields SHALL evolve conservatively.

Existing field meaning SHALL remain stable.

---

## 28.2 Evolution Rules

When modification is required:

1. Prefer clarification over replacement.
2. Prefer introducing a new field over redefining an existing one.
3. Deprecate before removal.
4. Record all changes in schema version history.

---

# 29. Field Inheritance Rules

## 29.1 Independence

Logical fields SHALL NOT inherit business meaning from other fields.

Each field SHALL define its own semantics explicitly.

---

## 29.2 Reuse

Different entities MAY define fields with similar names only when their semantics are identical.

If semantics differ, separate fields SHALL be defined.

---

## 29.3 Ownership

Inheritance SHALL NOT transfer ownership.

Every logical field SHALL continue to have exactly one Owner.

---

# 30. Field Identity

Every logical field SHALL possess a stable identity.

Field identity is determined by:

* FieldName
* Owner
* Semantic Meaning

Field identity SHALL NOT depend upon:

* display labels
* storage location
* implementation language
* spreadsheet layout

---

# 31. Canonical Field Example

The following example illustrates a logical field definition.

| Property        | Value                                       |
| --------------- | ------------------------------------------- |
| FieldName       | CharacterName                               |
| Owner           | Identity                                    |
| DataType        | String                                      |
| Required        | true                                        |
| Cardinality     | 1                                           |
| EnumRef         | —                                           |
| Default         | —                                           |
| Validation      | CharacterNameRule                           |
| Description     | Canonical historical name of the character. |
| Example         | Xiao Chuo                                   |
| SinceVersion    | 2.0.0                                       |
| Deprecated      | false                                       |
| DeprecatedSince | —                                           |
| Replacement     | —                                           |
| Notes           | Stable identifier field.                    |

This example is informative.

Implementations MAY present the same information in another format while preserving semantics.

---

# 32. Field Definition Quality Requirements

Every field definition SHALL satisfy the following quality requirements.

## Completeness

All required properties SHALL be present.

---

## Consistency

The field SHALL not contradict another field definition.

---

## Unambiguity

The semantic meaning SHALL be precise.

Interpretation SHALL not depend upon human assumptions.

---

## Machine Readability

Every property SHALL be processable by software.

---

## Stability

Field semantics SHALL remain stable across compatible schema versions.

---

# 33. Compliance Requirements

A Field Model implementation SHALL be considered compliant only if it:

* preserves the canonical field definition structure
* preserves field ownership
* preserves semantic meaning
* preserves logical independence
* preserves implementation independence

Partial implementations SHALL declare unsupported capabilities.

---

# 34. Relationship to Other Specifications

This specification SHALL be referenced by all specifications that define logical fields.

Including, but not limited to:

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

Those specifications SHALL define business fields using the Field Model defined herein.

---

# 35. Part 3 Completion

The remaining sections define:

* implementation conformance
* prohibited practices
* normative references
* freeze decision
* end of specification

These sections continue in Part 4 without restarting numbering.

End of Part 3.

---

# 36. Implementation Conformance

## 36.1 General Requirement

Any implementation claiming compatibility with the HCDS Field Model SHALL conform to this specification.

Conformance SHALL include:

* canonical field definition structure
* logical field semantics
* ownership rules
* version compatibility
* implementation independence

---

## 36.2 Accepted Implementations

The following implementations are expected to consume the Field Model.

Examples include:

* Excel generators
* JSON Schema generators
* YAML Schema generators
* Python model generators
* TypeScript interface generators
* Rust structure generators
* SQL schema generators
* Validator generators
* Documentation generators

Each implementation SHALL preserve logical field semantics.

---

# 37. Compiler Readiness

## 37.1 Purpose

The HCDS Field Model is designed to support automated schema compilation.

The Field Model SHALL be sufficiently structured for software to generate multiple implementation targets without requiring manual interpretation.

---

## 37.2 Compiler Inputs

A schema compiler SHALL consume:

* HCDS Schema
* Field Model
* Entity Specifications

These inputs SHALL be sufficient to derive implementation-specific representations.

---

## 37.3 Compiler Outputs

Future compiler targets MAY include:

* Excel workbook definitions
* JSON Schema
* YAML Schema
* Python data models
* TypeScript interfaces
* Rust structs
* Go structs
* SQL table definitions
* API contracts
* Validation rule templates
* Documentation tables

The Field Model SHALL remain independent of any specific output target.

---

# 38. Prohibited Practices

The following practices are prohibited.

Defining physical storage information inside logical field definitions.

Duplicating logical field definitions across specifications.

Embedding implementation-specific logic inside field metadata.

Changing semantic meaning without a schema version update.

Using generated artifacts as authoritative field definitions.

Creating multiple Owners for the same logical field.

Encoding workflow behavior inside field metadata.

---

# 39. Normative References

This specification depends upon:

* HCDS_Schema.md

The following specifications SHALL depend upon this document:

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

Implementation specifications MAY reference this document when generating physical representations.

---

# 40. Field Model Authority

This specification is the sole authority defining the HCDS logical field definition model.

No other specification SHALL redefine:

* field definition structure
* field metadata properties
* field metadata semantics

Business specifications SHALL define only business fields.

They SHALL NOT redefine the Field Model.

---

# 41. Freeze Decision

The HCDS Field Model defined by this specification is hereby frozen for HCDS v2.0.

All future logical field definitions SHALL conform to this model.

Changes to the Field Model constitute schema-level changes and SHALL require a new schema version.

---

# 42. Completion Statement

The HCDS Field Model establishes a uniform method for defining logical fields across the entire HCDS ecosystem.

Together with the HCDS Schema, it forms the normative foundation for:

* Dataset specifications
* Entity specifications
* Validators
* Schema compilers
* Documentation generators
* Export pipelines
* Future implementation tooling

---

# 43. Implementation Readiness

This specification is implementation-ready.

It is intended for direct consumption by:

* Claude Code
* Codex
* Python generators
* Schema compiler implementations
* Validation engines
* Documentation generators
* Future HCDS tooling

No additional interpretation should be required before implementation.

---

# 44. End of Specification

This document is the authoritative Field Model specification for HCDS v2.0.

It defines the logical field metadata model upon which all subsequent HCDS business specifications SHALL be built.

End of document.
