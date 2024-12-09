from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LaborManagement
from .serializers import LaborManagementSerializer

@api_view(['GET'])
def labor_list(request):
    labors = LaborManagement.objects.select_related('skill').all()
    serializer = LaborManagementSerializer(labors, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def labor_create(request):
    serializer = LaborManagementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def labor_update(request, id):
    try:
        labor = LaborManagement.objects.get(id=id)
    except LaborManagement.DoesNotExist:
        return Response({'error': 'Labor not found'}, status=404)

    serializer = LaborManagementSerializer(labor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def labor_delete(request, id):
    try:
        labor = LaborManagement.objects.get(id=id)
    except LaborManagement.DoesNotExist:
        return Response({'error': 'Labor not found'}, status=404)

    labor.delete()
    return Response(status=204)
