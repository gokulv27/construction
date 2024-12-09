from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)  # Display client name

    class Meta:
        model = Project
        fields = [
            'id', 'client', 'client_name', 'project_name', 'location', 'budget',
            'land_facing', 'land_width', 'land_breadth', 'num_floors', 
            'build_area', 'created_at', 'updated_at', 'active_status'
        ]
