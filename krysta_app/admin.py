from django.contrib import admin
from .models import user,RawMaterial,Vendor,Damaged,Addrawmaterial,Product,ProductDetails,PackingDetails,PackingMaterial,\
                    Labour,Invoice,Formula,FormulaMaterials,Production,ProductionDetails,ProductionPacking
# Register your models here.

class Adminuser(admin.ModelAdmin):
    list_display=('UserID','EmailID','Role','UserStatus')

class Adminrawmeterial(admin.ModelAdmin):
    list_display=(['MaterialID','MaterialCode','MaterialName','QtyType','TotalQuantity','ConsumedQuantity','AddedTimestamp'])

class AdminVendor(admin.ModelAdmin):
    list_display=(['VendorID','VendorCode','VendorName'])

class AdminDamaged(admin.ModelAdmin):
    list_display=(['DamgeID','DamagedQty','DamagedResion','LossofAmount'])


class AdminAddrawmaterial(admin.ModelAdmin):
    list_display=(['Id','BatchNo','OrderedQuantity','ReceivedQuantity','MaterialID','VendorID','DamgeID','InvoiceID'])
#----------------------
class AdminProduct(admin.ModelAdmin):
    list_display=(['ProductID','ProductCode','ProductName','QtyType','TotalQuantity','ConsumedQuantity'])

class AdminProductDetails(admin.ModelAdmin):
    list_display=(['Id','BatchNo','OrderedQuantity','ReceivedQuantity','ProductID','VendorID','DamgeID','InvoiceID'])
#----------------------
class AdminPacking(admin.ModelAdmin):
    list_display=(['PackingMaterialID','PackingMaterialCode','PackingMaterialName','QtyType','TotalQuantity','ConsumedQuantity'])

class AdminPackingDetails(admin.ModelAdmin):
    list_display=(['Id','BatchNo','OrderedQuantity','ReceivedQuantity','PackingMaterialID','VendorID','DamgeID','InvoiceID'])
#----------------------
class AdminLabour(admin.ModelAdmin):
    list_display=(['ID','TotalLabours','MorningShiftCount','NightShiftCount','MorningShiftAmount','NightShiftAmount','AddedTimeStamp'])
#----------------------
class AdminInvoice(admin.ModelAdmin):
    list_display=(['InvoiceID','InvoiceNumber','InwardNumber','InvoiceDate','RecievedDate','VendorID','AddedTimeStamp'])

#----------------------
class AdminFormula(admin.ModelAdmin):
    list_display=(['FormulaID','FormulaName','TotalMaterialsUsed','AddedTimeStamp','UpdatedTimeStamp'])
#----------------------
class AdminFormulaMaterial(admin.ModelAdmin):
    list_display=(['ID','Quantity','MaterialID','FormulaID','AddedTimeStamp','UpdatedTimeStamp'])

#----------------------
class AdminProduction(admin.ModelAdmin):
    list_display=(['ProductionID','TransactionDate','FormulaID','ProductionQuantity','AddedTimeStamp','UpdatedTimeStamp'])
#----------------------
class AdminProductionDetails(admin.ModelAdmin):
    list_display=(['Pro_detailsID','ProductionID','MaterialID','Quantity','AddedTimeStamp','UpdatedTimeStamp'])

#----------------------
class AdminProductionPacking(admin.ModelAdmin):
    list_display=(['production_packing_ID','ProductionID','PackingMaterialID','Quantity','AddedTimeStamp','UpdatedTimeStamp'])

######################################################################

admin.site.register(user,Adminuser)
admin.site.register(RawMaterial,Adminrawmeterial)
admin.site.register(Vendor,AdminVendor)
admin.site.register(Damaged,AdminDamaged)
admin.site.register(Addrawmaterial,AdminAddrawmaterial)
#----------------------
admin.site.register(Product,AdminProduct)
admin.site.register(ProductDetails,AdminProductDetails)
#----------------------
admin.site.register(PackingMaterial,AdminPacking)
admin.site.register(PackingDetails,AdminPackingDetails)
#----------------------
admin.site.register(Labour,AdminLabour)
#----------------------
admin.site.register(Invoice,AdminInvoice)
#----------------------
admin.site.register(Formula,AdminFormula)
admin.site.register(FormulaMaterials,AdminFormulaMaterial)
#----------------------
admin.site.register(Production,AdminProduction)
admin.site.register(ProductionDetails,AdminProductionDetails)
admin.site.register(ProductionPacking,AdminProductionPacking)