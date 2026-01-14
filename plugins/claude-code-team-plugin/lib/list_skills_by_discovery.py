#!/usr/bin/env python3
"""
List skills and commands by discovery phase.

Usage:
    list_skills_by_discovery.py <phase>
    list_skills_by_discovery.py requirements-clarity

Searches all skills and commands for (discovery: <phase>) in their descriptions.
"""

import sys
import re
from pathlib import Path

def extract_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown file."""
    if not content.startswith('---'):
        return {}

    # Find closing ---
    end_idx = content.find('---', 3)
    if end_idx == -1:
        return {}

    frontmatter = content[3:end_idx].strip()
    result = {}

    for line in frontmatter.split('\n'):
        if ':' in line:
            key, _, value = line.partition(':')
            result[key.strip()] = value.strip()

    return result


def find_skills_by_discovery(phase: str) -> list[tuple[str, str]]:
    """Find all skills with (discovery: phase) in description."""
    results = []
    skills_dir = Path.home() / '.claude' / 'skills'

    pattern = f'(discovery: {phase})'

    for skill_dir in skills_dir.iterdir():
        if not skill_dir.is_dir():
            continue

        skill_file = skill_dir / 'SKILL.md'
        if not skill_file.exists():
            continue

        content = skill_file.read_text()
        fm = extract_frontmatter(content)

        desc = fm.get('description', '')
        if pattern in desc:
            name = skill_dir.name
            results.append((name, desc))

    return results


def find_commands_by_discovery(phase: str) -> list[tuple[str, str]]:
    """Find all commands with (discovery: phase) in description."""
    results = []
    commands_dir = Path.home() / '.claude' / 'commands'

    if not commands_dir.exists():
        return results

    pattern = f'(discovery: {phase})'

    for cmd_file in commands_dir.glob('*.md'):
        content = cmd_file.read_text()
        fm = extract_frontmatter(content)

        desc = fm.get('description', '')
        if pattern in desc:
            name = cmd_file.stem
            results.append((f'/{name}', desc))

    return results


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    phase = sys.argv[1]

    print(f"Skills with (discovery: {phase}):")
    print("=" * 40)

    skills = find_skills_by_discovery(phase)
    commands = find_commands_by_discovery(phase)

    all_matches = skills + commands

    if not all_matches:
        print(f"No skills/commands found with (discovery: {phase})")
    else:
        for name, desc in all_matches:
            print(f"- **{name}**: {desc}")
            print()

    print()
    print("In Thought 1, reason about which of these skills apply to the current task.")


if __name__ == '__main__':
    main()
