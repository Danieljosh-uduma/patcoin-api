from rest_framework import generics
from user.models import *
from user.serializers import *


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        ref_code = self.kwargs.get('ref_code')
        ref = self.request.content_params
        print(ref)
        if ref_code:
            user = User.objects.filter(profile__code__iexact=ref_code)
            return user if user.exists() else User.objects.all()
        
        return User.objects.all()

    
    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    