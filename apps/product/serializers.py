from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.product.models import Category, Product

from apps.core.serializers import ImageSerializer as CoreImageSerializer


class ProductSerializer(serializers.ModelSerializer):
    images = CoreImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
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
            'get_thumbnail',
            'images'
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'image_url',
            'image_alt',
            'parent',
            'get_absolute_url',
            'products'
        )
