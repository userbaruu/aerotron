# Generated by Django 3.2.5 on 2021-07-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perawatan', '0003_alter_fasilitas_nama'),
    ]

    operations = [
        migrations.AddField(
            model_name='fasilitas',
            name='singkatan',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
