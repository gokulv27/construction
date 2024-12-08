from rest_framework import serializers
from .models import LaborManagement
from masters.models import LaborSkill



class LaborManagementSerializer(serializers.ModelSerializer):
    skill_id = serializers.PrimaryKeyRelatedField(queryset=LaborSkill.objects.all(), source='skill')

    class Meta:
        model = LaborManagement
        fields = [
            'id', 'name', 'phone_no', 'skill_id', 'aadhar_no', 'emergency_contact_number',
            'address', 'city', 'state', 'pincode', 'daily_wages',
            'created_at', 'updated_at'
        ]
