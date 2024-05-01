from django.db import models

# Create your models here.
class Tache(models.Model):
    date=models.DateField()
    
    object=models.CharField(max_length=150,null=True)
    description = models.TextField(max_length=1000,null=True)