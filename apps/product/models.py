from django.db import models
from django.conf import Settings, settings


class Category(models.Model):
    """
    This model defines the category table in the database
    """
    name = models.CharField(
        max_length=255, help_text="The name of the category")
    slug = models.SlugField(
        max_length=255, help_text="This is the slug field of the category. It would be appended to the url e.g \"https://www.example.com/categories/category-slug\"")
    image = models.ImageField(
        upload_to="images", help_text="This is the image that represents this category.")
    image_alt = models.CharField(
        max_length=500, help_text="This would show whenever the image refuses to display", blank=True, null=True)

    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        """
        This is the string representation of this category
        """
        return self.name

    def get_absolute_url(self):
        """
        This method returns the url to get the product
        """
        return f'/{self.slug}/'

    def image_url(self):
        """
        This method returns the url of the image
        """
        # Check if setting is on debug mode.
        if settings.DEBUG:
            return "http://127.0.0.1"+self.image.url
        else:
            return self.image.url

    class Meta:
        verbose_name_plural = 'Categories'
