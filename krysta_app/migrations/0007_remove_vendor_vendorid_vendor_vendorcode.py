# Generated by Django 4.1.2 on 2023-04-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0006_alter_rawmaterial_qtytype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='VendorID',
        ),
        migrations.AddField(
            model_name='vendor',
            name='VendorCode',
            field=models.IntegerField(default='1', primary_key=True, serialize=False),
        ),
    ]
