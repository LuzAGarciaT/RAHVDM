from django.db import models

# Create your models here.
class Rol(models.Model):

    idrol = models.AutoField(primary_key=True)
    typerol = models.CharField(max_length=20)

    def __str__(self):
        return self.typerol
    
    
    class Meta:
        db_table = 'rol'