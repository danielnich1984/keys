from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .models import Key, KeyAssignment, Users
from .serializers import KeySerializer, UserSerializer, KeyAssignmentSerializer

# API View for Key Checkout

# ViewSet for Key - Handle CRUD operations for keys
class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer
    
    @action(detail=False, methods=['get'])
    def report(self, request):
        # Get a report of key status
        keys = Key.objects.all()
        data = {
            key.name: {
                'total_quantity': key.total_quantity,
                'checked_out_quantity': key.checked_out_quantity(),
                'available_quantity': key.available_quantity(),
                'lost_quantity': key.lost_quantity(),
            }
            for key in keys
        }
        return Response(data)
    
  
def key_inventory_status(request):
    keys = Key.objects.all()
    # Get all key assignments to display which users have which keys checked out or lost
    key_assignments = KeyAssignment.objects.select_related('user', 'key').all()
    
    return render(request, 'inventory/key_inventory_status.html', {
        'keys': keys,
        'key_assignments': key_assignments,
    })

# User List API View for fetching users (if needed for your API)
class UserListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    
class UserCreateView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class KeyAssignmentView(viewsets.ModelViewSet):
    queryset = KeyAssignment.objects.all()
    serializer_class = KeyAssignmentSerializer

    @action(detail=False, methods=['get'])
    def assign(self, request):
        # Custom action to render drop-down options for assignment
        keys = Key.objects.all()  # Get all available keys
        # This could be a context or form rendering if you’re using DRF’s Browsable API
        return Response({
            'keys': [key.name for key in keys]
        })

