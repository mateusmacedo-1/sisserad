# Generated by Django 5.0.6 on 2024-06-04 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='previsao_finalizacao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='data_solicitação',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='previsao_finalizacao',
            field=models.DateField(),
        ),
    ]
