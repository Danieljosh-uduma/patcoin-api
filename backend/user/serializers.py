from rest_framework import serializers
from.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'recommended_by']

        

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    inviter = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'username', 'code', 'inviter']

    def get_username(self, obj):
        if obj.user is not None:
            return obj.user.username
        else:
            return None
            
    def get_inviter(self, obj):
        if obj.recommended_by is not None:
            return obj.recommended_by.username
        else:
            return None