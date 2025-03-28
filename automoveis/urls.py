from django.urls import path
from . import views

urlpatterns = [
    path('consulta-veiculos/', views.consulta_veiculos, name='consulta_veiculos'),
]