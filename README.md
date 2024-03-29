# image_recognition

## Overview
This project is aimed at performing image recognition using a convolutional neural network (CNN) implemented with Keras. The model is trained on the CIFAR-10 dataset, which consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class. After training, the model can predict the class of custom images provided by the user.

## Installation
1. Clone this repository to your local machine:

```git clone https://github.com/Harshit1o/image-recognition-project.git```

## Usage
Ensure that you have a trained model saved as cifar10_model.h5. If you don't have one, you can train your model or use a pre-trained model.

Replace 'path_to_your_image.jpg' in the code with the actual path to your custom image that you want to classify.

Run the script:

```python image_recognition.py```

The script will display the custom image along with the predicted class.

## Code Explanation

The script loads the saved CNN model trained on the CIFAR-10 dataset.
It loads a custom image provided by the user.
The image is resized to match the input size of the model (32x32 pixels).
The image is converted to a numpy array and normalized.
The image is reshaped to match the input shape of the model.
Predictions are made on the custom image using the loaded model.
The predicted class label is obtained along with the corresponding class name.
Finally, the custom image and the predicted class are displayed using matplotlib.

## Thank You
