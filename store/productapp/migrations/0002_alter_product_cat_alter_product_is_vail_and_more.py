# Generated by Django 4.2.4 on 2023-10-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_vail',
            field=models.BooleanField(verbose_name='Is_available'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Price(per qty)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
    ]