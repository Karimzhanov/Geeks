from rest_framework import serializers
from apps.collection.models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'description', 'image']
