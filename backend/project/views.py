from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404
from .models import Project, ProjectDocument
from .serializers import ProjectSerializer, ProjectDocumentSerializer
import logging

logger = logging.getLogger(__name__)

# --- Project CRUD Operations ---
@api_view(['GET'])
def project_list(request):
    """
    Fetch a list of all projects.
    """
    projects = Project.objects.select_related('client').prefetch_related('documents').all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def project_create(request):
    """
    Create a new project.
    """
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def project_update(request, id):
    """
    Update an existing project.
    """
    project = get_object_or_404(Project, id=id)
    serializer = ProjectSerializer(project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def project_delete(request, id):
    """
    Delete a project by ID.
    """
    project = get_object_or_404(Project, id=id)
    project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# --- Project Document Upload ---
class UploadDocumentView(views.APIView):
    """
    Handles document uploads.
    """
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ProjectDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- Project Document Views ---
class ProjectDocumentListView(ListAPIView):
    """
    List all project documents, optionally filter by project ID.
    """
    serializer_class = ProjectDocumentSerializer

    def get_queryset(self):
        queryset = ProjectDocument.objects.all()
        project_id = self.request.query_params.get('project')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset


class ProjectDocumentDetailView(RetrieveAPIView):
    """
    Retrieve a specific project document by ID.
    """
    queryset = ProjectDocument.objects.all()
    serializer_class = ProjectDocumentSerializer
