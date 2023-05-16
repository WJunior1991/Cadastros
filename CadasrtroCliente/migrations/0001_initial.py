# Generated by Django 4.2 on 2023-04-19 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('matricula', models.IntegerField()),
                ('renda_mensal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Ativo', models.BooleanField()),
            ],
        ),
    ]
