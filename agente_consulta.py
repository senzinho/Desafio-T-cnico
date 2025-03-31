import requests
import json

def main():
    print("Olá, sou seu agente virtual da MCP! Como posso ajudar? Você está em busca de quê ?")
    resposta_inicial = input("> ")

    # Verifica se o usuário está procurando um veículo
    if "veiculo" in resposta_inicial.lower() or "carro" in resposta_inicial.lower():
        print("\nÓtimo! Vamos buscar um veículo para você.")
        
        # Coleta dos filtros desejados
        marca = input("Informe a marca desejada (ou deixe em branco para qualquer): ").strip()
        modelo = input("Informe o modelo desejado (ou deixe em branco para qualquer): ").strip()
        ano_min = input("Informe o ano mínimo (ou deixe em branco para qualquer): ").strip()
        ano_max = input("Informe o ano máximo (ou deixe em branco para qualquer): ").strip()
        combustivel = input("Informe o tipo de combustível desejado (ou deixe em branco para qualquer): ").strip()
        preco_min = input("Informe o preço mínimo (ou deixe em branco para qualquer): ").strip()
        preco_max = input("Informe o preço máximo (ou deixe em branco para qualquer): ").strip()

        # Monta o dicionário de filtros
        filtros = {}
        if marca:
            filtros["marca"] = marca
        if modelo:
            filtros["modelo"] = modelo
        if ano_min:
            try:
                filtros["ano_min"] = int(ano_min)
            except ValueError:
                print("Valor inválido para ano mínimo. Ignorando filtro.")
        if ano_max:
            try:
                filtros["ano_max"] = int(ano_max)
            except ValueError:
                print("Valor inválido para ano máximo. Ignorando filtro.")
        if combustivel:
            filtros["combustivel"] = combustivel
        if preco_min:
            try:
                filtros["preco_min"] = float(preco_min)
            except ValueError:
                print("Valor inválido para preço mínimo. Ignorando filtro.")
        if preco_max:
            try:
                filtros["preco_max"] = float(preco_max)
            except ValueError:
                print("Valor inválido para preço máximo. Ignorando filtro.")

        # Exibe os filtros coletados para confirmação
        print("\nFiltros de busca informados:")
        print(json.dumps(filtros, indent=4, ensure_ascii=False))

        # Envia os dados para o servidor MCP
        print("\nEnviando filtros para o servidor MCP...")
        url = "http://127.0.0.1:5000/api/filtrar-veiculos/"
        try:
            # Caso tenha problema com proxy, desabilita
            proxies = {"http": None, "https": None}
            response = requests.post(url, json=filtros, proxies=proxies)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "sucesso":
                    veiculos = data.get("dados", [])
                    if veiculos:
                        print("\nAchei os seguintes veículos compatíveis com sua busca:")
                        print("-" * 40)
                        for v in veiculos:
                            print(f"Marca: {v.get('marca')}")
                            print(f"Modelo: {v.get('modelo')}")
                            print(f"Ano: {v.get('ano')}")
                            print(f"Cor: {v.get('cor')}")
                            print(f"Quilometragem: {v.get('quilometragem')} km")
                            print(f"Preço: R$ {v.get('preco')}")
                            print("-" * 40)
                    else:
                        print("Não foram encontrados veículos com os filtros informados.")
                else:
                    print("Erro na resposta do servidor:", data.get("mensagem"))
            else:
                print("Erro na requisição. Código de status:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Erro ao fazer a requisição:", e)
    else:
        print("Desculpe, neste momento só posso ajudar na busca por veículos.")

if __name__ == "__main__":
    main()
