import requests

API_KEY = "6229a9369f0851b281b57425b8ac889d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def buscar_clima(cidade):
    parametros = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    resposta = requests.get(BASE_URL, params=parametros)

    if resposta.status_code == 200:
        dados = resposta.json()

        nome_cidade = dados["name"]
        temperatura = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        umidade = dados["main"]["humidity"]
        vento = dados["wind"]["speed"]

        print(f"\nClima em {nome_cidade}")
        print(f"temperatura: {temperatura}°C")
        print(f"Condição: {descricao.capitalize()}")
        print(f"Umidade: {umidade}%")
        print(f"Vento: {vento} m/s")

    elif resposta.status_code == 404:
        print("Cidade não encontrada.")
    else:
        print("Erro ao buscar dados do clima.")

cidade_input = input("Digite o nome da cidade: ")
buscar_clima(cidade_input)