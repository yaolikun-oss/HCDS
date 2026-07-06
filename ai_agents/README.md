# AI Collaboration

HCDS uses repository-driven AI collaboration.

> Chat is temporary. Repository is permanent.

## Workflow v1.0

```text
ChatGPT -> ai_agents/inbox/ -> Codex
Codex   -> ai_agents/inbox/ -> ChatGPT
```

The Project Owner reviews, approves, and commits final changes.

## Responsibilities

| Agent | Responsibility |
| --- | --- |
| Project Owner | Final decisions, review, approval, commits |
| ChatGPT | Architecture, specifications, schema decisions |
| Codex | Repository engineering, CI, automation, implementation infrastructure |
| Claude Code | Review, challenge, optimization, future implementation assistance |
| Python tools | Deterministic generation, validation, and automation |

Agents SHALL NOT modify another agent's responsibility area without an explicit accepted decision.

## Project Memory

| Source | Purpose |
| --- | --- |
| `docs/` | Official specifications and documentation |
| `ai_agents/decisions.md` | Accepted agent, architecture, schema, and repository decisions |
| `ai_agents/tasks/` | Current task state |
| `ai_agents/inbox/` | Temporary agent communication |
| `ai_agents/reviews/` | Architecture, specification, and engineering reviews |

## Agent Message Format

Agent inbox messages SHOULD use this structure:

```text
[Agent Message]

Target:
Codex | ChatGPT | Claude | All

Type:
Specification | Engineering | Review | Decision Request | Status

Action:

Sections:

Dependencies:

Constraints:

Notes:
```

## Rules

- Communicate through `ai_agents/inbox/` for cross-agent handoff.
- Record durable conclusions in `ai_agents/decisions.md`.
- Move processed inbox content to `ai_agents/inbox/archive/` or summarize it elsewhere.
- Keep task state in `ai_agents/tasks/active`, `completed`, or `blocked`.
- Treat repository files as the source of truth, not chat history.
