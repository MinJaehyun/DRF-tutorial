from .serializers import UserSerializer
from .models import User
from rest_framework import generics


# CreateAPIView: 회원가입
class UserCreate(generics.CreateAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer