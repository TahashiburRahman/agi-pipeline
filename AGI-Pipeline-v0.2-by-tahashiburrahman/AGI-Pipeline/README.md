# AGI Pipeline

**A model-agnostic, multi-agent orchestration research prototype.**

Created by **[@tahashiburrahman](https://github.com/tahashiburrahman)**  
Repository: `https://github.com/tahashiburrahman`

## The idea

AGI Pipeline explores a system-level approach to general intelligence: instead of requiring one model to perform every task, an orchestrator can understand a goal, break it into tasks, discover available capabilities, delegate work to specialist agents, evaluate their results, and preserve execution history.

**This repository is an experiment toward AGI-oriented system design. It is not AGI and does not claim to achieve AGI.**

## Designed to be understandable across AI models

This project uses ordinary, widely supported formats and conventions:
- Markdown for human- and AI-readable project instructions.
- Python with type hints for implementation.
- JSON-compatible task and result structures for future model adapters.
- `AGENTS.md` as the primary repository instruction file, with `AI_MODEL_GUIDE.md` as a provider-neutral guide.
- No required proprietary model SDK or vendor-specific prompt format.

No instruction file can guarantee identical behavior from every AI model. Models differ in context limits, tool access, and instruction-following. The documentation therefore states the project goals, vocabulary, interfaces, constraints, and workflow explicitly.

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -e .
agi-pipeline "Build a simple inventory application"
```

Run directly without installing:

```bash
python -m agi_pipeline.cli "Research accessible website design"
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## What currently works

1. Accepts a text goal.
2. Creates a small task plan using a transparent heuristic planner.
3. Routes each task by required capability.
4. Runs a matching demo agent.
5. Evaluates basic output structure and retries a bounded number of times.
6. Stores a trace in SQLite.

The included agents are **offline demonstrations**. They do not call real models, browse the web, write applications, or independently verify facts.

## Architecture at a glance

```text
GOAL
  |
  v
ORCHESTRATOR
  |-- PLANNER ----------> ordered tasks + required capabilities
  |-- ROUTER -----------> best matching registered agent
  |-- EXECUTOR ---------> agent receives task + prior task context
  |-- EVALUATOR --------> accept / retry (bounded)
  `-- MEMORY -----------> SQLite execution history
```

See:
- `SYSTEM_OVERVIEW.md` for the shared vocabulary and lifecycle.
- `ARCHITECTURE.md` for components and extension points.
- `AI_MODEL_GUIDE.md` for instructions intended for any coding/reasoning model.
- `AGENTS.md` for repository-level coding-agent rules.

## Add a specialist

Implement the `Agent` protocol in `agi_pipeline/agents/base.py`:

```python
from agi_pipeline.models import AgentResult

class MyAgent:
    name = "my-agent"
    capabilities = {"data-analysis", "summarization"}
    priority = 10

    def run(self, task, context) -> AgentResult:
        return AgentResult(
            agent_name=self.name,
            output="Result goes here",
            success=True,
        )
```

Register your agent with `AgentRegistry`. See `agi_pipeline/agents/demo_agents.py`.

## Connect a real model

Build an adapter that implements `Agent.run()`. The adapter may call a local model, hosted API, or another framework. Keep provider-specific code inside the adapter; the orchestrator should only depend on the common `Agent` interface.

Recommended adapter responsibilities:
- Convert task and context into provider-specific input.
- Call the model with explicit timeouts and bounded token limits.
- Parse and validate the response.
- Return an `AgentResult`.
- Report provider errors without exposing credentials.

Never commit API keys. Use environment variables or a secret manager.

## Safety and limitations

- The planner is heuristic, not general reasoning.
- Routing is capability matching, not learned model selection.
- Evaluation checks only basic structure, not truth or safety.
- Memory stores traces; it does not train models or automatically improve intelligence.
- No arbitrary shell, browser, network, or filesystem agent is included.
- Do not use this prototype for safety-critical decisions.

Add permission-scoped tools and human approval gates before enabling agents to take external actions.

## Research roadmap

1. Add provider-neutral model adapters.
2. Improve planning with explicit task dependencies and validation.
3. Add parallel execution with deterministic dependency handling.
4. Add independent verification and calibrated confidence.
5. Create benchmark tasks and baseline comparisons.
6. Experiment with learned routing and retrieval from memory.
7. Add sandboxed tools and human approval for consequential actions.

## Attribution

**Created and initiated by [tahashiburrahman](https://github.com/tahashiburrahman).** Please retain this attribution in forks and substantial derivative work.

## License

MIT. See `LICENSE`.
