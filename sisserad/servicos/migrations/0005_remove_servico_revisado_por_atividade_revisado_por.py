# Generated by Django 5.0.6 on 2024-06-05 21:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0004_servico_revisado_por'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='revisado_por',
        ),
        migrations.AddField(
            model_name='atividade',
            name='revisado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='revisado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]