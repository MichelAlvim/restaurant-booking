from rest_framework import serializers
from ..models.custom_user import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined']
        read_only_fields = ['id', 'is_active', 'date_joined']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            # Custom authenticate function to use email instead of username
            user = CustomUser.objects.filter(email=email).first()
            if user is not None and user.check_password(password):
                data['user'] = user
            else:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'")

        return data
