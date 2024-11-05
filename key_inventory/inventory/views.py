from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Key
from .serializers import KeySerializer

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
