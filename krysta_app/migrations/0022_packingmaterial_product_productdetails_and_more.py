# Generated by Django 4.1.2 on 2023-04-13 13:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0021_alter_rawmaterial_consumedquantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackingMaterial',
            fields=[
                ('PackingMaterialID', models.AutoField(primary_key=True, serialize=False)),
                ('PackingMaterialCode', models.CharField(max_length=255)),
                ('PackingMaterialName', models.CharField(max_length=25)),
                ('QtyType', models.CharField(blank=True, max_length=20, null=True)),
                ('TotalQuantity', models.IntegerField(default=0)),
                ('ConsumedQuantity', models.IntegerField(blank=True, default=0, null=True)),
                ('AddedTimestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('UpdatedTimestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ProductID', models.AutoField(primary_key=True, serialize=False)),
                ('ProductCode', models.CharField(max_length=255)),
                ('ProductName', models.CharField(max_length=25)),
                ('QtyType', models.CharField(blank=True, max_length=20, null=True)),
                ('TotalQuantity', models.IntegerField(default=0)),
                ('ConsumedQuantity', models.IntegerField(blank=True, default=0, null=True)),
                ('AddedTimestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('UpdatedTimestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('TransactionDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('BatchNo', models.CharField(max_length=25)),
                ('OrderedQuantity', models.IntegerField()),
                ('ReceivedQuantity', models.IntegerField()),
                ('AmountPaid', models.IntegerField()),
                ('AddedTimestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('UpdatedTimestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('DamgeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.damaged')),
                ('ProductID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.product')),
                ('VendorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='PackingDetails',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('TransactionDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('BatchNo', models.CharField(max_length=25)),
                ('OrderedQuantity', models.IntegerField()),
                ('ReceivedQuantity', models.IntegerField()),
                ('AmountPaid', models.IntegerField()),
                ('AddedTimestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('UpdatedTimestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('DamgeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.damaged')),
                ('PackingMaterialID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.packingmaterial')),
                ('VendorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.vendor')),
            ],
        ),
    ]