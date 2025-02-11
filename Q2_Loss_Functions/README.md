# Implementing and Comparing Loss Functions

## Overview
This code demonstrates how to implement and compare different loss functions using **TensorFlow**. The primary focus is on computing **Mean Squared Error (MSE)** and **Categorical Cross-Entropy (CCE)** for model predictions.

## Dataset
Tensors are generated **manually** for `y_true` and `y_pred` values to simulate different loss calculations. No external datasets are used.

## Code Flow

1. **Defining True Values and Predictions:**
   - `y_true`: Ground truth labels.
   - `y_pred`: Model's predicted values.

2. **Computing Loss Functions:**
   - **Mean Squared Error (MSE)**: Measures squared differences between actual and predicted values.
   - **Categorical Cross-Entropy (CCE)**: Measures classification error based on probability distributions.

3. **Modifying Predictions and Recomputing Loss:**
   - Analyzing how slight modifications in `y_pred` affect MSE and CCE.

4. **Visualizing Loss Values:**
   - Uses **Matplotlib** to plot a **bar chart** comparing MSE and CCE for different predictions.

## Installation & Requirements

### Running on **Google Colab** (Pre-installed TensorFlow and Matplotlib):
- No additional installation required.

### Running on a **Local System**:
```sh
pip install tensorflow matplotlib
```

## Running the Script
To execute the script, run the following command in your terminal or Colab:
```sh
python ha1_2.py
```

## Output

- **Loss values printed** for different predictions.
- **Bar chart comparing MSE and CCE losses**.

📌 **Note:** Open the **HA1_2.ipynb** notebook to view the **executed output**.
📍 **Path:** `Q2_Loss_Functions/HA1_2.ipynb`

## Observations

1. **Loss Value Trends:**
   - **MSE values change gradually** as predictions slightly vary.
   - **CCE is highly sensitive** to small variations in predicted probabilities.

2. **Effect of Modifying Predictions:**
   - A small change in `y_pred` results in a **larger shift in CCE than in MSE**.
   - MSE penalizes squared differences, while CCE emphasizes incorrect classifications more aggressively.

## Remarks
- The code is **properly commented**, explaining each step in detail.
- Use `Q2_Loss_Functions/HA1_2.ipynb` to view the **executed code in Google Colab**.
- **Attaching the `ha1_2.py` script for reference.**

## Contact
**Name:** Harshith Reddy Gundra  
**Student ID:** 700780724  
**Email:** hxg07240@ucmo.edu  

📍 **Code Path:** `Q2_Loss_Functions/HA1_2.ipynb`

