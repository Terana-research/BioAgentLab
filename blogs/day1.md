# Day 1 - Building My First AI Agent

**Date**

2026-07-15

---

# Today's Goal

Build the architecture of my first Protein Agent.

---

# What I Implemented

Today I implemented the basic workflow of a Protein Agent.

Current architecture:

User

↓

Task Understanding

↓

Planner

↓

Tool Router

↓

ESM Tool

↓

Fallback (UniProt)

↓

Response

I also implemented a fallback mechanism.

When the ESM model is unavailable, the agent automatically switches to UniProt.

---

# Problems I Encountered

## Git Merge

At the beginning I didn't understand why Git asked me to merge.

After learning Git workflow, I realized Merge means combining two versions instead of overwriting them.

## ToolResult Design

Initially I thought every tool could simply return a dictionary.

After discussing the system design, I realized a unified ToolResult interface is much easier to maintain.

---

# What I Learned

Today I learned that an Agent is not simply a language model.

A modern AI Agent consists of several components:

- Task Understanding
- Planner
- Tool Routing
- Tool Execution
- Response Generation

The model itself (such as ESM) is only one tool inside the agent.

---

# Reflection

The biggest change in my thinking today is that I started to think about software architecture instead of only writing Python code.

I realized that each tool should have a single responsibility, while the Agent should focus on planning and coordinating different tools.

---

# Next Step

- Learn inheritance
- Design BaseTool interface
- Read the ReAct paper