
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max


# Create your jwt token .
# import jwt 
# from jose import jwt 
from django.conf import settings
import datetime

# views.py
from rest_framework import generics

from rest_framework import generics
from .models import user,RawMaterial,Vendor,Damaged ,Addrawmaterial,Invoice,FormulaMaterials,ProductDetails,PackingDetails,Formula,Production,\
                    ProductionPacking
from .serializers import UserSerializer,meterialSerializer,VendorSerializer,AddrawmaterialSerializer,\
                         DamagedSerializer,InvoiceSerializer,joinmaterialSerializer,joinProductionFormulaSerializer,\
                         joinProductionSerializer,joinPackingSerializer,formulaMaterial_detailsSerializer,join_FormulaSerializer,\
                            viewProductionFormulaSerializer,production_packing_details_join_Serializer


current_date = datetime.datetime.now().date()
current_date_time = datetime.datetime.now()


@api_view(['GET','POST'])
def UserList(request):
    if request.method == 'GET':
        queryset = user.objects.filter(UserStatus=True)
        serializer_data = UserSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    elif request.method == 'POST':
        queryset = user.objects.all().values()
        useriem = user.objects.get(EmailID=request.data['EmailID'])
        user_details = {  
                'UserID':0,	
                'EmailID' :'',	
                'Password'  :'',	
                'Role':'',	
                'UserStatus':'',		
        }
        user_details['UserID'] = useriem.UserID
        user_details['EmailID'] = useriem.EmailID
        user_details['Password'] = useriem.Password
        user_details['Role'] = useriem.Role
        user_details['UserStatus'] = useriem.UserStatus

        # userdata = UserSerializer(data = user_details)
        serializer_data = UserSerializer(instance=useriem ,data = user_details)
        if serializer_data.is_valid():
            for fields in queryset:
                if fields['EmailID'] ==  user_details['EmailID'] and fields['Password'] ==  user_details['Password']:
                        print('login sucessfully')
                        # Generate the JWT token
                        # token_data_obj = user.objects.get(UserID=userdata.initial_data['EmailID'])
                        # token = jwt.encode(token_data_obj, settings.SECRET_KEY, algorithm='HS256')
                    
                        #audir app
                        # encoded_jwt = jwt.encode(
                        #     {"exp": exp, "nbf": now, "sub": email}, settings.SECRET_KEY, algorithm="HS256",
                        # )
                        return Response(serializer_data.data, status=status.HTTP_200_OK)
                        
                        
                #return Response(userdata.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer_data.data.errors, status=status.HTTP_400_BAD_REQUEST)


     

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
     
@api_view(['POST'])
def deleteUser(request,id):
    if request.method == 'POST':
        queryset = user.objects.get(UserID=id)
        queryset.UserStatus = False
        user_details = {  
                'UserID':0,	
                'EmailID' :'',	
                'Password'  :'',	
                'Role':'',	
                'UserStatus':'',		
        }
        user_details['UserID'] = queryset.UserID
        user_details['EmailID'] = queryset.EmailID
        user_details['Password'] = queryset.Password
        user_details['Role'] = queryset.Role
        user_details['UserStatus'] = queryset.UserStatus
       
        serializer_data = UserSerializer(instance=queryset ,data = user_details)
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)
     
    

#Raw Meterial API ########################################

@api_view(['GET','POST'])
def getmaterials(request):
    if request.method == 'GET':
        queryset = RawMaterial.objects.all().order_by('-MaterialID')
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
        queryset = RawMaterial.objects.filter(MaterialID=id)
        serializer_data = meterialSerializer(queryset ,many=True)
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


@api_view(['GET'])
def getDamagedItem(request,id):
    if request.method == 'GET':
        queryset = Damaged.objects.filter(DamgeID=id)
        serializer_data = DamagedSerializer(queryset ,many=True)
        return Response(serializer_data.data)
     

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

    
@api_view(['GET'])
def getrawmaterialStock(request,id):
    if request.method == 'GET':
        queryset = Addrawmaterial.objects.filter(MaterialID=id)
        serializer_data = AddrawmaterialSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
 #this api is useing  in stock module  
@api_view(['GET'])
def getrawmaterial_list(request,id):
    if request.method == 'GET':
        queryset = Addrawmaterial.objects.filter(Id=id)
        serializer_data = AddrawmaterialSerializer(queryset ,many=True)
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
        los_amount = request.data['LossofAmount']
        if los_amount == "":
            request.data['LossofAmount'] = 0
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


#update addrawmaterial
@api_view(['POST'])
def UpdateRawmaterialDetails(request):
    if request.method == 'POST':
        damaged_data = request.data['damaged']
        materialDetails_data = request.data['materialDetails']
        rawmaterial_data = request.data['rawmaterial']

        detail_material_id = request.data['materialDetails']['Id']
        raw_material_id = request.data['rawmaterial']['MaterialID']
        damage_item_id = request.data['damaged']['DamgeID']

        #damaged table
        damaged_data['DamagedQty'] = int(materialDetails_data['OrderedQuantity']) - int(materialDetails_data['ReceivedQuantity'])
        queryset = Damaged.objects.get(DamgeID=damage_item_id)
        serializer_data = DamagedSerializer(instance=queryset ,data = damaged_data)
        if serializer_data.is_valid():
            serializer_data.save()
          

        # update ramaterial total qty
        queryset = RawMaterial.objects.get(MaterialID=raw_material_id)
        serializer_data = meterialSerializer(instance=queryset, data=rawmaterial_data)
        if serializer_data.is_valid():
            serializer_data.save()

        request.data['materialDetails']['UpdatedTimestamp'] = current_date_time
        queryset = Addrawmaterial.objects.get(Id = detail_material_id)
        x = request.data['materialDetails']['UpdatedTimestamp']
        meterial_data = AddrawmaterialSerializer(instance=queryset, data = materialDetails_data)
        if meterial_data.is_valid():
            meterial_data.save()
            return Response(meterial_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(meterial_data.errors, status=status.HTTP_400_BAD_REQUEST)


#invoiceAPI ########################################

@api_view(['GET'])
def getinvoices(request):
    if request.method == 'GET':
        queryset = Invoice.objects.all().order_by('-AddedTimeStamp')
        serializer_data = InvoiceSerializer(queryset ,many=True)
        return Response(serializer_data.data)

@api_view(['GET'])
def getInvoiceData(request,id):
    if request.method == 'GET':
        queryset = Invoice.objects.get(InvoiceID=id)
        serializer_data = InvoiceSerializer(queryset)
        return Response(serializer_data.data)

@api_view(['POST'])
def addinvoice(request):
    if request.method == 'POST':
        max_value = Invoice.objects.aggregate(max_value=Max('InvoiceID'))
        max_value = max_value['max_value']+1
        key_to_get = 'InvoiceID'
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
        reciveddata = request.data['RecievedDate']
        if reciveddata == "":
            request.data['RecievedDate']= "0001-01-01"
        Invoice_Number = request.data['InvoiceNumber']
        existinginvoice = Invoice.objects.filter(InvoiceNumber=Invoice_Number).exists()
        if existinginvoice:
            return Response({'error': 'Invoice number already exists'},status=status.HTTP_226_IM_USED)

        invoice_data = InvoiceSerializer(data = request.data)
        if invoice_data.is_valid():
            invoice_data.save()
            return Response(invoice_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(invoice_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def UpdateInvoiceData(request,id):
    if request.method == 'POST':
        queryset = Invoice.objects.get(InvoiceID=id)
        serializer_data = InvoiceSerializer(instance=queryset,data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)

# join tables views

from rest_framework import generics
class MaterialViewSet(generics.ListCreateAPIView):
    queryset =Addrawmaterial.objects.all().order_by('-AddedTimestamp')
    serializer_class = joinmaterialSerializer
    lookup_field = 'MaterialID'


from rest_framework.generics import RetrieveAPIView
class materialDetail(RetrieveAPIView):
    queryset =Addrawmaterial.objects.all()
    serializer_class = joinmaterialSerializer
    lookup_field = 'MaterialID'

       
#fro formula productions 
class ProductionMaterialViewSet(generics.ListCreateAPIView):
    queryset =FormulaMaterials.objects.all()
    serializer_class = joinProductionFormulaSerializer
    # lookup_field = 'MaterialID'


#whitelabeling join tables 
class WhitelabelingViewSet(generics.ListCreateAPIView):
    queryset =ProductDetails.objects.all()
    serializer_class = joinProductionSerializer
    lookup_field = 'ProductID'

#packing join tables 
class PackingViewSet(generics.ListCreateAPIView):
    queryset =PackingDetails.objects.all()
    serializer_class = joinPackingSerializer
    lookup_field = 'PackingMaterialID'

#packing join product + formula
class Formula_Material_ViewSet(generics.ListCreateAPIView):
    queryset =FormulaMaterials.objects.all().order_by('-AddedTimeStamp')
    serializer_class = formulaMaterial_detailsSerializer
    lookup_field = 'FormulaID'

#view table  fro production  join production + formula
class Production_Formula_ViewSet(generics.ListCreateAPIView):
    queryset =Production.objects.all()
    serializer_class = viewProductionFormulaSerializer
    lookup_field = 'FormulaID'

#view table  fro production  join production + packing materials
class Production_Formula_ViewSet(generics.ListCreateAPIView):
    queryset =Production.objects.all().order_by('-AddedTimeStamp')
    serializer_class = viewProductionFormulaSerializer
    lookup_field = 'FormulaID'

#view table  fro production  join production + packing materials
class Production_packing_ViewSet(generics.ListCreateAPIView):
    queryset =ProductionPacking.objects.all()
    serializer_class = production_packing_details_join_Serializer
    lookup_field = 'ProductionID'