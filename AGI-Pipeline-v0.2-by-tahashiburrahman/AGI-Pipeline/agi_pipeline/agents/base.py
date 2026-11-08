from typing import Protocol
from agi_pipeline.models import AgentResult, Task

class Agent(Protocol):
    name: str
    capabilities: set[str]
    priority: int

    def run(self, task: Task, context: dict) -> AgentResult:
        ...
