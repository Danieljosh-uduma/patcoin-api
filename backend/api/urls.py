from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<str:ref_code>/', UserList.as_view()),

    
    path('users/register/new-user/<str:ref_code>/', UserCreate.as_view()),
    path('users/register/new-user/', UserCreate.as_view()),

    path('user/<int:pk>/', UserDetail.as_view()),
    
    path('profiles/', ProfileList.as_view()),
    path('profiles/<int:pk>/', ProfileView.as_view())
]