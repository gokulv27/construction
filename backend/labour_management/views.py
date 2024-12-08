from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import LaborManagement
from .serializers import LaborManagementSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import LaborManagement
from .serializers import LaborManagementSerializer

@api_view(['GET'])
def labor_list(request):
    labors = LaborManagement.objects.all()
    serializer = LaborManagementSerializer(labors, many=True)
    return Response({'data': serializer.data})

@api_view(['POST'])
def labor_create(request):
    serializer = LaborManagementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def labor_update(request, id):
    labor = get_object_or_404(LaborManagement, id=id)
    serializer = LaborManagementSerializer(labor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def labor_delete(request, id):
    labor = get_object_or_404(LaborManagement, id=id)
    labor.delete()
    return Response({'success': True}, status=status.HTTP_200_OK)

@api_view(['GET'])
def labor_list(request):
    labors = LaborManagement.objects.all()
    serializer = LaborManagementSerializer(labors, many=True)
    return Response({'data': serializer.data})

@api_view(['POST'])
def labor_create(request):
    serializer = LaborManagementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def labor_update(request, id):
    labor = get_object_or_404(LaborManagement, id=id)
    serializer = LaborManagementSerializer(labor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def labor_delete(request, id):
    labor = get_object_or_404(LaborManagement, id=id)
    labor.delete()
    return Response({'success': True}, status=status.HTTP_200_OK)
