# Generated by Django 4.2.7 on 2023-11-21 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investimeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Investimeto', models.TextField(max_length=255)),
                ('valor', models.FloatField()),
                ('pago', models.BooleanField(default=False)),
                ('data', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
