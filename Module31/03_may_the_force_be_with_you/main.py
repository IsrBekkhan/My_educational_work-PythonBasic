import requests


my_req = requests.get('https://breakingbadapi.com/api/characters/8')
print(my_req)
print(my_req.text)
