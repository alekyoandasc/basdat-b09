from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class PromoMinTransaksiForm(forms.Form):
      
      promoname = forms.CharField(
            max_length=15,
            label='Nama Promo',
            widget = forms.TextInput(
                  attrs={
                        'name': 'promoname',
                        'id': 'promoname',
                        'type' : 'text',
                        'placeholder': 'Beli Banyak Lebih Murah',
                        'class': 'form-control',
                        'aria-describedby': 'inputGroupPrepend',
                  }
            ),
      )
      discount = forms.IntegerField(
            validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=100)],
            label='Diskon',
            widget = forms.TextInput(
                  attrs={
                        'name': 'discount',
                        'id': 'discount',
                        'type':'number',
                        'placeholder':'100',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )
      minimumtransactionnum = forms.IntegerField(
            label='Minimum Jumlah Transaksi',
            widget = forms.TextInput(
                  attrs={
                        'name': 'minimumtransactionnum',
                        'id': 'minimumtransactionnum',
                        'type':'number',
                        'palceholder':'3',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),

      )
            


class PromoHariSpesialForm(forms.Form):
      promoname = forms.CharField(
            max_length=15,
            label='Nama Promo',
            widget = forms.TextInput(
                  attrs={
                        'name': 'promoname',
                        'id': 'promoname',
                        'type' : 'text',
                        'placeholder': 'Beli Banyak Lebih Murah',
                        'class': 'form-control',
                        'aria-describedby': 'inputGroupPrepend',
                  }
            ),
      )
      discount = forms.IntegerField(
            validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=100)],
            label='Diskon',
            widget = forms.TextInput(
                  attrs={
                        'name': 'discount',
                        'id': 'discount',
                        'type':'number',
                        'placeholder':'100',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )

      date = forms.DateField(
            label='Tanggal Spesial',
            widget = forms.DateInput(
                  attrs={
                        'name':'date',
                        'id':'date',
                        'type':'date',
                        'plceholder':'17 Agustus 2022',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )

  