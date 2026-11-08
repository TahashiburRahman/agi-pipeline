# Architecture and Extension Points

## Package map

```text
agi_pipeline/
  models.py              Shared task/result/routing data structures
  agents/base.py         Provider-neutral Agent protocol
  agents/demo_agents.py  Offline illustrative agents
  registry.py            Agent registration and lookup
  planner.py              Starter heuristic task planner
  router.py               Capability-based selection
  evaluator.py            Basic structural result evaluator
  orchestrator.py         End-to-end pipeline coordinator
  memory.py               SQLite execution history
  demo.py                 Offline dependency wiring
  cli.py                  Command-line interface
tests/
  test_pipeline.py        Deterministic unit tests
```

## Contracts

### Task

A task has:
- unique `id`
- natural-language `description`
- `required_capabilities`
- `dependencies` referring to earlier task IDs

### Agent

An agent advertises `name`, `capabilities`, and `priority`, and implements:

```python
run(task: Task, context: dict) -> AgentResult
```

### AgentResult

A result includes the agent name, textual output, success flag, and optional metadata.

## Routing

The current router scores each agent using capability overlap and priority. If a task has required capabilities and no agent overlaps, the task is marked unroutable. This is a transparent baseline, not a learned routing policy.

## Evaluation and retries

The basic evaluator checks that the agent reports success and returns non-empty output. The orchestrator retries a rejected result up to `max_retries`, which is capped at three. This does not establish factual accuracy, usefulness, or safety.

## Adding a provider adapter

Create a new module that:
1. Implements the common Agent interface.
2. Reads credentials from environment variables.
3. Applies timeouts and provider-side resource limits.
4. Converts task/context into provider-specific input.
5. Validates and normalizes the response.
6. Returns `AgentResult`, including safe diagnostic metadata.

Keep provider SDK imports out of core modules. Add mocked tests so the test suite remains offline.

## Future architecture questions

- How should agents report calibrated confidence and evidence?
- How can a planner detect missing capabilities?
- When should tasks run in parallel?
- How can the system detect contradictory specialist outputs?
- How should memory retrieval be evaluated against a no-memory baseline?
- How can routing improve without overfitting to benchmark tasks?
