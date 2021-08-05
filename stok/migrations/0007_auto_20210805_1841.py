# Generated by Django 3.2.5 on 2021-08-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0006_barang_keterangan'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='barang',
            name='stok_barang_nama_20bb95_idx',
        ),
        migrations.RemoveField(
            model_name='barang',
            name='lokasi',
        ),
        migrations.AddField(
            model_name='barang',
            name='lokasi',
            field=models.ManyToManyField(to='stok.Lokasi'),
        ),
        migrations.AddIndex(
            model_name='barang',
            index=models.Index(fields=['nama', 'kategori'], name='stok_barang_nama_352ce0_idx'),
        ),
    ]
