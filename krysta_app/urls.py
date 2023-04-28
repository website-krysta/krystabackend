
from django.urls import path
from .views import UserList,Useradd,Userupdate,getUserdate,deleteUser,getmaterials,\
                  addmaterial,updatematerial,getmaterial,deletematerial,getvendorlist,\
                  addvendor,getvendor,addRawmaterial,getAddrawmaterial,adddamageditem,\
                  getdamagedlist,getrawmaterial,getinvoices,addinvoice,getInvoiceData,getrawmaterialStock ,\
                  MaterialViewSet ,materialDetail,getrawmaterial_list     

from .productApi import addProduct,getProduct,addProductDetails
from .packingApi import addPacking,getPacking,addPackingDetails
from .labour import addLabour,getLabour
from .formula import getformula,addformula,getformulamaterial,addformulamaterial,getformula_ID_Data


# router = routers.DefaultRouter()
# router.register(r'modela', MaterialViewSet)    

urlpatterns = [
    path('user/', UserList, name='userlist'),
    path('useradd/', Useradd, name='useradd'),
    path('userupdate/<int:id>/', Userupdate, name='userupdate'),
    path('userget/<int:id>/', getUserdate, name='userget'),
    path('deleteuser/<int:id>/', deleteUser, name='deleteUser'),
    #------meterial ------#
    path('meterial/list/', getmaterials, name='meteriallist'),
    path('meterial/add/', addmaterial, name='meterialadd'),
    path('meterial/update/<int:id>/', updatematerial, name='meterialupdate'),
    path('meterial/<int:id>/', getmaterial, name='meterialid '),
    path('meterial/delet/<int:id>/', deletematerial, name='meterialdelet'),
    #------vendor ------#
    path('vendor/list/', getvendorlist, name='vendorlist'),
    path('vendor/<int:id>/', getvendor, name='get_vendor '),
    path('vendor/add/', addvendor, name='vendoradd'),
  #------vendor ------#
    path('damaged/list/', getdamagedlist, name='damagedlist'),
    path('damaged/add/', adddamageditem, name='dagameditem'),
    #------addRawMaterial ------#   
    path('addRawmaterial/list/', getAddrawmaterial, name='getaddRawmaterial'),
    path('addRawmaterial/add/', addRawmaterial, name='addRawmaterial'),
    path('addRawmaterial/<int:id>/', getrawmaterial, name='get_addRawmaterial '),
    path('RawmaterialStock/<int:id>/', getrawmaterialStock, name='get_RawmaterialStock '),
    path('rawmaterial_item/<int:id>/', getrawmaterial_list, name='rawmaterial_item '),

    #------product ------#   
    path('product/list/', getProduct, name='getproduct'),
    path('product/add/', addProduct, name='addproduct'),
    path('product/ProductDetails/add/', addProductDetails, name='get_product_details '),
    #------packing ------#   
    path('packing/list/', getPacking, name='getpacking'),
    path('packing/add/', addPacking, name='addpacking'),
    path('packing/packingdetails/add/', addPackingDetails, name='addpackingdata '),
    #------labour ------#   
    path('labour/list/', getLabour, name='getlabour'),
    path('labour/add/', addLabour, name='addlabour'),
    #------labour ------#   
    path('invoice/list/', getinvoices, name='getinvoice'),
    path('invoice/add/', addinvoice, name='addinvoice'),
    path('invoce/getinvoice/<int:id>/', getInvoiceData, name='get_invoiceData '),
    #------formula ------#   
    path('formula/list/', getformula, name='getformula'),
    path('formula/add/', addformula, name='addformula'),
    path('formulamaterial/list/', getformulamaterial, name='getformula_material'),
    path('formulamaterial/add/', addformulamaterial, name='addformula_material'),
    path('formulamaterialiitems/<int:id>/', getformula_ID_Data, name='formulamaterialiitems'),

    #-----join tables ------#  
    path('materialviewSet/', MaterialViewSet.as_view()),
    path('materialdetails/<int:MaterialID>/', materialDetail.as_view(), name='material-list'),
]
