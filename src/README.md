#Source Code Architecture

This directory contains the core logic for the **Traffic Sign Intelligent System**, organized into a modular pipeline from data processing to reinforcement learning.

---

## 🏗 Modular Components

### **1. Data & Pre-processing**
* **`data_pipeline.py`**: Handles image resizing (32x32), grayscale conversion, and normalization. It prepares the GTSRB data for the CNN.
* **`baseline.py`**: Contains simpler models (like Logistic Regression or Random Forest) used to compare against our CNN performance.

### **2. Computer Vision (CNN)**
* **`models/cnn_model.py`**: Defines the neural network architecture (Convolutional layers + ReLU + Pooling).
* **`train.py`**: The main training loop. It optimizes the CNN weights and saves the best model to `models/final_cnn.pth`.

### **3. Decision Making (RL)**
* **`rl_agent.py`**: Implements the Q-Learning agent. It receives the classification from the CNN and decides the "Smart Action" (Stop, Slow, or Go).
* **`nlp_component.py`**: Translates the agent's decisions into human-readable text commands (e.g., "Stopping at Stop Sign").

### **4. Evaluation**
* **`eval.py`**: The final testing script. It runs the trained model on test data and generates the Confusion Matrix and Learning Curves found in the `/results` directory.

---

## Execution Flow
The system is designed to be run in a specific order, which is automated by the root **`run.sh`**:
1. **Prepare:** `data_pipeline.py`
2. **Train:** `train.py`
3. **Simulate:** `rl_agent.py`
4. **Evaluate:** `eval.py`

---

## Coding Standards
* **Python 3.9+** compliance.
* **Docstrings:** All major functions include documentation.
* **Error Handling:** Try-except blocks are used for model loading and directory creation.

---
*Developed for 6INTELSY - Intelligent Systems Final Project*
