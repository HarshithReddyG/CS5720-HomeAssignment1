# CS5720 - Home Assignment 1

## Overview
This repository contains the solutions for **CS5720 - Home Assignment 1**, covering multiple tasks related to **TensorFlow, Neural Networks, Loss Functions, and Optimizers**. Each task is organized into separate directories with **Jupyter Notebooks (`.ipynb`)** and **Python scripts (`.py`)**.

## Repository Structure
```
CS5720-HomeAssignment1/
│── Q1_Tensor_Manipulations/
│   ├── HA1_1.ipynb
│   ├── ha1_1.py
│   ├── README.md
│
│── Q2_Loss_Functions/
│   ├── HA1_2.ipynb
│   ├── ha1_2.py
│   ├── README.md
│
│── Q3_Model_Training_Optimizers/
│   ├── HA1_3.ipynb
│   ├── ha1_3.py
│   ├── README.md
│
│── Q4_TensorBoard_Logging/
│   ├── HA1_4.ipynb
│   ├── ha1_4.py
│   ├── logs/
│   │   ├── fit/
│   │   │   ├── 20250211-200738/
│   │   │   │   ├── train/
│   │   │   │   ├── validation/
│   ├── README.md
│
├── README.md  # Main ReadMe file
```

## Assignment Breakdown

### **1. Tensor Manipulations** (Q1_Tensor_Manipulations)
- Covers **TensorFlow operations** such as **reshaping, transposing, broadcasting**.
- Demonstrates basic tensor operations for deep learning.

### **2. Loss Function Comparisons** (Q2_Loss_Functions)
- Implements **Mean Squared Error (MSE)** and **Categorical Cross-Entropy (CCE)**.
- Compares their behavior in **regression vs. classification problems**.

### **3. Training with Different Optimizers** (Q3_Model_Training_Optimizers)
- Trains a neural network on **MNIST** using **Adam & SGD optimizers**.
- Compares accuracy and convergence behavior.

### **4. TensorBoard Logging** (Q4_TensorBoard_Logging)
- Implements **TensorBoard callbacks** for visualization.
- Stores logs for **training & validation** under `logs/fit/`.
- **GitHub links to logs**:
  - **[Training Logs](https://github.com/yourusername/your-repo/blob/main/Q4_TensorBoard_Logging/logs/fit/20250211-200738/train/)**
  - **[Validation Logs](https://github.com/yourusername/your-repo/blob/main/Q4_TensorBoard_Logging/logs/fit/20250211-200738/validation/)**

## Installation & Requirements
Ensure you have the following dependencies installed:
```sh
pip install tensorflow matplotlib numpy
```
If using **Google Colab**, TensorFlow is pre-installed.

## Running the Code
To execute a specific task, navigate to the corresponding folder and run:
```sh
python ha1_X.py  # Replace X with the question number (1-4)
```
Or open the corresponding `.ipynb` file in **Jupyter Notebook / Colab**.

## Viewing TensorBoard (For Q4)
- Run in **Google Colab**:
  ```python
  %load_ext tensorboard
  %tensorboard --logdir logs/fit
  ```
- Run on **Local Machine**:
  ```sh
  tensorboard --logdir=logs/fit
  ```
  Then open **http://localhost:6006/** in a browser.

## Contact
**Name:** Harshith Reddy Gundra  
**Student ID:** 700780724  
**Email:** hxg07240@ucmo.edu  

---
This repository serves as a structured reference for CS5720 assignments, focusing on deep learning concepts and implementation. 🚀

