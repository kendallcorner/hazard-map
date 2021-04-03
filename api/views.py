from rest_framework import viewsets

from .serializers import SiteSerializer
from .models import Site


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all().order_by('name')
    serializer_class = SiteSerializer
    