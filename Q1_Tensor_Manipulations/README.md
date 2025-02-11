Tensor Manipulation & Reshaping

Overview: This code focuces on tensor manipulations using TensorFlow, including creating, reshaping, transposing, and broadcasting tensors. These operations are essential for handling multi-dimensional data in deep learning.

Dataset: Tensors are generated randomly using TensorFlow functions. No external datasets are used

Code Flow: 
  i. creating a random tensor: 
    Generates a 4×6 random tensor with integer values between 0 and 1
  ii. Finding Rank and Shape:
    Computes the rank (number of dimensions) and shape (size of each dimension) using TensorFlow functions.
  iii. Reshaping & Transposing Tensors:
    Reshapes the tensor from (4,6) to (2,3,4).
    Transposes it to (3,2,4) to modify axis positions.
  iv. Broadcasting a Smaller Tensor:
    Creates a (1,4) tensor and broadcasts it to match a larger tensor before performing element-wise addition.
  v. Explanation of Broadcasting:
    Demonstrates how smaller tensors are expanded to match larger tensor shapes.

Installation & Requirements (libraries/packages used): 
  i. code was written on Google colab where TensorFlow is pre installed: 
  ii. Running on a local system: 
    pip install tensorflow

Running the Script: 
  Run the following command in your terminal or Colab to execute the script: python ha1_1.py

Output: 
  i. Prints the rank and shape before and after reshaping.
  ii. Displays the broadcasted tensor’s shape after addition.
  Note: Open the HA1_1.ipynb to view to notebook with executed output 
  Path: Q1_Tensor_Manipulations/HA1_1.ipynb

Observation: 
  i. Rank & Shape Analysis:
    Before reshaping: Rank = 2, Shape = (4,6).
    After reshaping: Rank = 3, Shape = (2,3,4).
    After transposing: Shape changes based on new axis order.
  ii. Broadcasting Behaviour: 
    The smaller tensor automatically expands dimensions to match the larger tensor’s shape before addition.

Remarks: Code is commented properly explanning each step in detail. use Q1_Tensor_Manipulations/HA1_1.ipynb to view the code
in proper format because the code was written and executed in Google colab. Attaching the HA1_1.py (.py format) code for reference.

Contact: 
  Name: Harshith Reddy Gundra
  Student ID: 700780724
  Email: hxg07240@ucmo.edu


