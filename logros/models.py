
from django.db import models

# Create your models here.
class Logro(models.Model):

    idlogro = models.AutoField( primary_key=True)
    nombre = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    
    class Meta:
        db_table = 'logros'
