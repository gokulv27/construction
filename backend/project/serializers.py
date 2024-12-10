from rest_framework import serializers
from .models import Project, ProjectDocument

class ProjectDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDocument
        fields = ['id', 'project', 'document_name', 'file', 'uploaded_at']

    def validate_file(self, value):
        allowed_extensions = ('.pdf', '.docx', '.txt', '.jpg')
        if not value.name.lower().endswith(allowed_extensions):
            raise serializers.ValidationError(f"Only {', '.join(allowed_extensions)} files are allowed.")
        return value


class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)
    documents = ProjectDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'client', 'client_name', 'project_name', 'location', 'budget',
            'land_facing', 'land_width', 'land_breadth', 'num_floors',
            'build_area', 'created_at', 'updated_at', 'active_status', 'documents'
        ]
