# Generated by Django 4.2 on 2023-04-24 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadasrtroCliente', '0003_cliente_estado_civil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado_civil',
            field=models.CharField(choices=[('Sol', 'Solteiro(a)'), ('Cas', 'Casado(a)'), ('Div', 'Divorciado(a)'), ('Viu', 'Viuvo(a)')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nro',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
