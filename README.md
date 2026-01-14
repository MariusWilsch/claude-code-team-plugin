# Claude Code Team Plugin

Team onboarding plugin with clarity workflow commands, worktree skill, and commit guards.

## Install

```bash
claude plugin add MariusWilsch/claude-code-team-plugin
```

## Contents

### Commands

| Command | Purpose |
|---------|---------|
| `/onboarding` | Start session, link issue, bootstrap context |
| `/requirements-clarity` | Disambiguate WHAT to build |
| `/implementation-clarity` | Plan HOW to build |
| `/evaluation-clarity` | Define success criteria |
| `/rubber-duck` | Thinking partner (Stage 2.7 with execution gate) |
| `/flag-for-improvement` | Capture system issues |
| `/issue-comment` | Post GitHub issue comments |

### Skills

| Skill | Purpose |
|-------|---------|
| `worktree` | Create isolated git worktrees for issue work |

### Hooks

| Hook Type | Trigger | Script |
|-----------|---------|--------|
| SessionStart | Session begins | Export `CLAUDE_CONVERSATION_PATH` |
| PreToolUse (Bash) | Before Bash | jsonl-blocker, pip-blocker, gh-api-guard, git-commit-guard |
| PreToolUse (Read) | Before Read | jsonl-blocker |
| PostToolUse (Bash) | After git push | context-check |

### Lib Scripts

- `onboarding_bootstrap.py` - Session context capture
- `fetch_issue_context.py` - GitHub issue fetcher
- `list_skills_by_discovery.py` - Skill discovery helper

## Protocol

Includes `CLAUDE.md` with:
- Task lifecycle (clarity phases)
- Confidence gating (✗/✓)
- Authority model (investigation vs execution)
- JIT knowledge retrieval
