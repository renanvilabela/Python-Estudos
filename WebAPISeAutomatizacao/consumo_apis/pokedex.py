import requests

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"\nome: {dados['name'].capitalize}")
        print(f"ID: {dados['id']}")
        print(f"Altura: {dados['height'] / 10} m")
        print(f"Peso: {dados['weight'] / 10} kg")

        tipos = [tipo['type']['name'] for tipo in dados['types']]
        print(f"Tipo(s): {', '.join(tipos)}")

        print(f"Imagem: {dados['sprites']['front_default']}")
    else:
        print("Pokémon não encontrado. Verifique o nome ou ID.")

nome_pokemon = input("Digite o nome ou número do Pokémon: ")
buscar_pokemon(nome_pokemon)
    