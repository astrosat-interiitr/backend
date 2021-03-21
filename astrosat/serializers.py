from rest_framework.serializers import ModelSerializer
from astrosat.models import Satellite, CosmicSource, Publication


class SatelliteSerializer(ModelSerializer):

    class Meta:
        model = Satellite
        fields = '__all__'


class CosmicSourceSerializer(ModelSerializer):

    class Meta:
        model = CosmicSource
        fields = '__all__'


class PublicationSerializer(ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'
