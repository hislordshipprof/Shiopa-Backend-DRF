from django.db import models
from django.conf import settings
from django.db.models.fields import NullBooleanField


class Settings(models.Model):
    # Basic store settings
    store_name = models.CharField(max_length=255)
    store_tagline = models.CharField(
        max_length=500, help_text="This is the tagline of the store. Optional!")
    store_logo = models.ImageField(upload_to='settings')
    favicon = models.ImageField(
        upload_to="settings", help_text="This is the icon that would be shown on the title bar of the browser", null=True, blank=True)

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
        # Check if setting is on debug mode.
        if settings.DEBUG:
            return "http://127.0.0.1"+self.store_logo.url
        else:
            return self.store_logo.url

    def favicon_url(self):
        """
        This method returns the url of the favicon
        """
        # Check if setting is on debug mode.
        if settings.DEBUG:
            return "http://127.0.0.1"+self.favicon.url
        else:
            return self.favicon.url

    class Meta:
        verbose_name_plural = 'Store Settings'
