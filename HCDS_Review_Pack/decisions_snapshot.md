# HCDS Decisions Snapshot

Snapshot Date: 2026-07-06

Only active decisions are listed. Superseded decisions and decision templates are excluded.

| Decision ID | Short Title | Status | Impact Summary |
| --- | --- | --- | --- |
| Decision-000 | **Status:** Proposed \| Accepted \| Superseded \| Rejected | Proposed \| Accepted \| Superseded \| Rejected | **Related Files:** |
| Decision-001 | Chat is temporary; repository is permanent. | Accepted | Agents should summarize accepted conclusions into durable files and avoid treating inbox files as permanent documentation. |
| Decision-002 | Establish HCDS three-layer schema specification model. | Accepted | Future schema specs should reference `Field_Model_Spec.md` for field definition format instead of inventing field tables independently. |
| Decision-003 | Freeze HCDS collaboration architecture v1.0. | Accepted | All agents should now focus on specification and engineering work using the frozen workflow. |
| Decision-004 | Rule 001: Repository is the project memory. | Accepted | Agents should not rely on chat history as durable context. Every important output should be represented in repository files. |
| Decision-005 | Enter Phase 2: Schema Engineering. | Accepted | Agents should prioritize `docs/02_schema/` specifications, field models, dataset specs, entity specs, and future validator/generator readiness. |
| Decision-006 | Rule 002: Architecture is frozen. | Accepted | Future work should use normative specification language such as SHALL, SHOULD, and MAY instead of reopening architecture questions. |
| Decision-007 | Rule 003: New ideas follow proposal review decision spec implementation. | Accepted | New ideas should be captured as proposals, reviewed, accepted or rejected, and then represented in specifications before implementation. |
| Decision-008 | Adopt HCDS v2.0 version line discipline. | Accepted | Agents should treat frozen milestones as stable baselines and use future versions for significant changes. |
| Decision-009 | Field Model Defines Logical Fields Only | Accepted | * `Field_Model_Spec.md` defines logical field metadata only. * `Dataset_Master_Spec.md` should describe logical dataset structure. * `Excel_Implementation_Guide.md` should define physical Excel workbook and column lay... |
| Decision-010 | Add Controlled Vocabulary specification before Dataset Master. | Accepted | The next schema specification after `Field_Model_Spec.md` SHALL be `Controlled_Vocabulary_Spec.md`. `Dataset_Master_Spec.md` and entity-specific specifications should reference it whenever defining enum-backed logical... |
| Decision-012 | Stop adding Meta Specifications and begin Business Specifications. | Accepted | `Validation_Rules_Spec.md` is deferred to the Implementation Specifications stage. Validation concepts may be referenced in business specifications without creating a standalone validation rules specification yet. The... |
| Decision-013 | Use a common structure for Entity Specifications. | Accepted | Starting with `Character_Identity_Spec.md`, entity specifications should reuse this structure unless a specific accepted decision justifies deviation. |
| Decision-014 | Entity fields SHALL be organized by domain categories. | Accepted | `Character_Identity_Spec.md` Part 1 is revised to introduce Identity Categories. Future entity specifications should define their domain categories before declaring logical fields. |
| Decision-015 | Observable Principle. | Accepted | All future Entity Specifications SHALL follow the Observable Principle. Existing and future fields in Appearance, Costume, Pose, Expression, Camera, Scene, and Metadata should use observable, implementation-independen... |
| Decision-016 | Enter Generation Pipeline after Data Foundation MVP. | Accepted | Camera, Scene, Metadata, and remaining schema specifications are deferred unless they become required by the Generation Layer. The next priority sequence becomes `Prompt_Generation_Spec.md`, `Image_Filename_Spec.md`,... |
