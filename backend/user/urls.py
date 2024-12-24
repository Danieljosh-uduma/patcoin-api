from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListCreateView.as_view()),
    # path('list/', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view())
]