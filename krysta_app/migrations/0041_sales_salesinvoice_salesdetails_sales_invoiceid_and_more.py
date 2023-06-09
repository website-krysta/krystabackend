# Generated by Django 4.1.2 on 2023-05-18 04:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0040_alter_production_formulaid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('SalesID', models.AutoField(primary_key=True, serialize=False)),
                ('TotalProducts', models.CharField(max_length=10)),
                ('TotalAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TransactionDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('AddedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('UpdatedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('InvoiceID', models.IntegerField(primary_key=True, serialize=False)),
                ('InvoiceNumber', models.CharField(max_length=10)),
                ('InwardNumber', models.CharField(max_length=20)),
                ('InvoiceDate', models.DateField()),
                ('RecievedDate', models.DateField(blank=True, default='', null=True)),
                ('VendorID', models.IntegerField()),
                ('AddedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('UpdatedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SalesDetails',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('AddedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('UpdatedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('FormulaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.formula')),
                ('SalesID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.sales')),
            ],
        ),
        migrations.AddField(
            model_name='sales',
            name='InvoiceID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.salesinvoice'),
        ),
        migrations.AddField(
            model_name='sales',
            name='VendorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.vendor'),
        ),
    ]
