from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = User
        fields = [ 'token' ]
        
        def create(self, validated_data):
            '''
            Override the create method of this to create user
            '''
            user = User.objects.create(
            username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
            return user
        