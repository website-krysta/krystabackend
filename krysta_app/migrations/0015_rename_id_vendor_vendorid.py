# Generated by Django 4.1.2 on 2023-04-11 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0014_remove_vendor_vendorid_vendor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='ID',
            new_name='VendorID',
        ),
    ]
