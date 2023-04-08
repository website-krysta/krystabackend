from django.contrib import admin
from .models import user,RawMaterial,Vendor,Addrawmaterial
# Register your models here.

class Adminuser(admin.ModelAdmin):
    list_display=('UserID','EmailID','Role','UserStatus')

class Adminrawmeterial(admin.ModelAdmin):
    list_display=('MaterialID','MaterialCode','MaterialName','TotalQuantity','AddedTimestamp')

class AdminVendor(admin.ModelAdmin):
    list_display=('VendorCode','VendorName','VendorShopName','Phone','EmailID','Address','State')

class AdminAddrawmaterial(admin.ModelAdmin):
    list_display=('Id','BatchNo','OrderedQuantity','ReceivedQuantity','AmountPaid','DamagedQty','DamagedResion','LossofAmount')

admin.site.register(user,Adminuser)
admin.site.register(RawMaterial,Adminrawmeterial)
admin.site.register(Vendor,AdminVendor)
admin.site.register(Addrawmaterial,AdminAddrawmaterial)