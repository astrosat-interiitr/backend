from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from astrosat.serializers import SatelliteSerializer, CosmicSourceSerializer, PublicationSerializer
from astrosat.models import Satellite, CosmicSource, Publication
from rest_framework import status, viewsets, filters, generics


class SatelliteViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request):
        queryset = Satellite.objects.order_by('pk')
        serializer = SatelliteSerializer(queryset, many=True)
        return Response(serializer.data)


class CosmicSourceViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request, pk=None):
        if pk == None:
            queryset = CosmicSource.objects.order_by('pk')
        else:
            queryset = CosmicSource.objects.get(id = pk)
            
        serializer = CosmicSourceSerializer(queryset, many=True)
        return Response(serializer.data)
   
    
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