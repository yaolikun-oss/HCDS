# RFC0004: HCDS Dataset_Master Schema vNext Architecture

Status: Draft
Version: v1.0
Project: HCDS
Owner: HCDS Architecture Team
Created: 2026-07-07
Related: RFC0003, Decision-019, `docs/02_schema/Dataset_Master_Spec.md`

---

## 1. Purpose

This RFC defines the next Dataset_Master model required to implement the Character/Sample separation accepted in Decision-019.

Decision-019 established that `Character_ID` identifies a historical person, `Sample_ID` identifies a generated dataset sample, and one Character SHALL support multiple Samples. That decision did not define the concrete Dataset_Master record structure, field ownership, or lifecycle mechanics needed to implement it. This RFC defines that structure.

---

## 2. Motivation

The frozen `docs/02_schema/Dataset_Master_Spec.md` predates Decision-019. Its Section 5 ("Each Character Record SHALL represent exactly one historical character") and Section 6 (each Character Record contains exactly one Pose, Costume, Camera, and Scene) describe a one-record-per-person model with no defined Sample concept.

Decision-019 accepted the direction of a fix — Character_ID vs Sample_ID separation — but a decision record is not a schema. `Dataset_Master_Spec.md` remains frozen and unchanged. Without a concrete vNext structure, no implementation work can proceed without re-deriving the same ambiguity this RFC exists to close.

---

## 3. Decision

HCDS SHALL define a Dataset_Master vNext structure as follows.

### 3.1 Sample_ID

`Sample_ID` SHALL uniquely and stably identify one generated dataset sample.

`Sample_ID` SHALL NOT depend upon Excel row numbers, filenames, prompt text, or generation order, consistent with `Dataset_Master_Spec.md` Section 8's existing identifier rules.

### 3.2 Character_ID Relationship

Each Sample SHALL reference exactly one `Character_ID`.

A Sample SHALL NOT duplicate Identity, Role, Appearance, or Language data owned by the referenced Character Profile.

One `Character_ID` MAY be referenced by many Samples, consistent with Decision-019.

### 3.3 Dataset Record Structure

A Dataset_Master vNext record (one row per Sample) SHALL contain:

* `Sample_ID` — owned by the Sample
* `Character_ID` — reference to the Character Profile
* Sample-varying entities already implemented: Pose (Behavior_Identity), Costume selection
* Sample lifecycle state (see 3.4)

A Dataset_Master vNext record SHALL NOT contain fields already owned by Character Profile (Identity, Role, Appearance_Identity, Language_Control), per Decision-019's "Character_Profile remains identity-only" rule.

### 3.4 Sample Lifecycle Ownership

Dataset_Master SHALL own Sample lifecycle state, consistent with Decision-019's Sample Lifecycle Rule.

Sample lifecycle states follow the existing pattern already used across HCDS entity specifications: Draft, Review, Approved, Active, Deprecated, Archived.

Changing a Sample's lifecycle state SHALL NOT alter the Character Profile it references. Changing a Character Profile SHALL NOT implicitly alter the lifecycle state of any Sample referencing it.

### 3.5 Future Generation Compatibility Boundary

This RFC defines the logical Sample structure only. It SHALL NOT define:

* how a generator consumes Sample records
* how Camera or Scene attach to a Sample
* how a Caption is produced for a Sample

These remain explicit boundaries for future RFCs, so that generation-layer implementation work has a stable Sample structure to consume without this RFC also deciding generation behavior.

---

## 4. Scope

### 4.1 Included

* `Sample_ID` field definition and identity rules
* `Character_ID` relationship (Sample references Character, one-to-many)
* Dataset record structure (what a Sample record contains and does not contain)
* Sample lifecycle ownership (Dataset_Master owns it, independent of Character_Profile)
* Future generation compatibility boundary (explicit statement of what this RFC does not decide)

### 4.2 Excluded

* Camera implementation
* Scene implementation
* Caption generator
* Prompt generator rewrite

---

## 5. Compatibility

This RFC does not modify `schemas/`, `generators/`, `templates/`, or `characters/`.

`docs/02_schema/Dataset_Master_Spec.md` remains frozen and unchanged by this document. If accepted, implementing this RFC requires a formal version update to `Dataset_Master_Spec.md` per its own Section 27 (Freeze Decision), following the proposal → review → decision → spec → implementation path already used for Decision-019.

Until accepted, this RFC is advisory only.

---

## 6. Implementation Impact

Affected future components, none of which are modified by this RFC document:

* `docs/02_schema/Dataset_Master_Spec.md` — would require a versioned amendment introducing `Sample_ID` and the Sample record structure defined in Section 3.
* A future Dataset_Master physical implementation (Excel, CSV, or other) — would need to represent one row per Sample rather than one row per Character.
* `generators/prompt_generator.py` — would eventually need to consume Sample records referencing `Character_ID` rather than one flat row per character. Explicitly out of scope here per Section 3.5 and Section 4.2.
* `templates/Character_Profile_Template_v1.0.xlsx` and `characters/LIAO_XIAO_CHUO/Character_Profile.xlsx` — unaffected; both remain Character-scoped, not Sample-scoped.

No implementation changes are made by this RFC document.

---

## 7. Non Goals

This RFC does not:

* Implement Camera fields or behavior
* Implement Scene fields or behavior
* Implement caption generation
* Rewrite or modify `generators/prompt_generator.py`
* Modify frozen schema documents
* Modify `templates/Character_Profile_Template_v1.0.xlsx`
* Modify `characters/LIAO_XIAO_CHUO/Character_Profile.xlsx`
* Create a Dataset_Master file

---

## 8. Future Work

Potential future RFCs may define:

* Camera Specification
* Scene Specification
* Caption Generation Pipeline
* Dataset_Master physical implementation (Sample-per-row template)
* Generator support for Character_ID-to-Sample expansion

---

## 9. Decision Status

Pending Review.

This RFC must be reviewed before any Dataset_Master schema amendment or implementation work proceeds.

---

## 10. Final Rule

A Sample_ID identifies one generated dataset sample.

A Sample references exactly one Character_ID and owns only what varies per sample.

Dataset_Master owns Sample lifecycle; Character_Profile owns identity.

---

## 11. Dataset_Master Single Source Rule

Dataset_Master is the single source of truth for sample definitions.

Generated artifacts — prompt, filename, caption, metadata — SHALL derive from Dataset_Master.

Generated artifacts SHALL NOT be manually maintained, and SHALL NOT be treated as an independent source of truth once Dataset_Master exists.

---

## 12. Costume Ownership Boundary

Character Profile owns historical costume identity, as defined by `Costume_Identity` in the Character Profile model.

Dataset Samples SHALL support costume presentation variants while preserving Character Profile identity.

Dataset Samples SHALL NOT redefine identity-level costume owned by the Character Profile. A Sample choosing among costume presentations is not the same as a Sample overriding who a character canonically is.
