from django.urls import path
from . import views
from .views import iniciar_consulta, webhook_consulta

urlpatterns = [
    path('consulta-veiculos/', views.consulta_veiculos, name='consulta_veiculos'),
    path('filtrar-veiculos/', views.filtrar_veiculos, name='filtrar_veiculos'),
    path("webhook/", webhook_consulta, name="webhook_consulta"),
]

