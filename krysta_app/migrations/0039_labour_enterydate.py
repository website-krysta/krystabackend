# Generated by Django 4.1.2 on 2023-05-12 04:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0038_vendor_lossofamount_alter_damaged_lossofamount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='labour',
            name='EnteryDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
