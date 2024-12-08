from rest_framework import serializers  # Add this import
from .models import User

class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username',  'phone', 'role', 'status', 'created_at', 'updated_at']

class UserCreateSerializer(UserBaseSerializer):
    class Meta(UserBaseSerializer.Meta):
        fields = UserBaseSerializer.Meta.fields + ['password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

   

    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            username=validated_data['username'],
            phone=validated_data.get('phone'),
            role=validated_data['role'],
            status=validated_data['status'],
            created_by=validated_data.get('created_by')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
