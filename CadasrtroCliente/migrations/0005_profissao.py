# Generated by Django 4.2 on 2023-04-24 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadasrtroCliente', '0004_alter_cliente_estado_civil_alter_cliente_nro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
    ]
