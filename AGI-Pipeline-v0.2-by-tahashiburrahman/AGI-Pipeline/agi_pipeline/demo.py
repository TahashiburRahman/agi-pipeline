from agi_pipeline.agents.demo_agents import register_demo_agents
from agi_pipeline.memory import ExecutionMemory
from agi_pipeline.orchestrator import Orchestrator
from agi_pipeline.registry import AgentRegistry

def build_demo_orchestrator(memory_path=".agi_pipeline/memory.sqlite3"):
    registry = AgentRegistry()
    register_demo_agents(registry)
    return Orchestrator(registry, memory=ExecutionMemory(memory_path))
