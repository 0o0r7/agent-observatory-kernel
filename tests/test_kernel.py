"""Phase-0 scaffold tests for the AgentObservatory kernel."""

from agent_observatory_kernel import __version__, hello


def test_hello() -> None:
    assert hello() == "AgentObservatory kernel online."


def test_version() -> None:
    assert __version__ == "0.1.0"
