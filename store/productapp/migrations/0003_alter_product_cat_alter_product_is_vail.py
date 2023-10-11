# Generated by Django 4.2.4 on 2023-10-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_alter_product_cat_alter_product_is_vail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Mobile'), (2, 'Shoes'), (3, 'clothes')], verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_vail',
            field=models.BooleanField(choices=[(0, 'no'), (1, 'yes')], verbose_name='Is_available'),
        ),
    ]
