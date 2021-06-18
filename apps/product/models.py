from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.conf import settings

# Get the section and image models from the core app
from apps.core.models import Image, Section


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


class Product(models.Model):
    """
    This model defines the product table in the database.
    """
    # Basic Informations
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

    # Price
    price = models.DecimalField(max_digits=19, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=19, decimal_places=2, null=True, blank=True)

    # Images
    main_image = models.ImageField(
        upload_to='images', help_text="This is the default image of the product... It would be prioritized over other images")
    thumbnail = models.ImageField(
        upload_to="thumbnail", help_text="This is the smaller version of the main image. It would be autogenerated",
        null=True, blank=True)
    images = models.ManyToManyField(Image)

    # Stock
    sku = models.CharField(max_length=255, null=True, blank=True)
    available_to_purchase = models.BooleanField(default=True)

    # Dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Relationships
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='products')
    section = models.ManyToManyField(
        Section, related_name='products')

    def __str__(self):
        """
        String Representation of this model
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url of the product in format
        /category-slug/product-slug/
        """
        return f'/{self.category.slug}/{self.slug}/'

    def main_image_url(self):
        """
        This method returns the url of the main image
        """
        # Check if setting is on debug mode.
        if settings.DEBUG:
            return "http://127.0.0.1"+self.main_image.url
        else:
            return self.main_image.url

    def get_thumbnail(self):
        if self.thumbnail:
            # Check if setting is on debug mode.
            if settings.DEBUG:
                return "http://127.0.0.1"+self.thumbnail.url
            else:
                return self.thumbnail.url
        else:
            self.thumbnail = self.make_thumbnail(self.main_image)
            self.save()

    def make_thumbnail(self, image, size=[300, 200]):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
