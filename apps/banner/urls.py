from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.banner.views import BannerViewSet  


router = DefaultRouter()
router.register(r'banners', BannerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
