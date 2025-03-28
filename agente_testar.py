import requests
import json

def agente_virtual():
    print("Olá! Sou seu assistente virtual de veículos. Como posso te ajudar hoje?")
    resposta = input("Você está procurando um veículo? (sim/não): ").strip().lower()
    
    if resposta != "sim":
        print("Tudo bem! Se precisar, estou à disposição.")
        return
    
    filtros = coletar_filtros()
    print("\n🚀 Filtros coletados:", filtros)  # Debug

    veiculos = buscar_veiculos(filtros)
    
    if veiculos is None:
        print("\n❌ Erro ao buscar veículos. Verifique a API.")
    else:
        exibir_resultados(veiculos)

def coletar_filtros():
    print("Ótimo! Vou precisar de algumas informações para encontrar o veículo ideal para você.")
    marca = input("Digite a marca desejada (ou deixe em branco para qualquer marca): ").strip()
    modelo = input("Digite o modelo desejado (ou deixe em branco para qualquer modelo): ").strip()
    ano = input("Ano (ou deixe em branco): ").strip()
    combustivel = input("Tipo de combustível (ou deixe em branco para qualquer um): ").strip()
    
    filtros = {}
    if marca: filtros["marca"] = marca
    if modelo: filtros["modelo"] = modelo
    if ano: filtros["ano"] = ano
    if combustivel: filtros["combustivel"] = combustivel
    
    return filtros

def buscar_veiculos(filtros):
    url = "http://127.0.0.1:8000/automoveis/filtrar-veiculos/"  # URL da API
    
    print("\n🔎 Enviando requisição para a API...")
    print(f"📡 URL: {url}")
    print(f"📨 Payload enviado: {json.dumps(filtros, indent=2)}")

    headers = {"Content-Type": "application/json"}  # Adicionando o cabeçalho
    
    try:
        response = requests.post(url, json=filtros, headers=headers)  # Incluindo o cabeçalho

        print(f"\n✅ Status da resposta: {response.status_code}")
        print(f"📥 Resposta da API: {response.text}")

        response.raise_for_status()  # Lança um erro se a resposta for inválida
        
        return response.json().get("dados", [])
    
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Erro ao buscar veículos: {e}")
        return None


def exibir_resultados(veiculos):
    if not veiculos:
        print("Nenhum veículo encontrado com os critérios fornecidos.")
        return
    
    print("Aqui estão os veículos encontrados:")
    for v in veiculos:
        print("-" * 50)
        print(f"Marca: {v.get('marca', 'Desconhecido')}")
        print(f"Modelo: {v.get('modelo', 'Desconhecido')}")
        print(f"Ano: {v.get('ano', 'Desconhecido')}")
        print(f"Cor: {v.get('cor', 'Desconhecido')}")
        print(f"Quilometragem: {v.get('quilometragem', 'Desconhecido')} km")
        print(f"Preço: R$ {v.get('preco', 'Desconhecido')}")
        print("-" * 50)

if __name__ == "__main__":
    agente_virtual()
