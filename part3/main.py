import requests as api
import os


USERNAME = "dbotas12"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
  "token": os.environ["token"],
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes"
}

def run():
  #response = api.post(url = pixela_endpoint, json=user_params)
  #print(response.text)
  graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

  graph_config = {
    "id": "graph1",
    "name": "Code Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
  }

  headers={
    "X-USER-TOKEN": os.environ["token"]
  }
  

  response = api.post(url = graph_endpoint, json=graph_config, headers=headers)
  print(response.text)