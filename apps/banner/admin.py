from django.contrib import admin
from apps.banner.models import Banner
# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
