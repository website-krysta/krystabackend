from rest_framework import serializers
from .models import user,RawMaterial,Vendor,Addrawmaterial,Damaged,Product,ProductDetails,PackingMaterial,PackingDetails
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