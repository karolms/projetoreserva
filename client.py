import requests 

r = requests.get('localhost:8000/users')

r.json()