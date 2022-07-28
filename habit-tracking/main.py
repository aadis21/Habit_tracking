import requests
from datetime import datetime

USERNAME = "anuraag2"
TOKEN = "Secret_key"
GRAPH_ID = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
      "id": GRAPH_ID,
      "name": "Cycling Graph",
      "unit": "Km",
      "type": "float",
      "color": "ajisai"
  }

headers = {
      "X-USER-TOKEN": TOKEN
  }



pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_data = {
       "date": today.strftime("%Y%m%d"),

         "quantity": input("How many kilometers did you cycle today? "),
   }
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
# website result show krane ke liye url
# graphhapit_tracker_url;
# https://pixe.la/v1/users/anuraag2/graphs/graph2.html


# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# new_pixel_data = {
#      "date":"20220728",
#      "quantity": "100"
#
# }
# #
# # # ## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)
#
# #
# # delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# #
# #
# # ## DELETE
# # # response = requests.delete(url=delete_endpoint, headers=headers)
# # # print(response.text)