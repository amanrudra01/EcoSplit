import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Load saved model
model = tf.keras.models.load_model("my_model.keras")

# Define class names (based on your training folders)
class_names = ['inorganic', 'organic']

# Load and preprocess image
img_path = "sample/metal93.jpg"
img = image.load_img(img_path, target_size=(256, 256))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)  # (1, 256, 256, 3)

# Predict
prediction = model.predict(img_array)
predicted_class = int(prediction[0][0] > 0.5)
confidence = float(prediction[0][0]) * 100

# Show result
plt.imshow(img)
plt.title(f"Predicted: {class_names[predicted_class]} ({confidence:.2f}%)")
plt.axis('off')
plt.show()

# Also print to console
print(f"Predicted class: {class_names[predicted_class]}")
print(f"Confidence: {confidence:.2f}%")
