# Generated by Django 3.2.3 on 2021-06-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210608_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='currency',
            name='name',
            field=models.CharField(default='test', help_text='Currency name e.g Dollars, Naira', max_length=20),
            preserve_default=False,
        ),
    ]