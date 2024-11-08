from rest_framework import serializers
from .models import Key, KeyAssignment, Users

class KeySerializer(serializers.ModelSerializer):
    available_quantity = serializers.ReadOnlyField()

    class Meta:
        model = Key
        fields = ['id', 'name', 'total_quantity', 'checked_out_quantity', 'available_quantity', 'notes']
        read_only_fields = ['available_quantity']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'fname', 'lname', 'email']

class KeyAssignmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    key = KeySerializer(read_only=True)

    class Meta:
        model = KeyAssignment
        fields = ['user', 'key', 'checkout_date', 'return_date', 'is_returned', 'status']


