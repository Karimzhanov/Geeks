from django.contrib import admin
from apps.logo.models import Brand

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo')