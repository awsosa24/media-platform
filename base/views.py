from .models import Channel, Content
from .serializers import ChannelSerializer, ContentSerializer
# from django_filters import rest_framework as filters
from rest_framework import viewsets


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('category', 'in_stock')


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
