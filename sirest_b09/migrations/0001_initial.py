# Generated by Django 4.0.4 on 2022-11-19 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('no_hp', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Kurir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('no_hp', models.CharField(max_length=12)),
                ('nik', models.CharField(max_length=18)),
                ('bank_name', models.CharField(max_length=30)),
                ('no_rek', models.PositiveIntegerField(max_length=30)),
                ('plate_num', models.CharField(max_length=10)),
                ('sim_num', models.PositiveIntegerField(max_length=18)),
                ('vehicle_brand', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('nama', models.CharField(max_length=100)),
                ('no_hp', models.CharField(max_length=12)),
                ('nik', models.CharField(max_length=18)),
                ('bank_name', models.CharField(max_length=30)),
                ('no_rek', models.CharField(max_length=25)),
                ('bdate', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Restoran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('no_hp', models.CharField(max_length=12)),
                ('nik', models.CharField(max_length=18)),
                ('bank_name', models.CharField(max_length=30)),
                ('no_rek', models.CharField(max_length=30)),
                ('rest_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('no_telp', models.CharField(max_length=12)),
                ('street', models.CharField(max_length=50)),
                ('districts', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
            ],
        ),
    ]
