from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import UserBaseSerializer, UserCreateSerializer
from rest_framework.pagination import PageNumberPagination

class CustomUserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer
    pagination_class = CustomUserPagination
    permission_classes = []

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer
    permission_classes = []

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = []

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer
    permission_classes = []
