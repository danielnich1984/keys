from rest_framework import serializers
from .models import Key

class KeySerializer(serializers.ModelSerializer):
    available_quantity = serializers.ReadOnlyField()

    class Meta:
        model = Key
        fields = ['id', 'name', 'total_quantity', 'checked_out_quantity', 'available_quantity']
        read_only_fields = ['available_quantity']