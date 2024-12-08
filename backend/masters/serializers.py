from rest_framework import serializers
from .models import EmployeeType, DocumentType, VendorType, LaborSkill

class EmployeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeType
        fields = ['id', 'name', 'created_at', 'updated_at']


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ['id', 'name', 'created_at', 'updated_at']


class VendorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorType
        fields = ['id', 'name', 'created_at', 'updated_at']


class LaborSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaborSkill
        fields = ['id', 'name', 'created_at', 'updated_at']
