# Generated by Django 4.2.7 on 2023-12-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=60)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Empleado',
            },
        ),
    ]
