import argparse
import os
import utils
import requests

# speech to text 
endpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": "https://bit.ly/3yxKEIY"
}
headers = {
    "authorization": "646acad2d1114c38a644e646876a9553",
    "content-type": "application/json"
}
response = requests.post(endpoint, json=json, headers=headers)
print(response.json())


# translation to different languages
endpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": "https://bit.ly/3JNcp4Y",
    "language_detection": True
}
headers = {
    "authorization": "YOUR-API-TOKEN",
    "content-type": "application/json"
}
response = requests.post(endpoint, json=json, headers=headers)
print(response.json())