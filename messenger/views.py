from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from messenger.models import Message
from messenger.serializers import MessageSerializer ,MessageDetailsSerializer

class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('-created_at')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)

class MessageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all().order_by('-created_at')
    serializer_class = MessageDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        user_messages = self.request.user.messages.all()
        return user_messages

