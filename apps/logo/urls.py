from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.logo.views import LogoViewSet

router = DefaultRouter()
router.register(r'brands', LogoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
