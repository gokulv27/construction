from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import LaborManagement
from .serializers import LaborManagementSerializer
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"message": "CSRF cookie set."})

@api_view(['GET'])
def labor_list(request):
    labors = LaborManagement.objects.all()
    serializer = LaborManagementSerializer(labors, many=True)
    csrf_token = get_token(request)  # Generate CSRF token
    return Response({'csrfToken': csrf_token, 'data': serializer.data})



# POST: Create a new labor record
@csrf_protect
@api_view(['POST'])
def labor_create(request):
    serializer = LaborManagementSerializer(data=request.data)
    if serializer.is_valid():   
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT: Update an existing labor record
@api_view(['PUT'])
def labor_update(request, id):
    labor = get_object_or_404(LaborManagement, id=id)
    serializer = LaborManagementSerializer(labor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE: Delete a labor record
@api_view(['DELETE'])
def labor_delete(request, id):
    labor = get_object_or_404(LaborManagement, id=id)
    labor.delete()
    return Response({'success': True}, status=status.HTTP_200_OK)
