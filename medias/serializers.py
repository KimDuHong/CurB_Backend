from rest_framework.serializers import ModelSerializer
from .models import Media


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = ("url",)
