# Generated by Django 4.1.2 on 2022-11-22 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sirest_b09', '0007_alter_kurir_trans_type_alter_pelanggan_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriMakanan',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Makanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('stock', models.IntegerField()),
                ('price', models.BigIntegerField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sirest_b09.kategorimakanan')),
                ('rname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sirest_b09.restoran')),
            ],
        ),
    ]
