from django.db import models
from rol.models import Rol

# Create your models here.
class Student(models.Model):
 
    idstudent = models.AutoField(primary_key=True)
    typerol = models.ForeignKey(Rol, on_delete=models.CASCADE, default='')
    identification = models.BigIntegerField(null=True, blank=True)
    names = models.CharField(max_length=50, blank=True)
    lastnames = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)

    class Meta:
        db_table = 'student'