# Single Source of Truth

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect
Responsibility: Define the authoritative data ownership model for HCDS.

---

# 1. Purpose

This specification defines the Single Source of Truth (SSOT) principle for HCDS.

It establishes:

* the authoritative project data source
* ownership of project information
* rules governing derived artifacts
* constraints preventing duplicated authoritative data
* requirements for regeneration

All HCDS implementations SHALL conform to this specification.

---

# 2. Scope

This specification governs:

* source data ownership
* generated artifacts
* synchronization rules
* regeneration
* data consistency
* duplicate data prevention

This specification does not define:

* schema fields
* prompt generation
* export formats
* implementation details

---

# 3. Authoritative Data Source

The only authoritative production data source SHALL be:

```text
Dataset_Master.xlsx
```

No other editable file SHALL contain authoritative production information.

---

# 4. Ownership Model

Project information SHALL exist in one of two categories.

## 4.1 Authoritative Data

Authoritative data is editable.

Examples:

* Dataset_Master.xlsx
* official specifications
* schema definitions

Only authoritative data may be modified by project contributors.

---

## 4.2 Derived Data

Derived data is generated.

Examples:

* prompts
* captions
* metadata
* txt sidecars
* filenames
* manifests
* ComfyUI packages
* OneTrainer datasets
* generated images
* generated videos

Derived data SHALL NOT become authoritative.

---

# 5. Generation Rule

Every derived artifact SHALL originate from authoritative data.

The permitted flow is:

```text
Dataset_Master.xlsx
        ↓
Validation
        ↓
Structured Records
        ↓
Generation
        ↓
Export
        ↓
Derived Artifacts
```

Reverse generation is prohibited.

---

# 6. Duplicate Data Rule

Authoritative project information SHALL exist only once.

The following practices are prohibited:

* manually maintaining prompt libraries
* manually editing generated captions
* manually editing generated metadata
* maintaining duplicate Excel workbooks
* maintaining consumer-specific copies of source data

---

# 7. Synchronization Rule

Generated artifacts SHALL NOT require manual synchronization.

Instead:

```text
Update Dataset_Master.xlsx

↓

Regenerate Outputs
```

Regeneration SHALL replace synchronization.

---

# 8. Regeneration Principle

All derived artifacts SHALL be reproducible.

Deleting any generated artifact SHALL NOT result in permanent information loss.

The complete project SHALL be recoverable from:

* Dataset_Master.xlsx
* official specifications
* generator implementations

---

# 9. Version Authority

The following components SHALL be version controlled independently:

* Schema
* Generators
* Exporters
* Specifications

Generated artifacts SHALL record the versions from which they were produced.

---

# 10. Consumer Restrictions

Consumers SHALL be read-only with respect to authoritative data.

Consumers SHALL NOT:

* edit Dataset_Master.xlsx
* edit schema definitions
* create new authoritative project data
* modify generated artifacts upstream

Consumers MAY generate assets only.

---

# 11. Human Editing Policy

Manual editing SHALL occur only within authoritative sources.

Manual modification of generated artifacts is discouraged.

If generated output is incorrect, the authoritative source or generator SHALL be corrected instead.

---

# 12. Architecture Relationship

This specification complements:

* Documentation_Architecture.md
* Documentation_Tree.md
* System_Architecture.md
* Data_Flow_Architecture.md

It defines data ownership rather than system structure or processing flow.

---

# 13. Compliance Requirements

An implementation SHALL NOT claim HCDS compliance if it:

* maintains multiple authoritative datasets
* edits generated artifacts as source data
* bypasses Dataset_Master.xlsx
* introduces additional editable production databases
* reverses the defined data flow

---

# 14. Future Extensions

Future generators, exporters, consumers, and AI models MAY be added without altering the Single Source of Truth principle.

Regardless of implementation technology, Dataset_Master.xlsx SHALL remain the sole authoritative production dataset unless superseded by a future officially approved HCDS specification.

---

# 15. Freeze Decision

The Single Source of Truth model defined in this document is hereby frozen.

All future HCDS specifications and implementations SHALL preserve this principle.

Changes to the authoritative data ownership model constitute architectural changes and require formal architectural review.

---

# 16. End of Specification

This document establishes the authoritative data ownership model for HCDS.

Every HCDS component SHALL preserve the integrity of the Single Source of Truth throughout the entire data lifecycle.

End of document.
