from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


TIPE_PROMO = (
    ('m', 'Min Transaksi'),
    ('h', 'Hari Spesial')
)
class Promo(models.Model):
    nama_promo = models.CharField(max_length=15)
    diskon = models.IntegerField(validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=100)])
    tipe_promo = models.CharField(max_length=1, choices=TIPE_PROMO)


class PromoMinTransaksi(Promo):
    min_transaksi = models.IntegerField()

    

class PromoHariSpesial(Promo):
    tanggal_spesial = models.DateField()
    
    