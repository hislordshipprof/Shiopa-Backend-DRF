from rest_framework import serializers
from apps.core.models import Image as CoreImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreImage
        fields = (
            'id',
            'title',
            'alt_text',
            'image_url'
        )
