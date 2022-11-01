from rest_framework import serializers
from .models import Channel, Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'id',
            'name',
            'description',
            'author',
            'genre',
            'rating',
            'file',
        ]


class ContentLittleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'id',
            'name',
            'rating',
        ]


class SubChannelSerializer(serializers.ModelSerializer):
    contents = ContentLittleSerializer(many=True)

    class Meta:
        model = Channel
        fields = [
            'id',
            'title',
            'contents',
        ]


class ChannelSerializer(serializers.ModelSerializer):
    contents = ContentLittleSerializer(many=True)
    subchannels = SubChannelSerializer(many=True)
    avg_rating = serializers.ReadOnlyField()

    class Meta:
        model = Channel
        fields = [
            'id',
            'title',
            'language',
            'picture',
            'subchannels',
            'contents',
            'avg_rating',
        ]
