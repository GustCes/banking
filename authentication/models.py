from django.db import models

# Create your models here.
# escribir en singular primera mayuscula

class Country(models.Model):
    name = models.CharField(max_length=20, default='countryname')
    abrev = models.CharField(max_length=5, default='abv')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Department(models.Model):
    name = models.CharField(max_length=20, default='departmentname')
    abrev = models.CharField(max_length=5, default='abv')
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class City(models.Model):
    name = models.CharField(max_length=20, default='cityname')
    abrev = models.CharField(max_length=5, default='abv')
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)



class User(models.Model):
    first_name = models.CharField(max_length=20, default='username')
    last_name = models.CharField(max_length=20, default='userlastname')
    email = models.EmailField(max_length=150, unique=True, default='usermail')
    password = models.TextField(max_length=128, unique=True, default='userpass')
    #se que la contraseña no es unica pero quise hacerla por un meme que vi
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, unique=True, default='1234567890')
    address= models.CharField(max_length=255, default='enrique segoviano')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

#no se que hace esto pero se añadio solo, lo dejare comentareado por si acaso
#    def __str__(self):
