# Generated by Django 5.0.6 on 2024-06-05 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0005_remove_servico_revisado_por_atividade_revisado_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='procurar_por',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='servico',
            name='solicitado_por',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
