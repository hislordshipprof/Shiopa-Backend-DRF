"""
This models define the global level database tables.
The tables in this files are not dependent on any apps
of this project.
"""
from django.db import models
from django.conf import settings


class Image(models.Model):
    """
    This model defines the image table in the database.
    """
    title = models.CharField(
        max_length=255, help_text="The title of the image")
    alt_text = models.CharField(
        max_length=255, null=True, blank=True,
        help_text="This would show whenever the image refuses to show")
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title

    def image_url(self):
        """
        This method returns the url of the image
        """
        # Check if setting is on debug mode.
        if settings.DEBUG:
            return "http://127.0.0.1"+self.image.url
        else:
            return self.image.url


class Section(models.Model):
    """
    This model defines the section table in the database.
    """
    title = models.CharField(max_length=255)
    image = models.ForeignKey(
        Image, on_delete=models.SET_NULL, null=True, blank=True)
    ordering = models.IntegerField()

    class Meta:
        ordering = ('ordering',)

    def image_url(self):
        """
        This method returns the url of the image
        """
        image_url = self.image.image_url()
        # Check if setting is on debug mode.
        if settings.DEBUG:
            return image_url

    def __str__(self):
        return self.title
