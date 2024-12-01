# masters/serializers.py
from rest_framework import serializers
from .models import EmployeeType

class EmployeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeType
        fields = ['id', 'name', 'created_at', 'updated_at']

# class vendortypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = vendortype
#         fields = ['id', 'name', 'created_at', 'updated_at']

# class BrandTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BrandType
#         fields = ['id', 'name', 'created_at', 'updated_at']

# class EmployeeRolleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeRolles
#         fields = ['id', 'name', 'created_at', 'updated_at']


# class ItemSerializer(serializers.ModelSerializer):
#     brand_name = serializers.CharField(source='brand.name', read_only=True)  # Add 'brand_name' as a computed field

#     class Meta:
#         model = Item
#         fields = ['id', 'name', 'brand_name', 'created_at', 'updated_at']