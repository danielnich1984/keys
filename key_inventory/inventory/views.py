from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Key, KeyAssignment, Users
from .serializers import KeySerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        key = self.get_object()
        if key.available_quantity() <= 0:
            return Response({'error': 'No available keys for checkout.'}, status=status.HTTP_400_BAD_REQUEST)
        key.checked_out_quantity += 1
        key.save()
        return Response(self.get_serializer(key).data)

    @action(detail=True, methods=['post'])
    def checkin(self, request, pk=None):
        key = self.get_object()
        if key.checked_out_quantity <= 0:
            return Response({'error': 'No keys to check in.'}, status=status.HTTP_400_BAD_REQUEST)
        key.checked_out_quantity -= 1
        key.save()
        return Response(self.get_serializer(key).data)

    @action(detail=False, methods=['get'])
    def report(self, request):
        keys = Key.objects.all()
        data = {
            key.name: {
                'total_quantity': key.total_quantity,
                'checked_out_quantity': key.checked_out_quantity,
                'available_quantity': key.available_quantity(),
            }
            for key in keys
        }
        return Response(data)

def checkout_key(request, key_id):
    key = get_object_or_404(Key, pk=key_id)

    if request.method == 'POST':
        assignment = KeyAssignment(user=request.user, key=key)
        assignment.sae()
        return redirect('key_checkout_success')
    
    return render (request, 'checkout_key.html', {'key': key})

def my_assignments(request):
    assignments = KeyAssignment.objects.filter(user=request.user)
    return render(request, 'my_assignments.html', {'assignments': assignments})

def key_inventory_status(request):
    keys = Key.objects.all()
    # Get all key assignments to display which users have which keys checked out or lost
    key_assignments = KeyAssignment.objects.select_related('user', 'key').all()
    
    return render(request, 'inventory/key_inventory_status.html', {
        'keys': keys,
        'key_assignments': key_assignments,
    })

