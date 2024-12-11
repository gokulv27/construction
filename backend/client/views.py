from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer

@api_view(['GET'])
def client_list(request):
    """
    Retrieve all clients.
    """
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def client_create(request):
    """
    Create a new client. Ensures `name` (first_name + last_name) is unique.
    """
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        # Validate uniqueness of name (first_name + last_name)
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        name = f"{first_name} {last_name}"
        if Client.objects.filter(name=name).exists():
            return Response(
                {"error": "A client with this full name already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Save the client
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def client_update(request, id):
    """
    Update an existing client. Ensures `name` (first_name + last_name) is unique.
    """
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(client, data=request.data)
    if serializer.is_valid():
        # Validate uniqueness of name (first_name + last_name)
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        name = f"{first_name} {last_name}"
        if Client.objects.filter(name=name).exclude(id=client.id).exists():
            return Response(
                {"error": "A client with this full name already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Save the updated client
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def client_delete(request, id):
    """
    Delete a client.
    """
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
