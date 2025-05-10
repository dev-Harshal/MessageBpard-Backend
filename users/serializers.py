from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source='profile.display_name', required=False)
    bio = serializers.CharField(source='profile.bio', required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'display_name', 'bio']
        extra_kwargs = {'bio': {'style': {'base_template': 'textarea.html'}}}

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile_data = validated_data.get('profile', {})
        profile = instance.profile
        profile.display_name = profile_data.get('display_name', profile.display_name)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.save()

        return instance
      
        
class UserDetailsView(serializers.ModelSerializer):
    display_name = serializers.CharField(source='profile.display_name')
    bio = serializers.CharField(source='profile.bio')
    class Meta:
        model = User
        fields = ['username', 'email', 'display_name', 'bio']