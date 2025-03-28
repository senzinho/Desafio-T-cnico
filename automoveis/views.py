from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
import json
from .models import Automovel

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
