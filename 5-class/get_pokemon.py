
# Import the requests library to make HTTP requests
import requests

# Define a function to get information about a Pokémon by its ID
def get_pokemon_info(pokemon_id):
    # Construct the API URL using the provided Pokémon ID
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    
    # Make a GET request to the API
    response = requests.get(api_url)

    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        # Convert the response JSON data into a Python dictionary
        pokemon_data = response.json()
        return pokemon_data
    else:
        # If the response status code is not 200, print an error message
        print(f"Failed to retrieve data for Pokemon with ID {pokemon_id}")
        return None

# Main program
if __name__ == "__main__":
    # Prompt the user to enter the ID of the Pokémon
    pokemon_id = input("Enter the ID of the Pokémon: ")
    
    # Call the function to get information about the specified Pokémon
    pokemon_info = get_pokemon_info(pokemon_id)

    # Check if the function returned valid information
    if pokemon_info:
        # Print the retrieved Pokémon information
        print("Pokemon Information:")
        print(f"Name: {pokemon_info['name'].capitalize()}")
        print(f"Height: {pokemon_info['height']}")
        print(f"Weight: {pokemon_info['weight']}")
        print("Abilities:")
        # Loop through each ability of the Pokémon and print its name
        for ability in pokemon_info['abilities']:
            print(f"- {ability['ability']['name'].capitalize()}")

'''
import requests

from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)

pokemon = response.json()
pprint(pokemon)
'''
'''
Esse código em Python utiliza a biblioteca requests para fazer uma requisição HTTP à API do Pokémon. 

import requests: Isso importa a biblioteca requests, que é utilizada para fazer requisições
HTTP em Python.

from pprint import pprint: Isso importa a função pprint da biblioteca pprint, 
que permite imprimir objetos de forma mais legível, especialmente dicionários.

pokemon_number = input("What is the Pokemon's ID? "): Isso solicita ao usuário que
insira o ID de um Pokémon. O ID é uma forma única de identificar cada Pokémon na API.

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number): Isso cria uma URL para fazer
uma requisição à API do Pokémon, preenchendo o espaço reservado {} na URL com o número do Pokémon fornecido pelo usuário.

response = requests.get(url): Isso envia uma solicitação GET para a URL da API do Pokémon que você construiu.

print(response): Isso imprime o objeto de resposta da requisição. Pode ser útil 
para depurar, mas normalmente não é necessário para a saída final.

pokemon = response.json(): Isso converte os dados da resposta da API em um 
formato JSON e armazena no objeto pokemon.

pprint(pokemon): Isso utiliza a função pprint para imprimir o objeto pokemon de forma 
mais organizada e legível.


'''