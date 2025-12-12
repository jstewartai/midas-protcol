# MIDAS

**MIDAS (Multi-Turn Invariant Drift Analysis System)** is a protocol-first framework for measuring and constraining semantic drift in multi-turn large language model (LLM) interactions.

This repository provides a **reference implementation** of the MIDAS protocol, including a dual-LLM evaluation harness, reproducible drift and preservation metrics, and logging utilities intended to support independent replication studies.
This repository contains a minimal reference implementation of the MIDAS protocol for measuring and controlling drift in multi-turn LLM interactions.

## What MIDAS Is
- A runtime protocol for interaction-time stability
- A set of enforceable invariants over multi-turn LLM interactions
- A replication-first framework with no empirical claims

## What MIDAS Is Not
- A trained model or fine-tuning method
- A benchmark or leaderboard
- A claim about optimal performance or alignment

## Repository Structure
- `src/midas/` — Core protocol implementation
- `scripts/` — Example runners (baseline and MIDAS conditions)
- `examples/` — Minimal configuration and seed inputs
- `docs/` — Replication notes and checklists

## Status
This repository contains an early reference implementation corresponding to **WP 3.0 (v1.5)**.
The implementation is intentionally minimal and is expected to evolve through community replication and extension.

## License
Released under the MIT License.
10.5281/zenodo.17913021
