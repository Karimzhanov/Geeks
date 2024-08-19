from rest_framework import viewsets
from apps.collection.models import Collection
from .serializers import CollectionSerializer

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
