# Generated by Django 4.1.6 on 2023-02-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosAPI',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.DecimalField(decimal_places=3, max_digits=5, primary_key=True, serialize=False)),
                ('componente', models.TextField(max_length=10)),
                ('valor', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]
