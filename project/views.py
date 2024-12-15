from django.shortcuts import render, get_object_or_404
from .models import Project, Document
from .serializers import ProjectDocumentSerializer, ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def project_list(request):
    """
    Fetch a list of all projects.
    """
    projects = Project.objects.select_related('client').all()
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
    serializer = ProjectSerializer(project, data=request.data, partial=True)  # Use partial=True for partial updates
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


@api_view(['GET'])
def project_document_list(request, project_id=None):
    """
    Fetch a list of documents for a specific project or all documents.
    """
    if project_id:
        documents = Document.objects.filter(project_id=project_id).select_related('document_type')
    else:
        documents = Document.objects.select_related('project', 'document_type').all()

    serializer = ProjectDocumentSerializer(documents, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def project_document_create(request):
    """
    Create a new project document.
    """
    # Associate the document with the provided project ID
    project_id = request.data.get('project_id')  # Expect project_id in the request data
    project = get_object_or_404(Project, id=project_id)  # Validate project existence

    # Prepare the data for the serializer, including the associated project
    serializer = ProjectDocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(project=project)  # Save the document with the project association
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def project_document_update(request, id):
    """
    Update an existing project document.
    """
    document = get_object_or_404(Document, id=id)
    serializer = ProjectDocumentSerializer(document, data=request.data, partial=True)  # Use partial=True for partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def project_document_delete(request, id):
    """
    Delete a project document by ID.
    """
    document = get_object_or_404(Document, id=id)
    document.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def project_document_download(request, id):
    """
    Download a document file by ID.
    """
    from django.http import FileResponse
    document = get_object_or_404(Document, id=id)
    if not document.file:
        return Response({"error": "No file attached to this document."}, status=status.HTTP_404_NOT_FOUND)
    return FileResponse(document.file.open(), as_attachment=True, filename=document.document_name)
