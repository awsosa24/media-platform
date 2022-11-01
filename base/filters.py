from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Channel


class ChannelFilter(filters.FilterSet):
    # groups contains both parents and childs groups
    group_name = filters.CharFilter(method='filter_group_name')

    class Meta:
        model = Channel
        fields = ['group_name']

    def filter_group_name(self, queryset, name, value):
        return queryset.filter(Q(groups__name__icontains=value) | Q(subchannels__groups__name__icontains=value))
