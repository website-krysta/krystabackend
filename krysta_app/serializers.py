from rest_framework import serializers
from .models import user,RawMaterial,Vendor,Addrawmaterial,Damaged
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