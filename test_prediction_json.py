import os
import json
import requests
import numpy as np

# Input Test of 10 x 1 array
input_test = [[[ 892.317], [ 881.301], 
               [ 743.465], [ 666.988],
               [ 885.235], [ 691.533],
               [1027.745], [ 737.426],
               [1131.495], [ 753.244]]]

# Create Json File for dumping to the server
data = json.dumps({"data": input_test})

# Checking inside the dictionary of data inside of the JSON
print(data)

# Add header to JSON so the server recognize as an JSON Application Request
headers = {"content-type": "application/json"}

# Send Request to the Server for the Prediction
json_response = requests.post('http://34.101.121.113:80/predict', data=data, headers=headers)

# Received the response and print the prediction
prediction = json.loads(json_response.text)['prediction']
print(prediction)

