from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Channel


class ProductFilter(filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    # all_groups contains both parents and childs groups
    # all_groups = CharFilter(method='groups_filter')

    class Meta:
        model = Channel
        fields = ['title', 'groups']

    # def groups_filter(self, queryset, name, value):
    #     return queryset.filter(Q(groups__icontains=value) | Q(subchannels__iexact=value))
