from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from astrosat.serializers import SatelliteSerializer, CosmicSourceSerializer, PublicationSerializer
from astrosat.models import Satellite, CosmicSource, Publication


class SatelliteViewSet(ViewSet):

    def list(self, request):
        queryset = Satellite.objects.order_by('pk')
        serializer = SatelliteSerializer(queryset, many=True)
        return Response(serializer.data)


class CosmicSourceViewSet(ViewSet):

    def list(self, request):
        queryset = CosmicSource.objects.order_by('pk')
        serializer = CosmicSourceSerializer(queryset, many=True)
        return Response(serializer.data)



class PublicationViewSet(ViewSet):

    def list(self, request):
        queryset = Publication.objects.order_by('pk')
        serializer = PublicationSerializer(queryset, many=True)
        return Response(serializer.data)