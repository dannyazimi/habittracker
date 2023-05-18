import requests
from datetime import datetime
USERNAME = "dannyazimi"
PIXELA_TOKEN = "SOME_TOKEN"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)


# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config={
#     "id": "graph1",
#     "name": "Coding",
#     "unit": "Min",
#     "type": "int",
#     "color": "momiji",
# }
# headers = {
#     "X-USER-TOKEN": PIXELA_TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today= datetime.now()
graph_id = "graph1"
post_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today?"),
}
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
# response = requests.post(url=post_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity": "120"
}
# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)