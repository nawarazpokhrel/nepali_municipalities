from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
# # Create your views here.
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.municaplities import usecases, serializers, filtersets
from apps.municaplities.mixins import ResponseMixin
from drf_yasg.utils import swagger_auto_schema


class CreateMunicipalites(APIView):
    permission_classes = [IsAdminUser,]
    def post(self, request, *args, **kwargs):
        usecases.AddMunicipalities(
        ).execute()

        return Response({'Success': 'Create successfully.'}, status=status.HTTP_200_OK)


class ListMunicipalitiesView(generics.CreateAPIView, ResponseMixin):
    """
    use this endpoint to list all municipalites
    """
    serializer_class = serializers.GetMunicipality
    response_serializer_class = serializers.MunicipalitesSerializer

    def perform_create(self, serializer):
        return usecases.ListMunicipalitiesUseCase(
            serializer=serializer,
        ).execute()

    def response(self, serializer, result, status_code):
        response_serializer = self.get_response_serializer(result, many=True)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={
        200: serializers.MunicipalitesSerializer()
    })
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAllDataView(generics.ListAPIView):
    """
    use this endpoint to list all municipalites
    """
    serializer_class = serializers.ListAllMunicipalitesData
    # filterset_class = filtersets.MunicipalitiesSearchFilter?
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        'name',
    ]
    def get_queryset(self):
        return usecases.ListAllMunicipalitiesUseCase(
        ).execute()
