
from django.urls import path
from .views import UserList,Useradd,Userupdate,getUserdate,deleteUser,getmaterials,addmaterial,updatematerial,getmaterial,deletematerial,getvendorlist,addvendor,addRawmaterial,getAddrawmaterial

                     
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
    path('vendor/add/', addvendor, name='vendoradd'),
    #------addRawMaterial ------#   
    path('addRawmaterial/list/', getAddrawmaterial, name='getaddRawmaterial'),
    path('addRawmaterial/add/', addRawmaterial, name='addRawmaterial'),

]
