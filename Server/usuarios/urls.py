from django.urls import path 
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('register/', views.user_register),
    path('admin/bitacora/', views.ver_bitacora)
]