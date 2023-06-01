
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
from .models import Production,Formula,FormulaMaterials,ProductionDetails,ProductionPacking,RawMaterial,PackingMaterial,\
                    ProductionDamage
from .serializers import ProductionSerializer,ProductionDetailsSerializer,PaackingDetailsSerializer,meterialSerializer,\
                         PackingSerializer,FormulaSerializer,view_Production_Serializer,Production_Damage_Serializer


current_date = datetime.datetime.now().date()
current_date_time = datetime.datetime.now()

###############################################

@api_view(['GET'])
def getProduction(request):
    if request.method == 'GET':
        queryset = Production.objects.all()
        serializer_data = ProductionSerializer(queryset ,many=True)
        return Response(serializer_data.data)

#production details
@api_view(['GET'])
def getProductionDetails(request):
    if request.method == 'GET':
        queryset = ProductionDetails.objects.all()
        serializer_data = ProductionDetailsSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addProduction(request):
    if request.method == 'POST':
        request.data['ProductionID'] = int(request.data['ProductionID'])
        request.data['TransactionDate'] = current_date_time
        request.data['AddedTimeStamp'] = current_date_time
        request.data['UpdatedTimeStamp'] = current_date_time
        production_data = ProductionSerializer(data = request.data)
        if production_data.is_valid():
            production_data.save()
            queryset = Formula.objects.get(FormulaID=request.data['FormulaID'])
            queryset.TotalProductionQty = queryset.TotalProductionQty + int(request.data['ProductionQuantity'])
            serializer_data = FormulaSerializer(instance=queryset,data = queryset.__dict__)
            if serializer_data.is_valid():
                serializer_data.save()
            return Response(production_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(production_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addProduction_Packing(request):
    if request.method == 'POST':
        request.data
        production_details = {  
                'Pro_detailsID':0,	
                'ProductionID' :'',	
                'MaterialID'  :'',	
                'Quantity':'',	
                'AddedTimeStamp':'',		
                'UpdatedTimeStamp' :''
        }
        packing_details = {
                'production_packing_ID':0,	
                'ProductionID':'',	
                'PackingMaterialID' :'',	
                'Quantity' :'',	
                'AddedTimeStamp':'',	
                'UpdatedTimeStamp':''
        }
        FormulaID = int(request.data['productionData']['FormulaID'])
        aMaterial_item = FormulaMaterials.objects.filter(FormulaID=FormulaID)
        for oMaterial in aMaterial_item:
            production_details['ProductionID']= int(request.data['productionData']['ProductionID'])
            production_details['MaterialID']= oMaterial.MaterialID_id
            production_details['Quantity']= str(oMaterial.Quantity)
            production_details['AddedTimeStamp']= current_date_time
            production_details['UpdatedTimeStamp']= current_date_time
            production_data = ProductionDetailsSerializer(data = production_details)
            if production_data.is_valid():
                production_data.save()
                aMaterial_item = RawMaterial.objects.filter(MaterialID = oMaterial.MaterialID_id)
                for materialItem in aMaterial_item:
                    materialItem.ConsumedQuantity +=  int(oMaterial.Quantity)/100 * int(request.data["productionData"]["ProductionQuantity"])
                    serializer_data = meterialSerializer(instance=materialItem, data=materialItem)
                    if serializer_data.is_valid():
                        serializer_data.save()
                        
                    
 
        packing_item = list(request.data['packingQty'].items())
        for item in packing_item:
            packing_details['ProductionID']= int(request.data['productionData']['ProductionID'])
            packing_details['PackingMaterialID']= item[0]
            packing_details['Quantity']= item[1]
            packing_details['AddedTimeStamp']= current_date_time
            packing_details['UpdatedTimeStamp']= current_date_time
            x = packing_details
            packingdata_data = PaackingDetailsSerializer(data = packing_details)
            if packingdata_data.is_valid():
                packingdata_data.save()
                pass
                aPacking_item = PackingMaterial.objects.filter(PackingMaterialID = item[0])
                for packingItem in aPacking_item:
                    packingItem.ConsumedQuantity += int(item[1])
                    serializer_data = PackingSerializer(instance=packingItem, data=packingItem.__dict__)
                    if serializer_data.is_valid():
                        serializer_data.save()
    return Response(packingdata_data.initial_data, status=status.HTTP_201_CREATED)
            
@api_view(['GET'])
def getProductiondetails(request):
    if request.method == 'GET':
        queryset = ProductionDamage.objects.all()
        serializer_data = Production_Damage_Serializer(queryset ,many=True)
        return Response(serializer_data.data)

@api_view(['POST'])
def addProductionDamagedData(request):
     if request.method == 'POST':
        damage_obj = {
            'ProductionDamageID':2,
            'DamagedQuantity': "",
            'DamageReason': "",
            'LossPrice': "",
            'ID':'',
            'AddedTimeStamp':'',
            'UpdatedTimeStamp':'',
        }
        damage_obj['DamagedQuantity'] = int(request.data["damaged"]['DamagedQuantity'])
        damage_obj['DamageReason'] = request.data["damaged"]['DamageReason']
        damage_obj['LossPrice'] = int(request.data["damaged"]['LossPrice'])
        damage_obj['ID']=request.data["salseid"]
        damage_obj['AddedTimeStamp']=current_date_time
        damage_obj['UpdatedTimeStamp']=current_date_time

        serializer_data = Production_Damage_Serializer(data = damage_obj)
        if serializer_data.is_valid():
            serializer_data.save()
            print(damage_obj)
        return Response(serializer_data.data)
           
            
from rest_framework import generics
# from rest_framework.generics import RetrieveAPIView
class productioninfo_view(generics.ListCreateAPIView):
    queryset =Production.objects.all()
    serializer_class = view_Production_Serializer
    lookup_field = 'ProductionID'