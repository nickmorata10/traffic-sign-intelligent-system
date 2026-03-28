# Data Directory

This folder contains the metadata and scripts required to prepare the dataset for the **Traffic Sign Intelligent System**.

## ## Folder Structure
* `train/`: Training split (39,209 images).
* `val/`: Validation split for hyperparameter tuning.
* `test/`: Unseen test data for final evaluation.

## ## How to Get the Data
To keep the repository lightweight, the raw image files are not included in this commit. Follow these steps to prepare your environment:

1.  Download the **GTSRB** dataset from [Kaggle](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign).
2.  Extract the ZIP file.
3.  Place the images inside the `data/train` and `data/test` folders respectively.
4.  Run the pre-processing script:
    ```bash
    python src/data_pipeline.py
    ```

## ## Data Ethics & Governance
This project utilizes public research data. We have performed a "Data Scrub" to ensure:
* **No Bias:** Classes are balanced using oversampling in the pipeline.
* **Privacy:** All images are cropped to the sign only, removing any surrounding environmental PII.
* **Integrity:** MD5 checksums are used to verify file consistency during training.
