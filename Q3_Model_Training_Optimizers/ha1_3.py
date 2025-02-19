# -*- coding: utf-8 -*-
"""HA1_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19HLu742l3PPzxOv8SLOTmEajhpAMPORP

#Train model with different optimisers (Adam & SGD)

1. Importing required libraries
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import datetime

"""2. Loading the MNIST dataset from tensorflow (x_train, x_test, y_train, y_test)
3. The grayscale images in the MNIST dataset have pixel values ranging from 0 to 255 (8 bit representation), Neural networks perform better when the inpute values scaled to a smaller range (between 0 to 1).
Dividing by 255.0 scales the values to [0, 1], making the training process more stable (avaoding large weight updates), faster convergence (since values are in a small and manageable range), helps avoid issues elated to exploding or vanishing gradients.
"""

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

"""4. create_model() function creates and returns a tensorflow sequential mode.
i) sequential() to create a stack of layer where each layers output serves as an input to the next layer
ii) Flatten() to convert 2D image(28*28) into a 1D vector(784,)
iii) first hiddeen layer with 128 neurons, and relu activation function which helps in introducing non-linearity nd helping the network to learn complex patterns.
5. using create_model() function to reuse the same code for building independent models
"""

def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

"""6. Compiling the model ADAM(Adaptive moment estimation), sparse_categorical_crossentropy (best when lables are integers instead of one hot encoded values), accuracy (tracks model performance during training)"""

model_adam = create_model()
model_adam.compile(optimizer='adam',
                   loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])

"""7. Compiling the model SGD(stochastic gradient descent) genreally used for large-scale machine learning problems often encountered in text classification and natural language processing, sparse_categorical_crossentropy (best when lables are integers instead of one hot encoded values), accuracy (tracks model performance during training)"""

model_sgd = create_model()
model_sgd.compile(optimizer='sgd',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

"""8. for simple datasets like MNIST, 5 epoch is usually sufficient for achieving a good accuracy (>90%), and verbose 2 is to display one line per epoch"""

epochs = 5
history_adam = model_adam.fit(x_train, y_train, epochs=epochs, validation_data=(x_test, y_test), verbose=2)
history_sgd = model_sgd.fit(x_train, y_train, epochs=epochs, validation_data=(x_test, y_test), verbose=2)

"""9. Plotting the learning curve for both adam and sgd model using matplotlib library."""

plt.figure(figsize=(8, 6))
plt.plot(history_adam.history['accuracy'], label='Adam Training Accuracy', color='blue')
plt.plot(history_adam.history['val_accuracy'], label='Adam Validation Accuracy', linestyle='dashed', color='blue')
plt.plot(history_sgd.history['accuracy'], label='SGD Training Accuracy', color='red')
plt.plot(history_sgd.history['val_accuracy'], label='SGD Validation Accuracy', linestyle='dashed', color='red')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Adam vs. SGD Accuracy Comparison')
plt.show()

"""10. Printitng test loss and accuracy for both adam and sgd models"""

test_loss_adam, test_acc_adam = model_adam.evaluate(x_test, y_test, verbose=2)
test_loss_sgd, test_acc_sgd = model_sgd.evaluate(x_test, y_test, verbose=2)

print(f"Adam Test Accuracy: {test_acc_adam:.4f}")
print(f"SGD Test Accuracy: {test_acc_sgd:.4f}")

"""Observations:

*   Adam achieves faster convergence due to adaptive learning rates, while SGD requires more epochs to reach similar accuracy.
*   Training accuracy fluctuates more with SGD, whereas Adam provides smoother learning curves.
*   Validation accuracy with Adam is generally higher, indicating better generalization.
*   SGD may overfit less but needs tuning (learning rate scheduling) for better performance.
*   Adam is preferred for efficient and stable training, while SGD is useful for controlled, steady updates in larger datasets.






"""