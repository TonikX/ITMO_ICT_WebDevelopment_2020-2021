from rest_framework import serializers
from easy_thumbnails.templatetags.thumbnail import thumbnail_url


class ThumbnailSerializer(serializers.ImageField):
    def __init__(self, alias, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_only = True
        self.alias = alias

    def to_representation(self, value):
        if not value:
            return None
        print(value)
        print(self.alias)
        url = thumbnail_url(value, self.alias)
        return url
