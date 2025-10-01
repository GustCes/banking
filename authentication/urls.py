from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries/', views.index, name='countries'),
    path('departments/', views.index, name='departments'),
    path('cities/', views.index, name='cities'),
    
    ]