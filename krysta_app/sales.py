
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max

from django.core import serializers
from django.conf import settings
import datetime



from rest_framework import generics
from .models import SalesInvoice,Sales,SalesDetails,Vendor,Production,Formula
from .serializers import SalesInvoiceSerializer,SalesSerializer,SalesDetailsSerializer,FormulaSerializer


current_date = datetime.datetime.now().date()
current_date_time = datetime.datetime.now()

####################  formulaMaterial API ########################################
@api_view(['GET'])
def getSalesInvoice(request):
    if request.method == 'GET':
        queryset = SalesInvoice.objects.all()
        serializer_data = SalesInvoiceSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['GET'])
def getSalesInvoice_ID_Data(request,id):
    if request.method == 'GET':
        queryset = SalesInvoice.objects.get(InvoiceID=id)
        serializer_data = SalesInvoiceSerializer(queryset)
        return Response(serializer_data.data)

@api_view(['POST'])
def addSalesInvoiceData(request):
    if request.method == 'POST':
        max_value = SalesInvoice.objects.aggregate(max_value=Max('InvoiceID'))
        max_value = max_value['max_value']+1
        key_to_get = 'InvoiceID'
        request.data[key_to_get] = max_value
        vendordata = Vendor.objects.get(VendorID=int(request.data["VendorID"]))
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
        serializer_data = SalesInvoiceSerializer(data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)

#sales table apis 
@api_view(['GET'])
def getSales(request):
    if request.method == 'GET':
        queryset = Sales.objects.all()
        serializer_data = SalesSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['GET'])
def getSales_ID_Data(request,id):
    if request.method == 'GET':
        queryset = Sales.objects.get(InvoiceID=id)
        serializer_data = SalesSerializer(queryset)
        return Response(serializer_data.data)
    
@api_view(['POST'])
def addSalesData(request):
    if request.method == 'POST':
        values = list(request.data['productioninfo'].values())
        alternative_values = values[::2]  # Get alternative values using slicing
        sum_tot_amount = sum(int(value) for value in alternative_values) 
        max_value = Sales.objects.aggregate(max_value=Max('SalesID'))
        max_value = max_value['max_value']+1
        sales_data = {
            "SalesID": max_value,
            'TotalProducts':str(len(request.data['productIdata'])),
            'TotalAmount' :str(sum_tot_amount),
            'TransactionDate' :current_date_time,
            'InvoiceID' :request.data['salsedata']['InvoiceID'],
            'VendorID' :request.data['salsedata']['VendorID'],
            'AddedTimeStamp':current_date_time,
            'UpdatedTimeStamp':current_date_time
        }
        serializer_data = SalesSerializer(data=sales_data)
        if serializer_data.is_valid():
            serializer_data.save()

        for item in request.data['productIdata']:
            queryset = Production.objects.get(ProductionID=item["productId"])
            formulaId = queryset.FormulaID_id
            salesid = sales_data['SalesID']
            pairs = list(request.data['productioninfo'].items())[:2]  
            first_two_pairs = dict(pairs)  
            two_pairs = list(first_two_pairs.values())
            amount = two_pairs[0]
            qty = two_pairs[1]
            del request.data['productioninfo'][pairs[0][0]] 
            del request.data['productioninfo'][pairs[1][0]]

            salesDetails_data = {
                    "ID": 0,
                    "Quantity": qty,
                    "Price": amount,
                    "AddedTimeStamp": current_date_time,
                    "UpdatedTimeStamp": current_date_time,
                    "FormulaID": formulaId,
                    "SalesID": salesid
            }
            # queryset = Formula.objects.get(FormulaID=salesDetails_data["FormulaID"])
            serializer_info = SalesDetailsSerializer(data=salesDetails_data)
            if serializer_info.is_valid():
                serializer_info.save()
                queryset = Formula.objects.get(FormulaID=salesDetails_data["FormulaID"])
                queryset.TotalSaledQty = qty
                formula_serializer = FormulaSerializer(instance=queryset, data=queryset.__dict__)
                if formula_serializer.is_valid():
                    formula_serializer.save()
                
        return Response(serializer_data.data)

@api_view(['GET'])
def getSalesdetails(request):
    if request.method == 'GET':
        queryset = SalesDetails.objects.all()
        serializer_data = SalesDetailsSerializer(queryset ,many=True)
        return Response(serializer_data.data)