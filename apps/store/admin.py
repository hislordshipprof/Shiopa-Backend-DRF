from django.contrib import admin
from apps.store.models import Settings, Country, Currency

admin.site.register(Currency)
admin.site.register(Country)


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'store_email', 'store_phone_number')
    fieldsets = (
        (None, {
            'fields': ('store_name', 'store_tagline', 'store_logo', 'favicon')
        }),
        ('Contact Details', {
            'fields': ('store_phone_number', 'store_email', 'store_address', 'copyright_text')
        }),
        ('Social Details', {
            'fields': ('facebook_url', 'instagram_url', 'twitter_url')
        }),
        ('SEO Details', {
            'fields': ('meta_description', 'keywords')
        })
    )


admin.site.register(Settings, SettingsAdmin)
