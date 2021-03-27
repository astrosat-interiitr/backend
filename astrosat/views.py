from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from astrosat.serializers import *
from astrosat.models import *
from rest_framework import status, viewsets, filters, generics


class SatelliteViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = None
    serializer_class = SatelliteSerializer
    queryset = Satellite.objects.all()

class CosmicSourceViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = None
    serializer_class = CosmicSourceSerializer
    queryset = CosmicSource.objects.all()

class AstrosatViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = None
    serializer_class = AstrosatSerializer
    queryset = Astrosat.objects.all()
    
class PublicationGetView(generics.RetrieveAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'abstract', 'author', 'keyword']

class PublicationListView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'abstract', 'author', 'keyword']
