
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max


# Create your jwt token .
# import jwt 
from django.conf import settings
import datetime



from rest_framework import generics
from .models import Labour
from .serializers import LabourSerializer


current_date = datetime.datetime.now().date()
current_date_time = datetime.datetime.now()


#Raw Meterial API ########################################


@api_view(['GET','POST'])
def getLabour(request):
    if request.method == 'GET':
        queryset = Labour.objects.all()
        serializer_data = LabourSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addLabour(request):
    if request.method == 'POST':
        labour_data = LabourSerializer(data = request.data)
        if labour_data.is_valid():
            labour_data.save()
            return Response(labour_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(labour_data.errors, status=status.HTTP_400_BAD_REQUEST)
    