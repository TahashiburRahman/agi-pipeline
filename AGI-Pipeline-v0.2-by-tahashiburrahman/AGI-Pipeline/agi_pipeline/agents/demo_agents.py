from agi_pipeline.models import AgentResult

class DemoAgent:
    """Offline placeholder. Replace with a real model adapter."""
    def __init__(self, name, capabilities, priority=1):
        self.name = name
        self.capabilities = set(capabilities)
        self.priority = priority

    def run(self, task, context):
        output = (
            f"[DEMO ONLY] {self.name} handled: {task.description}\n"
            f"Capabilities: {', '.join(sorted(task.required_capabilities))}\n"
            f"Prior tasks in context: {len(context.get('completed_tasks', {}))}\n"
            "Placeholder output; no real research or implementation was performed."
        )
        return AgentResult(self.name, output, True, {"demo": True})

def register_demo_agents(registry):
    registry.register(DemoAgent("research-agent", {"research"}, 5))
    registry.register(DemoAgent("planning-agent", {"planning"}, 8))
    registry.register(DemoAgent("coding-agent", {"coding"}, 7))
    registry.register(DemoAgent("writing-agent", {"writing"}, 4))
    registry.register(DemoAgent("evaluation-agent", {"evaluation"}, 6))
