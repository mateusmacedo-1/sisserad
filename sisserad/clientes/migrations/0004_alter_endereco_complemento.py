# Generated by Django 5.0.6 on 2024-06-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_cliente_documento_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
