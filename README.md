# Claude Code Team Plugin

Team onboarding plugin with clarity workflow commands, worktree skill, and commit guards.

## Dependencies

Install these before using the plugin:

**uv** (Python package manager):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**git-worktree-runner** (worktree management):
```bash
git clone https://github.com/coderabbitai/git-worktree-runner.git
cd git-worktree-runner
./install.sh
```

**Homebrew** (package manager - required for Supabase CLI):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
source ~/.bashrc
```

**gcc** (required to build Supabase on WSL/Linux):
```bash
brew install gcc
```

**Supabase CLI** (database operations):
```bash
brew install supabase/tap/supabase
```

## Install

```
/plugin marketplace add MariusWilsch/claude-code-team-plugin
```

## Contents

### Commands

| Command | Purpose |
|---------|---------|
| `/onboarding` | Start session, link issue, bootstrap context |
| `/requirements-clarity` | Disambiguate WHAT to build |
| `/implementation-clarity` | Plan HOW to build |
| `/evaluation-clarity` | Define success criteria |
| `/ac-verify` | Verify acceptance criteria (separate session) |
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
