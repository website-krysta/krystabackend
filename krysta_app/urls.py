
from django.urls import path
from .views import UserList,Useradd,Userupdate,getUserdate,deleteUser
urlpatterns = [
    path('user/', UserList, name='userlist'),
    path('useradd/', Useradd, name='useradd'),
    path('userupdate/<int:id>/', Userupdate, name='userupdate'),
    path('userget/<int:id>/', getUserdate, name='userget'),
    path('deleteuser/<int:id>/', deleteUser, name='deleteUser'),
   
]
