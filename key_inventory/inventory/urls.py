from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KeyViewSet, UserListView, KeyAssignmentView, key_inventory_status, UserCreateView
from . import views

router = DefaultRouter()
router.register(r'keys', KeyViewSet)
router.register(r'keyassignments', KeyAssignmentView, basename='key_assignment')

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),  # User API endpoint
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('key-inventory/', views.key_inventory_status, name='key_inventory_status'),
    path('assign-key', views.assign_key, name='assign-key'),
    path('', include(router.urls)),  # Register the KeyViewSet API routes
]