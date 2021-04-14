from rest_framework import viewsets

from .serializers import SiteSerializer, ScenarioSerializer
from .models import Site, Scenario


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all().order_by('name')
    serializer_class = SiteSerializer

class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all().order_by('name')
    serializer_class = ScenarioSerializer
