# Generated by Django 4.1.2 on 2023-04-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0007_remove_vendor_vendorid_vendor_vendorcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='VendorCode',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]