from django import forms

class AdminForm(forms.Form):
      
      email = forms.EmailField(
            label='Email',
            widget= forms.TextInput(
                  
                  attrs={
                        'name': 'email',
                        'type' : 'email',
                        'placeholder' : 'Email',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      password = forms.CharField(
            max_length=30, 
            label='Password',
            widget= forms.TextInput(
                  attrs={
                        'name': 'password',
                        'type' : 'password',
                        'placeholder' : 'Password',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      fname = forms.CharField(
            max_length=100, 
            label='Nama Depan',
            widget= forms.TextInput(
                  
                  attrs={
                        'name':'fname',
                        'type' : 'text',
                        'placeholder' : 'Nama Depan',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )

      lname = forms.CharField(
            max_length=100, 
            label='Nama Akhir',
            widget= forms.TextInput(
                  
                  attrs={
                        'name':'lname',
                        'type' : 'text',
                        'placeholder' : 'Nama Akhir',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      no_hp = forms.CharField(
            max_length=12, 
            label='No Handphone',
            widget= forms.TextInput(
                  
                  attrs={
                        'name':'no_hp',
                        'type' : 'tel',
                        'placeholder' : 'No Handphone',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )




class PelangganForm(forms.Form):

            
      email = forms.EmailField(
            label = 'Email',
            widget = forms.TextInput(
                  attrs={
                        'name' : 'email',
                        'type' : 'email',
                        'placeholder': 'username@domain',
                        'class': 'form-control',
                        'aria-describedby': 'inputGroupPrepend',
                  }
            ),
      )
      password = forms.CharField(
            max_length=30,
            label = 'Password',
            widget = forms.TextInput(
                  attrs={
                        'name': 'password',
                        'type':'password',
                        'placeholder':'Password',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )
      fname = forms.CharField(
            max_length=100,
            label = 'Nama Depan',
            widget = forms.TextInput(
                  attrs={
                        'name': 'fname',
                        'type':'text',
                        'palceholder':'Nama Depan',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )
      lname = forms.CharField(
            max_length=100,
            label = 'Nama Akhir',
            widget = forms.TextInput(
                  attrs={
                        'name': 'lname',
                        'type':'text',
                        'palceholder':'Nama Akhir',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )
      no_hp = forms.CharField(
            max_length=12, 
            label='No Handphone',
            widget= forms.TextInput(
                  
                  attrs={
                        'name':'no_hp',
                        'type' : 'tel',
                        'placeholder' : 'No Handphone',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      nik = forms.CharField(
            max_length=18,
            label = 'NIK',
            widget = forms.TextInput(
                  attrs={
                        'name': 'nik',
                        'type' : 'number',
                        'placeholder' : 'NIK',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      bank_name = forms.CharField(
            max_length=30,
            label = 'Nama Bank',
            widget = forms.TextInput(
                  attrs={
                        'name': 'bank_name',
                        'type' : 'text',
                        'placeholder' : 'Nama Bank',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      no_rek = forms.CharField(
            max_length=25,
            label = 'No Rekening',
            widget = forms.TextInput(
                  attrs={
                        'name': 'no_rek',
                        'type' : 'number',
                        'placeholder' : 'Nomor Rekening',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      bdate = forms.DateField(
            label = 'Tanggal lahir',
            widget = forms.DateInput(
                  attrs={
                        'name': 'bdate',
                        'type' : 'date',
                        'placeholder' : 'Tanggal Lahir',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      JK = [('M', 'Pria'), ('F', 'Wanita'),]
      gender = forms.ChoiceField(
            choices=JK, 
            label = 'Jenis Kelamin',
            widget = forms.Select(
                  attrs={
                        'name': 'gender'
                  }
            )
      )


     

class RestoranForm(forms.Form):
      
      email = forms.EmailField(
            label = 'Email',
            widget = forms.TextInput(
                  attrs={
                        'name' : 'email',
                        'type' : 'email',
                        'placeholder': 'username@domain',
                        'class': 'form-control',
                        'aria-describedby': 'inputGroupPrepend',
                  }
            ),
      )
      password = forms.CharField(
            max_length=30,
            label = 'Password',
            widget = forms.TextInput(
                  attrs={
                        'name': 'password',
                        'type':'password',
                        'placeholder':'Password',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )
      fname = forms.CharField(
            max_length=100,
            label = 'Nama Depan',
            widget = forms.TextInput(
                  attrs={
                        'name': 'fname',
                        'type':'text',
                        'palceholder':'Nama Depan',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )
      lname = forms.CharField(
            max_length=100,
            label = 'Nama Akhir',
            widget = forms.TextInput(
                  attrs={
                        'name': 'lname',
                        'type':'text',
                        'palceholder':'Nama Akhir',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )
      no_hp = forms.CharField(
            max_length=12, 
            label='No Handphone',
            widget= forms.TextInput(
                  
                  attrs={
                        'name':'no_hp',
                        'type' : 'tel',
                        'placeholder' : 'No Handphone',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      nik = forms.CharField(
            max_length=18,
            label = 'NIK',
            widget = forms.TextInput(
                  attrs={
                        'name': 'nik',
                        'type' : 'number',
                        'placeholder' : 'NIK',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      bank_name = forms.CharField(
            max_length=30,
            label = 'Nama Bank',
            widget = forms.TextInput(
                  attrs={
                        'name': 'bank_name',
                        'type' : 'text',
                        'placeholder' : 'Nama Bank',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      no_rek = forms.CharField(
            max_length=25,
            label = 'No Rekening',
            widget = forms.TextInput(
                  attrs={
                        'name': 'no_rek',
                        'type' : 'number',
                        'placeholder' : 'Nomor Rekening',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      rest_name = forms.CharField(
            max_length=50,
            label = 'Nama Restoran',
            widget= forms.TextInput(
                  attrs={
                        'name': 'rest_name',
                        'type':'text',
                        'placeholder' : 'Nama Restoran',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      branch = forms.CharField(
            max_length=50,
            label = 'Nama Cabang',
            widget= forms.TextInput(
                  attrs={
                        'name': 'branch',
                        'type':'text',
                        'placeholder' : 'Cabang',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      no_telp = forms.CharField(
            max_length=12,
            label = 'Kontak Restoran',
            widget= forms.TextInput(
                  attrs={
                        'name': 'no_telp',
                        'type':'number',
                        'placeholder' : 'No Telepon Restoran',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      street = forms.CharField(
            max_length=50,
            label = 'Jalan',
            widget= forms.TextInput(
                  attrs={
                        'name': 'street',
                        'type':'char',
                        'placeholder' : 'Nama Jalan',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      district = forms.CharField(
            max_length=50,
            label = 'Kecamatan',
            widget= forms.TextInput(
                  attrs={
                        'name': 'district',
                        'type':'text',
                        'placeholder' : 'Nama Kecamatan',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      city = forms.CharField(
            max_length=50,
            label = 'Kota',
            widget= forms.TextInput(
                  attrs={
                        'name': 'city',
                        'type':'text',
                        'placeholder' : 'Nama Kota/Kabupaten',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )



      





            
      

class KurirForm(forms.Form):
      email = forms.EmailField(
            label = 'Email',
            widget = forms.TextInput(
                  attrs={
                        'name' : 'email',
                        'type' : 'email',
                        'placeholder': 'username@domain',
                        'class': 'form-control',
                        'aria-describedby': 'inputGroupPrepend',
                  }
            ),
      )
      password = forms.CharField(
            max_length=30,
            label = 'Password',
            widget = forms.TextInput(
                  attrs={
                        'name': 'password',
                        'type':'password',
                        'placeholder':'Password',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )
      fname = forms.CharField(
            max_length=100,
            label = 'Nama Depan',
            widget = forms.TextInput(
                  attrs={
                        'name': 'fname',
                        'type':'text',
                        'palceholder':'Nama Depan',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )
      lname = forms.CharField(
            max_length=100,
            label = 'Nama Akhir',
            widget = forms.TextInput(
                  attrs={
                        'name': 'lname',
                        'type':'text',
                        'palceholder':'Nama Akhir',
                        'class':'form-control',
                        'aria-describedby':'inputGroupPrepend',
                  }
            ),
      )
      no_hp = forms.CharField(
            max_length=12, 
            label='No Handphone',
            widget= forms.TextInput(
                  
                  attrs={
                        'name':'no_hp',
                        'type' : 'tel',
                        'placeholder' : 'No Handphone',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      nik = forms.CharField(
            max_length=18,
            label = 'NIK',
            widget = forms.TextInput(
                  attrs={
                        'name': 'nik',
                        'type' : 'number',
                        'placeholder' : 'NIK',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      bank_name = forms.CharField(
            max_length=30,
            label = 'Nama Bank',
            widget = forms.TextInput(
                  attrs={
                        'name': 'bank_name',
                        'type' : 'text',
                        'placeholder' : 'Nama Bank',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      no_rek = forms.CharField(
            max_length=25,
            label = 'No Rekening',
            widget = forms.TextInput(
                  attrs={
                        'name': 'no_rek',
                        'type' : 'number',
                        'placeholder' : 'Nomor Rekening',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      
      plate_num = forms.CharField(
            max_length=10,
            label='Plat Nomor',
            widget= forms.TextInput(
                  attrs={
                        'name': 'plate_num',
                        'type':'text',
                        'placeholder' : 'Plat Nomor Kendaraan',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      sim_num = forms.CharField(
            max_length=18,
            label='Nomor SIM',
            widget= forms.TextInput(
                  attrs={
                        'name': 'sim_num',
                        'type':'number',
                        'placeholder' : 'Nomor SIM',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      vehicle_brand = forms.CharField(
            max_length=30,
            label='Merk Kendaraan',
            widget= forms.TextInput(
                  attrs={
                        'name': 'vehicle_brand',
                        'type':'text',
                        'placeholder' : 'Merk Kendaraan',
                        'class' : 'form-control',
                        'aria-describedby' : 'inputGroupPrepend',
                  }
            ),
      )
      TRANS = [('motor', 'Motor'), ('mobil', 'Mobil')]
      trans_type = forms.ChoiceField(
            choices=TRANS, 
            label='Tipe Kendaraan',
            widget= forms.Select(
                  attrs={
                        'name':'trans_type'
                  }
            )
      )


     
