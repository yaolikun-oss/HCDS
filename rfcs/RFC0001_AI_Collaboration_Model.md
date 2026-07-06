# RFC0001: AI Collaboration Model

Status: Accepted
Version: v1.0
Project: HCDS
Owner: User
Created: 2026-07-03

---

## 1. Purpose

This RFC defines how ChatGPT, Claude Code, and Codex collaborate inside the HCDS project.

HCDS is a schema-driven historical character dataset standard.
It is not a prompt project, not a LoRA project, and not a ComfyUI workflow project.

The goal is to prevent different AI agents from overwriting each other’s responsibilities.

---

## 2. Core Principle

HCDS is governed by documents and schemas, not by chat history.

All durable decisions must be written into repository files.

Chat is temporary.
Repository files are authoritative.

---

## 3. Collaboration Model

The HCDS workflow follows this order:

RFC
→ Specification
→ Task
→ Implementation
→ Test
→ Review
→ Version Update

No implementation should happen before the relevant specification exists.

---

## 4. Agent Responsibilities

### ChatGPT

Responsible for:

* Architecture
* Schema design
* Dataset standard
* Design decisions
* Specification documents
* Rule definitions
* HCDS governance

ChatGPT must not directly rewrite implementation code unless explicitly requested.

---

### Claude Code

Responsible for:

* Generator implementation
* Dataset generation scripts
* Prompt generation scripts
* Caption generation scripts
* Metadata generation scripts
* ComfyUI batch generation

Claude Code must follow HCDS specifications and must not invent schema fields.

---

### Codex

Responsible for:

* Engineering implementation
* Repository structure
* Templates
* Refactoring
* Tests
* Validation scripts
* CI-style checks
* Task automation

Codex must not modify HCDS architecture or schema without an accepted RFC.

---

## 5. Schema Rule

Never invent new schema.

Never rename existing fields.

Never delete existing fields.

New fields may only be added after:

RFC
→ Review
→ Acceptance
→ Schema update

---

## 6. Single Source of Truth

The authoritative source of HCDS data is the HCDS schema and master data files.

Generated outputs must not be manually maintained.

Generated outputs include:

* prompts
* captions
* metadata
* image filenames
* ComfyUI batch files
* OneTrainer dataset files

---

## 7. Data-Driven Rule

HCDS is schema-driven.

Excel is one implementation of the schema.

Future implementations may include:

* CSV
* JSON
* SQLite
* PostgreSQL

Code must depend on the schema, not on hard-coded prompt logic.

---

## 8. Change Control

Any major change must be proposed as an RFC.

Accepted decisions must be recorded in:

`docs/Design_Decisions.md`

Rejected proposals remain in `rfcs/` for historical reference.

---

## 9. First Implementation Tasks

After this RFC is accepted, Codex should create:

* `ai_agents/ChatGPT.md`
* `ai_agents/Claude_Code.md`
* `ai_agents/Codex.md`
* `ai_agents/README.md`
* `tasks/task0001.md`
* `issues/0001.md`

These files are templates only until formal specifications are provided.

---

## 10. Final Rule

Do not treat HCDS as an AI image project.

Treat HCDS as a dataset standard and schema system.

LoRA, ComfyUI, Flux, Wan, Qwen Image Edit, and OneTrainer are consumers of HCDS.
