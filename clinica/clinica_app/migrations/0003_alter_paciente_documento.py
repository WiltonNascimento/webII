# Generated by Django 5.1.2 on 2024-12-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica_app', '0002_consulta_observacoes_medico_crm_medico_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='documento',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
    ]
