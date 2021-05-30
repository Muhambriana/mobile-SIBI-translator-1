import json
import requests

for i in range(10):
    data = json.dumps({"data": "is Server Online?"})

    headers = {"content-type": "application/json"}

    json_response = requests.post('http://localhost:5000/ping', data=data, headers=headers)

    response_of_the_server = json.loads(json_response.text)['answer']
    print(response_of_the_server)
