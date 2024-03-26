from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User
from .serializers import UserSerializer, UserListSerializer


class UserAPIView(APIView):
   
    def get(self,request):
      
        users = User.objects.all()
        users_serializer = UserListSerializer(users, many=True)

        return Response(users_serializer.data)
    
   
@api_view(['GET', 'PUT',])
def user_detail_view(request, pk=None):
    user = User.objects.get(id=pk)

    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        if request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)