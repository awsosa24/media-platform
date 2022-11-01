from rest_framework import serializers
from .models import Channel, Content, ContentFile, ChannelGroup


class ChannelGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelGroup
        fields = [
            'id',
            'name',
        ]


class ContentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentFile
        fields = [
            'id',
            'name',
            'file',
        ]


class ContentSerializer(serializers.ModelSerializer):
    files = ContentFileSerializer(many=True)
    class Meta:
        model = Content
        fields = [
            'id',
            'name',
            'description',
            'author',
            'genre',
            'rating',
            'files',
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
    groups = ChannelGroupSerializer(many=True)

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
            'groups',
        ]
