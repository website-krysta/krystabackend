
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from rest_framework import generics
from .models import user
from .serializers import UserSerializer

@api_view(['GET','POST'])
def UserList(request):
    if request.method == 'GET':
        queryset = user.objects.all()
        serializer_data = UserSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    elif request.method == 'POST':
        queryset = user.objects.all().values()
        user_data = UserSerializer(data = request.data)
        for fields in queryset:
            if ((fields['EmailID'] == user_data.initial_data['EmailID'])  and (fields['Password'] == user_data.initial_data['Password'])):
                print('login sucessfully')
               
                return Response(user_data.initial_data, status=status.HTTP_200_OK)
            
            return Response(user_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Useradd(request):
    if request.method == 'POST':
        user_data = UserSerializer(data = request.data)
        if user_data.is_valid():
            user_data.save()
            return Response(user_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(user_data.errors, status=status.HTTP_400_BAD_REQUEST)
     
@api_view(['POST'])
def Userupdate(request,id):
    if request.method == 'POST':
        queryset = user.objects.get(UserID=id)
        serializer_data = UserSerializer(instance=queryset ,data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)
     

@api_view(['GET'])
def getUserdate(request,id):
    if request.method == 'GET':
        queryset = user.objects.get(UserID=id)
        serializer_data = UserSerializer(queryset ,many=False)
        return Response(serializer_data.data)
     
@api_view(['DELETE'])
def deleteUser(request,id):
    if request.method == 'DELETE':
        queryset = user.objects.get(UserID=id)
        queryset.delete()
        return Response('item delet sucessfully!')
     