# Notebooks & Data Exploration

This directory contains Jupyter notebooks and analysis scripts used during the **Exploratory Data Analysis (EDA)** and prototyping phases.

## Contents
* **`eda.txt`**: A summarized text version of the findings for quick reference.

## Key Insights from Analysis
1. **Class Imbalance:** Certain signs (e.g., Speed Limit 50) have 10x more images than others (e.g., Dangerous Curve). We addressed this using oversampling.
2. **Resolution:** Most images are ~32x32 pixels, confirming our CNN input layer size.
3. **Lighting Conditions:** A significant portion of the data is underexposed, leading us to implement **Histogram Equalization** in our `data_pipeline.py`.
