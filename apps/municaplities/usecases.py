import json
import os

from apps.municaplities.models import Province, District, Municipalities


class AddMunicipalities:
    def execute(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        json_data_path = os.path.join(BASE_DIR, 'prades.json')  # for province
        file = open(json_data_path, 'r')
        data_values = json.loads(file.read())

        for data in data_values:
            province = Province(**data)
            province.save()

        district_path = os.path.join(BASE_DIR, 'district.json')  # for district
        file = open(district_path, 'r')
        data_values = json.loads(file.read())
        for data in data_values:
            province = Province.objects.get(name=data['province'])
            District(
                name=data['name'],
                province=province,
            ).save()
        municipality_path = os.path.join(BASE_DIR, 'municipalities.json')  # for municipalites
        file = open(municipality_path, 'r')
        data_values = json.loads(file.read())
        for data in data_values:
            district = District.objects.get(name=data['district'])
            Municipalities(
                name=data['name'],
                district=district,
            ).save()


class ListMunicipalitiesUseCase:
    def __init__(self, serializer):
        self._serialzier = serializer
        self._data = serializer.validated_data

    def execute(self):
        self._factory()
        return self._municipalites

    def _factory(self):
        self._municipalites = Municipalities.objects.filter(name=self._data['name'])


class ListAllMunicipalitiesUseCase:

    def execute(self):
        self._factory()
        return self._municipalites

    def _factory(self):
        self._municipalites = Municipalities.objects.select_related('district', 'district__province').all()
