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
    MaterialCode = models.CharField(max_length=255)
    MaterialName  = models.CharField(max_length=25)
    QtyType = models.CharField(max_length=20 ,null=True, blank=True)
    TotalQuantity = models.IntegerField(default=0)
    ConsumedQuantity =  models.IntegerField(default=0,null=True, blank=True)
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)

    def __int__(self):
            return self.MaterialID

class Vendor(models.Model):
    VendorID = models.AutoField(primary_key=True)
    VendorCode = models.CharField(max_length=100)
    VendorName = models.CharField(max_length=100)
    RegisteredName  = models.CharField(max_length=100)
    Phone = models.CharField(max_length=25)
    EmailID = models.EmailField()
    Address =  models.CharField(max_length=255)
    City =  models.CharField(max_length=25)
    State =  models.CharField(max_length=25)
    Zip = models.CharField(max_length=10,default=0)
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)

    def __int__(self):
            return self.VendorID
    
class Damaged(models.Model):
    DamgeID = models.IntegerField(primary_key=True)
    DamagedQty = models.IntegerField(null=True,blank=True)
    DamagedResion = models.CharField(max_length=100,null=True,blank=True)
    LossofAmount = models.IntegerField(null=True,blank=True)

    def __int__(self):
        return self.DamgeID

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
    InvoiceID = models.ForeignKey('Invoice', on_delete=models.CASCADE,default=1) 

    def __int__(self):
        return self.MaterialID
    

# product models==================================================
class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductCode = models.CharField(max_length=255)
    ProductName  = models.CharField(max_length=25)
    QtyType = models.CharField(max_length=20 ,null=True, blank=True)
    TotalQuantity = models.IntegerField(default=0)
    ConsumedQuantity =  models.IntegerField(default=0,null=True, blank=True)
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)

    def __int__(self):
            return self.ProductID
    

class ProductDetails(models.Model):
    Id = models.AutoField(primary_key=True)
    TransactionDate = models.DateTimeField(default=timezone.now)
    BatchNo = models.CharField(max_length=25)
    OrderedQuantity	= models.IntegerField()
    ReceivedQuantity = models.IntegerField()
    AmountPaid = models.IntegerField()
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)
    ProductID = models.ForeignKey('Product', on_delete=models.CASCADE)
    VendorID = models.ForeignKey('Vendor', on_delete=models.CASCADE) 
    DamgeID = models.ForeignKey('Damaged', on_delete=models.CASCADE) 
    InvoiceID = models.ForeignKey('Invoice', on_delete=models.CASCADE,default=1) 

    def __str__(self):
        return self.BatchNo
    



# packingmaterial models==================================================
class PackingMaterial(models.Model):
    PackingMaterialID = models.AutoField(primary_key=True)
    PackingMaterialCode = models.CharField(max_length=255)
    PackingMaterialName  = models.CharField(max_length=25)
    QtyType = models.CharField(max_length=20 ,null=True, blank=True)
    TotalQuantity = models.IntegerField(default=0)
    ConsumedQuantity =  models.IntegerField(default=0,null=True, blank=True)
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)

    def __int__(self):
            return self.PackingMaterialID
    

class PackingDetails(models.Model):
    Id = models.AutoField(primary_key=True)
    TransactionDate = models.DateTimeField(default=timezone.now)
    BatchNo = models.CharField(max_length=25)
    OrderedQuantity	= models.IntegerField()
    ReceivedQuantity = models.IntegerField()
    AmountPaid = models.IntegerField()
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)
    PackingMaterialID = models.ForeignKey('PackingMaterial', on_delete=models.CASCADE)
    VendorID = models.ForeignKey('Vendor', on_delete=models.CASCADE) 
    DamgeID = models.ForeignKey('Damaged', on_delete=models.CASCADE) 
    InvoiceID = models.ForeignKey('Invoice', on_delete=models.CASCADE,default=1) 

    def __str__(self):
        return self.BatchNo
    

#labour detailsssss

class Labour(models.Model):
    ID	= models.AutoField(primary_key=True)
    TotalLabours	= models.IntegerField()
    MorningShiftCount	= models.IntegerField()
    NightShiftCount = models.IntegerField()
    MorningShiftAmount =	models.DecimalField(max_digits=10, decimal_places=2)
    NightShiftAmount =	models.DecimalField(max_digits=10, decimal_places=2)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    updatedTimeStamp	= models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.ID
    
class Invoice(models.Model):
    InvoiceID = models.IntegerField(primary_key=True)
    InvoiceNumber =	models.CharField(max_length=10)
    InwardNumber  = models.CharField(max_length=20)
    InvoiceDate   = models.DateField()
    RecievedDate  = models.DateField()
    VendorID = models.IntegerField()
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.InvoiceID

     
class Formula(models.Model):		
    FormulaID	= models.IntegerField(primary_key=True)
    FormulaName  = models.CharField(max_length=20)
    TotalMaterialsUsed = models.IntegerField()
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)

		
class FormulaMaterials(models.Model):
    ID	= models.AutoField(primary_key=True)
    Quantity = 	models.DecimalField(max_digits=10, decimal_places=2)
    MaterialID = models.ForeignKey('RawMaterial', on_delete=models.CASCADE)
    FormulaID = models.ForeignKey('Formula', on_delete=models.CASCADE)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)


##############---PRODUCTION MODELS ---####################

class Production(models.Model):		
    ProductionID	= models.IntegerField(primary_key=True)
    TransactionDate = models.DateTimeField(default=timezone.now)
    FormulaID  = models.IntegerField()
    ProductionQuantity = models.DecimalField(max_digits=10, decimal_places=2)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
    def __int__(self):
        return self.ProductionID
    
class ProductionDetails(models.Model):		
    Pro_detailsID	= models.AutoField(primary_key=True)
    ProductionID = models.ForeignKey('Production', on_delete=models.CASCADE) 
    MaterialID = models.ForeignKey('RawMaterial', on_delete=models.CASCADE,default=1) 
    Quantity = models.DecimalField(max_digits=10, decimal_places=2)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
    def __int__(self):
        return self.Pro_detailsID

class ProductionPacking(models.Model):		
    production_packing_ID	= models.AutoField(primary_key=True)
    ProductionID = models.ForeignKey('Production', on_delete=models.CASCADE) 
    PackingMaterialID = models.ForeignKey('PackingMaterial', on_delete=models.CASCADE,default=1) 
    Quantity = models.DecimalField(max_digits=10, decimal_places=2)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
    def __int__(self):
        return self.production_packing_ID