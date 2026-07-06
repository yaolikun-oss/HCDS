# Agent Inbox

This directory is for temporary cross-agent communication.

Inbox files are not permanent project memory. Once processed, messages SHOULD be moved to `archive/` or summarized into one of the durable sources:

- `ai_agents/decisions.md`
- `ai_agents/tasks/`
- `ai_agents/reviews/`
- `docs/`
- `rfcs/`

## Standard Message Format

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

## Need Decision Format

```text
[Need Decision]

Issue:

Options:

Recommendation:

Impact:

Requested Owner:
```
