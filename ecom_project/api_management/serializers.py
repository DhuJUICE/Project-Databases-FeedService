from rest_framework import serializers
from project_management.models import PROJECT
from django.contrib.auth.models import User
from client_management.models import CLIENT

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PROJECT
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)  # related_name='projects'

    class Meta:
        model = CLIENT
        fields = ['id', 'name', 'type', 'projects']