from rest_framework import serializers
from home.models import User,Job

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name', 'birth', 'school', 'hometown', 'email']
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'