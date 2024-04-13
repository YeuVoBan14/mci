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
class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    def validate_old_password(self, value):
        user_id = self.context.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
        except (User.DoesNotExist, ValueError):
            raise serializers.ValidationError("User not found or invalid ID")

        if not user.check_password(value):
            raise serializers.ValidationError("Incorrect old password")
        return value
    
#     {
#     "old_password": "current_password",
#     "new_password": "new_password"
# }