# automoveis/views.py
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Automovel

def consulta_veiculos(request):
    if request.method == 'GET':
        # Renderiza a página de consulta
        return render(request, 'automoveis/consulta_veiculos.html')
    
    if request.method == 'POST':
        try:
            # Obter os dados do corpo da requisição (critério de filtro)
            dados = json.loads(request.body)
            marca = dados.get('marca')
            ano = dados.get('ano')
            tipo_combustivel = dados.get('combustivel')  # Corrigido o nome do campo

            # Consultar o banco de dados com base nos filtros
            automovel = Automovel.objects.all()

            if marca:
                automovel = automovel.filter(marca=marca)
            if ano:
                automovel = automovel.filter(ano=ano)
            if tipo_combustivel:
                automovel = automovel.filter(combustivel=tipo_combustivel)

            # Preparar a resposta com os dados dos veículos encontrados
            resultado = list(automovel.values())  # Converte os resultados para lista de dicionários
            return JsonResponse({'status': 'sucesso', 'dados': resultado}, safe=False)
        except Exception as e:
            return JsonResponse({'status': 'erro', 'mensagem': str(e)}, status=400)
