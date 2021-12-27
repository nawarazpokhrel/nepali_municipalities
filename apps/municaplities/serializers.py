from rest_framework import serializers

from apps.municaplities.models import Municipalities


class GetMunicipality(serializers.Serializer):
    name = serializers.CharField()


class MunicipalitesSerializer(serializers.Serializer):
    district = serializers.CharField()


class ListAllMunicipalitesData(serializers.ModelSerializer):
    province = serializers.CharField(source='district.province.name')

    district = serializers.CharField(source='district.name')
    country = serializers.CharField(default='Nepal')

    class Meta:

        model = Municipalities
        fields = (
            'id',
            'name',
            'district',
            'province',
            'country'

        )
