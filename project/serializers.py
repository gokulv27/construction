import os
from rest_framework import serializers

from master.serializers import DocumentTypeSerializer
from .models import Project, Document

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for project details.
    """
    client_name = serializers.CharField(source='client.name', read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'client', 'client_name', 'project_name', 'location', 'budget',
            'land_facing', 'land_width', 'land_breadth', 'num_floors',
            'build_area', 'created_at', 'updated_at', 'active_status'
        ]


class ProjectDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

    def validate_file(self, file):
        """
        Validate file size and type.
        """
        # Validate file size
        max_file_size = 2 * 1024 * 1024  # 2MB
        if file.size > max_file_size:
            raise serializers.ValidationError("File size exceeds the 2MB limit.")

        # Validate file type
        allowed_extensions = ['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx', 'xls', 'xlsx']
        file_extension = os.path.splitext(file.name)[1].lower().strip('.')
        if file_extension not in allowed_extensions:
            raise serializers.ValidationError(
                f"Unsupported file type: '{file_extension}'. Allowed types: {', '.join(allowed_extensions)}"
            )

        return file