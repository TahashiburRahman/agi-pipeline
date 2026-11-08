from dataclasses import dataclass, field
from typing import Any

@dataclass
class Task:
    id: str
    description: str
    required_capabilities: set[str] = field(default_factory=set)
    dependencies: list[str] = field(default_factory=list)

@dataclass
class AgentResult:
    agent_name: str
    output: str
    success: bool
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class RoutingDecision:
    agent_name: str | None
    score: int
    reason: str
