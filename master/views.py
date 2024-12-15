from django.shortcuts import get_object_or_404
from .models import DocumentType, VendorType, LaborSkill,UserRole
from .serializers import DocumentTypeSerializer, VendorTypeSerializer, LaborSkillSerializer,UserRoleSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


def create_or_update_instance(instance=None, serializer_class=None, data=None):
    """
    Handles creating or updating an instance using a serializer.
    """
    if instance:
        serializer = serializer_class(instance, data=data)
    else:
        serializer = serializer_class(data=data)

    if serializer.is_valid():
        obj = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED if not instance else status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---------------------------
# Document Type Views
# ---------------------------
@api_view(['GET'])
def document_type_list(request):
    document_types = DocumentType.objects.all()
    serializer = DocumentTypeSerializer(document_types, many=True)
    return Response({"success": True, "data": serializer.data})

@api_view(['POST'])
def document_type_create(request):
    return create_or_update_instance(serializer_class=DocumentTypeSerializer, data=request.data)

@api_view(['PUT'])
def document_type_update(request, id):
    document_type = get_object_or_404(DocumentType, id=id)
    return create_or_update_instance(instance=document_type, serializer_class=DocumentTypeSerializer, data=request.data)

@api_view(['DELETE'])
def document_type_delete(request, id):
    document_type = get_object_or_404(DocumentType, id=id)
    document_type.delete()
    return Response({"success": True, "message": "Document type deleted successfully"}, status=status.HTTP_200_OK)

# ---------------------------
# Vendor Type Views
# ---------------------------
@api_view(['GET'])
def vendor_type_list(request):
    vendor_types = VendorType.objects.all()
    serializer = VendorTypeSerializer(vendor_types, many=True)
    return Response({"success": True, "data": serializer.data})

@api_view(['POST'])
def vendor_type_create(request):
    return create_or_update_instance(serializer_class=VendorTypeSerializer, data=request.data)

@api_view(['PUT'])
def vendor_type_update(request, id):
    vendor_type = get_object_or_404(VendorType, id=id)
    return create_or_update_instance(instance=vendor_type, serializer_class=VendorTypeSerializer, data=request.data)

@api_view(['DELETE'])
def vendor_type_delete(request, id):
    vendor_type = get_object_or_404(VendorType, id=id)
    vendor_type.delete()
    return Response({"success": True, "message": "Vendor type deleted successfully"}, status=status.HTTP_200_OK)

# ---------------------------
# Labor Skill Views
# ---------------------------
@api_view(['GET'])
def labor_skill_list(request):
    labor_skills = LaborSkill.objects.all()
    serializer = LaborSkillSerializer(labor_skills, many=True)
    return Response({"success": True, "data": serializer.data})

@api_view(['POST'])
def labor_skill_create(request):
    return create_or_update_instance(serializer_class=LaborSkillSerializer, data=request.data)

@api_view(['PUT'])
def labor_skill_update(request, id):
    labor_skill = get_object_or_404(LaborSkill, id=id)
    return create_or_update_instance(instance=labor_skill, serializer_class=LaborSkillSerializer, data=request.data)

@api_view(['DELETE'])
def labor_skill_delete(request, id):
    labor_skill = get_object_or_404(LaborSkill, id=id)
    labor_skill.delete()
    return Response({"success": True, "message": "Labor skill deleted successfully"}, status=status.HTTP_200_OK)

# ---------------------------
# User Role Views
# ---------------------------


@api_view(['GET'])
def user_role_list(request):
    user_roles = UserRole.objects.all()
    serializer = UserRoleSerializer(user_roles, many=True)
    return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def user_role_create(request):
    return create_or_update_instance(serializer_class=UserRoleSerializer, data=request.data)


@api_view(['PUT'])
def user_role_update(request, id):
    user_role = get_object_or_404(UserRole, id=id)
    return create_or_update_instance(instance=user_role, serializer_class=UserRoleSerializer, data=request.data)


@api_view(['DELETE'])
def user_role_delete(request, id):
    user_role = get_object_or_404(UserRole, id=id)
    user_role.delete()
    return Response({"success": True, "message": "UserRole deleted successfully"}, status=status.HTTP_200_OK)