from django.db import models

# Create your models here.
# escribir en singular primera mayuscula
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    #email = models.EmailField(max_length=150, unique=True)
    #password = models.TextField(max_length=128, unique=True) #se que la contraseña no es unica pero quise hacerla por un meme que vi
    #mobile_number = models.CharField(max_length=15, unique=True)
    #address= models.CharField(max_length=255)
    #status = models.BooleanField(default=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now_add=True)

class Countries(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE) #ejemplo de llave foranea