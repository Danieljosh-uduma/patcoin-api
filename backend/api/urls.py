from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListCreate.as_view()),
    path('users/<str:ref_code>/', UserListCreate.as_view()),

    path('user/<int:pk>/', UserDetail.as_view()),
    
    path('profiles/', ProfileList.as_view()),
    path('profiles/<int:pk>/', ProfileView.as_view())
]