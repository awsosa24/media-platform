from django_filters import rest_framework as filters
from rest_framework import viewsets
from .filters import ChannelFilter
from .models import Channel, Content, ContentFile
from .serializers import ChannelSerializer, ContentSerializer, ContentFileSerializer



class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ChannelFilter


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentFileViewSet(viewsets.ModelViewSet):
    queryset = ContentFile.objects.all()
    serializer_class = ContentFileSerializer
