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

# NexusTiQ24 - GCC Banking Document Validator | Explainable AI

> Banks don't need just Yes/No. They need WHY.

### Problem Statement
GCCs (Global Capability Centers) process 1000s of invoices daily. Manual checking causes:
- Human errors & delays
- High fraud risk
- No audit trail for decisions

### Our Solution - Reasoning Engine
An AI-powered validator that shows **step-by-step reasoning** for every decision, not just a final status.

**Workflow:**
1.  **Extract:** Invoice Amount & Vendor from document
2.  **Retrieve:** PO Amount from system / mock DB
3.  **Compare:** Tolerance-based logic (+/- 5%)
4.  **Reason & Decide:** Provides explainable reasoning + Status

**Explainable AI Output:**
- ✅ `APPROVED` - Reasoning: PERFECT MATCH. No fraud risk. Variance: 0%
- ⚠️ `REVIEW` - Reasoning: MINOR VARIANCE (2.3%) within tolerance. Needs human eye.
- ❌ `REJECTED` - Reasoning: MAJOR MISMATCH! Potential fraud. Invoice: $50k, PO: $30k.

### Key Differentiator
**We give 35% extra for Explainable AI.** Every decision is auditable and compliant for banking.

### Tech Stack
- Python
- Rule-based Reasoning Engine (Explainable AI)
- GCC Banking Domain Logic

### How to Run
```bash
python app.py
