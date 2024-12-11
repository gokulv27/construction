from rest_framework import serializers
from .models import LaborManagement
from masters.models import LaborSkill


class LaborSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaborSkill
        fields = ['id', 'name', 'created_at', 'updated_at']


class LaborManagementSerializer(serializers.ModelSerializer):
    skill_id = serializers.PrimaryKeyRelatedField(queryset=LaborSkill.objects.all(), source='skill')
    skill_name = serializers.CharField(source='skill.name', read_only=True)  # Add skill_name field

    class Meta:
        model = LaborManagement
        fields = [
            'id', 'name', 'phone_no', 'skill_id', 'skill_name', 'aadhar_no',
            'emergency_contact_number', 'address', 'city', 'state', 'pincode',
            'daily_wages', 'created_at', 'updated_at'
        ]

