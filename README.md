# Traffic Sign Classifier + RL Policy (Vision + RL)

## Team: TAURATAPHI
* **Project Lead / Integration:** Morata, Nick Christian G.  
* **Data & Ethics:** Muli, Icent Kurt  
* **Modeling:** Alvarez, Rainier  
* **Evaluation & MLOps:** Esguerra, Keane  

---

## Project Overview
This intelligent system integrates a **Convolutional Neural Network (CNN)** for traffic sign recognition with a **Reinforcement Learning (RL) agent** to simulate decision-making in a controlled environment.

The system also includes a lightweight **Natural Language Processing (NLP)** component to process traffic sign labels and metadata, forming a complete intelligent pipeline from perception to action.

---

## Objectives
- Develop a CNN model for traffic sign classification  
- Implement a Q-learning RL agent for decision-making  
- Integrate an NLP component for label processing  
- Build a complete ML pipeline (data → training → evaluation)  
- Provide ethical analysis and model documentation  

---

## Dataset
- **German Traffic Sign Recognition Benchmark (GTSRB)**  
- Contains labeled traffic sign images across multiple classes  
- Organized into training, validation, and testing sets  

---

## System Components

### 1. CNN (Vision)
- Classifies traffic sign images  
- Built using a custom CNN architecture  

### 2. NLP Component
- Processes traffic sign labels  
- Converts text labels into numerical representations  

### 3. RL Agent
- Q-learning based agent  
- Uses CNN predictions as input  
- Learns optimal actions through reward feedback  

---

## Project Structure
project-root/
│
├── data/                  # Dataset info and files
├── docs/                  # proposal.pdf, checkpoint.pdf, final_report.pdf, model_card.md
├── env/                   # environment.yml
├── notebooks/             # EDA notebook
├── results/               # outputs, logs, metrics
├── src/                   # source code
│   ├── baseline.py
│   ├── cnn_model.py
│   ├── nlp_component.py
│   ├── rl_agent.py
│
├── requirements.txt       # dependencies
├── run.sh                 # one-command run script
└── README.md
