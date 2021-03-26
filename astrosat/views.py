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


class SatelliteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SatelliteSerializer
    queryset = Satellite.objects.all()


class CosmicSourceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CosmicSourceSerializer
    queryset = CosmicSource.objects.all()

class AstrosatViewSet(viewsets.ReadOnlyModelViewSet):
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


def GeneratePdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


class HealthCheck(APIView):
    permission_classes = []

    @staticmethod
    def get(request):
        return Response(status=status.HTTP_200_OK)