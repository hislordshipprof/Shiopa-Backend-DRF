from django.contrib import admin
from apps.product.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sku',
                    'available_to_purchase', 'created_at')
    list_filter = ('name', 'price', 'available_to_purchase',
                   'created_at')
    filter_horizontal = ('images', 'section')

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'additional_info')
        }),
        ('Price', {
            'fields': ('price', 'discount_price')
        }),
        ('Images', {
            'fields': ('main_image', 'images')
        }),
        ('Stock', {
            'fields': ('sku', 'available_to_purchase')
        })

    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    list_filter = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
