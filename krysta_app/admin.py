from django.contrib import admin
from .models import user,RawMaterial,Vendor,Damaged,Addrawmaterial
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

admin.site.register(user,Adminuser)
admin.site.register(RawMaterial,Adminrawmeterial)
admin.site.register(Vendor,AdminVendor)
admin.site.register(Damaged,AdminDamaged)
admin.site.register(Addrawmaterial,AdminAddrawmaterial)