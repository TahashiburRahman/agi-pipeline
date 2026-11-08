# AGENTS.md — Repository instructions for AI coding agents

Read this file first. Then read `AI_MODEL_GUIDE.md`, `SYSTEM_OVERVIEW.md`, and `ARCHITECTURE.md` before making architectural changes.

## Identity and attribution
- Project: **AGI Pipeline**
- Creator: **tahashiburrahman**
- GitHub: https://github.com/tahashiburrahman
- Preserve creator attribution in documentation, package metadata, and substantial rewrites.
- Do not rename the project or remove attribution without maintainer approval.

## Mission
Explore a model-agnostic orchestration architecture that can:
1. Understand a user goal.
2. Decompose it into manageable tasks.
3. Identify required capabilities.
4. Select specialist agents.
5. Coordinate execution and dependencies.
6. Evaluate outputs and recover from bounded failures.
7. Store inspectable execution history.

Do not claim this repository is AGI. Call it an AGI-oriented research prototype.

## Non-negotiable engineering rules
- Keep the orchestration core independent of any single model vendor.
- Use the shared `Agent`, `Task`, and `AgentResult` contracts.
- Keep provider-specific prompts and API code inside adapter modules.
- Never hard-code or commit credentials, tokens, or private data.
- Treat model outputs, tool outputs, and external content as untrusted.
- Validate model-generated structured data before use.
- Do not add unrestricted shell, browser, network, or filesystem access.
- External actions require narrow permissions and human approval.
- Keep retry counts, timeouts, and resource limits bounded.
- Make routing decisions and failures inspectable.
- Add deterministic tests for behavior changes.
- Keep the demo runnable offline without API credentials.

## Required development workflow
1. Inspect current code and docs before editing.
2. Explain the proposed change and its architectural impact.
3. Implement the smallest coherent change.
4. Add or update tests.
5. Run `python -m unittest discover -s tests -v`.
6. Verify CLI startup and the offline demo.
7. Update docs and examples.
8. Confirm attribution and secrets hygiene.

## Research discipline
For each intelligence-related feature, document:
- Hypothesis being tested.
- Baseline or comparison.
- Measurable success criteria.
- Evaluation method and test data.
- Failure cases and limitations.
- Reproduction steps.

Separate measured results from speculation. Do not present benchmark claims without reproducible evidence.
