from django.db import models
from django.conf import settings
from django.db.models.fields import NullBooleanField
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class Settings(models.Model):
    # Basic store settings
    store_name = models.CharField(max_length=255)
    store_tagline = models.CharField(
        max_length=500, help_text="This is the tagline of the store. Optional!")
    store_logo = models.ImageField(upload_to='settings', storage=gd_storage)
    favicon = models.ImageField(
        upload_to="settings", storage=gd_storage,help_text="This is the icon that would be shown on the title bar of the browser", null=True, blank=True)

    # Contact settings
    store_phone_number = models.CharField(
        max_length=20, help_text="The contact phone number for the store")
    store_email = models.CharField(
        max_length=80, help_text="The contact email of the store")
    store_address = models.TextField(
        null=True, help_text="The address the store is located at")
    copyright_text = models.CharField(
        max_length=500, help_text="This is the copyright text that would be shown in the footer of your store",
        null=True, blank=True)

    # Social Settings
    facebook_url = models.CharField(
        max_length=500, null=True, help_text="The link to the facebook account of the store")
    instagram_url = models.CharField(
        max_length=500, null=True, help_text="The link to the facebook account of the store")
    twitter_url = models.CharField(
        max_length=500, null=True, help_text="The link to the facebook account of the store")

    # Seo Settings
    meta_description = models.TextField(
        null=True, blank=True, help_text="This is the description of the store that would be showm on search engines")
    keywords = models.CharField(max_length=500, null=True, blank=True,
                                help_text="This are the keywords that relaes with the store and it should be seperated be commas e.g clothes, summer, trouser")

    def logo_url(self):
        """
        This method returns the url of the logo
        """
        return self.store_logo.url

    def favicon_url(self):
        """
        This method returns the url of the favicon
        """
        return self.favicon.url

    class Meta:
        verbose_name_plural = 'Store Settings'


class Currency(models.Model):
    POSITION_CHOICES = (
        ('right', 'Right'),
        ('left', 'Left'),
    )
    
    code = models.CharField(max_length=5, help_text='The code that represents the currency e.g NGN, USD')
    exchange_rate = models.DecimalField(decimal_places=2, max_digits=19, help_text='The rate of the currency compared to USD')
    symbol = models.CharField(max_length=3, null=True, blank=True, help_text='Optional. The sign that represents the currency e.g $, If not specified the currency code would be used instead.')
    position = models.CharField(max_length=8, choices=POSITION_CHOICES, null=True, blank=True, default='left', help_text='Optional. Where is the currency symbol placed? Default is left')

    class Meta:
        verbose_name_plural = 'Currencies'

    def __str__(self) -> str:
        return self.code

class Country(models.Model):
    name = models.CharField(max_length=100, help_text='The name of the country')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, help_text='What currency do they use in this country')
    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self) -> str:
        return self.name