# Generated by Django 5.1.7 on 2025-03-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('motorizacao', models.CharField(max_length=100)),
                ('combustivel', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=50)),
                ('quilometragem', models.FloatField()),
                ('portas', models.IntegerField()),
                ('transmissao', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
