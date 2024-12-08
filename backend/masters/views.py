from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EmployeeType, DocumentType, VendorType, LaborSkill
from .serializers import LaborSkillSerializer

# ---------------------------
# Employee Type Views
# ---------------------------

# GET: List all employee types
def employee_type_list(request):
    if request.method == 'GET':
        employee_types = EmployeeType.objects.all()
        data = [
            {
                'id': et.id,
                'name': et.name,
                'created_at': et.created_at,
                'updated_at': et.updated_at
            }
            for et in employee_types
        ]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Invalid Request'}, status=400)


# POST: Create a new employee type
@api_view(['POST'])
def employee_type_create(request):
    name = request.data.get('name', '').strip()
    if not name:
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

    employee_type = EmployeeType.objects.create(name=name)
    return Response({
        'id': employee_type.id,
        'name': employee_type.name,
        'created_at': employee_type.created_at,
        'updated_at': employee_type.updated_at
    }, status=status.HTTP_201_CREATED)


# PUT: Update an existing employee type
@api_view(['PUT'])
def employee_type_update(request, id):
    employee_type = get_object_or_404(EmployeeType, id=id)
    name = request.data.get('name', '').strip()

    if not name:
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

    employee_type.name = name
    employee_type.save()

    return Response({
        'id': employee_type.id,
        'name': employee_type.name,
        'created_at': employee_type.created_at,
        'updated_at': employee_type.updated_at
    }, status=status.HTTP_200_OK)


# DELETE: Delete an employee type
@csrf_exempt
@require_http_methods(["DELETE"])
def employee_type_delete(request, id):
    try:
        employee_type = get_object_or_404(EmployeeType, id=id)
        employee_type.delete()
        return JsonResponse({'success': True}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# ---------------------------
# Document Type Views
# ---------------------------

# GET: List all document types
def document_type_list(request):
    if request.method == 'GET':
        document_types = DocumentType.objects.all()
        data = [
            {
                'id': dt.id,
                'name': dt.name,
                'created_at': dt.created_at,
                'updated_at': dt.updated_at
            }
            for dt in document_types
        ]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Invalid Request'}, status=400)


# POST: Create a new document type
@api_view(['POST'])
def document_type_create(request):
    name = request.data.get('name', '').strip()
    if not name:
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

    document_type = DocumentType.objects.create(name=name)
    return Response({
        'id': document_type.id,
        'name': document_type.name,
        'created_at': document_type.created_at,
        'updated_at': document_type.updated_at
    }, status=status.HTTP_201_CREATED)


# PUT: Update an existing document type
@api_view(['PUT'])
def document_type_update(request, id):
    document_type = get_object_or_404(DocumentType, id=id)
    name = request.data.get('name', '').strip()

    if not name:
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

    document_type.name = name
    document_type.save()

    return Response({
        'id': document_type.id,
        'name': document_type.name,
        'created_at': document_type.created_at,
        'updated_at': document_type.updated_at
    }, status=status.HTTP_200_OK)


# DELETE: Delete a document type
@csrf_exempt
@require_http_methods(["DELETE"])
def document_type_delete(request, id):
    try:
        document_type = get_object_or_404(DocumentType, id=id)
        document_type.delete()
        return JsonResponse({'success': True}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# ---------------------------
# Vendor Type Views
# ---------------------------

# GET: List all vendor types
def vendor_type_list(request):
    if request.method == 'GET':
        vendor_types = VendorType.objects.all()
        data = [
            {
                'id': vt.id,
                'name': vt.name,
                'created_at': vt.created_at,
                'updated_at': vt.updated_at
            }
            for vt in vendor_types
        ]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Invalid Request'}, status=400)


# POST: Create a new vendor type
@api_view(['POST'])
def vendor_type_create(request):
    name = request.data.get('name', '').strip()
    if not name:
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

    vendor_type = VendorType.objects.create(name=name)
    return Response({
        'id': vendor_type.id,
        'name': vendor_type.name,
        'created_at': vendor_type.created_at,
        'updated_at': vendor_type.updated_at
    }, status=status.HTTP_201_CREATED)


# PUT: Update an existing vendor type
@api_view(['PUT'])
def vendor_type_update(request, id):
    vendor_type = get_object_or_404(VendorType, id=id)
    name = request.data.get('name', '').strip()

    if not name:
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

    vendor_type.name = name
    vendor_type.save()

    return Response({
        'id': vendor_type.id,
        'name': vendor_type.name,
        'created_at': vendor_type.created_at,
        'updated_at': vendor_type.updated_at
    }, status=status.HTTP_200_OK)


# DELETE: Delete a vendor type
@csrf_exempt
@require_http_methods(["DELETE"])
def vendor_type_delete(request, id):
    try:
        vendor_type = get_object_or_404(VendorType, id=id)
        vendor_type.delete()
        return JsonResponse({'success': True}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

# ---------------------------
# Labor Skill Views
# ---------------------------

# GET: List all labor skills
@api_view(['GET'])
def labor_skill_list(request):
    labor_skills = LaborSkill.objects.all()
    data = [
        {
            'id': skill.id,
            'name': skill.name,
            'created_at': skill.created_at,
            'updated_at': skill.updated_at
        }
        for skill in labor_skills
    ]
    return JsonResponse(data, safe=False)


# POST: Create a new labor skill
@api_view(['POST'])
def labor_skill_create(request):
    name = request.data.get('name', '').strip()
    if not name:
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

    labor_skill = LaborSkill.objects.create(name=name)
    return Response({
        'id': labor_skill.id,
        'name': labor_skill.name,
        'created_at': labor_skill.created_at,
        'updated_at': labor_skill.updated_at
    }, status=status.HTTP_201_CREATED)


# PUT: Update an existing labor skill
@api_view(['PUT'])
def labor_skill_update(request, id):
    labor_skill = get_object_or_404(LaborSkill, id=id)
    name = request.data.get('name', '').strip()

    if not name:
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

    labor_skill.name = name
    labor_skill.save()

    return Response({
        'id': labor_skill.id,
        'name': labor_skill.name,
        'created_at': labor_skill.created_at,
        'updated_at': labor_skill.updated_at
    }, status=status.HTTP_200_OK)


# DELETE: Delete a labor skill
@csrf_exempt
@require_http_methods(["DELETE"])
def labor_skill_delete(request, id):
    try:
        labor_skill = get_object_or_404(LaborSkill, id=id)
        labor_skill.delete()
        return JsonResponse({'success': True}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
