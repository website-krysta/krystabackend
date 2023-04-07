
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your jwt token .
# import jwt 
from django.conf import settings



from rest_framework import generics
from .models import user,RawMaterial
from .serializers import UserSerializer,meterialSerializer

@api_view(['GET','POST'])
def UserList(request):
    if request.method == 'GET':
        queryset = user.objects.all()
        serializer_data = UserSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    elif request.method == 'POST':
        queryset = user.objects.all().values()
        userdata = UserSerializer(data = request.data)
        # userdata.is_valid(raise_exception=True)
        # username = user_data.validated_data['EmailID']
        # password = user_data.validated_data['Password']
        if not userdata.is_valid():
            for fields in queryset:
                if fields['EmailID'] == userdata.initial_data['EmailID'] and fields['Password'] == userdata.initial_data['Password']:
                        print('login sucessfully')
                        # Generate the JWT token
                        # token_data_obj = user.objects.get(UserID=userdata.initial_data['EmailID'])
                        # token = jwt.encode(token_data_obj, settings.SECRET_KEY, algorithm='HS256')
                        return Response(userdata.initial_data, status=status.HTTP_200_OK)
                        
                        
                #return Response(userdata.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(userdata.errors, status=status.HTTP_400_BAD_REQUEST)


     

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
     


#Raw Meterial API ########################################


@api_view(['GET','POST'])
def getmaterials(request):
    if request.method == 'GET':
        queryset = RawMaterial.objects.all()
        serializer_data = meterialSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addmaterial(request):
    if request.method == 'POST':
        meterial_data = meterialSerializer(data = request.data)
        if meterial_data.is_valid():
            meterial_data.save()
            return Response(meterial_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(meterial_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def updatematerial(request,id):
    if request.method == 'POST':
        queryset = RawMaterial.objects.get(MaterialID=id)
        serializer_data = meterialSerializer(instance=queryset ,data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)
     

@api_view(['GET'])
def getmaterial(request,id):
    if request.method == 'GET':
        queryset = RawMaterial.objects.get(MaterialID=id)
        serializer_data = meterialSerializer(queryset ,many=False)
        return Response(serializer_data.data)
     
@api_view(['DELETE'])
def deletematerial(request,id):
    if request.method == 'DELETE':
        queryset = RawMaterial.objects.get(MaterialID=id)
        queryset.delete()
        return Response('meterial item delet sucessfully!')
     