import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status() #Lança erro se status_code >= 400
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado")
        else:
            print(f"CEP: {dados['cep']}")
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    except requests.exceptions.RequestException as erro:
        print(f"Erro ao consultar o CEP: {erro}")


consultar_cep("53220-375")