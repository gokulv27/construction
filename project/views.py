from django.shortcuts import get_object_or_404
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from master.models import DocumentType
from .models import (
    LaborToProject, Project, Document
)
from .serializers import (
    LaborToProjectSerializer,
    ProjectSerializer, ProjectDocumentSerializer
)

# Project Views
@api_view(['GET'])
def project_list(request):
    """Fetch a list of all projects."""
    projects = Project.objects.select_related('client').all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def project_create(request):
    """Create a new project."""
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def project_update(request, id):
    """Update an existing project."""
    project = get_object_or_404(Project, id=id)
    serializer = ProjectSerializer(project, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def project_delete(request, id):
    """Delete a project by ID."""
    project = get_object_or_404(Project, id=id)
    project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Document Views
@api_view(['GET'])
def project_document_list(request, project_id=None):
    """Fetch documents for a specific project or all documents."""
    documents = (
        Document.objects.filter(project_id=project_id).select_related('document_type')
        if project_id else
        Document.objects.select_related('project', 'document_type').all()
    )
    serializer = ProjectDocumentSerializer(documents, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def project_document_create(request):
    """
    Create a new project document.
    """
    # Validate the project
    project_id = request.data.get('project_id')
    project = get_object_or_404(Project, id=project_id)

    # Validate the document type
    document_type_id = request.data.get('document_type')
    document_type = get_object_or_404(DocumentType, id=document_type_id)

    # Serialize the data
    serializer = ProjectDocumentSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        # Save the document with validated project and document type
        serializer.save(project=project, document_type=document_type)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Handle validation errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
def project_document_update(request, id):
    """Update an existing project document."""
    document = get_object_or_404(Document, id=id)
    serializer = ProjectDocumentSerializer(document, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def project_document_delete(request, id):
    """Delete a project document by ID."""
    document = get_object_or_404(Document, id=id)
    document.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def project_document_download(request, id):
    """Download a document file by ID."""
    document = get_object_or_404(Document, id=id)
    if not document.file:
        return Response({"error": "No file attached to this document."}, status=status.HTTP_404_NOT_FOUND)
    return FileResponse(document.file.open(), as_attachment=True, filename=document.document_name)


# LaborToProject Views
@api_view(['GET'])
def labor_to_project_list(request):
    """Fetch a list of labor-to-project assignments."""
    labor_to_projects = LaborToProject.objects.select_related('labor', 'project').all()
    serializer = LaborToProjectSerializer(labor_to_projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def labor_to_project_create(request):
    """Create a new labor-to-project assignment."""
    serializer = LaborToProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def labor_to_project_update(request, id):
    """Update an existing labor-to-project assignment."""
    labor_to_project = get_object_or_404(LaborToProject, id=id)
    serializer = LaborToProjectSerializer(labor_to_project, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def labor_to_project_delete(request, id):
    """Delete a labor-to-project assignment."""
    labor_to_project = get_object_or_404(LaborToProject, id=id)
    labor_to_project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




