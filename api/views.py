# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from automoveis.models import Automovel
from .serializers import AutomovelSerializer  # Importe o serializer
import json

class FiltrarVeiculosView(APIView):
    def post(self, request):
        try:
            filtros = request.data  # Dados enviados no corpo da requisição

            marca = filtros.get('marca')
            ano = filtros.get('ano')
            combustivel = filtros.get('combustivel')
            filtrar_semelhantes = filtros.get('filtrarSemelhantes', False)

            # Construir a consulta com base nos filtros
            query = Automovel.objects.all()

            if marca:
                query = query.filter(marca__icontains=marca)
            if ano:
                query = query.filter(ano=ano)
            if combustivel:
                query = query.filter(combustivel__icontains=combustivel)

            # Filtrar semelhantes se necessário
            if filtrar_semelhantes:
                query = query.filter(tipo_veiculo__icontains="semelhante")  # Ajuste conforme a lógica

            # Se não encontrar resultados
            if not query.exists():
                response_data = {
                    "status": "sucesso",
                    "mensagem": "Nenhum veículo encontrado.",
                    "dados": []
                }
                return Response(response_data)

            # Se houver resultados, inclui os novos campos
            dados = AutomovelSerializer(query, many=True).data

            response_data = {
                "status": "sucesso",
                "mensagem": "Consulta realizada com sucesso.",
                "dados": dados
            }
            return Response(response_data)

        except Exception as e:
            error_message = str(e)
            response_data = {
                "status": "erro",
                "mensagem": error_message,
                "dados": []
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
