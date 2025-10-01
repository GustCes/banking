from django.db import models

# Create your models here.
# escribir en singular primera mayuscula

class Country(models.Model):
    name = models.CharField(max_length=20, default='countryname')
    abrev = models.CharField(max_length=5, default='abv')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"{self.name} {self.abrev} {'active' if self.status==True else 'inactive'}"

class Department(models.Model):
    name = models.CharField(max_length=20, default='departmentname')
    abrev = models.CharField(max_length=5, default='abv')
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"{self.name} {self.abrev}"

class City(models.Model):
    name = models.CharField(max_length=20, default='cityname')
    abrev = models.CharField(max_length=5, default='abv')
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"{self.name} {self.abrev}"

class User(models.Model):
    first_name = models.CharField(max_length=20, default='username')
    last_name = models.CharField(max_length=20, default='userlastname')
    email = models.EmailField(max_length=150, unique=True, default='usermail')
    password = models.TextField(max_length=128, unique=True, default='userpass')
    #se que la contraseña no es unica pero quise hacerla por un meme que vi
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, default='1234567890')
    address= models.CharField(max_length=255, default='enrique segoviano')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
#sirve para que los objetos se muestren con un nombre
    def __str__(self):
        return self.first_name + ' ' + self.last_name
