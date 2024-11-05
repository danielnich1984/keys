# inventory/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KeyViewSet

router = DefaultRouter()
router.register(r'keys', KeyViewSet)  # Register the Key viewset

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]
