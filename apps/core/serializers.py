from rest_framework import serializers
from apps.core.models import Image as CoreImage
from apps.core.models import Section


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreImage
        fields = (
            'id',
            'title',
            'alt_text',
            'image_url'
        )
