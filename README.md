# Bayesian Optimization Catalyst Discovery

## Overview

This project demonstrates an AI-driven catalyst discovery workflow using Gaussian Process Regression (GPR) and Bayesian Optimization concepts.

The workflow predicts catalyst performance, estimates uncertainty, ranks virtual catalysts, and selects promising candidates for experimental validation.

---

## Objectives

- Train a GPR model on catalyst data
- Generate virtual catalyst search spaces
- Predict catalyst overpotential
- Estimate prediction uncertainty
- Rank catalyst candidates
- Apply Expected Improvement (EI)
- Simulate Bayesian Optimization cycles
- Visualize catalyst discovery results

---

## Workflow

Literature Data
↓
Train GPR
↓
Generate Search Space
↓
Predict Virtual Catalysts
↓
Estimate Uncertainty
↓
Calculate EI
↓
Rank Candidates
↓
Select Best Candidate
↓
Simulate Experiment
↓
Update Dataset

---

## Repository Structure

```text
bayesian-optimization-catalyst-discovery/

├── data/
├── figures/
├── results/
├── src/
│   ├── train_gpr.py
│   ├── generate_search_space.py
│   ├── predict_virtual_catalysts.py
│   ├── rank_candidates.py
│   ├── optimization_cycle.py
│   └── visualize_results.py
│
└── README.md