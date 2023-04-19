# Generated by Django 4.1.2 on 2023-04-18 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0026_alter_addrawmaterial_id_alter_invoice_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrawmaterial',
            name='InvoiceID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='krysta_app.invoice'),
        ),
        migrations.AddField(
            model_name='packingdetails',
            name='InvoiceID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='krysta_app.invoice'),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='InvoiceID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='krysta_app.invoice'),
        ),
    ]
