from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('automoveis/', include('automoveis.urls')),  # Incluir as URLs do app automoveis
    path('api/', include('api.urls')),  # Incluindo as URLs da API/
    
]