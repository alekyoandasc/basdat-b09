from django import forms
from sirest_b09.models import Admin, Pelanggan, Restoran, Kurir

class AdminForm(forms.ModelForm):
      class Meta:
            model = Admin
            fields = ('email', 'password', 'name', 'no_hp')

            # custom labels
            labels = {
                  'email' : 'Email',
                  'password' : 'Password',
                  'name' : 'Nama Lengkap',
                  'no_hp' : 'No Handphone',
            }

            # custom widgets
            widgets = {
                  'email' : forms.TextInput(
                        attrs={
                              'type' : 'email',
                              'placeholder' : 'username@domain',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'password' : forms.TextInput(
                        attrs={
                              'type' : 'password',
                              'placeholder' : 'Password',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'name' : forms.TextInput(
                        attrs={
                              'type' : 'text',
                              'placeholder' : 'Nama Lengkap',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'no_hp' : forms.TextInput(
                        attrs={
                              'type' : 'tel',
                              'placeholder' : 'No Handphone',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  )
            }

class PelangganForm(forms.ModelForm):
      class Meta:
            model = Pelanggan
            fields = ('email', 'password', 'name', 'no_hp', 'nik', 'bank_name', 'no_rek', 'bdate', 'gender')
            def __init__(self, *args, **kwargs):
                  super().__init__(*args, **kwargs)
                  self.fields['gender'].queryset = Pelanggan.objects.none()

            labels = {
                  'email' : 'Email',
                  'password' : 'Password',
                  'name' : 'Nama Lengkap',
                  'no_hp': 'No Handphone',
                  'nik' : 'NIK',
                  'bank_name' : 'Nama Bank',
                  'no_rek' : 'Nomor Rekening',
                  'bdate' : 'Tanggal Lahir',
                  'gender' : 'Jenis Kelamin'
            }

            widgets = {
                  'email' : forms.TextInput(
                        attrs={
                              'type' : 'email',
                              'placeholder': 'username@domain',
                              'class': 'form-control',
                              'aria-describedby': 'inputGroupPrepend',
                        }
                  ),
                  'password': forms.TextInput(
                        attrs={
                              'type':'password',
                              'placeholder':'Password',
                              'class':'form-control',
                              'aria-describedby':'inputGroupPrepend',
                        }
                  ),
                  'name':forms.TextInput(
                        attrs={
                              'type':'text',
                              'palceholder':'Nama Lengkap',
                              'class':'form-control',
                              'aria-describedby':'inputGroupPrepend',
                        }
                  ),
                  'no_hp' : forms.TextInput(
                        attrs={
                              'type' : 'telp',
                              'placeholder' : 'No Handphone',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'nik' : forms.TextInput(
                        attrs={
                              'type' : 'number',
                              'placeholder' : 'NIK',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'bank_name' : forms.TextInput(
                        attrs={
                              'type' : 'text',
                              'placeholder' : 'Nama Bank',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'no_rek' : forms.TextInput(
                        attrs={
                              'type' : 'number',
                              'placeholder' : 'Nomor Rekening',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'bdate' : forms.DateInput(
                        attrs={
                              'type' : 'date',
                              'placeholder' : 'Tanggal Lahir',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'gender' : forms.Select(
                        # choices=JK
                        # attrs={
                        #       'type' : 'text',
                        #       'placeholder' : 'Jenis Kelamin',
                        #       'class' : 'form-control',
                        #       'aria-describedby' : 'inputGrouPrepend',
                        # }
                  )
            }

class RestoranForm(forms.ModelForm):
      class Meta:
            model = Restoran
            fields = ('email', 'password', 'name', 'no_hp', 'nik', 'bank_name', 'no_rek', 'rest_name',
                        'branch', 'no_telp', 'street', 'districts', 'city', 'province')

            labels = {
                  'email': 'Email',
                  'password':'Password',
                  'name' : 'Nama Lengkap',
                  'no_hp': 'No Handphone',
                  'nik': 'NIK Pemilik',
                  'bank_name': 'Nama Bank',
                  'no_rek': 'Nomor Rekening',
                  'rest_name': 'Nama Restoran',
                  'branch': 'Cabang',
                  'no_telp': 'No Telepon',
                  'street': 'Nama Jalan',
                  'districts': 'Kecamatan',
                  'city': 'Kota',
                  'province': 'Provinsi'
            }

            widgets = {
                  'email' : forms.TextInput(
                        attrs={
                              'type':'email',
                              'placeholder' : 'username@domain',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'password' : forms.TextInput(
                        attrs={
                              'type':'password',
                              'placeholder' : 'Password',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'name' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Nama Lengkap',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'no_hp' : forms.TextInput(
                        attrs={
                              'type':'number',
                              'placeholder' : 'No Handphone',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'nik' : forms.TextInput(
                        attrs={
                              'type':'number',
                              'placeholder' : 'NIK',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'bank_name' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Nama Bank',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'no_rek' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Nomor Rekening',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'rest_name' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Nama Restoran',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'branch' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Cabang',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'no_telp' : forms.TextInput(
                        attrs={
                              'type':'number',
                              'placeholder' : 'No Telepon Restoran',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'street' : forms.TextInput(
                        attrs={
                              'type':'char',
                              'placeholder' : 'Nama Jalan',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'districts' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Nama Kecamatan',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'city' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Nama Kota/Kabupaten',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'province' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Nama Provinsi',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
            }

class KurirForm(forms.ModelForm):
      class Meta:
            model = Kurir
            fields = ('email', 'password', 'name', 'no_hp', 'nik', 'bank_name', 'no_rek',
                        'plate_num', 'sim_num', 'vehicle_brand', 'trans_type')
            def __init__(self, *args, **kwargs):
                  super().__init__(*args, **kwargs)
                  self.fields['trans_type'].queryset = Kurir.objects.none()

            labels = {
                  'email': 'Email',
                  'password': 'Password',
                  'name': 'Nama Lengkap',
                  'no_hp': 'No Handphone',
                  'nik': 'NIK',
                  'bank_name': 'Nama Bank',
                  'no_rek': 'Nomor Rekening',
                  'plate_num': 'Plat Nomor Kendaraan',
                  'sim_num': 'Nomor SIM',
                  'vehicle_brand': 'Merk Kendaraan',
                  'trans_type': 'Jenis Kendaraan',

            }

            widgets = {
                  'email' : forms.TextInput(
                        attrs={
                              'type':'email',
                              'placeholder' : 'username@domain',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'password' : forms.TextInput(
                        attrs={
                              'type':'password',
                              'placeholder' : 'Password',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'name' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Nama Lengkap',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'no_hp' : forms.TextInput(
                        attrs={
                              'type':'telp',
                              'placeholder' : 'No Handphone',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'nik' : forms.TextInput(
                        attrs={
                              'type':'number',
                              'placeholder' : 'NIK',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'bank_name' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Nama Bank',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'no_rek' : forms.TextInput(
                        attrs={
                              'type':'number',
                              'placeholder' : 'Nomor Rekening',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'plate_num' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Plat Nomor Kendaraan',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'sim_num' : forms.TextInput(
                        attrs={
                              'type':'number',
                              'placeholder' : 'Nomor SIM',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'vehicle_brand' : forms.TextInput(
                        attrs={
                              'type':'text',
                              'placeholder' : 'Merk Kendaraan',
                              'class' : 'form-control',
                              'aria-describedby' : 'inputGroupPrepend',
                        }
                  ),
                  'trans_type' : forms.Select(
                        # attrs={
                        #       'type':'email',
                        #       'placeholder' : 'username@domain',
                        #       'class' : 'form-control',
                        #       'aria-describedby' : 'inputGroupPrepend',
                        # }
                  )
            }