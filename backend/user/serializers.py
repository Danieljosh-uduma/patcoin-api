from rest_framework import serializers
from.models import User


class UserSerializer(serializers.ModelSerializer):
    token_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'token_name']

    def get_token_name(self, obj):
        try:
            return obj.nickname
        except:
            return None