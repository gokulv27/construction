from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserBaseSerializer, UserCreateSerializer


# Custom pagination to allow a client-defined page size
class CustomUserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50  # Limit maximum page size


class UserListView(generics.ListAPIView):
    """
    Endpoint to list all users.
    """
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Allow authenticated users only
    permission_classes = [] 
    pagination_class = CustomUserPagination

    def get_queryset(self):
        """
        Optionally filter users based on query parameters like username.
        """
        queryset = super().get_queryset()
        username = self.request.query_params.get('username', None)
        if username:
            queryset = queryset.filter(username__icontains=username)
        return queryset


class UserCreateView(generics.CreateAPIView):
    """
    Endpoint to create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # permission_classes = [permissions.IsAdminUser]  # Allow admin users only
    permission_classes = [] 

    def create(self, request, *args, **kwargs):
        """
        Custom create method to handle responses and validation better.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "User created successfully", "user": serializer.data},
            status=status.HTTP_201_CREATED
        )


class UserDetailView(generics.RetrieveAPIView):
    """
    Endpoint to retrieve a single user's details.
    """
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [] 

class UserUpdateView(generics.UpdateAPIView):
    """
    Endpoint to update a user.
    """
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer
    # permission_classes = [permissions.IsAdminUser]  # Allow admin users only
    permission_classes = [] 
    def update(self, request, *args, **kwargs):
        """
        Custom update method to handle responses better.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "User updated successfully", "user": serializer.data},
            status=status.HTTP_200_OK
        )


class UserDeleteView(generics.DestroyAPIView):
    """
    Endpoint to delete a user.
    """
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [] 
    def destroy(self, request, *args, **kwargs):
        """
        Custom delete method to handle responses better.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "User deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
