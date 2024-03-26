
from django.urls import path, include
from .api import *


app_name = 'users_api'
urlpatterns = [
    path('users/', UserAPIView.as_view(), name='users_api'),
    path('users_put/<int:pk>/', user_detail_view, name='users_put_api'),
   # path('', include('applications.users.routers')),
]