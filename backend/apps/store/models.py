from django.db import models


class Currency(models.Model):
    """
    This model contains the lists of currencies for the store
    """
    POSITION_CHOICES = (
        ('r', 'RIGHT'),
        ('l', 'LEFT')
    )
    name = models.CharField(max_length=20, help_text="Currency name e.g Dollars, Naira")
    code = models.CharField(max_length=255, help_text="e.g USD, NGN")
    symbol = models.CharField(max_length=5, null=True, blank=True,
                              help_text="Optional. This is the symbol of the currency e.g $")
    position = models.CharField(max_length=5, choices=POSITION_CHOICES)
    exchange_rate = models.DecimalField(decimal_places=2, max_digits=10,
                                        help_text='This is the exchange rate of the currency to dollars')

    class Meta:
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return f"{self.name}"


class Setting(models.Model):
    """
    This model contains all major settings for the store
    """
    store_name = models.CharField(max_length=255)
    store_tagline = models.CharField(max_length=255, null=True, blank=True)
    store_logo = models.ImageField(upload_to='store')
    store_address = models.TextField()
    store_contact_phone_number = models.IntegerField()
    store_email = models.EmailField(max_length=255)
    copyright_text = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"Major settings for {self.store_name}"


class SEO(models.Model):
    """
    This model contains all SEO requirements for the store
    """
    meta_description = models.TextField(help_text="This is the description that would be shown on search engines")
    keywords = models.TextField(
        help_text="This are what your stores are related with. It could be seperated with commas \",\"")
    favicon = models.ImageField(upload_to='store',
                                help_text='This is the little icon that would be shown beside your title in the browser')

    class Meta:
        verbose_name_plural = "SEO"

    def __str__(self) -> str:
        return f"SEO Settings for {Setting.store_name}"


class SocialIcon(models.Model):
    social_icon_choices = (
        ('fb', 'Facebook'),
        ('tw', 'Twitter'),
        ('ig', 'Instagram'),
        ('lkdn', 'Linkedin'),
        ('ptr', 'Pinterest')
    )
    name = models.CharField(max_length=255, help_text="The name of the social media e.g Facebook, Twitter, Google")
    url = models.URLField(max_length=555,
                          help_text="The URL of your social media page e.g https://facebook.com/my-page")
    icon = models.CharField(max_length=500)


class Paypal(models.Model):
    is_active = models.BooleanField()
    is_live = models.BooleanField()
    test_public_key = models.CharField(max_length=800, null=True, blank=True)
    test_private_key = models.CharField(max_length=800, null=True, blank=True)
    live_public_key = models.CharField(max_length=800, null=True, blank=True)
    live_private_key = models.CharField(max_length=800, null=True, blank=True)

    def __str__(self):
        return f"Paypal Payment Integration"


class Stripe(models.Model):
    is_active = models.BooleanField()
    is_live = models.BooleanField()
    test_public_key = models.CharField(max_length=800, null=True, blank=True)
    test_private_key = models.CharField(max_length=800, null=True, blank=True)
    live_public_key = models.CharField(max_length=800, null=True, blank=True)
    live_private_key = models.CharField(max_length=800, null=True, blank=True)

    def __str__(self):
        return f"Stripe Payment Integration"


class Paystack(models.Model):
    is_active = models.BooleanField()
    is_live = models.BooleanField()
    test_public_key = models.CharField(max_length=800, null=True, blank=True)
    test_private_key = models.CharField(max_length=800, null=True, blank=True)
    live_public_key = models.CharField(max_length=800, null=True, blank=True)
    live_private_key = models.CharField(max_length=800, null=True, blank=True)

    def __str__(self):
        return f"PayStack Payment Integration"


class Flutterwave(models.Model):
    is_active = models.BooleanField()
    is_live = models.BooleanField()
    test_public_key = models.CharField(max_length=800, null=True, blank=True)
    test_private_key = models.CharField(max_length=800, null=True, blank=True)
    live_public_key = models.CharField(max_length=800, null=True, blank=True)
    live_private_key = models.CharField(max_length=800, null=True, blank=True)

    def __str__(self):
        return f"FlutterWave Payment Integration"
