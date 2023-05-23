
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
        queryset = Product.objects.all().order_by('-AddedTimestamp')
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
    
@api_view(['GET'])
def getProducItem(request,id):
    if request.method == 'GET':
        queryset = Product.objects.filter(ProductID=id)
        serializer_data = ProductlSerializer(queryset ,many=True)
        return Response(serializer_data.data)

@api_view(['GET'])
def getProducDetails_item(request,id):
    if request.method == 'GET':
        queryset = ProductDetails.objects.filter(Id=id)
        serializer_data = ProductlDetailsSerializer(queryset ,many=True)
        return Response(serializer_data.data)

    
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
        los_amount = request.data['LossofAmount']
        if los_amount == "":
            request.data['LossofAmount'] = 0
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
    
#update packeing details
@api_view(['POST'])
def Update_whitelabel_Details(request):
    if request.method == 'POST':
        damaged_data = request.data['damaged']
        productDetails_data = request.data['productItem']
        product = request.data['product']

        detail_product_id = request.data['productItem']['Id']
        raw_product_id = request.data['product']['ProductID']
        damage_item_id = request.data['damaged']['DamgeID']

        #damaged table
        damaged_data['DamagedQty'] = int(productDetails_data['OrderedQuantity']) - int(productDetails_data['ReceivedQuantity'])
        queryset = Damaged.objects.get(DamgeID=damage_item_id)
        serializer_data = DamagedSerializer(instance=queryset ,data = damaged_data)
        if serializer_data.is_valid():
            serializer_data.save()
          

        # update ramaterial total qty
        queryset = Product.objects.get(ProductID=raw_product_id)
        serializer_data = ProductlSerializer(instance=queryset, data=product)
        if serializer_data.is_valid():
            serializer_data.save()

        request.data['productItem']['UpdatedTimestamp'] = current_date_time
        queryset = ProductDetails.objects.get(Id = detail_product_id)
        meterial_data = ProductlDetailsSerializer(instance=queryset, data = productDetails_data)
        if meterial_data.is_valid():
            meterial_data.save()
            return Response(meterial_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(meterial_data.errors, status=status.HTTP_400_BAD_REQUEST)