import requests
import json

url = "https://exp.host/--/api/v2/push/send"

def send_push_message(message):
    payload = json.dumps(message)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
