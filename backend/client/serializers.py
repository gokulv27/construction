from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'customer_tags', 'country', 'address', 'city', 'postal_code', 'name'
        ]
        read_only_fields = ['name']  # The name field is read-only since it is auto-generated

    def validate(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        # Generate the full name
        name = f"{first_name} {last_name}"

        # Check if the combination of first_name and last_name already exists
        if Client.objects.filter(name=name).exists():
            raise serializers.ValidationError("A client with this full name already exists.")
        return data
