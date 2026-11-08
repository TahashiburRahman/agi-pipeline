import tempfile
import unittest
from pathlib import Path
from agi_pipeline.agents.demo_agents import DemoAgent
from agi_pipeline.memory import ExecutionMemory
from agi_pipeline.models import Task
from agi_pipeline.orchestrator import Orchestrator
from agi_pipeline.registry import AgentRegistry
from agi_pipeline.router import CapabilityRouter

class PipelineTests(unittest.TestCase):
    def test_router_matches_capability(self):
        registry = AgentRegistry()
        registry.register(DemoAgent("writer", {"writing"}))
        decision = CapabilityRouter(registry).route(Task("1", "write", {"writing"}))
        self.assertEqual(decision.agent_name, "writer")

    def test_router_handles_missing_capability(self):
        registry = AgentRegistry()
        registry.register(DemoAgent("writer", {"writing"}))
        decision = CapabilityRouter(registry).route(Task("1", "see", {"vision"}))
        self.assertIsNone(decision.agent_name)

    def test_pipeline_persists_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry = AgentRegistry()
            for name, caps in [("planner", {"planning"}), ("coder", {"coding"}), ("reviewer", {"evaluation"})]:
                registry.register(DemoAgent(name, caps))
            memory = ExecutionMemory(str(Path(tmp) / "memory.db"))
            result = Orchestrator(registry, memory=memory).run("Build a small app")
            self.assertEqual(result["completed_tasks"], 3)
            self.assertEqual(len(memory.recent()), 1)

    def test_retry_limit_is_bounded(self):
        with self.assertRaises(ValueError):
            Orchestrator(AgentRegistry(), max_retries=9)

    def test_empty_goal_rejected(self):
        with self.assertRaises(ValueError):
            Orchestrator(AgentRegistry()).run(" ")

if __name__ == "__main__":
    unittest.main()
