from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from astrosat.serializers import *
from astrosat.models import *
from rest_framework import status, viewsets, filters, generics
from rest_framework.views import APIView

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse

from .html import generateHTML


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
    search_fields = ['title', 'abstract', 'authors', 'keyword']

class PublicationListView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'abstract', 'authors', 'keyword']


class GeneratePdf(APIView):
    permission_classes = []

    def get(self, request):
        result = BytesIO()
        publication_ids = self.request.query_params.getlist('publication_ids', [])
        cosmic_source_id = self.request.query_params.get('cosmic_source_id', '')
        astrosat_ids = self.request.query_params.getlist('astrosat_ids', [])

        html = generateHTML(
            publication_ids, 
            cosmic_source_id, 
            astrosat_ids
        )
        
        html_bytes = str.encode(html)
        pdf = pisa.pisaDocument(BytesIO(html_bytes), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None


class HealthCheck(APIView):
    permission_classes = []

    @staticmethod
    def get(request):
        return Response(status=status.HTTP_200_OK)
