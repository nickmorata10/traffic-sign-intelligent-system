# Ethics & Policy Statement: Traffic Sign Intelligent System
**Team:** TAURATAPHI  
**Date:** March 28, 2026

---

## 1. Project Overview and Intended Use
The **Traffic Sign Classifier + RL Policy** system is designed to integrate computer vision (CNN) with decision-making agents (RL) to enhance road safety in simulated environments. The intended use is for **educational and research purposes** within autonomous vehicle simulations. It is **not** intended for deployment in real-world vehicles without extensive hardware integration and rigorous safety testing.

## 2. Ethical Risk Register & Mitigations
We identified three primary ethical risks during the development of this intelligent system. Below are the mitigation strategies implemented:

| Risk | Description | Mitigation Strategy |
| :--- | :--- | :--- |
| **Misclassification Hazard** | The CNN may misidentify a "Stop" sign as a speed limit, causing the RL agent to accelerate. | **Confidence Thresholding:** If CNN confidence is <90%, the system defaults to a "Safety-Slow" state. |
| **Dataset Bias** | The GTSRB dataset consists of European signs; the model may fail in regions with different signage. | **Disclaimer & Scope:** The model card explicitly limits the operational domain to GTSRB-standard regions. |
| **Automation Bias** | Users may over-rely on the system, ignoring the need for human oversight. | **Human-in-the-Loop:** The system architecture includes a "Manual Override" hook in the RL policy. |

## 3. Data Privacy and Governance
* **Dataset Sourcing:** We utilized the **German Traffic Sign Recognition Benchmark (GTSRB)**. This dataset is public and contains no Personally Identifiable Information (PII) such as faces or license plates.
* **Consent:** As the data is open-source and anonymized, individual consent was not required. We adhere to the original licensing terms for academic use.
* **Data Minimization:** No user data or GPS coordinates are stored by the model during inference, upholding strict privacy standards.

## 4. Fairness and Representation
To ensure fairness, we performed a **Slice Analysis** (documented in `results/error_analysis.txt`). We found that while the model performs at 98% accuracy for warning signs, it drops to 91% for certain speed limits under low-lighting conditions. 
* **Action Taken:** We implemented **Data Augmentation** (Ablation 1) specifically to include blurred and darkened images, improving fairness across different environmental conditions.

## 5. Safety-Critical Limits of Simulation
The Reinforcement Learning component was trained in a simplified environment. While the agent shows a **91.2% success rate**, we acknowledge the "reality gap." 
* **Policy:** This system must be treated as a **Level 2 (Partial Automation)** prototype. It assumes a human supervisor is present to handle edge cases that the RL agent has not yet encountered.

## 6. Conclusion and Responsible Guidance
Team TAURATAPHI is committed to the responsible development of AI. By documenting our failures (Error Analysis) and being transparent about our model's limits (Model Card), we ensure that this technology is used as a tool for safety, not a replacement for human judgment.

---
*Developed for 6INTELSY - Intelligent Systems Final Project*
