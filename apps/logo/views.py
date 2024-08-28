from rest_framework import viewsets
from apps.logo.models import Logo
from apps.logo.serializers import LogoSerializer

# Create your views here.

class LogoViewSet(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
