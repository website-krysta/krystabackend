
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max

from django.core import serializers
import json
# Create your jwt token .
# import jwt 
# from jose import jwt
from django.conf import settings
import datetime



from rest_framework import generics
from django.db.models import F
from .models import Formula,FormulaMaterials,RawMaterial,Category
from .serializers import FormulaSerializer,FormulaMaterialsSerializer,FormulaCategorySerializer


current_date = datetime.datetime.now().date()
current_date_time = datetime.datetime.now()


#formula API ########################################
@api_view(['GET'])
def getformula(request):
    if request.method == 'GET':
        queryset = Formula.objects.all().order_by('-FormulaID')
        serializer_data = FormulaSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['GET'])
def getProductionformula(request):
    if request.method == 'GET':
        queryset = Formula.objects.filter(TotalProductionQty__gt=F('TotalSaledQty'))
        serializer_data = FormulaSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addformula(request):
    if request.method == 'POST':
        max_value = Formula.objects.aggregate(max_value=Max('FormulaID'))
        if max_value['max_value'] == None:
            max_value = 1
        else:
            max_value = max_value['max_value']+1

        formula_name = request.data['formulaname']['FormulaName']
        del request.data['formulaname']["FormulaName"]
        count_of_material = len(request.data['formulaname'])   
        mtqty= request.data['formulaname']  
        CategoryId = request.data['formulaname']['category'] 
        material_qty  = list(mtqty.values())
        #formula add
        formula = {
        'FormulaID': 0,
        'FormulaName': '',
        'TotalMaterialsUsed':'',
        'Category':"",
        'AddedTimeStamp': '',
        'UpdatedTimeStamp': ''
        }

        formula['FormulaID'] = max_value
        formula['FormulaName']= formula_name
        formula['TotalMaterialsUsed']= count_of_material
        formula['Category']= CategoryId
        formula['AddedTimeStamp']= current_date_time
        formula['UpdatedTimeStamp']= current_date_time
   
        aFormula_obj = []      

        for x, y in zip(request.data['materialiData'],material_qty):
            mid = x['materialid']
            qty = y
            #formula with material
            formula_material = {
            "ID": 0,
            "Quantity": "",
            "AddedTimeStamp": "",
            "UpdatedTimeStamp": "",
            "MaterialID": 1,
            "FormulaID": 1
            }

            formula_material['ID'] = 0
            formula_material['Quantity']= qty
            formula_material['AddedTimeStamp']= current_date_time
            formula_material['UpdatedTimeStamp']= current_date_time
            formula_material['MaterialID']= mid
            formula_material['FormulaID']= max_value
            aFormula_obj.append(formula_material)
       
        formula_data = FormulaSerializer( data=formula)
        existingformulaName = Formula.objects.filter(FormulaName=formula['FormulaName']).exists()
        if existingformulaName:
            return Response({'error': 'Formula Name already exists'},status=status.HTTP_226_IM_USED)
        if formula_data.is_valid():
            formula_data.save()
            for fmobj in aFormula_obj: 
                formulamaterial_data = FormulaMaterialsSerializer(data = fmobj)
                if formulamaterial_data.is_valid():
                    formulamaterial_data.save()
            return Response(formula_data.initial_data, status=status.HTTP_201_CREATED)
        
        
        return Response(formula_data.errors, status=status.HTTP_400_BAD_REQUEST)

#formulaMaterial API ########################################
@api_view(['GET'])
def getformulamaterial(request):
    if request.method == 'GET':
        queryset = FormulaMaterials.objects.all()
        serializer_data = FormulaMaterialsSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['GET'])
def getformula_ID_Data(request,id):
    if request.method == 'GET':
        queryset = FormulaMaterials.objects.filter(FormulaID=id)
        serializer_data = FormulaMaterialsSerializer(queryset, many=True)
        return Response(serializer_data.data)

    
@api_view(['POST'])
def addformulamaterial(request):
    if request.method == 'POST':
        formulamaterial_data = FormulaMaterialsSerializer(data = request.data)
        if formulamaterial_data.is_valid():
            formulamaterial_data.save()
            return Response(formulamaterial_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(formulamaterial_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getFormulaCategory(request):
    if request.method == 'GET':
        queryset = Category.objects.all()
        serializer_data = FormulaCategorySerializer(queryset ,many=True)
        return Response(serializer_data.data)
    