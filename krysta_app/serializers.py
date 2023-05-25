from rest_framework import serializers
from .models import user,RawMaterial,Vendor,Addrawmaterial,Damaged,Product,ProductDetails,PackingMaterial,\
                   PackingDetails,Labour,Invoice,Formula,FormulaMaterials,Production,ProductionDetails,ProductionPacking,\
                   SalesInvoice,Sales,SalesDetails,SalesDamage



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class meterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class DamagedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Damaged
        fields = '__all__'

class AddrawmaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addrawmaterial
        fields = '__all__'

class ProductlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductlDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'

class PackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingMaterial
        fields = '__all__'

class PackingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingDetails
        fields = '__all__'

class LabourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labour
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = '__all__'
class FormulaMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormulaMaterials
        fields = '__all__'

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__' 

class ProductionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionDetails
        fields = '__all__'        

class PaackingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPacking
        fields = '__all__'     

# joing three tables for 
#raw material Table
class StockmateriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = ['MaterialID','MaterialCode','MaterialName','QtyType']

#damaged Table
class StockDamagedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Damaged
        fields = ['DamgeID','DamagedQty','DamagedResion','LossofAmount']

#vendor Table
class StockvednorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['VendorID','VendorName']

#invoice Table
class StockinvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['InvoiceID','InwardNumber','InvoiceNumber']

 #add rawmaterial table  
class joinmaterialSerializer(serializers.ModelSerializer):
    Material = StockmateriaListSerializer(source='MaterialID')
    Damaged =  StockDamagedSerializer(source='DamgeID')
    Vendor = StockvednorSerializer(source='VendorID')
    invoice  = StockinvoiceSerializer(source='InvoiceID')
    class Meta:
        model = Addrawmaterial
        fields = ['Id','MaterialID','BatchNo','OrderedQuantity','ReceivedQuantity','AddedTimestamp','AmountPaid','Material','Damaged','Vendor','invoice']
        
# joing three tables for production 
class StockProddutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['ProductID','ProductCode','ProductName','QtyType']

class joinProductionSerializer(serializers.ModelSerializer):
    Production = StockProddutionSerializer(source='ProductID')
    Damaged =  StockDamagedSerializer(source='DamgeID')
    Vendor = StockvednorSerializer(source='VendorID')
    invoice  = StockinvoiceSerializer(source='InvoiceID')
    class Meta:
        model = ProductDetails
        fields = ['Id','ProductID','BatchNo','OrderedQuantity','ReceivedQuantity','AddedTimestamp','AmountPaid','Production','Damaged','Vendor','invoice'] 
# end join tables  for production 
       
# joing three tables for production 
class StockPackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingMaterial
        fields = ['PackingMaterialID','PackingMaterialCode','PackingMaterialName','QtyType']

class joinPackingSerializer(serializers.ModelSerializer):
    Packing = StockPackingSerializer(source='PackingMaterialID')
    Damaged =  StockDamagedSerializer(source='DamgeID')
    Vendor = StockvednorSerializer(source='VendorID')
    invoice  = StockinvoiceSerializer(source='InvoiceID')
    class Meta:
        model = PackingDetails
        fields = ['Id','PackingMaterialID','BatchNo','OrderedQuantity','ReceivedQuantity','AddedTimestamp','AmountPaid','Packing','Damaged','Vendor','invoice'] 


# joing three tables for formula  + formula Material + Material  ----------------------------------------
class join_FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = ['FormulaID','FormulaName','AddedTimeStamp']

class formulaMaterial_detailsSerializer(serializers.ModelSerializer):
    Formula = join_FormulaSerializer(source='FormulaID')
    aMaterial = StockmateriaListSerializer(source='MaterialID')
 
    class Meta:
        model = FormulaMaterials
        fields = ['ID','FormulaID','Quantity','Formula','aMaterial']


# joing three tables for production  + formula -----------------------------------------

class productionfor_materialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = ['MaterialID','MaterialCode','MaterialName','TotalQuantity','ConsumedQuantity','QtyType']

class ProductionFormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = ['FormulaID','FormulaName']

class joinProductionFormulaSerializer(serializers.ModelSerializer):
    material =  productionfor_materialSerializer(source='MaterialID')
    forumula = ProductionFormulaSerializer(source='FormulaID')
    
    class Meta:
        model = FormulaMaterials
        fields = ['ID','Quantity','MaterialID','FormulaID','material','forumula']
        
# joing production and formula table  production  + formula -----------------------------------------

class join_Formula_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = ['FormulaID','FormulaName','TotalProductionQty','TotalSaledQty','AddedTimeStamp']

class viewProductionFormulaSerializer(serializers.ModelSerializer):
    forumula = join_Formula_Serializer(source='FormulaID')
    class Meta:
        model = Production
        fields = ['ProductionID','ProductionQuantity','AddedTimeStamp','TransactionDate','FormulaID','forumula']


# detals
class Stock_Packing_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PackingMaterial
        fields = ['PackingMaterialID','PackingMaterialCode','PackingMaterialName','QtyType']

class Stock_rawmaterial_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = ['MaterialID','MaterialCode','MaterialName','QtyType']


class production_packing_details_join_Serializer(serializers.ModelSerializer):
    producton = viewProductionFormulaSerializer(source='ProductionID')
    packing =  Stock_Packing_Serializer(source='PackingMaterialID')
    class Meta:
        model = ProductionPacking
        fields = ['production_packing_ID','Quantity','producton','packing'] 

# create serializer for sales table -----------------------------------------
class SalesInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = '__all__'
class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class SalesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDetails
        fields = '__all__'
class SalesDamagedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDamage
        fields = '__all__'

# create join tables serializer for sales table -----------------------------------------
class Sales_InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = ['InvoiceID','InvoiceNumber','InwardNumber','InvoiceDate','RecievedDate','VendorID'] 

class Sales_Serializer(serializers.ModelSerializer):
    # sales_invoice = Sales_InvoiceSerializer(source='InvoiceID')
    class Meta:
        model = Sales
        fields = ['SalesID','TotalProducts','TotalAmount','TransactionDate','InvoiceID','VendorID'] 

class Sales_Damage_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDamage
        fields = ['SalesDamageID', 'DamagedQuantity', 'DamageReason', 'LossPrice']

class join_SalesDetails_Serializer(serializers.ModelSerializer):
    SaleInfo = Sales_Serializer(source='SalesID')
    formulainfo = join_Formula_Serializer(source='FormulaID')
    sales_damage = Sales_Damage_Serializer(many=True, read_only=True)

    class Meta:
        model = SalesDetails
        fields = ['ID','Quantity','Price','FormulaID','SalesID','SaleInfo','formulainfo','sales_damage']


