# Contributing to agent-observatory-kernel

Thanks for your interest in contributing!

This repository is part of the **AgentObservatory** project. Please read the
project-wide contribution guidelines first:

> https://github.com/0o0r7/agent-observatory/blob/main/CONTRIBUTING.md

## Repository-specific rules

- **English only** in code, comments, commit messages, PR titles/descriptions,
  issues, and documentation. CI enforces this via a Persian/Arabic-script
  character check on `src/` and `docs/`.
- Every PR must pass the CI pipeline (**lint + test + build**) before merge.
- Never commit secrets. Use `.env` locally (gitignored) and GitHub Actions
  secrets for CI.
