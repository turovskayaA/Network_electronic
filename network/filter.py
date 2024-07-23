import django_filters

from .models import NetworkLink


class SearchNetworkLink(django_filters.FilterSet):
    """ Поиск по стране """
    country = django_filters.CharFilter(lookup_expr='icontains', label='Страна')

    class Meta:
        model = NetworkLink
        fields = ['country']
