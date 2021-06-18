from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'image_url',
            'image_alt',
            'parent',
            'get_absolute_url',
        )
