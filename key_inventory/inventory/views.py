
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.decorators import action, api_view
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .models import Key, KeyAssignment, Users
from .serializers import KeySerializer, UserSerializer, KeyAssignmentSerializer

def index(request):
    return render(request, 'index.html')

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
    key_assignments = KeyAssignment.objects.select_related('user', 'key').all().order_by('user')
    
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
    

@api_view(['POST'])
def assign_key(request):
    try:
        user_id = request.data.get('user_id')
        key_id = request.data.get('key_id')

        if not user_id or not key_id:
            return Response({'error': 'User ID and Key ID are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the user and key objects
        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return Response({'error': 'User not found!'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            key = Key.objects.get(id=key_id)
        except Key.DoesNotExist:

            return Response({'error': 'Key not found!'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the key assignment
        KeyAssignment.objects.create(user=user, key=key)

        return Response({'message': 'Key assigned successfully!'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)