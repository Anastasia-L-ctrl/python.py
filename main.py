import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '822e8149e9407def35ad6f621b2da961'
HEADER = {"Content-Type":"application/json", "trainer_token":TOKEN} 
#body_create = {
    #"name": "Лабубу",
    #"photo_id": 909
#}

#response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
#print(response_create.text)

#message = response_create.json()['message']
#print(message)

#body_update = {

    #"pokemon_id": "342797",
    #"name": "Nectar",
    #"photo_id": 909
#}

#response_update=requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_update)
#print(response_update.json())

body_catch = {
    "pokemon_id": "342797"
}
response_catch=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_catch)
print(response_catch.json())