from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from astrosat.serializers import SatelliteSerializer, CosmicSourceSerializer, PublicationSerializer
from astrosat.models import Satellite, CosmicSource, Publication
from rest_framework import status, viewsets


class SatelliteViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request):
        queryset = Satellite.objects.order_by('pk')
        serializer = SatelliteSerializer(queryset, many=True)
        return Response(serializer.data)


class CosmicSourceViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request, pk=None):
        queryset = CosmicSource.objects.order_by('pk')
        if pk == None:
            queryset = CosmicSource.objects.order_by('pk')
        else:
            queryset = CosmicSource.objects.get(id = pk)
            
        serializer = CosmicSourceSerializer(queryset, many=True)
        return Response(serializer.data)



class PublicationViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request):
        queryset = Publication.objects.order_by('pk')
        serializer = PublicationSerializer(queryset, many=True)
        return Response(serializer.data)