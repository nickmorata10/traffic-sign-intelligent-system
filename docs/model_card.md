# 🆔 Model Card: Traffic Sign Intelligent System (v1.0)

## ## Model Details
* **Developed by:** Team TAURATAPHI (Lead: Nick Christian G. Morata)
* **Model Type:** Convolutional Neural Network (CNN) + Q-Learning (RL)
* **Architecture:** * **CNN:** 2 Convolutional layers with ReLU activation and Max Pooling, followed by 2 Fully Connected layers.
    * **RL:** Discrete Q-Learning table with a state-space mapped from CNN classifications.
* **Version:** 1.0 (Final Submission)
* **License:** MIT

## ## Intended Use
* **Primary Use:** Simulation of autonomous vehicle decision-making based on visual road signs.
* **Intended Users:** Academic researchers and students in the 6INTELSY course.
* **Out-of-Scope:** Real-world vehicle control, critical safety infrastructure, or high-speed highway navigation.

## ## Factors
* **Environmental Factors:** Optimized for daylight conditions with clear visibility. Performance may degrade in heavy rain, snow, or night-time simulations.
* **Technical Factors:** Model requires an input image resolution of 32x32 pixels (standardized from the GTSRB dataset).

## ## Metrics
The model was evaluated using the following performance indicators:
* **CNN Accuracy:** 96.42% (Measures correct sign identification).
* **RL Success Rate:** 91.2% (Measures the agent's ability to reach the goal without traffic violations).
* **Macro-F1 Score:** 0.941 (Ensures balanced performance across all 43 sign classes).

## ## Training Data
* **Dataset:** German Traffic Sign Recognition Benchmark (GTSRB).
* **Composition:** 39,209 training images and 12,630 test images.
* **Pre-processing:** Grayscale conversion, Histogram Equalization, and Normalization $[0, 1]$.

## ## Quantitative Analyses
Detailed results are available in the `/results` directory:
* **Confusion Matrix:** Shows high precision in "Stop" and "Yield" categories.
* **Learning Curve:** Demonstrates agent convergence after ~150 episodes.

## ## Limitations & Bias
* **Geographic Bias:** The model is trained exclusively on German (European) traffic signs. It may not recognize North American or Asian signage correctly.
* **Sim-to-Real Gap:** The RL agent's policy is limited by the constraints of the simulated environment and may not generalize to the physical complexities of real-world driving.

---
*Created for the Final Project of 6INTELSY - March 2026*
