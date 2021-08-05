# Generated by Django 3.2.5 on 2021-08-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0003_barang_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=180)),
                ('dibuat', models.DateTimeField(auto_now_add=True)),
                ('diubah', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Kategori',
            },
        ),
        migrations.RemoveIndex(
            model_name='pinjam',
            name='stok_pinjam_barang__ad1560_idx',
        ),
        migrations.RenameField(
            model_name='pinjam',
            old_name='peminjam',
            new_name='dipinjam',
        ),
        migrations.AddIndex(
            model_name='pinjam',
            index=models.Index(fields=['barang', 'dipinjam'], name='stok_pinjam_barang__0100b2_idx'),
        ),
        migrations.AddIndex(
            model_name='kategori',
            index=models.Index(fields=['nama'], name='stok_katego_nama_76a805_idx'),
        ),
    ]
