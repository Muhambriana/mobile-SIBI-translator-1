import os
import json
import requests
import numpy as np

input_test = [[[ 892.317], [ 881.301], 
               [ 743.465], [ 666.988],
               [ 885.235], [ 691.533],
               [1027.745], [ 737.426],
               [1131.495], [ 753.244]]]
xs = np.array(input_test)

data = json.dumps({"signature_name": "serving_default", "instances": xs.tolist()})
print(data)

headers = {"content-type": "application/json"}

json_response = requests.post('http://localhost:8501/v1/models/model_sibi:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)['predictions']
print(predictions)

for i, prediction in enumerate(predictions):
    print("Prediction: ",np.argmax(prediction))

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

for alphabets, values in classes.items():
    if values == np.argmax(prediction) :
        print(alphabets)
