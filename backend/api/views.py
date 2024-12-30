from rest_framework import generics
from user.models import *
from user.serializers import *


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        ref_code = self.kwargs.get('ref_code')
        user = serializer.save(referral_code=ref_code)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        # get individual object by referral code
        ref_code = self.kwargs.get('ref_code')
        
        if ref_code:
            user = User.objects.filter(profile__code__iexact=ref_code)
            return user if user.exists() else User.objects.all()
        
        return User.objects.all()


class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    