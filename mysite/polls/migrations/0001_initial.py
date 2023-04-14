# Generated by Django 4.1.2 on 2022-10-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=6)),
                ('modelo', models.CharField(max_length=400, null=True)),
                ('descripcion', models.TextField(max_length=200)),
                ('disponiible', models.IntegerField(null=True)),
                ('valor', models.IntegerField()),
            ],
        ),
    ]
