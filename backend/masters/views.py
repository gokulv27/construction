from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmployeeType
from .serializers import EmployeeTypeSerializer

@api_view(['GET'])
def employee_type_list(request):
    """List all employee types."""
    employee_types = EmployeeType.objects.all()
    serializer = EmployeeTypeSerializer(employee_types, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def employee_type_create(request):
    """Create a new employee type."""
    serializer = EmployeeTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user.username if request.user.is_authenticated else 'Anonymous')
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
def employee_type_update(request, id):
    """Update an existing employee type."""
    employee_type = get_object_or_404(EmployeeType, id=id)
    serializer = EmployeeTypeSerializer(employee_type, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(updated_by=request.user.username if request.user.is_authenticated else 'Anonymous')
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def employee_type_delete(request, id):
    """Delete an existing employee type."""
    employee_type = get_object_or_404(EmployeeType, id=id)
    employee_type.delete()
    return Response({'message': f'Employee type "{employee_type.name}" deleted successfully.'}, status=200)
