from django.db import models

# Create your models here.
class KategoriRestoran(models.Model):
      id = models.IntegerField(primary_key=True)
      name = models.CharField(max_length=50)

class KategoriMakanan(models.Model):
      id = models.IntegerField(primary_key=True)
      name = models.CharField(max_length=50)



class Restoran(models.Model):
      email = models.EmailField()
      password = models.CharField(max_length=30)
      name = models.CharField(max_length=100)
      no_hp = models.CharField(max_length=12)
      nik = models.CharField(max_length=18)
      bank_name = models.CharField(max_length=30)
      no_rek = models.CharField(max_length=30)
      rest_name = models.CharField(max_length=50)
      branch = models.CharField(max_length=50)
      no_telp = models.CharField(max_length=12)
      street = models.CharField(max_length=50)
      districts = models.CharField(max_length=50)
      city = models.CharField(max_length=50)
      province = models.CharField(max_length=50)
      category = models.ForeignKey(KategoriRestoran, null=True, on_delete=models.SET_NULL)
      def __str__(self) -> str:
            return f"{self.name} | {self.email}"


class Makanan(models.Model):
      rname = models.ForeignKey(Restoran, on_delete=models.CASCADE)
      foodname = models.CharField(max_length=50)
      description = models.TextField()
      stock = models.IntegerField()
      price = models.FloatField()
      kategori = models.ForeignKey(KategoriMakanan, blank=True, null=True, on_delete=models.SET_NULL)

