from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from automoveis.models import Automovel
from .serializers import AutomovelSerializer

class FiltrarVeiculosView(APIView):
    def post(self, request):
        try:
            filtros = request.data  # Obtém os filtros da requisição
            filtros_limpados = {k: v.strip().lower() for k, v in filtros.items() if v}  # Remove espaços e padroniza

            # Construir a consulta dinamicamente
            filtros_q = Q()
            
            if 'marca' in filtros_limpados:
                filtros_q &= Q(marca__icontains=filtros_limpados['marca'])
            
            # Tratar o filtro de ano como inteiro
            if 'ano' in filtros:
                try:
                    ano = int(filtros['ano'])
                    filtros_q &= Q(ano=ano)  # Aplica filtro para ano como inteiro
                except ValueError:
                    return Response({"status": "erro", "mensagem": "Ano inválido.", "dados": []}, status=status.HTTP_400_BAD_REQUEST)
            
            if 'combustivel' in filtros_limpados:
                filtros_q &= Q(combustivel__icontains=filtros_limpados['combustivel'])
            
            # Filtro de "filtrarSemelhantes"
            if filtros.get('filtrarSemelhantes', False):
                filtros_q &= Q(tipo_veiculo__icontains="semelhante")

            # Executar a consulta em uma única chamada ao banco
            query = Automovel.objects.filter(filtros_q).only('id', 'marca', 'ano', 'combustivel', 'cor', 'quilometragem', 'preco')

            # Verifica se há resultados
            if not query.exists():
                return Response({"status": "informativo", "mensagem": "Nenhum veículo encontrado.", "dados": []})

            # Serializa os dados
            dados = AutomovelSerializer(query, many=True).data
            return Response({"status": "sucesso", "mensagem": "Consulta realizada com sucesso.", "dados": dados})

        except Exception as e:
            return Response({"status": "erro", "mensagem": f"Erro inesperado: {str(e)}", "dados": []}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            # Mesmo tratamento da função POST, mas lendo de `request.GET`
            filtros = request.GET.dict()  # Convertendo para dicionário comum
            filtros_limpados = {k: v.strip().lower() for k, v in filtros.items() if v}

            filtros_q = Q()
            
            if 'marca' in filtros_limpados:
                filtros_q &= Q(marca__icontains=filtros_limpados['marca'])
            
            # Tratar o filtro de ano como inteiro
            if 'ano' in filtros:
                try:
                    ano = int(filtros['ano'])
                    filtros_q &= Q(ano=ano)  # Aplica filtro para ano como inteiro
                except ValueError:
                    return Response({"status": "erro", "mensagem": "Ano inválido.", "dados": []}, status=status.HTTP_400_BAD_REQUEST)
            
            if 'combustivel' in filtros_limpados:
                filtros_q &= Q(combustivel__icontains=filtros_limpados['combustivel'])
            
            if filtros.get('filtrarSemelhantes', False):
                filtros_q &= Q(tipo_veiculo__icontains="semelhante")

            # Executar a consulta em uma única chamada ao banco
            query = Automovel.objects.filter(filtros_q).only('id', 'marca', 'ano', 'combustivel', 'cor', 'quilometragem', 'preco')

            if not query.exists():
                return Response({"status": "informativo", "mensagem": "Nenhum veículo encontrado.", "dados": []})

            dados = AutomovelSerializer(query, many=True).data
            return Response({"status": "sucesso", "mensagem": "Consulta realizada com sucesso.", "dados": dados})

        except Exception as e:
            return Response({"status": "erro", "mensagem": f"Erro inesperado: {str(e)}", "dados": []}, status=status.HTTP_400_BAD_REQUEST)
