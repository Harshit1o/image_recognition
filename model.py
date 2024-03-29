from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the saved model
model = load_model('cifar10_model.h5')

# Load your custom image
custom_image = Image.open('path_to_your_image.jpg')  # Replace 'path_to_your_image.jpg' with the actual path to your image

# Resize the image to match the input size of the model
custom_image = custom_image.resize((32, 32))

# Convert the image to a numpy array
custom_image = np.array(custom_image)

# Normalize the image
custom_image = custom_image / 255.0

# Reshape the image to match the input shape of the model
custom_image = np.expand_dims(custom_image, axis=0)

# Make predictions on the custom image
predictions = model.predict(custom_image)

# Get the predicted class label
predicted_class = np.argmax(predictions[0])

# Get the corresponding class name
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
predicted_class_name = class_names[predicted_class]

# Display the custom image and the predicted class
plt.imshow(custom_image[0])
plt.title(f"Predicted Class: {predicted_class_name}")
plt.axis('off')
plt.show()
