# Generated by Django 3.2.4 on 2021-06-23 09:36

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='favicon',
            field=models.ImageField(blank=True, help_text='This is the icon that would be shown on the title bar of the browser', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='settings'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='store_logo',
            field=models.ImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='settings'),
        ),
    ]
