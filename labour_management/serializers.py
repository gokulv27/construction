from rest_framework import serializers

from project.models import LaborToProject, Project
from .models import AdHocEmployee, LaborManagement, LaborTransaction, WorkDay
from master.models import LaborSkill


class LaborSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaborSkill
        fields = ['id', 'name', 'created_at', 'updated_at']



class LaborManagementSerializer(serializers.ModelSerializer):
    skill_id = serializers.PrimaryKeyRelatedField(queryset=LaborSkill.objects.all(), source='skill')
    skill_name = serializers.CharField(source='skill.name', read_only=True)  

    class Meta:
        model = LaborManagement
        fields = [
            'id', 'name', 'phone_no', 'skill_id', 'skill_name', 'aadhar_no', 
            'emergency_contact_number', 'address', 'city', 'state', 
            'pincode', 'daily_wages', 'created_at', 'updated_at'
        ]


class AdHocEmployeeSerializer(serializers.ModelSerializer):
    labor = serializers.PrimaryKeyRelatedField(queryset=LaborManagement.objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = AdHocEmployee
        fields = ['id', 'labor', 'project', 'hired_date', 'is_active']




class WorkDaySerializer(serializers.ModelSerializer):
    labor_to_project = serializers.StringRelatedField()  # Serialize related LaborToProject as a string
    adhoc_employee = AdHocEmployeeSerializer(read_only=True)  # Nested serialization for AdHocEmployee

    class Meta:
        model = WorkDay
        fields = '__all__'


class LaborTransactionSerializer(serializers.ModelSerializer):
    labor_management = serializers.PrimaryKeyRelatedField(queryset=LaborManagement.objects.all())

    class Meta:
        model = LaborTransaction
        fields = ['id', 'labor_management', 'date', 'amount', 'transaction_type', 'description']
