# Generated by Django 4.0.4 on 2022-11-19 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirest_b09', '0002_alter_kurir_no_rek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurir',
            name='sim_num',
            field=models.IntegerField(max_length=18),
        ),
    ]
