from agi_pipeline.models import Task

class HeuristicPlanner:
    """Transparent starter planner; replace with a model-backed planner later."""
    def plan(self, goal):
        text = goal.lower()
        if any(w in text for w in ("research", "compare", "investigate", "find")):
            return [
                Task("task-1", f"Gather information for: {goal}", {"research"}),
                Task("task-2", "Organize findings into a concise plan", {"planning"}, ["task-1"]),
            ]
        if any(w in text for w in ("build", "create", "develop", "code", "website", "app")):
            return [
                Task("task-1", f"Clarify requirements and plan: {goal}", {"planning"}),
                Task("task-2", "Draft a technical implementation outline", {"coding"}, ["task-1"]),
                Task("task-3", "Review the outline for gaps and risks", {"evaluation"}, ["task-2"]),
            ]
        return [
            Task("task-1", f"Analyze the goal: {goal}", {"planning"}),
            Task("task-2", "Produce a structured response", {"writing"}, ["task-1"]),
        ]
