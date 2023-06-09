# Generated by Django 4.1.2 on 2023-05-30 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0050_production_batchno_salesinvoice_batchno'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesdetails',
            name='ProductID',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='krysta_app.product'),
        ),
        migrations.AddField(
            model_name='salesdetails',
            name='Type',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
