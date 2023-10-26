import requests as api
import os
import datetime as date


USERNAME = "dbotas12"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
  "token": os.environ["token"],
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes"
}

graph_config = {
  "id": GRAPH_ID,
  "name": "Code Graph",
  "unit": "minutes",
  "type": "int",
  "color": "sora"
}

headers={
  "X-USER-TOKEN": os.environ["token"]
}

pixel_data = {
  "date": "20231026",
  "quantity": "300"
}

def run():
  #response = api.post(url = pixela_endpoint, json=user_params)
  #print(response.text)
  graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

  #response = api.post(url = graph_endpoint, json=graph_config, headers=headers)
  #print(response.text)

  
  pixel_response = api.post(url = f"{graph_endpoint}/{GRAPH_ID}", json=pixel_data, headers=headers)
  print(pixel_response.text)