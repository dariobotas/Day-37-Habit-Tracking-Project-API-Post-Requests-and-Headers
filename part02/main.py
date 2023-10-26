import requests as api
import os

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
  "token": os.environ["token"],
  "username": "dbotas12",
  "agreeTermsOfService": "yes",
  "notMinor": "yes"
}

def run():
  response = api.post(url = pixela_endpoint, json=user_params)
  print(response.text)