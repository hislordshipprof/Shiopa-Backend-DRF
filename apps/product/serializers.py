from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.product.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'description',
            'additional_info',
            'price',
            'discount_price',
            'sku',
            'available_to_purchase',
            'get_absolute_url',
            'main_image_url',
            'get_thumbnail'
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'image_url',
            'image_alt',
            'parent',
            'get_absolute_url',
            'products'
        )
