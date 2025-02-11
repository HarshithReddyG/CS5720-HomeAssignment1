# Tensor Manipulation & Reshaping

## Overview
This project focuses on tensor manipulations using **TensorFlow**, including creating, reshaping, transposing, and broadcasting tensors. These operations are essential for handling multi-dimensional data in deep learning.

## Dataset
Tensors are generated **randomly** using TensorFlow functions. No external datasets are used.

## Code Flow
1. **Creating a Random Tensor:**
   - Generates a **4×6 random tensor** with integer values between **0 and 1**.
2. **Finding Rank and Shape:**
   - Computes the **rank (number of dimensions)** and **shape (size of each dimension)** using TensorFlow functions.
3. **Reshaping & Transposing Tensors:**
   - Reshapes the tensor from **(4,6) to (2,3,4)**.
   - Transposes it to **(3,2,4)** to modify axis positions.
4. **Broadcasting a Smaller Tensor:**
   - Creates a **(1,4)** tensor and broadcasts it to match a larger tensor before performing element-wise addition.
5. **Explanation of Broadcasting:**
   - Demonstrates how smaller tensors expand to match larger tensor shapes.

## Installation & Requirements
### Running on **Google Colab** (Pre-installed TensorFlow):
- No additional installation required.

### Running on a **Local System**:
```sh
pip install tensorflow
```

## Running the Script
To execute the script, run the following command in your terminal or Colab:
```sh
python ha1_1.py
```

## Output
- **Prints the rank and shape** before and after reshaping.
- **Displays the broadcasted tensor’s shape** after addition.

📌 **Note:** Open the **HA1_1.ipynb** notebook to view the **executed output**.
📍 **Path:** `Q1_Tensor_Manipulations/HA1_1.ipynb`

## Observations
1. **Rank & Shape Analysis:**
   - **Before reshaping:** Rank = **2**, Shape = **(4,6)**.
   - **After reshaping:** Rank = **3**, Shape = **(2,3,4)**.
   - **After transposing:** Shape changes based on the new axis order.
2. **Broadcasting Behavior:**
   - The **smaller tensor automatically expands dimensions** to match the larger tensor’s shape before addition.

## Remarks
- The code is **properly commented**, explaining each step in detail.
- Use **`Q1_Tensor_Manipulations/HA1_1.ipynb`** to view the **executed code in Google Colab**.
- **Attaching the `HA1_1.py`** script for reference.

## Contact
**Name:** Harshith Reddy Gundra  
**Student ID:** 700780724  
**Email:** hxg07240@ucmo.edu  

📍 **Code Path:** `Q1_Tensor_Manipulations/HA1_1.ipynb`

