import requests

# URL da API
url = "http://127.0.0.1:9000/api/filtrar-veiculos/"

# Dados a serem enviados no corpo da requisição POST
# Altere os dados conforme necessário para a sua API
payload = {
    "marca": "",  # Exemplo de parâmetro
    "ano": "2000",  # Exemplo de parâmetro
}

# Realiza a requisição POST para a API
response = requests.post(url, data=payload)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Se a resposta for bem-sucedida, extrai os dados
    dados = response.json()

    # Exibe a mensagem de sucesso e os dados
    print(dados["mensagem"])
    for veiculo in dados["dados"]:
        print(f"ID: {veiculo['id']}")
        print(f"Marca: {veiculo['marca']}")
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Ano: {veiculo['ano']}")
        print(f"Cor: {veiculo['cor']}")
        print(f"Quilometragem: {veiculo['quilometragem']}")
        print(f"Motorização: {veiculo['motorizacao']}")
        print(f"Combustível: {veiculo['combustivel']}")
        print(f"Preço: {veiculo['preco']}")
        print("-" * 40)
else:
    # Caso ocorra algum erro na requisição, exibe o status code
    print(f"Erro na requisição: {response.status_code}")
