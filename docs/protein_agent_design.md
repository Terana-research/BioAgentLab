# Protein Agent Design

## Goal

Predict protein functions using multiple AI tools.

---

## Architecture

User
↓
Input Validation
↓
Memory
↓
Task Understanding
↓
Task classification
↓
Planner
↓
Tool Router
↓
Tool Availability check
↓
Primary Tool
↓
Retry/Fallback
↓
Result integration
↓
LLM
↓
Answer

## Tool Routing

The agent selects tools based on task type.

## Failure Recovery

If the primary tool fails, the agent retries and selects a fallback tool.

## Result Validation

The agent compares model outputs with database and literature evidence before responding.

## Components

### ProteinAgent

Responsible for

- Task Understanding
- Planning
- Tool Selection
- Response Generation

### ESMTool

Responsible for

- Protein embedding
- Function prediction

### UniProtTool

Responsible for

- Database retrieval
- Similarity search

### ToolResult

Unified interface for every tool.

Fields

- status
- source
- data
- message

---

## Future Work

- Memory
- Reflection
- Multi-Agent
- PubMed Tool
- BLAST Tool
今天的第一篇论文
