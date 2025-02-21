"""
Serializer for the User model.
Fields:
    - id: The unique identifier for the user.
    - username: The username of the user.
    - email: The email address of the user.
    - password: The password of the user.
    - referral_code: The referral code associated with the user.
Methods:
    - get_referral_code(obj): Returns the referral code of the user if it exists, otherwise returns None.
"""
"""
Serializer for the Profile model.
Fields:
    - id: The unique identifier for the profile.
    - username: The username of the associated user.
    - code: The code associated with the profile.
    - inviter: The username of the user who recommended this profile.
Methods:
    - get_username(obj): Returns the username of the associated user if it exists, otherwise returns None.
    - get_inviter(obj): Returns the username of the user who recommended this profile if it exists, otherwise returns None.
"""

from rest_framework import serializers
from.models import *


class UserSerializer(serializers.ModelSerializer):
    referral_code = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'referral_code']

    def get_referral_code(self, obj):
        if obj.referral_code is not None:
            return obj.referral_code
        else:
            return None

        

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