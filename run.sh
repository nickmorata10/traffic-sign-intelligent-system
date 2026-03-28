#!/bin/bash

# 1. Install required libraries
echo "--- Installing Dependencies ---"
pip install -r requirements.txt

# 2. Run the Data Pipeline (Pre-processing)
echo "--- Preparing Dataset ---"
python src/data_pipeline.py

# 3. Train the CNN and ML Baselines
echo "--- Training CNN and Baseline Models ---"
python src/train.py

# 4. Run the Reinforcement Learning Simulation
echo "--- Running RL Agent Simulation ---"
python src/rl_agent.py

# 5. Generate Evaluation Metrics and Plots
echo "--- Generating Final Results and Plots ---"
python src/eval.py

echo "--- Project Successfully Reproduced! Results are in experiments/results/ ---"
