# System Overview

## Purpose

AGI Pipeline tests one architectural hypothesis:

> A general-purpose intelligent system can be explored as a coordinated pipeline of planning, capability selection, specialist execution, evaluation, and memory.

This is a research direction, not a demonstrated theory of AGI.

## Lifecycle

1. **Receive goal:** accept a natural-language objective.
2. **Plan:** transform the goal into a sequence of bounded tasks.
3. **Describe capabilities:** each task declares the capabilities it needs.
4. **Route:** choose a registered agent with matching capabilities.
5. **Execute:** provide the agent with the task and prior successful outputs.
6. **Evaluate:** accept or reject the result using explicit criteria.
7. **Recover:** retry only within a configured limit.
8. **Remember:** persist a trace for inspection and future research.

## Design principles

- **Model agnostic:** providers are replaceable adapters.
- **Capability first:** route by what work is needed, not by model brand.
- **Inspectable:** expose task plans, route reasons, attempts, and outcomes.
- **Bounded:** retries and future tool permissions must have limits.
- **Composable:** specialists implement a small common contract.
- **Honest evaluation:** distinguish structural checks from factual verification.
- **Human control:** consequential external actions should require approval.

## What memory means here

Current memory is a SQLite log of goals, summaries, and execution traces. It does not update model weights, create new knowledge automatically, or guarantee learning. Future research may add retrieval and feedback loops, but those require separate evaluation.
