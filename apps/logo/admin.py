from django.contrib import admin
from apps.logo.models import Logo

# Register your models here.

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('logo',)