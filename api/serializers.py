from rest_framework import serializers

from .models import Site, Scenario

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('name', 'latitude', 'longitude', 'zoom')

class ScenarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scenario
        fields = ('material', 'name', 'scenarioId', 'latitude', 'longitude', 'range0', 'frequency0', 'range1', 'frequency1', 'range2', 'frequency2')
