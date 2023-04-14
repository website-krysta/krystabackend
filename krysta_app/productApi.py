
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
from .models import user,RawMaterial,Vendor,Damaged ,Addrawmaterial,Product,ProductDetails
from .serializers import UserSerializer,meterialSerializer,VendorSerializer,AddrawmaterialSerializer,\
                         DamagedSerializer,ProductlSerializer,ProductlDetailsSerializer


current_date = datetime.datetime.now().date()
current_date_time = datetime.datetime.now()


#Raw Meterial API ########################################


@api_view(['GET','POST'])
def getProduct(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer_data = ProductlSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addProduct(request):
    if request.method == 'POST':
        product_data = ProductlSerializer(data = request.data)
        if product_data.is_valid():
            product_data.save()
            return Response(product_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(product_data.errors, status=status.HTTP_400_BAD_REQUEST)
    


    
@api_view(['POST'])
def addProductDetails(request):
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

        danaged_data = DamagedSerializer(data = request.data)
        if danaged_data.is_valid():
            danaged_data.save()
            print(danaged_data)
        # update ramaterial total qty
        Mid = request.data['ProductID']
        queryset = Product.objects.get(ProductID=Mid)
        queryset.TotalQuantity = int(queryset.TotalQuantity) + int(request.data['ReceivedQuantity'])
        serializer_data = ProductlSerializer(instance=queryset, data=queryset.__dict__)
        if serializer_data.is_valid():
            serializer_data.save()
            
        ProductlDetails_data = ProductlDetailsSerializer(data = request.data)
        if ProductlDetails_data.is_valid():
            ProductlDetails_data.save()
            return Response(ProductlDetails_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(ProductlDetails_data.errors, status=status.HTTP_400_BAD_REQUEST)