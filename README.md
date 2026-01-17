# Claude Code Team Plugin

Team onboarding plugin with clarity workflow commands, worktree skill, and commit guards.

## Dependencies

Install these before using the plugin:

**gh** (GitHub CLI):
```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
gh auth login
```

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

**Homebrew** (package manager for WSL):
```bash
# Install build-essential first (required for WSL)
sudo apt-get update
sudo apt-get install build-essential

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add to PATH
test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
echo "eval \$($(brew --prefix)/bin/brew shellenv)" >> ~/.bashrc
source ~/.bashrc
```

**Supabase CLI** (database operations):
```bash
npm install -g supabase
supabase login
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

## Recommended Settings

Plugins can't include permissions. Add these to your `~/.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(gh:*)", "Bash(git:*)", "Bash(uv:*)",
      "mcp__hand-picked-tools__**",
      "Skill(worktree)", "Skill(hippocampus)",
      "SlashCommand(/rubber-duck:*)"
    ],
    "deny": [
      "Bash(git push origin --delete:*)",
      "Bash(git branch -D:*)"
    ],
    "ask": [
      "Bash(rm:*)", "Bash(gh pr create:*)",
      "Bash(gh issue create:*)"
    ]
  }
}
```

See full recommended settings: [settings-template.md](docs/settings-template.md)

## Protocol

Includes `CLAUDE.md` with:
- Task lifecycle (clarity phases)
- Confidence gating (✗/✓)
- Authority model (investigation vs execution)
- JIT knowledge retrieval
