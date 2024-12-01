# masters/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from .models import EmployeeType 
from .forms import EmployeeType
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


# # Vendor Type List View
# @require_http_methods(["GET"])
# def vendor_type_list(request):
#     vendor_types = vendortype.objects.all()
#     return render(request, 'masters/vendor_type_list.html', {'vendor_types': vendor_types})

# # Vendor Type Create View
# @require_http_methods(["POST"])
# def vendor_type_create(request):
#     name = request.POST.get('name', '').strip()  # Remove whitespace
#     if not name:
#         return JsonResponse({'error': 'Name cannot be empty.'}, status=400)
#     vendor_type = vendortype.objects.create(name=name)
#     return JsonResponse({
#         'id': vendor_type.id,
#         'name': vendor_type.name,
#         'created_at': vendor_type.created_at,
#         'updated_at': vendor_type.updated_at
#     })

# # Vendor Type Update View
# @require_http_methods(["POST"])
# def vendor_type_update(request, id):
#     vendor_type = get_object_or_404(vendortype, id=id)
#     name = request.POST.get('name', '').strip()
#     if not name:
#         return JsonResponse({'error': 'Name cannot be empty.'}, status=400)
#     vendor_type.name = name
#     vendor_type.save()
#     return JsonResponse({
#         'id': vendor_type.id,
#         'name': vendor_type.name,
#         'created_at': vendor_type.created_at,
#         'updated_at': vendor_type.updated_at
#     })

# # Vendor Type Delete View
# @require_http_methods(["POST"])
# def vendor_type_delete(request, id):
#     vendor_type = get_object_or_404(vendortype, id=id)
#     vendor_type.delete()
#     return JsonResponse({'success': True})

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