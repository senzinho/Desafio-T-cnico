from django.db import models

class Automovel(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    motorizacao = models.CharField(max_length=100)
    combustivel = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    quilometragem = models.PositiveIntegerField()
    portas = models.PositiveIntegerField()
    transmissao = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ano} {self.marca} {self.modelo}"
