from django.db import models
from sirest_b09.models import *

# Create your models here.
class KategoriMakanan(models.Model):
      id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=100)

class Makanan(models.Model):
      rname = models.ForeignKey(Restoran, on_delete=models.CASCADE)
      name = models.CharField(max_length=50)
      description = models.TextField()
      stock = models.IntegerField()
      price = models.BigIntegerField()
      category = models.ForeignKey(KategoriMakanan, on_delete=models.SET_NULL, null=True)