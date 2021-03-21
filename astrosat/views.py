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

    def create(self, request):
        serializer = SatelliteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Satellite.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = SatelliteSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Satellite.objects.get(pk=pk)
        except Satellite.DoesNotExist:
            return Response(status=404)
        serializer = SatelliteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Satellite.objects.get(pk=pk)
        except Satellite.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CosmicSourceViewSet(ViewSet):

    def list(self, request):
        queryset = CosmicSource.objects.order_by('pk')
        serializer = CosmicSourceSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CosmicSourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = CosmicSource.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CosmicSourceSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = CosmicSource.objects.get(pk=pk)
        except CosmicSource.DoesNotExist:
            return Response(status=404)
        serializer = CosmicSourceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = CosmicSource.objects.get(pk=pk)
        except CosmicSource.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PublicationViewSet(ViewSet):

    def list(self, request):
        queryset = Publication.objects.order_by('pk')
        serializer = PublicationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Publication.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PublicationSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Publication.objects.get(pk=pk)
        except Publication.DoesNotExist:
            return Response(status=404)
        serializer = PublicationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Publication.objects.get(pk=pk)
        except Publication.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
