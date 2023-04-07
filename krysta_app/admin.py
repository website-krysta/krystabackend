from django.contrib import admin
from .models import user,RawMaterial
# Register your models here.

class Adminuser(admin.ModelAdmin):
    list_display=('UserID','EmailID','Role','UserStatus')

class Adminrawmeterial(admin.ModelAdmin):
    list_display=('MaterialID','MaterialCode','MaterialName','TotalQuantity','AddedTimestamp')

admin.site.register(user,Adminuser)
admin.site.register(RawMaterial,Adminrawmeterial)