# Generated by Django 5.0.6 on 2024-06-07 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0008_alter_atividade_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atividade',
            options={'permissions': (('pode_revisar', 'Pode revisar uma atividade'), ('pode_publicar', 'Pode publicar uma atividade'), ('pode_visualizar_planilha', 'Permite visualizar a planilha de atividades.'), ('pode_visualizar_laudo', 'Permite visualizar o laudo da atividades.'), ('pode_cancelar_atividade', 'Permite cancelar a atividade.'), ('pode_gerar_retorno', 'Permite gerar atividade de retorno.'), ('pode_abrir', 'Permite abrir uma atividade.'))},
        ),
    ]
