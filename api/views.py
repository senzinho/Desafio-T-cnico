from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from automoveis.models import Automovel
from .serializers import AutomovelSerializer
import json

class FiltrarVeiculosView(APIView):
    def post(self, request):
        try:
            filtros = request.data  # Dados enviados no corpo da requisição

            marca = filtros.get('marca')
            ano = filtros.get('ano')
            combustivel = filtros.get('combustivel')
            filtrar_semelhantes = filtros.get('filtrarSemelhantes', False)

            # Limpeza de filtros: removendo espaços e convertendo para minúsculas
            if marca:
                marca = marca.strip().lower()
            if combustivel:
                combustivel = combustivel.strip().lower()

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
                    "status": "informativo",  # Modificado para 'informativo' ao invés de 'sucesso'
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

    def get(self, request):
        try:
            # Obtendo filtros a partir da query string
            marca = request.GET.get('marca')
            ano = request.GET.get('ano')
            combustivel = request.GET.get('combustivel')
            filtrar_semelhantes = request.GET.get('filtrarSemelhantes', False)

            # Limpeza de filtros: removendo espaços e convertendo para minúsculas
            if marca:
                marca = marca.strip().lower()
            if combustivel:
                combustivel = combustivel.strip().lower()

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
                    "status": "informativo",  # Modificado para 'informativo'
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
