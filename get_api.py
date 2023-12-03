import requests

url_api = 'https://pokeapi.co/api/v2/pokemon/mewtwo'
usa_req = requests.get(url_api)
usa_json = usa_req.json()

print(usa_json)