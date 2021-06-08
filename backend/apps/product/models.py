from django.utils import timezone
from django.conf import settings
from django.db import models
from django.db.models import TextField
from mptt.managers import TreeManager
from mptt.models import MPTTModel
from versatileimagefield.fields import VersatileImageField
from django.utils.translation import gettext_lazy as _

from backend.apps.account.models import User


class Category(MPTTModel):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    image = VersatileImageField(
        upload_to="category-backgrounds", blank=True, null=True
    )
    image_alt = models.CharField(max_length=128, blank=True)

    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    objects = models.Manager()
    tree = TreeManager()

    class Meta:
        verbose_name_plural ='Categories'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    description = TextField(blank=True)
    additional_info = TextField(blank=True)
    section = models.CharField(max_length=255)

    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    stock = models.IntegerField(null=True, blank=True, default=0)
    available_for_purchase = models.DateField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=settings.DEFAULT_MAX_DIGITS,
        decimal_places=settings.DEFAULT_DECIMAL_PLACES,
        blank=True,
        null=True,
    )
    # currency = models.CharField(max_length=settings.DEFAULT_CURRENCY_CODE_LENGTH)


    rating = models.FloatField(null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        app_label = "product"
        ordering = ("slug",)


    def __repr__(self) -> str:
        class_ = type(self)
        return "<%s.%s(pk=%r, name=%r)>" % (
            class_.__module__,
            class_.__name__,
            self.pk,
            self.name,
        )

    def __str__(self) -> str:
        return self.name


class ProductMedia(models.Model):
    product = models.ForeignKey(Product, related_name="media", on_delete=models.CASCADE)
    image = VersatileImageField(
        upload_to="products", ppoi_field="ppoi", blank=True, null=True
    )

    alt = models.CharField(max_length=128, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("pk",)
        app_label = "product"

    def get_media_queryset(self):
        return self.product.media.all()


class ProductReview(models.Model):

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Product Reviews")
        ordering = ("-created_at",)

    SCALE = (
        (1, _('1/5')),
        (2, _('2/5')),
        (3, _('3/5')),
        (4, _('4/5')),
        (5, _('5/5')),
    )

    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name= _("Name"))
    comment = models.CharField(max_length=255,blank=True, null=True, verbose_name=_("Comment"))
    stars = models.IntegerField(choices=SCALE, verbose_name=_("Rating on five stars"))
    created_at = models.DateTimeField(default=timezone.now, editable=False, verbose_name=_("Date Created"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Date Updadet"))

    def __str__(self):
        return self.stars
