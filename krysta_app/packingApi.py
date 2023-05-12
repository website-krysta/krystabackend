
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
from .models import user,RawMaterial,Vendor,Damaged ,Addrawmaterial,Product,ProductDetails,PackingMaterial,PackingDetails
from .serializers import UserSerializer,meterialSerializer,VendorSerializer,AddrawmaterialSerializer,\
                         DamagedSerializer,ProductlSerializer,PackingSerializer,PackingDetailsSerializer


current_date = datetime.datetime.now().date()
current_date_time = datetime.datetime.now()


#packing material API ########################################
@api_view(['GET','POST'])
def getPacking(request):
    if request.method == 'GET':
        queryset = PackingMaterial.objects.all()
        serializer_data = PackingSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addPacking(request):
    if request.method == 'POST':
        packing_data = PackingSerializer(data = request.data)
        if packing_data.is_valid():
            packing_data.save()
            return Response(packing_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(packing_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def getPackingItem(request,id):
    if request.method == 'GET':
        queryset = PackingMaterial.objects.filter(PackingMaterialID=id)
        serializer_data = PackingSerializer(queryset ,many=True)
        return Response(serializer_data.data)


    
@api_view(['POST'])
def addPackingDetails(request):
    if request.method == 'POST':
        max_value = Damaged.objects.aggregate(max_value=Max('DamgeID'))
        max_value = max_value['max_value']+1
        key_to_get = 'DamgeID'
        request.data[key_to_get] = max_value
        set_difference = 'DamagedQty'
        request.data[set_difference] = int(request.data['OrderedQuantity']) - int(request.data['ReceivedQuantity'])
   
        #set data 
        get_t_date = 'TransactionDate'
        request.data[get_t_date] = current_date_time
        get_add_time = 'AddedTimestamp'
        request.data[get_add_time] = current_date_time
        get_update_time = 'UpdatedTimestamp'
        request.data[get_update_time] = current_date_time
        los_amount = request.data['LossofAmount']
        if los_amount == "":
            request.data['LossofAmount'] = 0
        danaged_data = DamagedSerializer(data = request.data)
        if danaged_data.is_valid():
            danaged_data.save()
            print(danaged_data)
        # update PACKING total qty
        Mid = request.data['PackingMaterialID']
        queryset = PackingMaterial.objects.get(PackingMaterialID=Mid)
        queryset.TotalQuantity = int(queryset.TotalQuantity) + int(request.data['ReceivedQuantity'])
        serializer_data = PackingSerializer(instance=queryset, data=queryset.__dict__)
        if serializer_data.is_valid():
            serializer_data.save()
            
        packingmeterial_data = PackingDetailsSerializer(data = request.data)
        if packingmeterial_data.is_valid():
            packingmeterial_data.save()
            return Response(packingmeterial_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(packingmeterial_data.errors, status=status.HTTP_400_BAD_REQUEST)