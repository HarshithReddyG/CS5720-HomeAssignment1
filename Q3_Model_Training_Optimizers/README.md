# Train a Model with Different Optimizers

## Overview
This code demonstrates the training of a neural network on the **MNIST dataset** using different optimizers, **Adam** and **SGD (Stochastic Gradient Descent)**, and compares their performance in terms of training and validation accuracy.

## Dataset
The MNIST dataset consists of **handwritten digits (0-9)** with **28x28 grayscale images**. The dataset is split into:
- **60,000 training images**
- **10,000 test images**

## Code Flow

1. **Load and preprocess the MNIST dataset:**
   - Normalize pixel values between **0 and 1**.

2. **Create a Neural Network Model:**
   - Input: **Flatten Layer (28x28 → 784)**
   - Hidden Layer: **128 neurons, ReLU activation**
   - Dropout Layer: **20%**
   - Output Layer: **10 neurons (Softmax activation for classification)**

3. **Compile and Train the Model:**
   - Train **one model with Adam optimizer** and **one with SGD optimizer**.
   - Evaluate and compare training and validation accuracy.

4. **Plot Accuracy Comparison:**
   - Visualize training and validation accuracy trends for both optimizers.

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
python ha1_3.py
```

## Output

- **Training and validation accuracy** for Adam and SGD models.
- **Plot comparing accuracy trends of both optimizers**.

📌 **Note:** Open the **HA1_3.ipynb** notebook to view the **executed output**.
📍 **Path:** `Q3_Model_Training_Optimizers/HA1_3.ipynb`

## Observations

1. **Adam vs. SGD Performance:**
   - **Adam optimizer converges faster**, reaching high accuracy in fewer epochs.
   - **SGD requires more epochs** to achieve similar accuracy but may generalize better in some cases.

2. **Training vs. Validation Accuracy:**
   - Adam exhibits **smoother convergence** with stable training.
   - SGD has **larger fluctuations** in accuracy, requiring **careful learning rate tuning**.

## Remarks
- The code is **properly commented**, explaining each step in detail.
- Use `Q3_Model_Training_Optimizers/HA1_3.ipynb` to view the **executed code in Google Colab**.
- **Attaching the `ha1_3.py` script for reference.**

## Contact
**Name:** Harshith Reddy Gundra  
**Student ID:** 700780724  
**Email:** hxg07240@ucmo.edu  

📍 **Code Path:** `Q3_Model_Training_Optimizers/HA1_3.ipynb`

