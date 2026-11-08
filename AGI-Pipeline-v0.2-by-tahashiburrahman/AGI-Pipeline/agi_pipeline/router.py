from agi_pipeline.models import RoutingDecision

class CapabilityRouter:
    def __init__(self, registry):
        self.registry = registry

    def route(self, task):
        candidates = []
        for agent in self.registry.all():
            overlap = task.required_capabilities.intersection(agent.capabilities)
            score = len(overlap) * 100 + int(getattr(agent, "priority", 0))
            if not task.required_capabilities:
                score = int(getattr(agent, "priority", 0))
            candidates.append((score, agent.name, overlap))
        if not candidates:
            return RoutingDecision(None, 0, "No agents are registered")
        candidates.sort(key=lambda item: (-item[0], item[1]))
        score, name, overlap = candidates[0]
        if task.required_capabilities and not overlap:
            return RoutingDecision(None, 0, f"No agent supports: {sorted(task.required_capabilities)}")
        return RoutingDecision(name, score, f"Matched {sorted(overlap)}; score={score}")
