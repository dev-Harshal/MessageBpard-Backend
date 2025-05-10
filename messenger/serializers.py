from rest_framework import serializers
from messenger.models import Message

class MessageSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Message
        fields = '__all__'


class MessageDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['body']
