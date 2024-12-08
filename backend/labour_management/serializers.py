from rest_framework import serializers
from .models import LaborManagement

class LaborManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaborManagement
        fields = [
            'id', 'name', 'phone_no', 'aadhar_no', 'emergency_contact_number',
            'address', 'city', 'state', 'pincode', 'daily_wages',
            'created_at', 'updated_at'
        ]
