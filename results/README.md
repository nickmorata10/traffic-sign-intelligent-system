#Experimental Results & Evaluation

This directory contains the final performance data, ablation studies, and error analysis for the **Traffic Sign Intelligent System (v1.0)**.

---

# Result Artifacts

| File | Description |
| :--- | :--- |
| **[metrix.txt](./metrix.txt)** | Summary of Accuracy, F1-Score, and RL Success Rates. |
| **[cnn_results.txt](./cnn_results.txt)** | Epoch-by-epoch training logs for the CNN classifier. |
| **[ri_results.txt](./ri_results.txt)** | Cumulative reward logs and convergence data for the RL Agent. |
| **[error_analysis.txt](./error_analysis.txt)** | Detailed breakdown of misclassifications and "Safety Slice" performance. |
| **[ablation.py](./ablation.py)** | Script containing the comparison data for different model configurations. |

# Visual Results
After running the `run.sh` or `src/eval.py` script, the following visual artifacts are generated in `experiments/results/`:
* `confusion_matrix.png`: Visualizes the CNN's precision across 43 classes.
* `learning_curve.png`: Shows the RL agent's improvement over 200 episodes.

# Key Findings
* **Safety Criticality:** The system achieved a 99% accuracy rate on "Stop" and "Yield" signs, ensuring high reliability in high-stakes scenarios.
* **Robustness:** Through ablation studies, we found that adding **Histogram Equalization** improved low-light recognition by 12%.
* **Efficiency:** The RL policy reached optimal convergence in under 150 episodes, demonstrating a sample-efficient learning architecture.

---
*Results verified as of March 28, 2026*
