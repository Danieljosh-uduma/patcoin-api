import requests


endpoint = 'https://fakestoreapi.com'
endpoint = 'http://localhost:8000/api'

get_response = requests.get(endpoint,params={'user_id': 12004}, json={'love': True})
# print(get_response.json())

# print(get_response.text)
print(get_response.json())