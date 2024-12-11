from rest_framework import serializers
from .models import Project, ProjectDocument, LaborToProject, LaborTransaction, WorkDay
from masters.serializers import DocumentTypeSerializer


class LaborTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for labor transactions, including fields like amount and transaction type.
    """
    class Meta:
        model = LaborTransaction
        fields = ['id', 'date', 'amount', 'transaction_type', 'description']


class WorkDaySerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='labor_to_project.project.project_name', read_only=True)
    labor_name = serializers.CharField(source='labor_to_project.labor.name', read_only=True)  # Updated source

    class Meta:
        model = WorkDay
        fields = ['id', 'labor_name', 'labor_to_project', 'date', 'work_type', 'hours_worked', 'overtime_hours', 'wages', 'project_name']


class LaborToProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for labor-to-project mapping, integrating transactions and workdays.
    """
    labor_name = serializers.CharField(source='labor.name', read_only=True)
    skill = serializers.CharField(source='labor.skill.name', read_only=True)
    wages_per_day = serializers.SerializerMethodField()
    transactions = LaborTransactionSerializer(many=True, read_only=True)
    work_days = WorkDaySerializer(many=True, read_only=True)  # Include workday entries
    pending_amount = serializers.SerializerMethodField()
    total_earnings = serializers.SerializerMethodField()

    class Meta:
        model = LaborToProject
        fields = [
            'id', 'labor', 'labor_name', 'skill', 'start_date', 'end_date',
            'wages_per_day', 'total_earnings', 'pending_amount', 'transactions', 'work_days'
        ]

    def get_wages_per_day(self, obj):
        return obj.get_wages_per_day()

    def get_pending_amount(self, obj):
        return obj.calculate_pending_amount()

    def get_total_earnings(self, obj):
        return obj.calculate_total_earnings()


class ProjectDocumentSerializer(serializers.ModelSerializer):
    """
    Serializer for project documents, including document type details.
    """
    document_type = DocumentTypeSerializer()  # Include document_type field

    class Meta:
        model = ProjectDocument
        fields = ['id', 'project', 'document_name', 'file', 'uploaded_at', 'document_type']


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for project details, integrating clients, documents, and labor assignments.
    """
    client_name = serializers.CharField(source='client.name', read_only=True)
    documents = ProjectDocumentSerializer(many=True, read_only=True)
    labors = LaborToProjectSerializer(source='labor_assignments', many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'client', 'client_name', 'project_name', 'location', 'budget',
            'land_facing', 'land_width', 'land_breadth', 'num_floors',
            'build_area', 'created_at', 'updated_at', 'active_status', 'documents', 'labors'
        ]
