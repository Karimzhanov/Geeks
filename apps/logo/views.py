from rest_framework import viewsets
from apps.logo.models import Brand
from apps.logo.serializers import BrandSerializer

# Create your views here.

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
