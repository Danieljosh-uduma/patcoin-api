import json
from django.shortcuts import render
from user.models import User
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    model_data = User.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'username', 'email'])
        # json.dumps(data)
    
    return Response(data)