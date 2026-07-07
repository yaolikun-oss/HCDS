# RFC0003: HCDS Dataset Sample Architecture

Status: Draft
Version: v1.0
Project: HCDS
Owner: HCDS Architecture Team
Created: 2026-07-07
Related: RFC0001, RFC0002, Decision-018, `docs/02_schema/Dataset_Master_Spec.md`

---

## 1. Purpose

This RFC defines the relationship between:

* Character Profile
* Dataset Sample

HCDS currently has a concrete, implemented Character Profile model (`templates/Character_Profile_Template_v1.0.xlsx`, `characters/LIAO_XIAO_CHUO/Character_Profile.xlsx`) but no defined relationship between one character and the multiple generated samples a production dataset requires.

---

## 2. Motivation

The Phase 2 Alpha readiness review of `docs/02_schema/Dataset_Master_Spec.md` found an unresolved structural gap.

`Dataset_Master_Spec.md` Section 5 states: "Each Character Record SHALL represent exactly one historical character."

`Dataset_Master_Spec.md` Section 6 states that each Character Record contains exactly one Pose, one Costume, one Camera, and one Scene.

Taken together, these statements describe one record per person with exactly one pose/costume/camera/scene combination. They do not define how a single character produces multiple samples, such as ten images of LIAO_XIAO_CHUO in different poses and costumes.

`Character_Profile_Template_v1.0.xlsx` and the accepted `LIAO_XIAO_CHUO` profile establish `CharacterId` as a stable, unique, per-person identifier. Nothing in the current schema or generator identifies an individual generated sample, or links many samples back to one character.

This gap blocks Phase 2 production work and must be resolved before a Dataset_Master can be populated.

---

## 3. Decision

HCDS SHALL separate two distinct identity concepts:

* **Character_ID** identifies exactly one historical character. It is permanent and is reused across every sample of that character.
* **Sample_ID** identifies exactly one generated dataset sample: one specific combination of pose, costume, and other per-sample attributes for a character.

One Character_ID MAY be referenced by many Sample_IDs.

A Sample SHALL reference its owning Character_ID. A Sample SHALL NOT duplicate Identity or Appearance data already owned by the Character Profile.

Canonical relationship:

```text
Character Profile (Character_ID)
        │
        ├── Sample (Sample_ID, Character_ID reference, Pose, Costume, ...)
        ├── Sample (Sample_ID, Character_ID reference, Pose, Costume, ...)
        └── Sample (Sample_ID, Character_ID reference, Pose, Costume, ...)
                ↓
        Dataset_Master
```

Dataset_Master SHALL own the collection of Samples. Dataset_Master SHALL NOT own Character Profiles; it references them by Character_ID.

Character Profile SHALL remain the single source of truth for Identity, Role, Appearance_Identity, and Language_Control. Samples SHALL own only what varies per generated image: Pose/Behavior, Costume selection, and any per-sample fields introduced by future RFCs.

---

## 4. Scope

### 4.1 Included

* Character_ID vs Sample_ID separation: definitions, uniqueness rules, and the reference relationship between them.
* One Character → Many Samples relationship: cardinality and ownership.
* Dataset_Master ownership: Dataset_Master owns Samples; Character Profile ownership of Identity/Appearance/Language data is unaffected.

### 4.2 Excluded

* Camera specification
* Scene specification
* Caption implementation
* Generator rewrite

These are explicitly deferred to future RFCs. This RFC defines the relationship structure only; it does not define what per-sample fields eventually live on a Sample beyond Pose and Costume, which already exist as implemented entities.

---

## 5. Compatibility

This RFC does not modify `schemas/`, `generators/`, `templates/`, or any existing pull request.

`docs/02_schema/Dataset_Master_Spec.md` remains frozen and unchanged by this document. If accepted, implementing this decision requires a formal schema version update to `Dataset_Master_Spec.md` per its own Section 27 (Freeze Decision), following the proposal → review → decision → spec → implementation path.

Until accepted, this RFC is advisory only.

---

## 6. Implementation Impact

Affected future components, none of which are modified by this RFC document:

* `docs/02_schema/Dataset_Master_Spec.md` — would require a versioned amendment clarifying Character Record vs. Sample cardinality.
* A future Dataset Sample template or specification — would define the physical shape of a Sample record.
* `generators/prompt_generator.py` — would eventually need to consume Sample-level records referencing a Character_ID rather than one flat row per character. Out of scope here.
* `templates/Character_Profile_Template_v1.0.xlsx` — unaffected; Sample-level fields would live in a separate future artifact, not in this template.

No implementation changes are made by this RFC document.

---

## 7. Non Goals

This RFC does not:

* Define Camera fields or behavior
* Define Scene fields or behavior
* Implement caption generation
* Rewrite or modify `generators/prompt_generator.py`
* Modify frozen schema documents
* Modify `templates/Character_Profile_Template_v1.0.xlsx`
* Modify PR #1 or PR #2
* Create a Dataset_Master file

---

## 8. Future Work

Potential future RFCs may define:

* Camera Specification
* Scene Specification
* Caption Generation Pipeline
* Dataset_Master physical implementation and Sample template
* Generator support for Character_ID-to-Sample expansion

---

## 9. Decision Status

Pending Review.

This RFC must be reviewed before any schema, generator, or Dataset_Master implementation work proceeds.

---

## 10. Final Rule

A Character Profile identifies who a character is.

A Dataset Sample identifies one specific generated instance of that character.

Dataset_Master owns Samples, not Characters.

---

## 11. Sample Lifecycle Rule

Dataset_Master owns sample lifecycle state.

Character_Profile defines identity and remains separate from sample lifecycle.

Sample states are independent from character identity. Changing a Sample's lifecycle state SHALL NOT alter, invalidate, or require changes to the Character Profile it references, and changing a Character Profile SHALL NOT implicitly alter the lifecycle state of any Sample that references it.
