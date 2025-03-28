
from rest_framework import serializers
from automoveis.models import Automovel  # Importe o modelo Automovel

class AutomovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovel
        fields = ['id', 'marca', 'modelo', 'ano', 'cor', 'quilometragem', 'motorizacao', 'combustivel', 'preco']
