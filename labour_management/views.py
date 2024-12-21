from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LaborManagement, LaborTransaction, WorkDay
from .serializers import LaborManagementSerializer, LaborTransactionSerializer, WorkDaySerializer
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    LaborManagementSerializer,
    AdHocEmployeeSerializer,
    WorkDaySerializer,
    LaborTransactionSerializer
)
from .models import (
    LaborManagement,
    AdHocEmployee,
    WorkDay,
    LaborTransaction
)

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
        return Response("successfully labor is created", status=201)
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

# AdHocEmployee Views
@api_view(['GET'])
def adhoc_employee_list(request):
    adhoc_employees = AdHocEmployee.objects.select_related('labor', 'project').all()
    serializer = AdHocEmployeeSerializer(adhoc_employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def adhoc_employee_create(request):
    serializer = AdHocEmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def adhoc_employee_update(request, id):
    try:
        adhoc_employee = AdHocEmployee.objects.get(id=id)
    except AdHocEmployee.DoesNotExist:
        return Response({'error': 'AdHocEmployee not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AdHocEmployeeSerializer(adhoc_employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def adhoc_employee_delete(request, id):
    try:
        adhoc_employee = AdHocEmployee.objects.get(id=id)
    except AdHocEmployee.DoesNotExist:
        return Response({'error': 'AdHocEmployee not found'}, status=status.HTTP_404_NOT_FOUND)

    adhoc_employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# WorkDay Views
@api_view(['GET'])
def workday_list(request):
    workdays = WorkDay.objects.select_related('labor_to_project', 'adhoc_employee').all()
    serializer = WorkDaySerializer(workdays, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def workday_create(request):
    serializer = WorkDaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def workday_update(request, id):
    try:
        workday = WorkDay.objects.get(id=id)
    except WorkDay.DoesNotExist:
        return Response({'error': 'WorkDay not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = WorkDaySerializer(workday, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def workday_delete(request, id):
    try:
        workday = WorkDay.objects.get(id=id)
    except WorkDay.DoesNotExist:
        return Response({'error': 'WorkDay not found'}, status=status.HTTP_404_NOT_FOUND)

    workday.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
# List all transactions
@api_view(['GET'])
def labor_transaction_list(request):
    transactions = LaborTransaction.objects.select_related('labor_to_project').all()
    serializer = LaborTransactionSerializer(transactions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create a new transaction
@api_view(['POST'])
def labor_transaction_create(request):
    serializer = LaborTransactionSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"error": f"Unexpected error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Update an existing transaction
@api_view(['PUT'])
def labor_transaction_update(request, id):
    try:
        transaction = LaborTransaction.objects.get(id=id)
    except LaborTransaction.DoesNotExist:
        return Response(
            {'error': 'LaborTransaction not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = LaborTransactionSerializer(transaction, data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': f'Unexpected error: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a transaction
@api_view(['DELETE'])
def labor_transaction_delete(request, id):
    try:
        transaction = LaborTransaction.objects.get(id=id)
    except LaborTransaction.DoesNotExist:
        return Response(
            {'error': 'LaborTransaction not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    transaction.delete()
    return Response(
        {'message': f'LaborTransaction with ID {id} deleted successfully'},
        status=status.HTTP_204_NO_CONTENT
    )