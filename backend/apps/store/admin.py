from django.contrib import admin
from backend.apps.store.models import Setting, Currency, SEO, SocialIcon

admin.site.register(Setting)
admin.site.register(Currency)
admin.site.register(SEO)
admin.site.register(SocialIcon)