"""
test api
"""
import requests

#создание покемона

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '19b6d91565ec3a49c2f5b528026139a0'}

bodyadd = {
    "name": "Bus", 
    "photo": "https://dolnikov.ru/pokemons/albums/125.png"
}

response = requests.post(url=f'{URL}/pokemons', json=bodyadd, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Cообщение: {response.text}')
response_json = response.json()


#изменить имя покемона

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '19b6d91565ec3a49c2f5b528026139a0'}

bodyadd = {
    "pokemon_id": "159",
    "name": "Bulba",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png" 
}

response = requests.put(url=f'{URL}/pokemons', json=bodyadd, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Cообщение: {response.text}')
response_json = response.json()


#поймать покемона в пакебол
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '19b6d91565ec3a49c2f5b528026139a0'}

bodyadd = {
    "pokemon_id": "159"  
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=bodyadd, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Cообщение: {response.text}')
response_json = response.json()