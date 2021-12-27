from django_filters import filters
from django_filters import rest_framework as filters, BaseInFilter


class MunicipalitiesSearchFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name="name",
        label='municipalities name'
    )

    class Meta:
        fields = (
            'name',
        )
