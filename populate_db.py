import os
import django
from faker import Faker

# Ajustar o caminho para o settings.py do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')  
django.setup()

# Agora você pode importar o modelo Automovel
from automoveis.models import Automovel

# Instanciar o Faker
fake = Faker()

# Função para gerar e popular o banco com 100 veículos
def populate_automoveis():
    for _ in range(100):
        automovel = Automovel(
            marca=fake.company(),
            modelo=fake.word(),
            ano=fake.year(),
            motorizacao=f"{fake.random_int(min=1, max=3)}.{fake.random_int(min=0, max=9)}L {fake.random_int(min=8, max=16)}V",
            combustivel=fake.random_element(elements=("Gasolina", "Álcool", "Flex", "Diesel", "Elétrico")),
            cor=fake.color_name(),
            quilometragem=fake.random_int(min=1000, max=200000),
            portas=fake.random_int(min=2, max=5),
            transmissao=fake.random_element(elements=("Manual", "Automática", "CVT")),
            preco=fake.random_number(digits=5),
        )
        automovel.save()
        print(f"Automóvel {automovel} criado com sucesso!")

# Chamar a função
populate_automoveis()
