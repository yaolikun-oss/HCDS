# HCDS Agent Decision Log

This file records accepted decisions that affect agent collaboration, repository engineering, schema workflow, or specification process.

It is not a chat transcript.

## Decision Template

### Decision-000

**Title:**

**Status:** Proposed | Accepted | Superseded | Rejected

**Date:** YYYY-MM-DD

**Owner:**

**Context:**

**Decision:**

**Reason:**

**Impact:**

**Related Files:**

---

### Decision-001

**Title:** Chat is temporary; repository is permanent.

**Status:** Accepted

**Date:** 2026-07-04

**Owner:** Project Owner

**Context:** HCDS uses multiple AI agents for architecture, specifications, repository engineering, and future implementation.

**Decision:** Short-term coordination SHALL happen through `ai_agents/inbox/`, while durable conclusions SHALL be recorded in repository files such as decisions, tasks, RFCs, and specifications.

**Reason:** The repository must serve as project memory instead of relying on chat history.

**Impact:** Agents should summarize accepted conclusions into durable files and avoid treating inbox files as permanent documentation.

**Related Files:** `ai_agents/README.md`, `ai_agents/inbox/`

---

### Decision-002

**Title:** Establish HCDS three-layer schema specification model.

**Status:** Accepted

**Date:** 2026-07-04

**Owner:** HCDS Chief Architect

**Context:** `HCDS_Schema.md` defines entities, relationships, validation model, data types, and cardinality. A separate field meta model is needed before entity-specific field specifications.

**Decision:** HCDS SHALL use three schema specification layers: `HCDS_Schema.md` for the entity model, `Field_Model_Spec.md` for the field meta model, and entity-specific specifications for concrete business fields.

**Reason:** This separates Entity Model, Field Meta Model, and Business Field Specs, allowing future Excel, JSON Schema, YAML, Python dataclass, Pydantic, TypeScript, Rust, Go, and Java generation.

**Impact:** Future schema specs should reference `Field_Model_Spec.md` for field definition format instead of inventing field tables independently.

**Related Files:** `docs/02_schema/HCDS_Schema.md`, `docs/02_schema/Field_Model_Spec.md`

---

### Decision-003

**Title:** Freeze HCDS collaboration architecture v1.0.

**Status:** Accepted

**Date:** 2026-07-04

**Owner:** Project Owner

**Context:** HCDS established a repository-driven collaboration model for ChatGPT, Codex, Claude Code, Python tools, and the Project Owner.

**Decision:** The collaboration architecture v1.0 is frozen. Future work SHOULD use the current `ai_agents/` structure without further process redesign unless a concrete new requirement appears.

**Reason:** The collaboration mechanism is mature enough to support specification production, repository engineering, reviews, task flow, and durable decisions. Further process changes would distract from completing HCDS specifications.

**Impact:** All agents should now focus on specification and engineering work using the frozen workflow.

**Related Files:** `ai_agents/README.md`, `ai_agents/status.md`, `ai_agents/inbox/`, `ai_agents/tasks/`, `ai_agents/reviews/`

---

### Decision-004

**Title:** Rule 001: Repository is the project memory.

**Status:** Accepted

**Date:** 2026-07-04

**Owner:** Project Owner

**Context:** HCDS must avoid chat-driven project memory and preserve all important project knowledge in the repository.

**Decision:** Architecture decisions MUST enter `ai_agents/decisions.md`. Formal specifications MUST enter `docs/`. Engineering execution MUST enter task or repository files. Temporary discussions MAY exist only in `ai_agents/inbox/` and SHOULD be archived or summarized after processing.

**Reason:** The repository is the single source of truth for project knowledge.

**Impact:** Agents should not rely on chat history as durable context. Every important output should be represented in repository files.

**Related Files:** `ai_agents/decisions.md`, `docs/`, `ai_agents/tasks/`, `ai_agents/inbox/`

---

### Decision-005

**Title:** Enter Phase 2: Schema Engineering.

**Status:** Accepted

**Date:** 2026-07-04

**Owner:** Project Owner

**Context:** HCDS Architecture is complete and repository-driven collaboration is frozen.

**Decision:** HCDS enters Phase 2: Schema Engineering. Work now focuses on formal specifications rather than architecture design discussion.

**Reason:** Architecture decisions are closed enough to support production specification work.

**Impact:** Agents should prioritize `docs/02_schema/` specifications, field models, dataset specs, entity specs, and future validator/generator readiness.

**Related Files:** `ai_agents/status.md`, `docs/02_schema/`

---

### Decision-006

**Title:** Rule 002: Architecture is frozen.

**Status:** Accepted

**Date:** 2026-07-04

**Owner:** Project Owner

**Context:** HCDS has completed the architecture phase and moved into schema specification work.

**Decision:** Architecture is frozen. Discussion is over. Specification becomes the source of implementation.

**Reason:** HCDS must now behave as a software standard with stable architectural foundations.

**Impact:** Future work should use normative specification language such as SHALL, SHOULD, and MAY instead of reopening architecture questions.

**Related Files:** `docs/01_architecture/`, `docs/02_schema/`

---

### Decision-007

**Title:** Rule 003: New ideas follow proposal review decision spec implementation.

**Status:** Accepted

**Date:** 2026-07-04

**Owner:** Project Owner

**Context:** New ideas may arise after architecture freeze, but should not mutate architecture through chat.

**Decision:** New ideas SHALL follow this path: Proposal -> Review -> Decision -> New Spec -> Implementation.

**Reason:** This protects frozen architecture and preserves traceable evolution.

**Impact:** New ideas should be captured as proposals, reviewed, accepted or rejected, and then represented in specifications before implementation.

**Related Files:** `rfcs/`, `ai_agents/reviews/`, `ai_agents/decisions.md`, `docs/`

---

### Decision-008

**Title:** Adopt HCDS v2.0 version line discipline.

**Status:** Accepted

**Date:** 2026-07-04

**Owner:** Project Owner

**Context:** HCDS is being maintained as a software standard rather than a chat-driven project.

**Decision:** HCDS v2.0 SHALL progress through frozen milestones: Architecture Frozen -> Schema Frozen -> Generator Frozen -> Release Candidate -> v2.0 Release. Incompatible or post-freeze changes should move to v2.1 or v3.0 rather than rewriting frozen v2.0 decisions.

**Reason:** Version discipline makes HCDS maintainable as a long-term standard.

**Impact:** Agents should treat frozen milestones as stable baselines and use future versions for significant changes.

**Related Files:** `CHANGELOG.md`, `docs/`, `ai_agents/decisions.md`

---

### Decision-009

**Title:** Field Model Defines Logical Fields Only

**Status:** Accepted

**Date:** 2026-07-04

**Phase:** Phase 2 - Schema Engineering

**Owner:** HCDS Chief Architect

**Context:** HCDS is entering `Field_Model_Spec.md` after freezing `HCDS_Schema.md`. The Field Model must remain implementation independent and must not become tied to Excel or any other physical representation.

**Decision:** HCDS Field Model SHALL define logical fields only.

Physical representations such as Excel columns, JSON keys, YAML structures, database columns, API payloads, Python attributes, TypeScript interfaces, or other implementation-specific formats SHALL NOT be defined by `Field_Model_Spec.md`.

Physical representation rules SHALL be defined by dedicated implementation specifications.

Examples:

* Excel physical layout belongs to `Excel_Implementation_Guide.md`.
* JSON Schema output belongs to generated schema artifacts under `schemas/json/`.
* YAML Schema output belongs to generated schema artifacts under `schemas/yaml/`.
* Python model mapping belongs to implementation tooling.
* TypeScript interface mapping belongs to implementation tooling.

**Reason:** This preserves HCDS as an implementation-independent domain data standard. It prevents the Field Model from becoming tied to Excel or any single storage format. It also allows future schema compilers to generate multiple physical representations from the same logical field definitions.

**Impact:**

* `Field_Model_Spec.md` defines logical field metadata only.
* `Dataset_Master_Spec.md` should describe logical dataset structure.
* `Excel_Implementation_Guide.md` should define physical Excel workbook and column layout.
* Future compiler targets may include Excel, JSON Schema, YAML, Python, TypeScript, Rust, Go, SQL, and API formats.

**Related Files:** `docs/02_schema/Field_Model_Spec.md`, `docs/02_schema/HCDS_Schema.md`, `schemas/json/`, `schemas/yaml/`

---

### Decision-010

**Title:** Add Controlled Vocabulary specification before Dataset Master.

**Status:** Accepted

**Date:** 2026-07-04

**Phase:** Phase 2 - Schema Engineering

**Owner:** HCDS Chief Architect

**Context:** `Field_Model_Spec.md` defines `EnumRef`, controlled vocabulary references, and enumeration references, but the target specification for controlled vocabularies does not yet exist.

**Decision:** HCDS SHALL add `docs/02_schema/Controlled_Vocabulary_Spec.md` before `Dataset_Master_Spec.md`.

**Reason:** EnumRef requires a normative target defining enumeration naming, storage location, versioning, extensibility, multilingual representation, and deprecation rules. Adding this specification closes the Schema layer loop before business field specifications begin.

**Impact:** The next schema specification after `Field_Model_Spec.md` SHALL be `Controlled_Vocabulary_Spec.md`. `Dataset_Master_Spec.md` and entity-specific specifications should reference it whenever defining enum-backed logical fields.

**Related Files:** `docs/02_schema/Field_Model_Spec.md`, `docs/02_schema/Controlled_Vocabulary_Spec.md`, `docs/02_schema/Dataset_Master_Spec.md`

---

### Decision-011

**Title:** Add Validation Rules specification before Dataset Master.

**Status:** Superseded

**Date:** 2026-07-04

**Phase:** Phase 2 - Schema Engineering

**Owner:** HCDS Chief Architect

**Context:** `HCDS_Schema.md`, `Field_Model_Spec.md`, and `Controlled_Vocabulary_Spec.md` define the schema meta model. Validation-related concepts already appear across the schema layer, including `Validation`, validation rule references, validation status, and future validators.

**Decision:** HCDS SHALL add `docs/02_schema/Validation_Rules_Spec.md` before `Dataset_Master_Spec.md`.

**Reason:** Validation rules need a normative specification defining validation rule structure, rule identifiers, error codes, severity, lifecycle, and validator output expectations. Adding this before business specifications prevents each downstream document, validator, schema compiler, or generator from inventing its own validation model.

**Impact:** The next schema specification after `Controlled_Vocabulary_Spec.md` SHALL be `Validation_Rules_Spec.md`. `Dataset_Master_Spec.md`, schema compilers, validators, and generators should reference it for validation rule semantics instead of redefining validation behavior.

**Related Files:** `docs/02_schema/Field_Model_Spec.md`, `docs/02_schema/Controlled_Vocabulary_Spec.md`, `docs/02_schema/Validation_Rules_Spec.md`, `docs/02_schema/Dataset_Master_Spec.md`

---

### Decision-012

**Title:** Stop adding Meta Specifications and begin Business Specifications.

**Status:** Accepted

**Date:** 2026-07-04

**Phase:** Phase 2 - Schema Engineering

**Owner:** HCDS Chief Architect

**Context:** HCDS has completed the core meta specifications: `HCDS_Schema.md`, `Field_Model_Spec.md`, and `Controlled_Vocabulary_Spec.md`. Continuing to add additional foundation specifications before business specifications risks delaying the start of concrete schema production.

**Decision:** HCDS SHALL stop adding new Meta Specifications for now and begin Business Specifications. The next specification SHALL be `docs/02_schema/Dataset_Master_Spec.md`.

**Reason:** `Dataset_Master_Spec.md` is the bridge between the HCDS Schema, business entities, generators, validators, Excel-oriented workflows, OneTrainer, ComfyUI, and future implementation layers. Business specifications will reveal the real validation and implementation needs more reliably than continuing abstract decomposition.

**Impact:** `Validation_Rules_Spec.md` is deferred to the Implementation Specifications stage. Validation concepts may be referenced in business specifications without creating a standalone validation rules specification yet. The immediate schema sequence becomes `Dataset_Master_Spec.md`, `Character_Profile_Spec.md`, entity-specific specifications, and then implementation specifications.

**Related Files:** `docs/02_schema/HCDS_Schema.md`, `docs/02_schema/Field_Model_Spec.md`, `docs/02_schema/Controlled_Vocabulary_Spec.md`, `docs/02_schema/Dataset_Master_Spec.md`

---

### Decision-013

**Title:** Use a common structure for Entity Specifications.

**Status:** Accepted

**Date:** 2026-07-04

**Phase:** Phase 2 - Schema Engineering

**Owner:** HCDS Chief Architect

**Context:** After completing the schema meta model and `Dataset_Master_Spec.md`, subsequent business specifications will define concrete fields for entities. Without a common structure, entity specifications may drift in format and become harder to validate automatically.

**Decision:** HCDS Entity Specifications SHOULD use a common structure: Purpose, Responsibilities, Logical Fields, Field Constraints, Relationships, Validation Notes, Examples, and Compliance.

**Reason:** `Field_Model_Spec.md` defines how fields are described, Entity Specifications define which fields each entity owns, and `Dataset_Master_Spec.md` defines how entities compose into a dataset. A shared entity specification structure preserves this separation and enables future consistency checks.

**Impact:** Starting with `Character_Identity_Spec.md`, entity specifications should reuse this structure unless a specific accepted decision justifies deviation.

**Related Files:** `docs/02_schema/Field_Model_Spec.md`, `docs/02_schema/Dataset_Master_Spec.md`, `docs/02_schema/Character_Identity_Spec.md`

---

### Decision-014

**Title:** Entity fields SHALL be organized by domain categories.

**Status:** Accepted

**Date:** 2026-07-04

**Phase:** Phase 2 - Schema Engineering

**Owner:** HCDS Chief Architect

**Context:** `Character_Identity_Spec.md` initially listed identity fields directly. Some fields, such as birth year, death year, courtesy name, temple name, and posthumous name, are not universal for all historical characters. A flat field list risks making entity specifications look like column inventories rather than domain models.

**Decision:** Entity specifications SHALL organize logical fields by domain categories before listing concrete fields. For Identity, the categories include Core Identity, Historical Names, Historical Classification, Historical Titles, Historical Timeline, and Historical Notes.

**Reason:** Domain categories preserve semantic structure, clarify optionality, and prevent entity specifications from becoming unstructured field lists.

**Impact:** `Character_Identity_Spec.md` Part 1 is revised to introduce Identity Categories. Future entity specifications should define their domain categories before declaring logical fields.

**Related Files:** `docs/02_schema/Character_Identity_Spec.md`, `docs/02_schema/Field_Model_Spec.md`, `docs/02_schema/Dataset_Master_Spec.md`

---

### Decision-015

**Title:** Observable Principle.

**Status:** Accepted

**Date:** 2026-07-04

**Phase:** Phase 2 - Schema Engineering

**Owner:** HCDS Chief Architect

**Context:** HCDS entity specifications increasingly distinguish observable training data from narrative or interpretive descriptions. Pose, Expression, and Costume specifications already prohibit abstract terms such as heroic, powerful, brave, determined, majestic, noble, and wise because these terms describe audience interpretation rather than visible attributes.

**Decision:** HCDS SHALL adopt the Observable Principle. All training-oriented data fields SHALL describe what a camera can directly capture. They SHALL NOT describe meanings, judgments, emotions, social impressions, or interpretations that exist only in the viewer's mind.

**Rule:** Entity specifications SHALL prefer directly observable descriptions over interpretive labels.

**Examples:**

| Prohibited | Recommended Observable Description |
| --- | --- |
| 威严 | 双手背后，抬头，目视前方 |
| 坚定 | 双眼直视前方，嘴唇闭合 |
| 悲伤 | 双眼下垂，嘴角下压 |
| 愤怒 | 双眉压低，眼睛睁大，嘴唇紧闭 |

**Reason:** Observable descriptions are more useful for LoRA training, dataset validation, prompt generation, and downstream image generation because they describe visible signals rather than subjective interpretation. This improves consistency, machine readability, and generator reliability.

**Impact:** All future Entity Specifications SHALL follow the Observable Principle. Existing and future fields in Appearance, Costume, Pose, Expression, Camera, Scene, and Metadata should use observable, implementation-independent descriptions whenever the field contributes to training data or generation behavior.

**Related Files:** `docs/02_schema/Appearance_Spec.md`, `docs/02_schema/Costume_Spec.md`, `docs/02_schema/Pose_Action_Spec.md`, `docs/02_schema/Expression_Spec.md`, `docs/02_schema/Field_Model_Spec.md`

---

### Decision-016

**Title:** Enter Generation Pipeline after Data Foundation MVP.

**Status:** Accepted

**Date:** 2026-07-04

**Phase:** Phase 3 - Generation Pipeline

**Owner:** HCDS Chief Architect

**Context:** HCDS has completed the architecture foundation, schema foundation, dataset master, and the core entity specifications required for first-version data production: Character Identity, Appearance, Costume, Pose & Action, and Expression. These are sufficient to support the first production path from dataset to prompt, image, caption, and OneTrainer dataset.

**Decision:** HCDS SHALL stop expanding Schema specifications for the moment and enter the Generation Layer. The next major specification SHALL be `docs/03_generation/Prompt_Generation_Spec.md`.

**Rule:** Prompt generation specifications SHALL define how prompts are generated from structured HCDS data. They SHALL NOT define hand-written prompt prose as the source of truth.

**Generation Flow:**

```text
Specification
        ↓
Dataset Master
        ↓
Prompt Generator
        ↓
Image Generator
        ↓
Caption Generator
        ↓
OneTrainer Dataset
        ↓
LoRA
```

**Reason:** HCDS is intended to be a complete data production standard, not only a schema library. Moving into the Generation Layer connects `Dataset_Master_Spec.md` and core entity specifications to the actual production pipeline: prompts, generated images, captions, OneTrainer datasets, and LoRA training.

**Impact:** Camera, Scene, Metadata, and remaining schema specifications are deferred unless they become required by the Generation Layer. The next priority sequence becomes `Prompt_Generation_Spec.md`, `Image_Filename_Spec.md`, `Caption_Generation_Spec.md`, and `OneTrainer_Dataset_Spec.md`.

**Related Files:** `docs/02_schema/Dataset_Master_Spec.md`, `docs/02_schema/Character_Identity_Spec.md`, `docs/02_schema/Appearance_Spec.md`, `docs/02_schema/Costume_Spec.md`, `docs/02_schema/Pose_Action_Spec.md`, `docs/02_schema/Expression_Spec.md`, `docs/03_generation/Prompt_Generation_Spec.md`

---

### Decision-017

**Title:** Character Profile is the Aggregate Root before Generation.

**Status:** Accepted

**Date:** 2026-07-04

**Phase:** Phase 2 - Schema Engineering

**Owner:** HCDS Chief Architect

**Context:** After defining the core entities and preparing to enter the Generation Layer, HCDS identified a missing aggregation layer between entity specifications and prompt generation. Prompts are not generated directly from an unstructured dataset; they are generated from a complete Character Profile composed from Identity, Appearance, Costume, Pose, Expression, and optional future entities.

**Decision:** HCDS SHALL define `docs/02_schema/Character_Profile_Spec.md` before `docs/03_generation/Prompt_Generation_Spec.md`. Character Profile SHALL be treated as the logical aggregate root for a complete character representation.

**Rule:** Prompt generators SHALL consume Character Profiles as their primary logical input, not individual entity specifications directly and not physical dataset representations directly.

**Canonical Flow:**

```text
Specification
        ↓
Entity Specifications
        ↓
Character Profile
        ↓
Dataset Master
        ↓
Prompt Generator
        ↓
Image Generator
        ↓
Caption Generator
        ↓
OneTrainer Dataset
```

**Character Profile Composition:**

```text
Character Profile
        ├── Identity
        ├── Appearance
        ├── Costume
        ├── Pose
        ├── Expression
        ├── Camera (optional, deferred)
        └── Metadata (optional, deferred)
```

**Reason:** Character Profile answers the missing data-model question: what constitutes one complete character for generation. Dataset Master is a collection of Character Profiles, while Prompt Generation compiles a Character Profile into prompt output.

**Impact:** `Prompt_Generation_Spec.md` is deferred until `Character_Profile_Spec.md` is defined. `Decision-016` remains valid as the Generation Pipeline direction, but its immediate next-document priority is superseded by this decision.

**Related Files:** `docs/02_schema/Character_Profile_Spec.md`, `docs/02_schema/Dataset_Master_Spec.md`, `docs/02_schema/Character_Identity_Spec.md`, `docs/02_schema/Appearance_Spec.md`, `docs/02_schema/Costume_Spec.md`, `docs/02_schema/Pose_Action_Spec.md`, `docs/02_schema/Expression_Spec.md`, `docs/03_generation/Prompt_Generation_Spec.md`

