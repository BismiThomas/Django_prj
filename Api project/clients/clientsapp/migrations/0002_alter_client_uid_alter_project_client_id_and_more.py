# Generated by Django 4.2.5 on 2023-09-28 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='client_id',
            field=models.ForeignKey(db_column='client_id', on_delete=django.db.models.deletion.CASCADE, to='clientsapp.client'),
        ),
        migrations.AlterField(
            model_name='project',
            name='user_id',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
