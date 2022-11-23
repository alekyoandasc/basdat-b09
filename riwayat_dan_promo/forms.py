from django import forms
from riwayat_dan_promo.models import *

class PromoMinTransaksiForm(forms.ModelForm):
      class Meta:
            model = PromoMinTransaksi
            fields = ['nama_promo', 'diskon', 'min_transaksi']
            labels = {
                  'nama_promo' : 'Nama Promo',
                  'diskon' : 'Diskon',
                  'min_transaksi' : 'Minimum Transaksi',
            }

            widgets = {
                  'nama_promo' : forms.TextInput(
                        attrs={
                              'type' : 'text',
                              'placeholder': 'Beli Banyak Lebih Murah',
                              'class': 'form-control',
                              'aria-describedby': 'inputGroupPrepend',
                        }
                  ),
                  'diskon': forms.TextInput(
                        attrs={
                              'type':'number',
                              'placeholder':'100',
                              'class':'form-control',
                              'aria-describedby':'inputGroupPrepend',
                        }
                  ),
                  'min_transaksi':forms.TextInput(
                        attrs={
                              'type':'number',
                              'palceholder':'3',
                              'class':'form-control',
                              'aria-describedby':'inputGroupPrepend',
                        }
                  ),
            }

class PromoHariSpesialForm(forms.ModelForm):
      class Meta:
            model = PromoHariSpesial
            fields = ['nama_promo', 'diskon', 'tanggal_spesial']

            labels = {
                  'nama_promo' : 'Nama Promo',
                  'diskon' : 'Diskon',
                  'tanggal_spesial' : 'Tanggal Berlangsung',
            }

            widgets = {
                  'nama_promo' : forms.TextInput(
                        attrs={
                              'type' : 'text',
                              'placeholder': 'Beli Banyak Lebih Murah',
                              'class': 'form-control',
                              'aria-describedby': 'inputGroupPrepend',
                        }
                  ),
                  'diskon': forms.TextInput(
                        attrs={
                              'type':'number',
                              'placeholder':'100',
                              'class':'form-control',
                              'aria-describedby':'inputGroupPrepend',
                        }
                  ),
                  'tanggal_spesial':forms.TextInput(
                        attrs={
                              'type':'date',
                              'palceholder':'17 Agustus 2022',
                              'class':'form-control',
                              'aria-describedby':'inputGroupPrepend',
                        }
                  ),
            }