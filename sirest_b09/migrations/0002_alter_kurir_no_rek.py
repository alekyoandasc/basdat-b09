# Generated by Django 4.0.4 on 2022-11-19 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirest_b09', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurir',
            name='no_rek',
            field=models.PositiveIntegerField(),
        ),
    ]