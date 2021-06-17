from django.contrib import admin
from apps.product.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    list_filter = ('name',)


admin.site.register(Category, CategoryAdmin)
