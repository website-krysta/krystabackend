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
    VendorID = models.AutoField(primary_key=True)
    VendorCode = models.CharField(max_length=100)
    VendorName = models.CharField(max_length=100)
    RegisteredName  = models.CharField(max_length=100)
    Phone = models.CharField(max_length=25)
    EmailID = models.EmailField(unique=True)
    Address =  models.CharField(max_length=255)
    City =  models.CharField(max_length=25)
    State =  models.CharField(max_length=25)
    Zip = models.CharField(max_length=10,default=0)
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return self.VendorCode
    
class Damaged(models.Model):
    DamgeID = models.AutoField(primary_key=True)
    DamagedQty = models.IntegerField(null=True,blank=True)
    DamagedResion = models.CharField(max_length=100,null=True,blank=True)
    LossofAmount = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.DamagedResion

class Addrawmaterial(models.Model):
    Id = models.AutoField(primary_key=True)
    TransactionDate = models.DateTimeField(default=timezone.now)
    BatchNo = models.CharField(max_length=25)
    OrderedQuantity	= models.IntegerField()
    ReceivedQuantity = models.IntegerField()
    AmountPaid = models.IntegerField()
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)
    MaterialID = models.ForeignKey('RawMaterial', on_delete=models.CASCADE)
    VendorID = models.ForeignKey('Vendor', on_delete=models.CASCADE) 
    DamgeID = models.ForeignKey('Damaged', on_delete=models.CASCADE) 

    def __str__(self):
        return self.BatchNo