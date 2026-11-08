from agi_pipeline.evaluator import BasicEvaluator
from agi_pipeline.planner import HeuristicPlanner
from agi_pipeline.router import CapabilityRouter

class Orchestrator:
    def __init__(self, registry, planner=None, evaluator=None, memory=None, max_retries=1):
        if not 0 <= max_retries <= 3:
            raise ValueError("max_retries must be between 0 and 3")
        self.registry = registry
        self.planner = planner or HeuristicPlanner()
        self.evaluator = evaluator or BasicEvaluator()
        self.memory = memory
        self.router = CapabilityRouter(registry)
        self.max_retries = max_retries

    def run(self, goal):
        if not goal.strip():
            raise ValueError("Goal cannot be empty")
        tasks = self.planner.plan(goal)
        completed, trace = {}, []
        for task in tasks:
            missing = [dep for dep in task.dependencies if dep not in completed]
            if missing:
                trace.append({"task_id": task.id, "status": "blocked", "reason": str(missing)})
                continue
            decision = self.router.route(task)
            if decision.agent_name is None:
                trace.append({"task_id": task.id, "status": "unroutable", "reason": decision.reason})
                continue
            agent = self.registry.get(decision.agent_name)
            context = {"goal": goal, "completed_tasks": dict(completed)}
            accepted, result, reason = False, None, ""
            attempts = 0
            for attempts in range(1, self.max_retries + 2):
                result = agent.run(task, context)
                accepted, reason = self.evaluator.evaluate(result)
                if accepted:
                    break
            trace.append({
                "task_id": task.id, "description": task.description,
                "agent": decision.agent_name, "routing_reason": decision.reason,
                "attempts": attempts, "accepted": accepted, "evaluation": reason,
                "output": result.output if result else None,
            })
            if accepted and result:
                completed[task.id] = result.output
        summary = f"Completed {len(completed)} of {len(tasks)} planned tasks."
        if self.memory:
            self.memory.save(goal, summary, trace)
        return {"goal": goal, "planned_tasks": len(tasks),
                "completed_tasks": len(completed), "summary": summary, "trace": trace}
