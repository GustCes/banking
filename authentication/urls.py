from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries/', views.countries, name='countries'),
    path('departments/', views.departments, name='departments'),
    path('cities/', views.cities, name='cities'),
    
    ]