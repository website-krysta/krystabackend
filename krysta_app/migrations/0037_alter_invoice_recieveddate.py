# Generated by Django 4.1.2 on 2023-05-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0036_alter_production_productionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='RecievedDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
