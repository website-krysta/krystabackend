
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max


# Create your jwt token .
# import jwt 
# from jose import jwt 
from django.conf import settings
import datetime



from rest_framework import generics
from .models import user,RawMaterial,Vendor,Damaged ,Addrawmaterial,Invoice
from .serializers import UserSerializer,meterialSerializer,VendorSerializer,AddrawmaterialSerializer,\
                         DamagedSerializer,InvoiceSerializer


current_date = datetime.datetime.now().date()
current_date_time = datetime.datetime.now()


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
                    
                        #audir app
                        # encoded_jwt = jwt.encode(
                        #     {"exp": exp, "nbf": now, "sub": email}, settings.SECRET_KEY, algorithm="HS256",
                        # )
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
     
#vendor API ########################################
@api_view(['GET'])
def getvendorlist(request):
    if request.method == 'GET':
        queryset = Vendor.objects.all()
        serializer_data = VendorSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addvendor(request):
    if request.method == 'POST':
        meterial_data = VendorSerializer(data = request.data)
        if meterial_data.is_valid():
            meterial_data.save()
            return Response(meterial_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(meterial_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getvendor(request,id):
    if request.method == 'GET':
        queryset = Vendor.objects.get(VendorID=id)
        serializer_data = VendorSerializer(queryset ,many=False)
        return Response(serializer_data.data)
     

#Damaged API ########################################
@api_view(['GET'])
def getdamagedlist(request):
    if request.method == 'GET':
        queryset = Damaged.objects.all()
        serializer_data = DamagedSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def adddamageditem(request):
    if request.method == 'POST':
        danaged_data = DamagedSerializer(data = request.data)
        if danaged_data.is_valid():
            danaged_data.save()
            return Response(danaged_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(danaged_data.errors, status=status.HTTP_400_BAD_REQUEST)

#Raw Meterial API ########################################
@api_view(['GET'])
def getAddrawmaterial(request):
    if request.method == 'GET':
        queryset = Addrawmaterial.objects.all()
        serializer_data = AddrawmaterialSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['GET'])
def getrawmaterial(request,id):
    if request.method == 'GET':
        print(id)
        queryset = Addrawmaterial.objects.get(Id=id)
        serializer_data = AddrawmaterialSerializer(queryset ,many=False)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addRawmaterial(request):
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
        Mid = request.data['MaterialID']
        queryset = RawMaterial.objects.get(MaterialID=Mid)
        queryset.TotalQuantity = int(queryset.TotalQuantity) + int(request.data['ReceivedQuantity'])
        serializer_data = meterialSerializer(instance=queryset, data=queryset.__dict__)
        if serializer_data.is_valid():
            serializer_data.save()
            
        meterial_data = AddrawmaterialSerializer(data = request.data)
        if meterial_data.is_valid():
            meterial_data.save()
            return Response(meterial_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(meterial_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

#invoiceAPI ########################################

@api_view(['GET'])
def getinvoices(request):
    if request.method == 'GET':
        queryset = Invoice.objects.all()
        serializer_data = InvoiceSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addinvoice(request):
    if request.method == 'POST':
        max_value = Invoice.objects.aggregate(max_value=Max('ID'))
        max_value = max_value['max_value']+1
        key_to_get = 'ID'
        request.data[key_to_get] = max_value
        id = request.data['VendorID']
        vendordata = Vendor.objects.get(VendorID=id)
        invoice_date = request.data['InvoiceDate']
        date_obj = date_obj = datetime.datetime.strptime(invoice_date, "%Y-%m-%d")
        formatted_date_str = date_obj.strftime("%d-%b-%Y")
        data_string = formatted_date_str.replace('-', '')
        inwardno = 'InwardNumber'
        request.data[inwardno] = f"{data_string}-{vendordata.VendorCode}"  
        get_add_time = 'AddedTimeStamp'
        request.data[get_add_time] = current_date_time
        get_update_time = 'UpdatedTimeStamp'
        request.data[get_update_time] = current_date_time

        invoice_data = InvoiceSerializer(data = request.data)
        if invoice_data.is_valid():
            invoice_data.save()
            print(invoice_data)
            return Response(invoice_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(invoice_data.errors, status=status.HTTP_400_BAD_REQUEST)