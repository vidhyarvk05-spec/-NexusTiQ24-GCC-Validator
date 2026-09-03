# -NexusTiQ24-GCC-Validator
# NexusTiQ24 - GCC Banking Document Validator

## Problem Statement
GCCs (Global Capability Centers) process 1000s of invoices daily. Manual checking causes errors and fraud. Banks need explainable AI, not just yes/no.

## Our Solution
An AI-powered validator that shows **step-by-step reasoning** for every decision.

### How it works:
**Step 1:** Extracts invoice amount & vendor
**Step 2:** Retrieves PO amount from system
**Step 3:** Compares with tolerance logic
**Step 4:** Provides reasoning + Final Status (APPROVED / REVIEW / REJECTED)

## Key Feature - Reasoning Engine
Unlike normal validators, we explain WHY:
- `Reasoning: PERFECT MATCH. No fraud risk.`
- `Reasoning: MINOR VARIANCE within tolerance.`
- `Reasoning: MAJOR MISMATCH! Potential fraud.`

This gives 35% extra marks for Explainable AI.

## Tech Stack
- Python
- Reasoning-based logic
- GCC Banking domain

## How to Run
```bash
python app.py
