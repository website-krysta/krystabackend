
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
from .models import Formula,FormulaMaterials,RawMaterial
from .serializers import FormulaSerializer,FormulaMaterialsSerializer


current_date = datetime.datetime.now().date()
current_date_time = datetime.datetime.now()


#formula API ########################################
@api_view(['GET'])
def getformula(request):
    if request.method == 'GET':
        queryset = Formula.objects.all()
        serializer_data = FormulaSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addformula(request):
    if request.method == 'POST':
        max_value = Formula.objects.aggregate(max_value=Max('ID'))
        max_value = max_value['max_value']+1

        formula_name = request.data['formulaname']['FormulaName']
        del request.data['formulaname']["FormulaName"]
        count_of_material = len(request.data['formulaname'])   
        mtqty= request.data['formulaname']  
        material_qty  = list(mtqty.values())
        #formula add
        formula = {
        'ID': 0,
        'FormulaName': '',
        'TotalMaterialsUsed':'',
        'AddedTimeStamp': '',
        'UpdatedTimeStamp': ''
        }

        formula['ID'] = max_value
        formula['FormulaName']= formula_name
        formula['TotalMaterialsUsed']= count_of_material
        formula['AddedTimeStamp']= "2023-04-19T06:10:14Z"
        formula['UpdatedTimeStamp']= "2023-04-19T06:10:14Z"
   
        aFormula_obj = []      

        for x, y in zip(request.data['materialiData'],material_qty):
            mid = x['materialid']
            qty = y[0]
            #formula with material
            formula_material = {
            "ID": 0,
            "Quantity": "",
            "AddedTimeStamp": "2023-04-20T07:58:34Z",
            "UpdatedTimeStamp": "2023-04-20T07:58:34Z",
            "RawMaterialID": 1,
            "FormulaID": 1
            }

            formula_material['ID'] = 0
            formula_material['Quantity']= qty
            formula_material['AddedTimeStamp']= "2023-04-19T06:10:14Z"
            formula_material['UpdatedTimeStamp']= "2023-04-19T06:10:14Z"
            formula_material['RawMaterialID']= mid
            formula_material['FormulaID']= max_value
            aFormula_obj.append(formula_material)

        formula_data = FormulaSerializer( data=formula)
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
    