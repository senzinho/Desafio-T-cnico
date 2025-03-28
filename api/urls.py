from django.urls import path
from .views import FiltrarVeiculosView

urlpatterns = [
    path('filtrar-veiculos/', FiltrarVeiculosView.as_view(), name='filtrar-veiculos'),
]