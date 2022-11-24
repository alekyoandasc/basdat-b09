from dataclasses import Field
from django import forms

class CreateKategoriRestoForm(forms.Form):
    nama_kategori = forms.CharField(max_length=20, 
    error_messages= {
        'required': 'Please fill out this field'
    })

class CreateBahanMakananForm(forms.Form):
    nama_bahan = forms.CharField(max_length=25, 
    error_messages= {
        'required': 'Please fill out this field'
    })