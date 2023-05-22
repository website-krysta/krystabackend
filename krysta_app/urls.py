
from django.urls import path
from .views import UserList,Useradd,Userupdate,getUserdate,deleteUser,getmaterials,\
                  addmaterial,updatematerial,getmaterial,deletematerial,getvendorlist,\
                  addvendor,getvendor,addRawmaterial,getAddrawmaterial,adddamageditem,\
                  getdamagedlist,getrawmaterial,getinvoices,addinvoice,getInvoiceData,getrawmaterialStock ,\
                  MaterialViewSet ,materialDetail,getrawmaterial_list ,ProductionMaterialViewSet,WhitelabelingViewSet,PackingViewSet,\
                  UpdateInvoiceData,UpdateRawmaterialDetails ,getDamagedItem,Formula_Material_ViewSet,Production_Formula_ViewSet,Production_packing_ViewSet
                  
                  
                

from .productApi import addProduct,getProduct,addProductDetails,getProducItem,Update_whitelabel_Details,getProducDetails_item
from .packingApi import addPacking,getPacking,addPackingDetails,getPackingItem,getpacking_material_list,UpdatePackingDetails
from .labour import addLabour,getLabour
from .formula import getformula,addformula,getformulamaterial,addformulamaterial,getformula_ID_Data
from .production import getProduction,addProduction,addProduction_Packing,getProductionDetails
from .sales import getSalesInvoice,getSalesInvoice_ID_Data,addSalesInvoiceData,getSales,getSales_ID_Data,addSalesData,getSalesdetails,updateSalesInvoice_ID_Data
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
    path('damaged/<int:id>/', getDamagedItem, name='getdamagedItem '),

    #------addRawMaterial ------#   
    path('addRawmaterial/list/', getAddrawmaterial, name='getaddRawmaterial'),
    path('addRawmaterial/add/', addRawmaterial, name='addRawmaterial'),
    path('addRawmaterial/<int:id>/', getrawmaterial, name='get_addRawmaterial '),
    path('RawmaterialStock/<int:id>/', getrawmaterialStock, name='get_RawmaterialStock '),
    path('rawmaterial_item/<int:id>/', getrawmaterial_list, name='rawmaterial_item '),
    path('updateRawmaterial/update/', UpdateRawmaterialDetails, name='updateRawmaterial'),

    #------product ------#   
    path('product/list/', getProduct, name='getproduct'),
    path('product/add/', addProduct, name='addproduct'),
    path('product/ProductDetails/add/', addProductDetails, name='get_product_details '),
    path('product/<int:id>/', getProducItem, name='get_productItem'),
    path('productDetails/<int:id>/', getProducDetails_item, name='get_productDetailsItem'),
    path('update_whitelabeling/update/', Update_whitelabel_Details, name='update_whitelabeling'),
    #------packing ------#   
    path('packing/list/', getPacking, name='getpacking'),
    path('packing/add/', addPacking, name='addpacking'),
    path('packing/packingdetails/add/', addPackingDetails, name='addpackingdata '),
    path('packing/<int:id>/', getPackingItem, name='get_packingItem'),
    path('packingDetails_list/<int:id>/', getpacking_material_list, name='get_packingDetails_item'),
    path('updatePackingDetails/update/', UpdatePackingDetails, name='updatePackingDetails'),
    #------labour ------#   
    path('labour/list/', getLabour, name='getlabour'),
    path('labour/add/', addLabour, name='addlabour'),
    #------labour ------#   
    path('invoice/list/', getinvoices, name='getinvoice'),
    path('invoice/add/', addinvoice, name='addinvoice'),
    path('invoce/getinvoice/<int:id>/', getInvoiceData, name='get_invoiceData '),
    path('invoce/updateinvoice/<int:id>/', UpdateInvoiceData, name='update_invoiceData '),
    #------formula ------#   
    path('formula/list/', getformula, name='getformula'),
    path('formula/add/', addformula, name='addformula'),
    path('formulamaterial/list/', getformulamaterial, name='getformula_material'),
    path('formulamaterial/add/', addformulamaterial, name='addformula_material'),
    path('formulamaterialiitems/<int:id>/', getformula_ID_Data, name='formulamaterialiitems'),

    #-----join tables ------#  
    path('materialviewSet/', MaterialViewSet.as_view()),
    path('materialdetails/<int:MaterialID>/', materialDetail.as_view(), name='material-list'),
     #-----join tables for production for show formulas ------#  
    path('formulaviewSet/', ProductionMaterialViewSet.as_view()),
    #-----join tables ------#  
    path('production/list/', getProduction, name='getproduction'),
    path('production/add/', addProduction, name='addproduction'),
    path('production/packingadd/', addProduction_Packing, name='packingadd'),
    #roduction details
    path('productiondetails/list/', getProductionDetails, name='getproductiondetails'),
    #roduction details
    path('WhitelabelingViewSet/', WhitelabelingViewSet.as_view()),
    #roduction details
    path('PackingViewSet/', PackingViewSet.as_view()),
    #production details
    path('Formula_Material_ViewSet/', Formula_Material_ViewSet.as_view()),
    #ppproduction details
    path('productionTable_ViewSet/', Production_Formula_ViewSet.as_view()),
    path('production_packingTable_ViewSet/', Production_packing_ViewSet.as_view()),
    #---- salesInvoice tables ------#  
    path('salesinvoice/list/', getSalesInvoice, name='getsalesData'),
    path('salesinvoice/<int:id>/', getSalesInvoice_ID_Data, name='getsalesIdData'),
    path('salesinvoice/add/', addSalesInvoiceData, name='addsalesIdData'),
    path('salesInvoiceupdate/', updateSalesInvoice_ID_Data , name="updatesalesrecord"),
    #---- sales tables ------#  
    path('sales/list/', getSales, name='getsalesData'),
    path('sales/<int:id>/', getSales_ID_Data, name='getsalesIdData'),
    path('sales/add/', addSalesData, name='addsalesIdData'),
    path('salesDetails/list/', getSalesdetails, name='getsalesDetails')
     
]
