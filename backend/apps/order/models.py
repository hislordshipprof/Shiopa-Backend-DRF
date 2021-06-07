from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.apps.account.models import User
from backend.apps.account.models import Address
from backend.apps.product.models import Product



class Coupon(models.Model):
    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")
        ordering = ("-created_at",)

    COUPON_TYPE = (
        ('percentage', 'Percentage'),
        ('amount', 'Amount'),
    )

    code = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255, choices=COUPON_TYPE)

    percentage = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    num_available = models.IntegerField(default=0)
    num_used = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Date Updadet"))

    def __str__(self):
        return f"{self.code}"


class Payment(models.Model):

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")
        ordering = ("-created_at",)

    PAYMENT_TYPE = (
        ('cash', 'CASH'),
        ('paypal', 'Paypal'),
        ('mastercard', 'Mastercard'),
    )

    user = models.ForeignKey(
        User,on_delete=models.SET_NULL, blank=True, null=True
    )
    amount = models.FloatField()
    payment_type = models.CharField(choices=PAYMENT_TYPE,max_length=255, default="cash",verbose_name=_("Payment Type"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Date Updadet"))

    def __str__(self):
        return f"{self.order.name}"


class Order(models.Model):

    STATUS_CHOICES = (
        ('ordered', 'Ordered'),
        ('shipped', 'Shipped'),
        ('arrived', 'Arrived'),
    )

    name = models.CharField(max_length=255)
    shipping_address = models.ForeignKey(
        Address,
        related_name="%(app_label)s_%(class)s_shipping_related",
        related_query_name="%(app_label)s_%(class)ss_shipping",
        on_delete=models.CASCADE
    )
    billing_address = models.ForeignKey(
        Address,
        related_name="%(app_label)s_%(class)s_billing_related",
        related_query_name="%(app_label)s_%(class)ss_billing",
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='ordered')

    payment = models.ForeignKey(
        Payment,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        Coupon,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        on_delete=models.SET_NULL, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    shipped_at = models.DateTimeField(blank=True, null=True)
    arrived_at = models.DateTimeField(blank=True, null=True)

    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Date Updadet"))

    def __str__(self):
        return f"{self.name}"


class OrderItem(models.Model):
    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
        ordering = ("pk",)

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Date Updadet"))

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


class Refund(models.Model):
    class Meta:
        verbose_name = _('Refund')
        verbose_name_plural = _('Refunds')
        ordering = ("pk",)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField(verbose_name=_("Reason of refund"))
    accepted = models.BooleanField(default=False,)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Date Updadet"))

    def __str__(self):
        return f"{self.pk}"


class UserOrder(Order):
    class Meta:
        verbose_name = _('User Order')
        verbose_name_plural = _('User Orders')
        ordering = ("pk",)

    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL)

class GuestOrder(Order):
    class Meta:
        verbose_name = _('Guest Order')
        verbose_name_plural = _('Guest Orders')
        ordering = ("pk",)