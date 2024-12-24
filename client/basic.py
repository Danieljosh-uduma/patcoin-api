import requests


endpoint = 'https://fakestoreapi.com'
endpoint = 'http://localhost:8000/api'

get_response = requests.post(endpoint,params={'user_id': 12004}, json={'username': 'nlisser', 'email': 'miker@gmail.com', 'password': '1234mean'})
# print(get_response.json())

# print(get_response.text)
print(get_response.json())