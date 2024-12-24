from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
