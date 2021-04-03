import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = 'created_user_name'
TOKEN = 'created_token'

#creating the account

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

#creating the graph

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

ID = 'graph1'

graph_config ={
    'id': ID,
    'name': 'Coding Graph',
    'unit': 'Min',
    'type': 'int',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#posting to the graph

entry_endpoint = f'{graph_endpoint}/{ID}'

today = datetime.now()


entry_config ={
    'date': today.strftime('%Y%m%d'),
    'quantity': '60',
}

#response = requests.post(url=entry_endpoint, json=entry_config, headers=headers)
#print(response.text)

#chaging a post

change_date = datetime(year=2021, month=3, day=4)
change_date_formatted = change_date.strftime('%Y%m%d')
entry_change_endpoint = f'{graph_endpoint}/{ID}/{change_date_formatted}'

entry_change_config ={
    'quantity': '20',
}

#response = requests.put(url=entry_change_endpoint, json=entry_change_config, headers=headers)
#print(response.text)

#deleting a post

delete_date = datetime(year=2021, month=3, day=4)
delete_date_formatted = change_date.strftime('%Y%m%d')
entry_delete_endpoint = f'{graph_endpoint}/{ID}/{change_date_formatted}'


#response = requests.delete(url=entry_delete_endpoint, headers=headers)
#print(response.text)
