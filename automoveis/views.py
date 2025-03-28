from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
import json
from .models import Automovel


import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Simula uma API externa que processa a consulta
API_URL = "http://localhost:8000/automoveis/consulta-veiculos/"
CALLBACK_URL = "http://localhost:8000/automoveis/webhook/"  # Webhook do seu Django

def iniciar_consulta(request):
    if request.method == "POST":
        data = request.POST  # Pegando os dados do formulário
        marca = data.get('marca', '')
        ano = data.get('ano', '')
        combustivel = data.get('combustivel', '')

        # Enviando para a API externa e informando o callback URL
        response = requests.post(API_URL, json={
            "marca": marca,
            "ano": ano,
            "combustivel": combustivel,
            "callback_url": CALLBACK_URL  # URL para receber a resposta
        })

        if response.status_code == 202:
            return JsonResponse({"status": "pendente", "message": "Consulta enviada. Aguarde o retorno via webhook."})
        else:
            return JsonResponse({"error": "Erro ao enviar consulta para a API."}, status=400)

    return JsonResponse({"error": "Método não permitido"}, status=405)


def consulta_veiculos(request):
    if request.method == "GET":
        return render(request, "automoveis/consulta_veiculos.html")  # Garante que a página abre corretamente
    
    elif request.method == "POST":
        data = json.loads(request.body)
        marca = data.get("marca", "").strip()
        ano = data.get("ano", "").strip()
        combustivel = data.get("combustivel", "").strip()
        filtrar_semelhantes = data.get("filtrarSemelhantes", False)

        filtros = Q()
        if filtrar_semelhantes:
            if marca:
                filtros |= Q(marca__iexact=marca)
            if ano:
                filtros |= Q(ano=ano)
            if combustivel:
                filtros |= Q(combustivel__icontains=combustivel)
        else:
            if marca:
                filtros &= Q(marca__iexact=marca)
            if ano:
                filtros &= Q(ano=ano)
            if combustivel:
                filtros &= Q(combustivel__icontains=combustivel)

        veiculos = Automovel.objects.filter(filtros).values()
        return JsonResponse({"status": "sucesso", "dados": list(veiculos)})

    return JsonResponse({"status": "erro", "mensagem": "Método inválido"}, status=400)


@csrf_exempt
def webhook_consulta(request):
    if request.method == "POST":
        data = request.POST  # Ou request.body para JSON
        veiculos = data.get("veiculos", [])

        # Salvar no banco de dados (simulando)
        for veiculo in veiculos:
            print(f"Veículo recebido: {veiculo}")  # Aqui você salvaria no banco

        return JsonResponse({"message": "Dados recebidos com sucesso!"}, status=200)

    return JsonResponse({"error": "Método não permitido"}, status=405)
