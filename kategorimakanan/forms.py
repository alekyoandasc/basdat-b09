from django.forms import ModelForm
from .models import *


class KategoriMakananForm(ModelForm):
    class Meta:
        model = KategoriMakanan
        fields = ['name']
