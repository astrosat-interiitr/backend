from rest_framework.serializers import ModelSerializer
from astrosat.models import Satellite, CosmicSource, Publication, Astrosat


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

class AstrosatSerializer(ModelSerializer):

    class Meta:
        model = Astrosat
        fields = '__all__'