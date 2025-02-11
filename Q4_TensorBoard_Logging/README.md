# Neural Network Training with TensorBoard

## Overview
This code demonstrates how to train a neural network on the **MNIST dataset** while enabling **TensorBoard logging** for real-time visualization of training and validation metrics.

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

3. **Compile and Train the Model with TensorBoard Logging:**
   - Enable **TensorBoard callback** to log training metrics.
   - Store logs in `logs/fit/<timestamp>/` to track multiple training sessions.

4. **Visualize Training with TensorBoard:**
   - Monitor training vs. validation loss and accuracy.
   - Detect **overfitting** and **training performance issues**.

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
python ha1_4.py
```

## Viewing TensorBoard

### **For Google Colab:**
Run the following command **after training** inside a Colab cell:
```python
%load_ext tensorboard
%tensorboard --logdir logs/fit
```
This will launch TensorBoard inside **Google Colab**.

### **For Local System:**
Run the following command in your **terminal or command prompt**:
```sh
tensorboard --logdir=logs/fit
```
Then, open **http://localhost:6006/** in your web browser to view the TensorBoard dashboard.

### **Download TensorBoard Logs from GitHub**
The training logs have been uploaded to GitHub and can be accessed at the following location:
- **Training Logs:** [`Q4_TensorBoard_Logging/logs/fit/20250211-200738/train/`](https://github.com/yourusername/your-repo/blob/main/Q4_TensorBoard_Logging/logs/fit/20250211-200738/train/)
- **Validation Logs:** [`Q4_TensorBoard_Logging/logs/fit/20250211-200738/validation/`](https://github.com/yourusername/your-repo/blob/main/Q4_TensorBoard_Logging/logs/fit/20250211-200738/validation/)

To use these logs locally, download them and run:
```sh
tensorboard --logdir=logs/fit
```
Then open **http://localhost:6006/** in your browser.

## Output

- **Training and validation accuracy/loss graphs in TensorBoard.**
- **Real-time insights into model convergence and overfitting detection.**

📌 **Note:** Open the **HA1_4.ipynb** notebook to view the **executed output**.
📍 **Path:** `Q4_TensorBoard_Logging/HA1_4.ipynb`

## Observations

1. **Training vs. Validation Accuracy Trends:**
   - If training accuracy **steadily increases** while validation accuracy **stagnates or decreases**, the model may be **overfitting**.
   - Ideally, both should **rise together**, indicating good generalization.

2. **Detecting Overfitting Using TensorBoard:**
   - **Overfitting occurs when validation loss starts increasing** while training loss continues decreasing.
   - TensorBoard visualizes this, allowing for early stopping or regularization adjustments.

3. **Effect of Increasing Epochs:**
   - More epochs improve training accuracy initially, but after a point, the model **memorizes the data** instead of generalizing.
   - **Dropout layers and early stopping** can help mitigate overfitting.

## Remarks
- The code is **properly commented**, explaining each step in detail.
- Use `Q4_TensorBoard_Logging/HA1_4.ipynb` to view the **executed code in Google Colab**.
- **Attaching the `ha1_4.py` script for reference.**

## Contact
**Name:** Harshith Reddy Gundra  
**Student ID:** 700780724  
**Email:** hxg07240@ucmo.edu  

📍 **Code Path:** `Q4_TensorBoard_Logging/HA1_4.ipynb`

