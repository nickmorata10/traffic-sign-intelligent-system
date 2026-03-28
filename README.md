# Traffic Sign Intelligent System: Perception to Action (v1.0)

## Team: TAURATAPHI
* **Project Lead / Integration:** Morata, Nick Christian G.  
* **Data & Ethics:** Muli, Icent Kurt  
* **Modeling:** Alvarez, Rainier  
* **Evaluation & MLOps:** Esguerra, Keane  

---

## Project Overview
This intelligent system integrates a **Convolutional Neural Network (CNN)** for high-accuracy traffic sign recognition with a **Reinforcement Learning (RL) agent** to simulate autonomous decision-making. 

By combining Computer Vision with a **Natural Language Processing (NLP)** component for label mapping, the system creates a complete "Perception-to-Action" pipeline, mimicking how a self-driving car interprets signs and chooses safe maneuvers.

---

## Objectives
- **Vision:** Develop a high-precision CNN for classifying 43 traffic sign classes.  
- **Decision:** Implement a Q-Learning RL agent that chooses safe actions (Stop/Slow/Go).  
- **Integration:** Map NLP labels to agent states for human-readable policy making.  
- **MLOps:** Build a fully reproducible pipeline (`run.sh`) from data to evaluation.  
- **Ethics:** Provide a formal Model Card and Risk Analysis for AI safety.  

---

## Project Structure & Navigation
* **`src/`**: Core Python logic (CNN, RL, NLP, and Training).
* **`docs/`**: Formal Reports, Ethics Statement, and Model Card.
* **`data/`**: Dataset metadata and setup instructions.
* **`results/`**: Training logs, Metrix, and Ablation studies.
* **`env/`**: Environment setup (Conda/Pip) and dependency lists.
* **`notebooks/`**: Exploratory Data Analysis (EDA) and visualizations.

---

## Dataset
* **Source:** German Traffic Sign Recognition Benchmark (GTSRB).
* **Scale:** 50,000+ images across 43 unique traffic categories.
* **Pre-processing:** Grayscale normalization and Histogram Equalization.

---

## System Components

### 1. CNN (Vision Layer)
- **Role:** The "Eyes" of the system.
- **Spec:** Custom 4-layer CNN optimized for sign-specific features.
- **Performance:** 96.42% accuracy on test data.

### 2. NLP (Semantic Layer)
- **Role:** The "Translator."
- **Spec:** Processes text labels into numerical semantic embeddings.
- **Benefit:** Allows the agent to understand the "meaning" of a sign before acting.

### 3. RL Agent (Policy Layer)
- **Role:** The "Brain."
- **Spec:** Q-Learning algorithm using CNN predictions as state inputs.
- **Goal:** Maximizes safety rewards (e.g., +10 for stopping at a Red sign).

---

## Quick Start (Reproducibility)
To reproduce the entire project from scratch, ensure you have Python installed and run:

```bash
# 1. Clone the repository
git clone [https://github.com/nickmorata10/traffic-sign-intelligent-system.git](https://github.com/nickmorata10/traffic-sign-intelligent-system.git)
cd traffic-sign-intelligent-system

# 2. Run the master pipeline
bash run.sh
