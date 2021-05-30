# Import the needed modules for prediction
from flask import Flask, request
import os
import tensorflow as tf
import numpy as np
import json

# Check for GPU Support and set it to True
gpu_devices = tf.config.experimental.list_physical_devices("GPU")
for device in gpu_devices:
    tf.config.experimental.set_memory_growth(device, True)

# Define Classes in Dictionary and Load Created Model Previously
classes = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25}

# Load Model and show the Summary of the Model
model = tf.keras.models.load_model('model_SIBI.h5')
model.summary()

# Check for GPU Support and set it to True
gpu_devices = tf.config.experimental.list_physical_devices("GPU")
for device in gpu_devices:
    tf.config.experimental.set_memory_growth(device, True)

# Define the Flask App
app = Flask(__name__)

### route request Prediction from JSON android
@app.route('/predict', methods=['POST'])
def predict():
    #If there's an input from Android
    request_json = request.json
    print("data: {}".format(request_json))
    print("type: {}".format(type(request_json)))

    # Convert into a Array for Prediction
    IMG_array = np.array(request_json.get('data'))

    # Feed input Array Into the Prediction
    predictions = model.predict(IMG_array)
    
    # Using numpy.argmax to find which class between 26 classes
    # have the highest probability between them
    # and Find classes using keys that found before in numpy.argmax
    for alphabets, values in classes.items():
        if values == np.argmax(predictions):
            out_val = alphabets
    
    # Edit Received JSON file to response to the Android with prediction
    response_json = {
        "data" : request_json.get("data"),
        "prediction" : str(out_val)
    }

    # Send Back the Prediction
    return json.dumps(response_json)

### route request PING from JSON android
@app.route('/ping', methods=['POST'])
def ping():
    request_json = request.json
    print("data: {}".format(request_json))
    print("type: {}".format(type(request_json)))

    response_json = {
        "data" : request_json.get("data"),
        "answer" : str("Server is Online")
    }

    return json.dumps(response_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
