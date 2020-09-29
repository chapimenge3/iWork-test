from django.shortcuts import render
from django.contrib.auth.models import User



# DRF imports 
from rest_framework import (permissions, mixins, viewsets)
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework import permissions


# My App Imports
from .serializers import UserSerializer , ItemSerializer
from .models import Item
class CreateUserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def perform_create(self, serializer):
        user = serializer.save()
        token = Token.objects.get_or_create(user=user)
        user = serializer.save(token=token[0])
class ItemViewset(viewsets.ModelViewSet):
    '''
    viewset.Modelviewset provide us the whole crud and automatic url generation
    '''
    queryset = Item.objects.all()
    serializer_class = ItemSerializer 
    permission_classes = [permissions.IsAuthenticated]
    