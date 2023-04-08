import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class user(models.Model):
    UserID = models.AutoField(primary_key=True)
    EmailID = models.EmailField(unique=True)
    Password = models.CharField(max_length=25, blank=False)
    Role = models.CharField(max_length=15, blank=True)
    UserStatus = models.BooleanField(default=True)
  
    def __str__(self):
            return self.EmailID
    

class RawMaterial(models.Model):
    MaterialID = models.AutoField(primary_key=True)
    MaterialCode = models.CharField(max_length=255,unique=True)
    MaterialName  = models.CharField(max_length=25)
    QtyType = models.CharField(max_length=20 ,null=True, blank=True)
    TotalQuantity = models.IntegerField(default=0)
    ConsumedQuantity =  models.IntegerField(default=0)
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return self.MaterialName

class Vendor(models.Model):
    VendorCode = models.IntegerField(primary_key=True)
    VendorName = models.CharField(max_length=100)
    VendorShopName  = models.CharField(max_length=100)
    Phone = models.CharField(max_length=10)
    EmailID = models.EmailField(unique=True)
    Address =  models.CharField(max_length=255)
    City =  models.CharField(max_length=25)
    State =  models.CharField(max_length=25)
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return self.VendorName

class Addrawmaterial(models.Model):
    Id = models.AutoField(primary_key=True)
    TransactionDate = models.DateTimeField(default=timezone.now)
    BatchNo = models.CharField(max_length=100)
    OrderedQuantity	= models.IntegerField()
    ReceivedQuantity = models.IntegerField()
    AmountPaid = models.IntegerField()
    DamagedQty = models.IntegerField(null=True,blank=True)
    DamagedResion = models.CharField(max_length=100,null=True,blank=True)
    LossofAmount = models.IntegerField(null=True,blank=True)
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)
    MaterialID = models.ForeignKey('RawMaterial', on_delete=models.CASCADE)
    VendorCode = models.ForeignKey('Vendor', on_delete=models.CASCADE) 