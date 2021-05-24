# Impoer the needed File for prediction
from flask import Flask
import os
import tensorflow as tf
import numpy as np


app = Flask(__name__)

### route dari html-nya nanti
@app.route('/', methods=['POST'])
def translator():
    gpu_devices = tf.config.experimental.list_physical_devices("GPU")
    for device in gpu_devices:
        tf.config.experimental.set_memory_growth(device, True)

    #Define Classes in Dictionary and Load Created Model Previously
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
        'Z': 25
    }

    model = tf.keras.models.load_model('model_SIBI.h5')
    model.summary()

    #Define the Input for the Inference
    # Thumb Finger or Jari Jempol
    thumb_fingerX = 0
    thumb_fingerY = 0
    # Index Finger or Jari Telunjuk
    index_fingerX = 0
    index_fingerY = 0
    # Middle Finger or Jari Tengah
    middle_fingerX = 0
    middle_fingerY = 0
    # Ring Finger or Jari Manis
    ring_fingerX = 0
    ring_fingerY = 0
    # Pinky Finger or Jari Kelingking
    pinky_fingerX = 0
    pinky_fingerY = 0

    while True: #Selama Apps Android Terkoneksi dengan Cloud
        #Kalau ada Input dari Android
        if #code:
            thumb_fingerX, thumb_fingerY, index_fingerX, index_fingerY, middle_fingerX, middle_fingerY, ring_fingerX, ring_fingerY, pinky_fingerX, pinky_fingerY, output_IMG = #Input dari Android terdiri dari 10 Value

        #Convert into a Array for Prediction
        input_IMG = [[[thumb_fingerX], [thumb_fingerY],
                  [index_fingerX], [index_fingerY],
                  [middle_fingerX], [middle_fingerY],
                  [ring_fingerX], [ring_fingerY],
                  [pinky_fingerX], [pinky_fingerY]]]
        IMG_array = np.array(input_IMG)

        #Feed input Array Into the Prediction
        predictions = model.predict_classes(IMG_array)
        for alphabets, values in classes.items():
            if values == predictions[0] :
                text_prediction = alphabets

        #Send Prediksi kembali ke Android berupa satu value yaitu text_prediction
        #text_prediction to Android

        #Kalau Apps android matiin koneksi, matiin Pythonnya
        if #code:
            break
