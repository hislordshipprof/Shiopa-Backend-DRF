# Generated by Django 3.2.4 on 2021-06-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_section'),
        ('product', '0004_alter_product_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(to='core.Image'),
        ),
    ]
