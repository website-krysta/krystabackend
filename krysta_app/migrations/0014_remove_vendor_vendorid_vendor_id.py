# Generated by Django 4.1.2 on 2023-04-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0013_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='VendorID',
        ),
        migrations.AddField(
            model_name='vendor',
            name='ID',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
