# masters/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from .models import EmployeeType,DocumentType,VendorType
from .forms import EmployeeType,DocumentType,VendorType
from django import forms
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST

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

@api_view(['PUT'])  # Use PUT for updates
def employee_type_update(request, id):
    try:
        # Fetch the existing EmployeeType object
        employee_type = EmployeeType.objects.get(id=id)
    except EmployeeType.DoesNotExist:
        return Response({'error': 'Employee type not found.'}, status=status.HTTP_404_NOT_FOUND)

    name = request.data.get('name', '').strip()

    if not name:
        return Response({'error': 'Name cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

    # Update the employee type
    employee_type.name = name
    employee_type.save()  # Save the changes

    return Response({
        'id': employee_type.id,
        'name': employee_type.name,
        'created_at': employee_type.created_at,
        'updated_at': employee_type.updated_at
    }, status=status.HTTP_200_OK)   

@csrf_exempt  # Only for development if CSRF issues arise
@require_http_methods(["DELETE"])
def employee_type_delete(request, id):
    try:
        # Get the object or return 404 if it doesn't exist
        employee_type = get_object_or_404(EmployeeType, id=id)
        employee_type.delete()
        return JsonResponse({'success': True}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


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
    try:
        document_type = DocumentType.objects.get(id=id)
    except DocumentType.DoesNotExist:
        return Response({'error': 'Document type not found.'}, status=status.HTTP_404_NOT_FOUND)

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
@csrf_exempt  # Only for development if CSRF issues arise
@require_http_methods(["DELETE"])
def document_type_delete(request, id):
    try:
        document_type = get_object_or_404(DocumentType, id=id)
        document_type.delete()
        return JsonResponse({'success': True}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
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
    try:
        vendor_type = VendorType.objects.get(id=id)
    except VendorType.DoesNotExist:
        return Response({'error': 'Vendor type not found.'}, status=status.HTTP_404_NOT_FOUND)

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
@csrf_exempt  # Only for development if CSRF issues arise
@require_http_methods(["DELETE"])
def vendor_type_delete(request, id):
    try:
        vendor_type = get_object_or_404(VendorType, id=id)
        vendor_type.delete()
        return JsonResponse({'success': True}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# # Brand Type Views

# def brand_type_list(request):
#     brand_types = BrandType.objects.all()
#     return render(request, 'masters/brand_type_list.html', {'brand_types': brand_types})

# def brand_type_create(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '').strip()
#         if not name:
#             return JsonResponse({'error': 'Name cannot be empty.'}, status=400)
#         brand_type = BrandType.objects.create(name=name)
#         return JsonResponse({
#             'id': brand_type.id,
#             'name': brand_type.name,
#             'created_at': brand_type.created_at,
#             'updated_at': brand_type.updated_at
#         })
#     return JsonResponse({'error': 'Invalid Request'}, status=400)

# def brand_type_update(request, id):
#     if request.method == 'POST':
#         brand_type = get_object_or_404(BrandType, id=id)
#         name = request.POST.get('name')
#         brand_type.name = name
#         brand_type.save()
#         return JsonResponse({
#             'id': brand_type.id,
#             'name': brand_type.name,
#             'created_at': brand_type.created_at,
#             'updated_at': brand_type.updated_at
#         })
#     return JsonResponse({'error': 'Invalid Request'}, status=400)

# def brand_type_delete(request, id):
#     if request.method == 'POST':
#         brand_type = get_object_or_404(BrandType, id=id)
#         brand_type.delete()
#         return JsonResponse({'success': True})
#     return JsonResponse({'error': 'Invalid Request'}, status=400)

# # employee_rolles Views

# def employee_rolles_list(request):
#     employee_rolles = EmployeeRolles.objects.all()
#     return render(request, 'masters/employee_rolles_list.html', {'employee_rolles': employee_rolles})

# def employee_rolles_create(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         employee_rolle = EmployeeRolles.objects.create(name=name)
#         return JsonResponse({
#             'id': employee_rolle.id,
#             'name': employee_rolle.name,
#             'created_at': employee_rolle.created_at,
#             'updated_at': employee_rolle.updated_at
#         })
#     return JsonResponse({'error': 'Invalid Request'}, status=400)

# def employee_rolles_update(request, id):
#     if request.method == 'POST':
#         employee_rolle = get_object_or_404(EmployeeRolles, id=id)
#         name = request.POST.get('name')
#         employee_rolle.name = name
#         employee_rolle.save()
#         return JsonResponse({
#             'id': employee_rolle.id,
#             'name': employee_rolle.name,
#             'created_at': employee_rolle.created_at,
#             'updated_at': employee_rolle.updated_at
#         })
#     return JsonResponse({'error': 'Invalid Request'}, status=400)

# def employee_rolles_delete(request, id):
#     if request.method == 'POST':
#         employee_rolle = get_object_or_404(EmployeeRolles, id=id)
#         employee_rolle.delete()
#         return JsonResponse({'success': True})
#     return JsonResponse({'error': 'Invalid Request'}, status=400)

# # Iteam Views

# def item_list(request):
#     """View to list all items and populate the brand dropdown."""
#     items = Item.objects.all()
#     brand_types = BrandType.objects.all()  # Fetch all brands
#     return render(request, 'masters/item_list.html', {
#         'items': items,
#         'brand_types': brand_types  # Pass the brands to the template
#     })

# @require_POST
# def item_create(request):
#     name = request.POST.get('name', '').strip()  # Remove whitespace
#     brand_id = request.POST.get('brand', '').strip()  # Ensure brand_id is not null

#     if not name:
#         return HttpResponseBadRequest("Name cannot be empty.")
#     if not brand_id:
#         return HttpResponseBadRequest("Brand is required.")

#     # Ensure the brand exists
#     try:
#         brand = BrandType.objects.get(id=brand_id)
#     except BrandType.DoesNotExist:
#         return HttpResponseBadRequest("Invalid Brand.")

#     # Create the item
#     item = Item.objects.create(name=name, brand=brand)
#     return JsonResponse({
#         'id': item.id,
#         'name': item.name,
#         'brand_name': item.brand.name,
#         'created_at': item.created_at,
#         'updated_at': item.updated_at
#     })

# def item_update(request, id):
#     if request.method == 'POST':
#         item = get_object_or_404(Item, id=id)
#         name = request.POST.get('name', '').strip()
#         brand_id = request.POST.get('brand', '').strip()

#         if not name:
#             return JsonResponse({'error': 'Name cannot be empty.'}, status=400)
#         if not brand_id:
#             return JsonResponse({'error': 'Brand is required.'}, status=400)

#         brand = get_object_or_404(BrandType, id=brand_id)

#         item.name = name
#         item.brand = brand
#         item.save()
#         return JsonResponse({
#             'id': item.id,
#             'name': item.name,
#             'brand_name': item.brand.name,
#             'created_at': item.created_at,
#             'updated_at': item.updated_at
#         })
#     return JsonResponse({'error': 'Invalid Request'}, status=400)

# # Delete an item
# def item_delete(request, id):
#     """View to delete an item."""
#     if request.method == 'POST':
#         item = get_object_or_404(Item, id=id)
#         item.delete()
#         return JsonResponse({'success': True})
#     return JsonResponse({'error': 'Invalid Request'}, status=400)