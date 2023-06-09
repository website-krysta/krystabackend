# Generated by Django 4.1.2 on 2023-04-13 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0020_alter_damaged_damgeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterial',
            name='ConsumedQuantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='EmailID',
            field=models.EmailField(max_length=254),
        ),
    ]
