import requests
import json

token = 'c8f6b12e1a3cca909d323c4c937eac40'


born = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "name": "Джигглипафф",
    "photo": "https://avatanplus.com/files/resources/original/57ebd8c6b583d1577146c857.png"
})

print(born.json)

renaming = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": 2289,
    "name": "Гастли",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/c/ca/092Gastly.png/revision/latest?cb=20140328204633"
})

print(renaming.json)

pokeball = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token': token}, json={
    "pokemon_id": 2288
})

print(pokeball.json)