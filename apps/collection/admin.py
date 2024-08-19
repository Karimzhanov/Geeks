from django.contrib import admin
from apps.collection.models import Collection
# Register your models here.
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
