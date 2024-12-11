from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Project, ProjectDocument,LaborToProject, WorkDay
from .serializers import ProjectSerializer, ProjectDocumentSerializer,LaborToProject,LaborToProjectSerializer, WorkDaySerializer
import logging
from labour_management.models import LaborManagement

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

class AddLaborToProjectView(APIView):
    def post(self, request, project_id):
        project = get_object_or_404(Project, id=project_id)
        labor_id = request.data.get('labor_id')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        labor = get_object_or_404(LaborManagement, id=labor_id)
        # Check if the laborer is already assigned to this project
        if LaborToProject.objects.filter(labor=labor, project=project).exists():
            return Response({'error': 'Laborer is already assigned to this project.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the labor-to-project mapping
        mapping = LaborToProject.objects.create(
            labor=labor,
            project=project,
            start_date=start_date,
            end_date=end_date
        )
        serializer = LaborToProjectSerializer(mapping)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class RemoveLaborFromProjectView(APIView):
    def delete(self, request, project_id, labor_id):
        project = get_object_or_404(Project, id=project_id)
        labor = get_object_or_404(LaborManagement, id=labor_id)

        # Check if the laborer is assigned to this project
        mapping = LaborToProject.objects.filter(labor=labor, project=project).first()
        if not mapping:
            return Response({'error': 'Laborer is not assigned to this project.'}, status=status.HTTP_404_NOT_FOUND)

        mapping.delete()
        return Response({'message': 'Laborer removed from project successfully.'}, status=status.HTTP_200_OK)

class WorkDayListView(APIView):
    """
    List all workdays for a specific LaborToProject assignment.
    """
    def get(self, request, labor_to_project_id):
        labor_to_project = get_object_or_404(LaborToProject, id=labor_to_project_id)
        workdays = WorkDay.objects.filter(labor_to_project=labor_to_project)
        serializer = WorkDaySerializer(workdays, many=True)
        return Response(serializer.data)


class WorkDayCreateView(APIView):
    """
    Create a new workday entry for a LaborToProject assignment.
    """
    def post(self, request, labor_to_project_id):
        labor_to_project = get_object_or_404(LaborToProject, id=labor_to_project_id)
        data = request.data
        data['labor_to_project'] = labor_to_project.id  # Attach the labor_to_project to the data
        serializer = WorkDaySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Workday created successfully.', 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkDayUpdateView(APIView):
    """
    Update an existing workday entry.
    """
    def put(self, request, workday_id):
        workday = get_object_or_404(WorkDay, id=workday_id)
        serializer = WorkDaySerializer(workday, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Workday updated successfully.', 'data': serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkDayDeleteView(APIView):
    """
    Delete a specific workday entry.
    """
    def delete(self, request, workday_id):
        workday = get_object_or_404(WorkDay, id=workday_id)
        workday.delete()
        return Response(
            {'message': 'Workday deleted successfully.'},
            status=status.HTTP_204_NO_CONTENT
        )