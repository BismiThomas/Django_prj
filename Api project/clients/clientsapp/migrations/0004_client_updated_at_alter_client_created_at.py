# Generated by Django 4.2.5 on 2023-09-29 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientsapp', '0003_client_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 29, 14, 11, 57, 274155)),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 29, 14, 11, 57, 274155)),
        ),
    ]
