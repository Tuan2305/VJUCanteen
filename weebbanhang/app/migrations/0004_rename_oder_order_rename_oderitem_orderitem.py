# Generated by Django 4.2.1 on 2023-06-01 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_sanpham_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oder',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='OderItem',
            new_name='OrderItem',
        ),
    ]
