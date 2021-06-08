from django.contrib import admin
from backend.apps.store.models import Setting, Currency, SEO, SocialIcon, Paypal, Stripe, Paystack, Flutterwave

admin.site.register(Setting)
admin.site.register(Currency)
admin.site.register(SEO)
admin.site.register(Paypal)
admin.site.register(SocialIcon)
admin.site.register(Stripe)
admin.site.register(Paystack)
admin.site.register(Flutterwave)