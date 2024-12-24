import json
from django.shortcuts import render
from user.models import User
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.serializers import UserSerializer


# Create your views here.
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF api view for users model
    get random user data
    """ 
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # print(serializer.data)
        # data = serializer.validated_data
        serializer.save()
        return Response(serializer.validated_data)
    # data = request.data
    # instance = User.objects.all().order_by('?').first()
    # data = {}
    # if instance:
    #     data = UserSerializer(instance).data
    return Response({'error': 'Invalid data'}, status=400)