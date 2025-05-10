from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from users.serializers import UserCreateSerializer, UserProfileSerializer, UserDetailsView

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    
class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsView
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'username'
    
