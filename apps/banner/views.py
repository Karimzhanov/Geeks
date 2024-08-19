from rest_framework import viewsets
from apps.banner.models import Banner
from apps.banner.serializers import BannerSerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
