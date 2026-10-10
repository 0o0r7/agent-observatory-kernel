"""AgentObservatory kernel - verdict engine + autoloop runner.

The kernel subscribes to vibe/vibe V6 LaunchFactory events on Robinhood
Chain Testnet via HTTP polling (5s interval - WebSocket does not exist on
this chain), generates evidence-grounded verdicts through a
provider-agnostic LLM router (Claude / Codex / Z.AI GLM / MiniMax /
HuggingFace / Ollama), and persists every run to
``artifacts/verdicts/<launch_address>/`` (file-first inspectable state:
input.json, evidence.json, verdict.json, replay.html).
"""

__version__ = "0.1.0"


def hello() -> str:
    """Return the kernel health-check message (Phase-0 scaffold)."""
    return "AgentObservatory kernel online."
