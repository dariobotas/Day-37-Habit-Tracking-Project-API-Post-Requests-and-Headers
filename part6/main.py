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
  "date": date.datetime.now().strftime("%Y%m%d"),
  "quantity": input("How many minutes did you code today? ")
}

def run():
  #response = api.post(url = pixela_endpoint, json=user_params)
  #print(response.text)
  graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

  #response = api.post(url = graph_endpoint, json=graph_config, headers=headers)
  #print(response.text)

  pixel_response = api.post(url = f"{graph_endpoint}/{GRAPH_ID}", json=pixel_data, headers=headers)
  print(pixel_response.text)

#  pixel_update = api.put(url = f"{graph_endpoint}/{GRAPH_ID}/{date.datetime(2023,10,25).strftime('%Y%m%d')}", json={"quantity": "220"}, headers=headers)
#  print(pixel_update.text)

#  pixel_delete = api.delete(url = f"{graph_endpoint}/{GRAPH_ID}/{date.datetime(2023,10,25).strftime('%Y%m%d')}", headers=headers)
  #print(pixel_delete.text)