from django.contrib import admin
from .models import user,RawMaterial,Vendor,Damaged,Addrawmaterial,Product,ProductDetails,PackingDetails,PackingMaterial,Labour
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
    list_display=(['Id','BatchNo','OrderedQuantity','ReceivedQuantity','AmountPaid','MaterialID','VendorID','DamgeID'])
#----------------------
class AdminProduct(admin.ModelAdmin):
    list_display=(['ProductID','ProductCode','ProductName','QtyType','TotalQuantity','ConsumedQuantity'])

class AdminProductDetails(admin.ModelAdmin):
    list_display=(['Id','BatchNo','OrderedQuantity','ReceivedQuantity','AmountPaid','ProductID','VendorID','DamgeID'])
#----------------------
class AdminPacking(admin.ModelAdmin):
    list_display=(['PackingMaterialID','PackingMaterialCode','PackingMaterialName','QtyType','TotalQuantity','ConsumedQuantity'])

class AdminPackingDetails(admin.ModelAdmin):
    list_display=(['Id','BatchNo','OrderedQuantity','ReceivedQuantity','AmountPaid','PackingMaterialID','VendorID','DamgeID'])
#----------------------
class AdminLabour(admin.ModelAdmin):
    list_display=(['ID','TotalLabours','MorningShiftCount','NightShiftCount','MorningShiftAmount','NightShiftAmount','AddedTimeStamp'])
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