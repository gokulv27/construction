import os
from rest_framework import serializers
from .models import Project, Document, LaborToProject

class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'client', 'client_name', 'project_name', 'location', 'budget',
            'land_facing', 'land_width', 'land_breadth', 'num_floors', 'build_area', 
            'created_at', 'updated_at', 'active_status'
        ]

class ProjectDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id','document_name','file','project_id','document_type_id','uploaded_at']

    def validate_file(self, file):
        max_file_size = 2 * 1024 * 1024  # 2MB
        if file.size > max_file_size:
            raise serializers.ValidationError("File size exceeds the 2MB limit.")

        allowed_extensions = ['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx', 'xls', 'xlsx','txt']
        file_extension = os.path.splitext(file.name)[1].lower().strip('.')
        if file_extension not in allowed_extensions:
            raise serializers.ValidationError(
                f"Unsupported file type: '{file_extension}'. Allowed types: {', '.join(allowed_extensions)}"
            )
        return file

class LaborToProjectSerializer(serializers.ModelSerializer):
    skill=serializers.CharField(source='labor.skill.name', read_only=True)
    labor_name=serializers.CharField(source='labor.name', read_only=True)
    class Meta:
        model = LaborToProject
        fields = '__all__'

