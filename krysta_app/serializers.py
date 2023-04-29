from rest_framework import serializers
from .models import user,RawMaterial,Vendor,Addrawmaterial,Damaged,Product,ProductDetails,PackingMaterial,\
                   PackingDetails,Labour,Invoice,Formula,FormulaMaterials
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

# joing three tables for 

class StockmateriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = ['MaterialID','MaterialCode','MaterialName','QtyType']

class StockDamagedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Damaged
        fields = ['DamgeID','DamagedQty','DamagedResion','LossofAmount']

class StockvednorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['VendorID','VendorName']

class StockinvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['InvoiceID','InwardNumber']
   
class joinmaterialSerializer(serializers.ModelSerializer):
    Material = StockmateriaListSerializer(source='MaterialID')
    Damaged =  StockDamagedSerializer(source='DamgeID')
    Vendor = StockvednorSerializer(source='VendorID')
    invoice  = StockinvoiceSerializer(source='InvoiceID')
    class Meta:
        model = Addrawmaterial
        fields = ['Id','MaterialID','BatchNo','OrderedQuantity','ReceivedQuantity','AddedTimestamp','AmountPaid','Material','Damaged','Vendor','invoice']
        
# joing three tables for production 

# class productionformula_materialSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FormulaMaterials
#         fields = ['ID','Quantity','MaterialID','FormulaID']

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
        