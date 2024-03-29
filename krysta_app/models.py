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
    TotalQuantity = models.DecimalField(max_digits=10,default=0, decimal_places=2)
    ConsumedQuantity =  models.DecimalField(max_digits=10, decimal_places=2,default=0,null=True, blank=True)
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)

    def __int__(self):
            return self.MaterialID
                                   
class Vendor(models.Model):
    VendorID = models.AutoField(primary_key=True)
    VendorCode = models.CharField(max_length=100)
    VendorName = models.CharField(max_length=100,null=True, blank=True)
    RegisteredName  = models.CharField(max_length=100)
    Phone = models.CharField(max_length=25,null=True, blank=True)
    EmailID = models.EmailField(null=True, blank=True)
    Address =  models.CharField(max_length=255)
    City =  models.CharField(max_length=25)
    State =  models.CharField(max_length=25)
    Zip = models.CharField(max_length=10,default=0)
    LossofAmount = models.IntegerField(null=True,blank=True,default=0)
    AddedTimestamp = models.DateTimeField(default=timezone.now)
    UpdatedTimestamp = models.DateTimeField(default=timezone.now)

    def __int__(self):
            return self.VendorID
    
class Damaged(models.Model):
    DamgeID = models.IntegerField(primary_key=True,default=0)
    DamagedQty = models.IntegerField(null=True,blank=True)
    DamagedResion = models.CharField(max_length=100,null=True,blank=True)
    LossofAmount = models.IntegerField(null=True,blank=True,default=0)

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
    EnteryDate = models.DateTimeField(default=timezone.now)
    Formulas = models.CharField(max_length=100,default='')
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    updatedTimeStamp	= models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.ID
    
class Invoice(models.Model):
    InvoiceID = models.IntegerField(primary_key=True,default=0)
    InvoiceNumber =	models.CharField(max_length=30)
    InwardNumber  = models.CharField(max_length=50)
    InvoiceDate   = models.DateField()
    RecievedDate  = models.DateField(null=True, blank=True,default="")
    VendorID = models.IntegerField()
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.InvoiceID

     
class Formula(models.Model):		
    FormulaID	= models.IntegerField(primary_key=True,default=0)
    FormulaName  = models.CharField(max_length=20)
    TotalMaterialsUsed = models.IntegerField()
    TotalProductionQty =  models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,default='0')
    TotalSaledQty      =  models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,default="0")
    Category = models.ForeignKey('Category', on_delete=models.CASCADE,default="1")
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
    ProductionID	= models.IntegerField(primary_key=True,default=0)
    TransactionDate = models.DateTimeField(default=timezone.now)
    BatchNo = models.CharField(max_length=25,null=True, blank=True,default="")
    FormulaID  = models.ForeignKey('Formula',related_name='production_details', on_delete=models.CASCADE)
    ProductionQuantity = models.DecimalField(max_digits=10, decimal_places=2)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
    BatchQty=  models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,default=0.0)
    def __int__(self):
        return self.ProductionID
    
class ProductionDetails(models.Model):		
    Pro_detailsID	= models.AutoField(primary_key=True)
    ProductionID = models.ForeignKey('Production',related_name='production_material', on_delete=models.CASCADE) 
    MaterialID = models.ForeignKey('RawMaterial', on_delete=models.CASCADE,default=1) 
    Quantity = models.DecimalField(max_digits=10, decimal_places=2)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
    def __int__(self):
        return self.Pro_detailsID

class ProductionPacking(models.Model):		
    production_packing_ID	= models.AutoField(primary_key=True)
    ProductionID = models.ForeignKey('Production',related_name='packing_material',on_delete=models.CASCADE) 
    PackingMaterialID = models.ForeignKey('PackingMaterial', on_delete=models.CASCADE,default=1) 
    Quantity = models.DecimalField(max_digits=10, decimal_places=2)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
    def __int__(self):
        return self.production_packing_ID

class ProductionDamage(models.Model):
    ProductionDamageID	= models.AutoField(primary_key=True)
    DamagedQuantity =	models.DecimalField(max_digits=10, decimal_places=2)
    DamageReason =	models.CharField(max_length=500)
    LossPrice  = models.DecimalField(max_digits=10, decimal_places=2)
    ID  = models.ForeignKey('Production',related_name='production_damage', on_delete=models.CASCADE,null=True, blank=True,default="")
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
   
    def __int__(self):
        return self.ProductionDamageID   
##############--- Sales  MODELS ---####################
class SalesInvoice(models.Model):
    InvoiceID = models.IntegerField(primary_key=True,default=0)
    InvoiceNumber =	models.CharField(max_length=30)
    InwardNumber  = models.CharField(max_length=50)
    InvoiceDate   = models.DateField()
    RecievedDate  = models.DateField(null=True, blank=True,default="")
    BatchNo = models.CharField(max_length=25,null=True, blank=True,default="")
    VendorID = models.IntegerField()
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.InvoiceID
    
class Sales(models.Model):
    SalesID	= models.IntegerField(primary_key=True,default=0)
    TotalProducts =	models.CharField(max_length=10)
    TotalAmount  = models.DecimalField(max_digits=10, decimal_places=2)
    TransactionDate = models.DateTimeField(default=timezone.now)
    InvoiceID = models.ForeignKey('SalesInvoice', on_delete=models.CASCADE) 
    VendorID = models.ForeignKey('Vendor', on_delete=models.CASCADE)  
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
   
    def __int__(self):
        return self.SalesID
    
class SalesDetails(models.Model):
    ID	= models.IntegerField(primary_key=True,default=0)
    Quantity =	models.DecimalField(max_digits=10, decimal_places=2)
    Price  = models.DecimalField(max_digits=10, decimal_places=2)
    FormulaID  = models.ForeignKey('Formula', on_delete=models.CASCADE,null=True, blank=True,default="")
    ProductID  = models.ForeignKey('Product', on_delete=models.CASCADE,null=True, blank=True,default="") 
    SalesID = models.ForeignKey('Sales', on_delete=models.CASCADE)  
    Type = models.CharField(max_length=30,null=True, blank=True,default="")
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
   
    def __int__(self):
        return self.ID
    
class SalesDamage(models.Model):
    SalesDamageID	= models.AutoField(primary_key=True)
    DamagedQuantity =	models.DecimalField(max_digits=10, decimal_places=2)
    DamageReason =	models.CharField(max_length=500)
    LossPrice  = models.DecimalField(max_digits=10, decimal_places=2)
    ID  = models.ForeignKey('SalesDetails',related_name='sales_damage', on_delete=models.CASCADE)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
   
    def __int__(self):
        return self.SalesDamageID
    
class Category(models.Model):
   ID	= models.AutoField(primary_key=True)
   Name =	models.CharField(max_length=20)
   def __int__(self):
        return self.ID

class BatchSale(models.Model):
    BatchID	= models.AutoField(primary_key=True)
    BatchNo = models.CharField(max_length=25,null=True, blank=True)
    Quantity =	models.DecimalField(max_digits=10, decimal_places=2)
    ID  = models.ForeignKey('SalesDetails',related_name='sales_batch', on_delete=models.CASCADE)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    UpdatedTimeStamp = models.DateTimeField(default=timezone.now)
   
    def __int__(self):
        return self.BatchID
     