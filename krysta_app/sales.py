
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
from .models import SalesInvoice,Sales,SalesDetails,Vendor,Production,Formula,SalesDamage,Product,BatchSale
from .serializers import SalesInvoiceSerializer,SalesSerializer,SalesDetailsSerializer,FormulaSerializer,ProductionSerializer,\
    join_SalesDetails_Serializer,SalesDamagedSerializer,ProductlSerializer,BatchSales_Serializer


current_date = datetime.datetime.now().date()
current_date_time = datetime.datetime.now()

####################  formulaMaterial API ########################################
@api_view(['GET'])
def getSalesInvoice(request):
    if request.method == 'GET':
        queryset = SalesInvoice.objects.all().order_by('-InvoiceID','-AddedTimeStamp')
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
            request.data['RecievedDate']= None
        Invoice_Number = request.data['InvoiceNumber']
        existinginvoice = SalesInvoice.objects.filter(InvoiceNumber=Invoice_Number).exists()
        if existinginvoice:
            return Response({'error': 'Invoice number already exists'},status=status.HTTP_226_IM_USED)
        serializer_data = SalesInvoiceSerializer(data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)
    
@api_view(['POST'])
def updateSalesInvoice_ID_Data(request):
    if request.method == 'POST':
        id =  request.data['InvoiceID']
        queryset = SalesInvoice.objects.get(InvoiceID=id)
        serializer_data = SalesInvoiceSerializer(instance=queryset , data=request.data)
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
        totAmount = 0
        for items in request.data['productioninfo']:
            totAmount += int(items['price'])
        max_value = Sales.objects.aggregate(max_value=Max('SalesID'))
        max_value = max_value['max_value']+1
        sales_data = {
            "SalesID": max_value,
            'TotalProducts':str(len(request.data['productIdata'])),
            'TotalAmount' :totAmount,
            'TransactionDate' :current_date_time,
            'InvoiceID' :request.data['salsedata']['InvoiceID'],
            'VendorID' :request.data['salsedata']['VendorID'],
            'AddedTimeStamp':current_date_time,
            'UpdatedTimeStamp':current_date_time
        }
        serializer_data = SalesSerializer(data=sales_data)
        if serializer_data.is_valid():
            serializer_data.save()

        for item,proInfo in zip(request.data['productIdata'],request.data['productioninfo']):
            # queryset = Production.objects.get(ProductionID=item["productId"])
            formulaId = item['productId']
            productname = item['productname']
            # avaQty = item['avaQty']
            salesid = sales_data['SalesID']
            if Formula.objects.filter(FormulaName=productname).exists():
                max_value = SalesDetails.objects.aggregate(max_value=Max('ID'))
                max_value = max_value['max_value']+1
                salesDetails_data = {
                    "ID": max_value,
                    "Quantity": int(proInfo["quantity"]),
                    "Price": int(proInfo["price"]),
                    "AddedTimeStamp": current_date_time,
                    "UpdatedTimeStamp": current_date_time,
                    "FormulaID": formulaId,
                    'ProductID':'',
                    "SalesID": salesid,
                    'Type':'Formula',
                }
                serializer_info = SalesDetailsSerializer(data=salesDetails_data)
                if serializer_info.is_valid():
                    serializer_info.save()
                    postBatchSales(salesDetails=salesDetails_data,batchsales=request.data['batch_info'])
                    queryset = Formula.objects.get(FormulaID=salesDetails_data["FormulaID"])
                    queryset.TotalSaledQty += int(proInfo["quantity"])
                    formula_serializer = FormulaSerializer(instance=queryset, data=queryset.__dict__)
                    if formula_serializer.is_valid():
                        formula_serializer.save()
            else:
                max_value = Sales.objects.aggregate(max_value=Max('ID'))
                max_value = max_value['max_value']+1
                salesDetails_data = {
                        "ID": max_value,
                        "Quantity": int(proInfo["quantity"]),
                        "Price": int(proInfo["price"]),
                        "AddedTimeStamp": current_date_time,
                        "UpdatedTimeStamp": current_date_time,
                        "FormulaID":"",
                        'ProductID':formulaId,
                        "SalesID": salesid,
                        'Type':'WhiteLabeling',
                }
                serializer_info = SalesDetailsSerializer(data=salesDetails_data)
                if serializer_info.is_valid():
                    serializer_info.save()
                    postBatchSales(salesDetails=salesDetails_data,batchsales=request.data['batch_info'])
                    queryset = Product.objects.get(ProductID=formulaId)
                    queryset.ConsumedQuantity += int(proInfo["quantity"])
                    formula_serializer = ProductlSerializer(instance=queryset, data=queryset.__dict__)
                    if formula_serializer.is_valid():
                        formula_serializer.save()
         
            # diff_qty= queryset.ProductionQuantity - int(proInfo["quantity"])
            # update_production = {
            #      'ProductionID'	:item["productId"],
            #      'TransactionDate':queryset.TransactionDate,
            #      'FormulaID' :queryset.FormulaID_id,
            #      'ProductionQuantity' :diff_qty,
            #      'AddedTimeStamp'	:queryset.AddedTimeStamp,
            #      'UpdatedTimeStamp':queryset.UpdatedTimeStamp
            # }
            # serializer_Info = ProductionSerializer(instance=queryset, data=update_production)
            # if serializer_Info.is_valid():
            #     serializer_Info.save()

            # serializer_info = SalesDetailsSerializer(data=salesDetails_data)
            # if serializer_info.is_valid():
            #     serializer_info.save()
            #     queryset = Formula.objects.get(FormulaID=salesDetails_data["FormulaID"])
            #     queryset.TotalSaledQty += int(proInfo["quantity"])
            #     formula_serializer = FormulaSerializer(instance=queryset, data=queryset.__dict__)
            #     if formula_serializer.is_valid():
            #         formula_serializer.save()
                
        return Response(serializer_data.data)

@api_view(['GET'])
def getSalesdetails(request):
    if request.method == 'GET':
        queryset = SalesDetails.objects.all()
        serializer_data = SalesDetailsSerializer(queryset ,many=True)
        return Response(serializer_data.data)

@api_view(['POST'])
def addSalesDamagedData(request):
     if request.method == 'POST':
        salse_obj = {
            'SalesDamageID':0,
            'DamagedQuantity': "",
            'DamageReason': "",
            'LossPrice': "",
            'ID':'',
            'AddedTimeStamp':'',
            'UpdatedTimeStamp':'',
        }
        salse_obj['DamagedQuantity'] = int(request.data["damaged"]['DamagedQuantity'])
        salse_obj['DamageReason'] = request.data["damaged"]['DamageReason']
        salse_obj['LossPrice'] = int(request.data["damaged"]['LossPrice'])
        salse_obj['ID']=int(request.data["salseid"])
        salse_obj['AddedTimeStamp']=current_date_time
        salse_obj['UpdatedTimeStamp']=current_date_time

        serializer_data = SalesDamagedSerializer(data = salse_obj)
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)

from rest_framework import generics
# from rest_framework.generics import RetrieveAPIView
class salesDetail_view(generics.ListCreateAPIView):
    queryset =SalesDetails.objects.all()
    serializer_class = join_SalesDetails_Serializer
    lookup_field = 'ID'

#Batch sales table apis 
@api_view(['GET'])
def getBatchSales(request):
    if request.method == 'GET':
        queryset = BatchSale.objects.all()
        serializer_data = BatchSales_Serializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['GET'])
def getBatchSales_ID(request,id):
    if request.method == 'GET':
        queryset = BatchSale.objects.get(BatchID=id)
        serializer_data = BatchSales_Serializer(queryset)
        return Response(serializer_data.data)
    
from itertools import groupby
def postBatchSales(salesDetails,batchsales):
    salesdata =  salesDetails
    batchdata = batchsales 
    remaningQty = ''
    sorted_batch_info = sorted(batchsales, key=lambda x: x['productname'])
    grouped_batch_info = [
        {'productname': key, 'batches': list(group)}
        for key, group in groupby(sorted_batch_info, key=lambda x: x['productname'])
        ]
    for item in grouped_batch_info:
        if item['productname'] == salesDetails['FormulaID']:
            if len(item["batches"]) == 1:
                batchno = item["batches"][0]['batchno']
                quantity = salesDetails['Quantity']
                ID = salesDetails['ID']
                batch_obj = {
                        'BatchID':0,
                        'BatchNo': batchno,
                        'Quantity': quantity,
                        'ID': ID,
                        'AddedTimeStamp':current_date_time,
                        'UpdatedTimeStamp':current_date_time,
                }
                serializer_data = BatchSales_Serializer(data=batch_obj)
                if serializer_data.is_valid():
                    serializer_data.save()
                Product_obj = Production.objects.get(BatchNo=batchno ,FormulaID=item['productname'])
                Product_obj.BatchQty += quantity
                product_data = {
                    "ProductionID":Product_obj.ProductionID,
                    "TransactionDate": str(Product_obj.TransactionDate),
                    "BatchNo": str(Product_obj.BatchNo),
                    "ProductionQuantity":str(Product_obj.ProductionQuantity),
                    "AddedTimeStamp": str(Product_obj.AddedTimeStamp),
                    "UpdatedTimeStamp": str(Product_obj.UpdatedTimeStamp),
                    "BatchQty":str(Product_obj.BatchQty),
                    "FormulaID": Product_obj.FormulaID_id
                }
                production_serializer = ProductionSerializer(instance=Product_obj, data=product_data)
                if production_serializer.is_valid():
                    production_serializer.save()
            else:
                x = item
                y = salesDetails
                ID = salesDetails['ID']
                for index,obj in enumerate(item['batches']):
                    if index == 0:
                        if obj['batchQty'] == None:
                            obj['batchQty'] = 0.0
                            avaliableQty = float(obj["productionQty"]) - obj['batchQty']
                        else:
                            avaliableQty = float(obj["productionQty"]) - float(obj['batchQty'])
                        if (salesDetails['Quantity'] >= avaliableQty):
                            batch_obj = {
                                    'BatchID':0,
                                    'BatchNo': obj['batchno'],
                                    'Quantity': avaliableQty,
                                    'ID': ID,
                                    'AddedTimeStamp':current_date_time,
                                    'UpdatedTimeStamp':current_date_time,
                            }
                            serializer_data = BatchSales_Serializer(data=batch_obj)
                            if serializer_data.is_valid():
                                serializer_data.save()
                            Product_obj = Production.objects.get(BatchNo=obj["batchno"] ,FormulaID=item['productname'])
                            product_data = {
                                "ProductionID":Product_obj.ProductionID,
                                "TransactionDate": str(Product_obj.TransactionDate),
                                "BatchNo": str(Product_obj.BatchNo),
                                "ProductionQuantity":str(Product_obj.ProductionQuantity),
                                "AddedTimeStamp": str(Product_obj.AddedTimeStamp),
                                "UpdatedTimeStamp":str(Product_obj.UpdatedTimeStamp),
                                "BatchQty":str(avaliableQty),
                                "FormulaID":Product_obj.FormulaID_id
                            }
                            production_serializer = ProductionSerializer(instance=Product_obj, data=product_data)
                            if production_serializer.is_valid():
                                production_serializer.save()
                                remaningQty = salesDetails['Quantity'] - avaliableQty
                    else:
                        batch_obj = {
                                    'BatchID':0,
                                    'BatchNo': obj['batchno'],
                                    'Quantity': remaningQty,
                                    'ID': ID,
                                    'AddedTimeStamp':current_date_time,
                                    'UpdatedTimeStamp':current_date_time,
                            }
                        serializer_data = BatchSales_Serializer(data=batch_obj)
                        if serializer_data.is_valid():
                            serializer_data.save()
                        Product_obj = Production.objects.get(BatchNo=obj["batchno"] ,FormulaID=item['productname'])
                        product_data = {
                                "ProductionID":Product_obj.ProductionID,
                                "TransactionDate": str(Product_obj.TransactionDate),
                                "BatchNo": str(Product_obj.BatchNo),
                                "ProductionQuantity":str(Product_obj.ProductionQuantity),
                                "AddedTimeStamp": str(Product_obj.AddedTimeStamp),
                                "UpdatedTimeStamp":str(Product_obj.UpdatedTimeStamp),
                                "BatchQty":str(remaningQty),
                                "FormulaID": Product_obj.FormulaID_id
                            }
                        production_serializer = ProductionSerializer(instance=Product_obj, data=product_data)
                        if production_serializer.is_valid():
                            production_serializer.save()
                            remaningQty = salesDetails['Quantity'] - avaliableQty
 

    return Response('')