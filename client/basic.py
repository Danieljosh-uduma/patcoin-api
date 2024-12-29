import requests


endpoint = 'https://fakestoreapi.com'
endpoint = 'http://localhost:8000/api/users/marc-df79d1f0-6b00-45d3-89c6-8e40a0fc88e8-patcoin.token-referral/'

get_response = requests.get(endpoint,params={'user_id': 12004}, json={'username': 'nlisser', 'email': 'miker@gmail.com', 'password': '1234mean'})
# print(get_response.json())

# print(get_response.text)
print(get_response.json())