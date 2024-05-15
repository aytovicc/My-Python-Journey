from datetime import datetime
import requests

TOKEN = "340556aytacpython"
USERNAME = "lythius"

GRAPH_ID = "lythiuscoding"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
ADD_VALUE_ENDPOINT = F"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# PARAMETERS
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}


graph_params = {
    "id": GRAPH_ID,
    "name": "hours coded",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

today = datetime(year= 2023, month= 10, day=28)
add_value_params = {
    "date" : today.strftime('%Y%m%d'),
    "quantity" : "14"
}

# HEADERS
header = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=PIXELA_ENDPOINT, json= user_params)
# print(response.text)

# GET THE GRAPH ONLINE
#graph_response = requests.post(url=GRAPH_ENDPOINT, json= graph_params, headers= header)
#print(graph_response.text)

# COPY IT AND SEARCH THE URL IN CHROME, OPERA...
GRAPH_URL = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}.html"
print("This is your graph's web url:",GRAPH_URL)

# ADD VALUE TO YOUR GRAPH
add_value_to_graph = requests.post(url=ADD_VALUE_ENDPOINT, headers= header, json= add_value_params)
print(add_value_to_graph.text)